#!/usr/bin/env python3
"""
Test harness for the Animation Assistant prompts.

Runs each prompt against its test cases and lets you evaluate 
the responses manually (or via an LLM judge if configured).

Usage:
    python test_prompts.py                    # Run all tests interactively
    python test_prompts.py --prompt 03         # Run one prompt's tests
    python test_prompts.py --list              # List all prompts and test cases
    python test_prompts.py --judge             # Use LLM to auto-judge (requires API)

This is a MANUAL evaluation harness — it shows you the prompt, 
the test input, and the model's response side by side so you can 
decide if the response meets expectations.
"""

import argparse
import json
import os
import sys
from pathlib import Path

# --- Test Case Definitions ---
# Each entry: (prompt_file, test_name, input_dict, expected_behavior_description)

TEST_CASES = [
    # Prompt 01: System Persona
    {
        "prompt_file": "01-system-persona.md",
        "tests": [
            {"name": "young_beginner_no_tool", 
             "input": "I want to make animations but I don't know where to start",
             "expect": "Recommends Scratch or Stop Motion Studio; asks age; introduces bouncing ball"},
            {"name": "teen_with_blender", 
             "input": "I'm 15 and I have Blender, how do I make a character walk?",
             "expect": "Blender-specific steps; references timing + follow-through principles"},
            {"name": "too_advanced_request", 
             "input": "I'm 11 and I want to make a full anime episode",
             "expect": "Gently redirects to age-appropriate starting point; doesn't dismiss the goal"},
            {"name": "vague_request", 
             "input": "I want to animate",
             "expect": "Asks clarifying questions: age? what kind? do you like to draw?"},
        ]
    },
    # Prompt 02: Tool Routing
    {
        "prompt_file": "02-tool-routing.md",
        "tests": [
            {"name": "10yo_coder", 
             "input": {"age": 10, "experience": "none", "interests": ["coding", "storytelling"]},
             "expect": "Scratch; first project = bouncing ball sprite"},
            {"name": "11yo_lego", 
             "input": {"age": 11, "experience": "none", "interests": ["lego/clay"]},
             "expect": "Stop Motion Studio; first project = LEGO walk cycle"},
            {"name": "13yo_artist", 
             "input": {"age": 13, "experience": "none", "interests": ["drawing"]},
             "expect": "Krita; first project = bouncing ball with squash & stretch"},
            {"name": "14yo_3d", 
             "input": {"age": 14, "experience": "some", "interests": ["3d", "coding"]},
             "expect": "Blender; first project = keyframed cube bounce"},
            {"name": "chromebook_constraint", 
             "input": {"age": 12, "platform": "chromebook"},
             "expect": "Scratch or web-based; no desktop tool recommended"},
        ]
    },
    # Prompt 03: Project Guide
    {
        "prompt_file": "03-project-guide.md",
        "tests": [
            {"name": "ball_in_scratch", 
             "input": {"tool": "scratch", "project": "bouncing-ball"},
             "expect": "Costume-based steps; wait blocks for timing; squash via costume change"},
            {"name": "ball_in_krita", 
             "input": {"tool": "krita", "project": "bouncing-ball"},
             "expect": "Onion skin steps; timeline frames; drawing tools"},
            {"name": "walk_in_opentoonz", 
             "input": {"tool": "opentoonz", "project": "walk-cycle"},
             "expect": "Timeline + levels; key contact poses first; inbetweens"},
            {"name": "jump_in_blender", 
             "input": {"tool": "blender", "project": "character-jump"},
             "expect": "Keyframes on timeline; graph editor mention; rig or simple cube"},
            {"name": "age_too_young", 
             "input": {"tool": "any", "project": "lip-sync", "age": 10},
             "expect": "Suggests simpler project first; doesn't refuse outright"},
        ]
    },
    # Prompt 04: Principle Explainer
    {
        "prompt_file": "04-principle-explainer.md",
        "tests": [
            {"name": "squash_stretch", 
             "input": {"principle": "squash-and-stretch"},
             "expect": "Rubber ball analogy; tennis ball demo; tool tips for Scratch/Krita/Blender"},
            {"name": "timing", 
             "input": {"principle": "timing"},
             "expect": "Fast = light/energetic, slow = heavy/sad; clap demo; frame count guidance"},
            {"name": "arcs", 
             "input": {"principle": "arcs"},
             "expect": "Throwing a ball demo; nothing in nature moves in a straight line"},
            {"name": "follow_through", 
             "input": {"principle": "follow-through"},
             "expect": "Hair/clothing trailing; wave arm and stop suddenly"},
            {"name": "invalid_principle", 
             "input": {"principle": "momentum"},
             "expect": "Notes it's not one of the 12; suggests closest match"},
        ]
    },
    # Prompt 05: Code-First Animation
    {
        "prompt_file": "05-code-first-animation.md",
        "tests": [
            {"name": "scratch_flapping_bird", 
             "input": {"tool": "scratch", "level": 1, "project": "flapping-bird"},
             "expect": "Costume switch loop with wait; 2 costumes; timing explained"},
            {"name": "scratch_bouncing_ball", 
             "input": {"tool": "scratch", "level": 2, "project": "bouncing-ball"},
             "expect": "Glide blocks for arc; multiple glide points for curve"},
            {"name": "python_turtle_spiral", 
             "input": {"tool": "python-turtle", "project": "spiral"},
             "expect": "Complete runnable code; for loop; color change"},
            {"name": "too_young_for_python", 
             "input": {"tool": "python", "age": 10},
             "expect": "Redirect to Scratch; Python is great for when you're ~13+"},
        ]
    },
    # Prompt 06: Critique & Feedback
    {
        "prompt_file": "06-critique-feedback.md",
        "tests": [
            {"name": "proud_11yo_flat_ball", 
             "input": {"age": 11, "tool": "krita", "project": "bouncing-ball", 
                       "description": "ball bounces but it's just a circle going up and down"},
             "expect": "Praise timing; suggest squash & stretch; ask about tennis ball"},
            {"name": "frustrated_13yo_slide_walk", 
             "input": {"age": 13, "tool": "opentoonz", "project": "walk-cycle", 
                       "description": "my character walks but it looks like sliding", "feel": "frustrated"},
             "expect": "Praise attempt; suggest foot planting; ask about contact frames"},
            {"name": "16yo_robotic_head", 
             "input": {"age": 16, "tool": "blender", "project": "head-turn", 
                       "description": "head turn, feels robotic", "feel": "not sure"},
             "expect": "More direct: easing curves; anticipation; asks about slow in/out"},
            {"name": "10yo_masterpiece", 
             "input": {"age": 10, "tool": "scratch", "project": "character-jump", 
                       "description": "my cat jumps and it looks awesome!"},
             "expect": "Celebrate; ask one gentle question about the landing (follow-through)"},
        ]
    },
    # Prompt 07: Troubleshooting
    {
        "prompt_file": "07-troubleshooting.md",
        "tests": [
            {"name": "scratch_too_fast", 
             "input": {"tool": "scratch", "issue": "too fast"},
             "expect": "Wait block adjustment; explains fps relationship"},
            {"name": "krita_no_onion_skin", 
             "input": {"tool": "krita", "issue": "no onion skin"},
             "expect": "Docker checklist; how to enable onion skin docker"},
            {"name": "blender_gp_wont_draw", 
             "input": {"tool": "blender", "issue": "grease pencil won't draw"},
             "expect": "Mode check; draw mode activation steps"},
            {"name": "vague_looks_weird", 
             "input": {"tool": "any", "issue": "it looks weird"},
             "expect": "Asks diagnostic questions; principle checklist"},
            {"name": "creative_block", 
             "input": {"issue": "I don't know what to animate"},
             "expect": "Warm-up exercise; reference study suggestion"},
        ]
    },
    # Prompt 08: Curriculum Planner
    {
        "prompt_file": "08-curriculum-planner.md",
        "tests": [
            {"name": "10yo_funny_cartoons", 
             "input": {"age": 10, "experience": "none", "goal": "funny cartoons"},
             "expect": "Scratch-based; 8 weeks; playful projects; bouncing ball → character shorts"},
            {"name": "14yo_anime_fight", 
             "input": {"age": 14, "experience": "some", "goal": "anime-style fight scene"},
             "expect": "OpenToonz/Blender; compressed foundations; fight scene in final weeks"},
            {"name": "16yo_short_film", 
             "input": {"age": 16, "experience": "intermediate", "goal": "short film about my dog"},
             "expect": "Full 8-week plan; storyboarding week; dog-specific reference study"},
            {"name": "11yo_lego_space", 
             "input": {"age": 11, "experience": "none", "tool": "stop-motion-studio", "goal": "LEGO space movie"},
             "expect": "Stop Motion Studio; physical setup weeks; storytelling weeks"},
            {"name": "low_time_budget", 
             "input": {"age": 13, "time_budget": 1},
             "expect": "Simplified plan; fewer projects per phase; same milestones"},
            {"name": "no_goal_stated", 
             "input": {"age": 12, "goal": ""},
             "expect": "Asks for goal; offers example goals to choose from"},
        ]
    },
    # Prompt 09: Daily Challenge
    {
        "prompt_file": "09-daily-challenge.md",
        "tests": [
            {"name": "monday_warmup", 
             "input": {"day": "Monday"},
             "expect": "Squash & stretch focus; warm-up difficulty; 15-20 min"},
            {"name": "friday_follow_through", 
             "input": {"day": "Friday"},
             "expect": "Follow-through focus; medium-hard; 30-45 min"},
            {"name": "weekend_creative", 
             "input": {"day": "Saturday"},
             "expect": "Combined principles; creative/free; longer time"},
            {"name": "hard_for_teen", 
             "input": {"difficulty": "hard", "age": 15},
             "expect": "Challenge difficulty; more constraints; older tone"},
            {"name": "easy_for_kid", 
             "input": {"difficulty": "easy", "age": 10},
             "expect": "Easy difficulty; fewer constraints; Scratch tips"},
            {"name": "no_day_given", 
             "input": {},
             "expect": "Asks what day or assigns based on last completed"},
        ]
    },
    # Prompt 10: Reference Library
    {
        "prompt_file": "10-reference-library.md",
        "tests": [
            {"name": "walking_reference", 
             "input": {"subject": "walking"},
             "expect": "4 walk cycle phases; slow-mo search terms; key poses"},
            {"name": "dog_walk", 
             "input": {"subject": "dog-walk"},
             "expect": "Diagonal leg pairs; slow-mo dog videos; common mistake"},
            {"name": "bouncing_ball_ref", 
             "input": {"subject": "bouncing-ball"},
             "expect": "Squash/stretch observations; phone slow-mo; arc path"},
            {"name": "emotional_walk", 
             "input": {"subject": "sad-walk"},
             "expect": "Posture cues; shuffle description; film yourself"},
            {"name": "unknown_subject", 
             "input": {"subject": "spaceship-launch"},
             "expect": "General physics reference; slow-mo search; adapts"},
            {"name": "dragon_flight", 
             "input": {"subject": "dragon-flight"},
             "expect": "Cross-references bird + lizard; composite approach"},
        ]
    },
    # Prompt 11: Progress Tracker
    {
        "prompt_file": "11-progress-tracker.md",
        "tests": [
            {"name": "first_animation_ever", 
             "input": {"completed_projects": ["2-frame ball"], "tools_used": ["scratch"], "current_level": 1, "badges_earned": []},
             "expect": "Level 1; 'I Made Something Move' badge; progress to next"},
            {"name": "ball_with_squash", 
             "input": {"completed_projects": ["bouncing ball"], "principles_demonstrated": ["squash-stretch", "timing"], "current_level": 2, "badges_earned": []},
             "expect": "'Squash Master' + 'Timing Keeper' badges; Level 2 progress"},
            {"name": "walk_cycle_sliding", 
             "input": {"completed_projects": ["walk cycle"], "principles_demonstrated": ["timing"], "current_level": 3, "badges_earned": [], "issue": "feet slide"},
             "expect": "No 'Walk Cycle Warrior' yet; specific feedback on foot planting"},
            {"name": "level3_almost_done", 
             "input": {"current_level": 3, "badges_earned": ["walk-warrior", "contact-frame", "anticipation-ace", "follow-through", "mood-master", "lip-sync"], "completed_projects": []},
             "expect": "Shows 2 remaining badges; suggests projects for each"},
            {"name": "completed_short_film", 
             "input": {"completed_projects": ["30s short film with 3 shots"], "principles_demonstrated": "all", "current_level": 5, "badges_earned": []},
             "expect": "'Short Film Finisher' + 'Cut Master'; Level 5 progress"},
            {"name": "helped_friend", 
             "input": {"completed_projects": ["helped friend with walk cycle"], "current_level": 6, "badges_earned": []},
             "expect": "'Mentor Badge'; celebration"},
        ]
    },
    # Prompt 12: Showcase & Exhibition
    {
        "prompt_file": "12-showcase-exhibition.md",
        "tests": [
            {"name": "quick_share_ball", 
             "input": {"format": "quick-share", "project": "bouncing-ball", "description": "ball goes up and down", "age": 11},
             "expect": "Title, proud-of, learned, fun framing; under 50 words"},
            {"name": "classroom_presentation", 
             "input": {"format": "presentation", "project": "walk-cycle", "tool": "krita", "age": 13, "description": "character walking"},
             "expect": "Full template filled; process-focused; tool and principles"},
            {"name": "portfolio_entry", 
             "input": {"format": "portfolio", "project": "short-film", "description": "30 second dog story", "age": 15},
             "expect": "Structured entry with date, tool, principles, self-rating"},
            {"name": "exhibition_label", 
             "input": {"format": "exhibition", "project": "character-jump", "description": "my cat jumps over a fence", "proud_of": "the ears flopping", "age": 12},
             "expect": "Gallery-style label; artist statement from student's words"},
            {"name": "no_proud_of", 
             "input": {"format": "quick-share", "proud_of": "", "project": "bouncing-ball", "age": 10},
             "expect": "Asks what they're proud of; gives examples"},
            {"name": "first_animation", 
             "input": {"format": "portfolio", "project": "2 frames", "description": "first try", "age": 10},
             "expect": "Extra encouraging; 'first animation' milestone noted"},
        ]
    },
    # Prompt 13: Glossary
    {
        "prompt_file": "13-glossary.md",
        "tests": [
            {"name": "onion_skinning", 
             "input": {"term": "onion-skinning"},
             "expect": "Tracing paper analogy; try-it exercise; don't confuse with layers"},
            {"name": "keyframe_vs_inbetween", 
             "input": {"term": "keyframe", "vs": "inbetween"},
             "expect": "Both defined; comparison; try-it for each"},
            {"name": "tweening", 
             "input": {"term": "tweening"},
             "expect": "Computer fills in; contrast with frame-by-frame; try-it"},
            {"name": "fps", 
             "input": {"term": "fps"},
             "expect": "Frames per second; 24/12/30 examples; slow-mo analogy"},
            {"name": "unknown_term", 
             "input": {"term": "bezier-curve"},
             "expect": "Explains best-effort in same format; try-it with drawing"},
            {"name": "wrong_usage", 
             "input": {"term": "timeline", "usage": "I put all my drawings on the timeline"},
             "expect": "Gently clarifies timeline vs layers; doesn't shame"},
            {"name": "comparison_request", 
             "input": {"term": "raster", "vs": "vector"},
             "expect": "Side-by-side; which tools use which; try-it for both"},
        ]
    },
    # Prompt 14: Tool Comparison
    {
        "prompt_file": "14-tool-comparison.md",
        "tests": [
            {"name": "krita_vs_pencil2d", 
             "input": {"tools": ["krita", "pencil2d"]},
             "expect": "Krita wins on drawing; Pencil2D on simplicity; tiebreaker"},
            {"name": "scratch_vs_stopmotion", 
             "input": {"tools": ["scratch", "stop-motion-studio"]},
             "expect": "Scratch for coders; Stop Motion for tactile; tiebreaker"},
            {"name": "synfig_vs_opentoonz", 
             "input": {"tools": ["synfig", "opentoonz"], "age": 14},
             "expect": "Synfig for tweening; OpenToonz for full control; tiebreaker"},
            {"name": "blender_vs_opentoonz", 
             "input": {"tools": ["blender", "opentoonz"], "age": 16},
             "expect": "Blender for 3D; OpenToonz for 2D pro; tiebreaker: 2D or 3D?"},
            {"name": "three_tools", 
             "input": {"tools": ["scratch", "krita", "blender"]},
             "expect": "3-column comparison; handles gracefully; quick verdict"},
            {"name": "unknown_tool", 
             "input": {"tools": ["maya", "krita"]},
             "expect": "Notes Maya not in library (paid/pro); compares best match"},
            {"name": "age_too_young", 
             "input": {"tools": ["opentoonz", "blender"], "age": 10},
             "expect": "Recommends neither; suggests Scratch/Krita; explains why"},
        ]
    },
    # Prompt 15: Parent & Teacher Guide
    {
        "prompt_file": "15-parent-teacher-guide.md",
        "tests": [
            {"name": "wont_start_fear", 
             "input": {"role": "parent", "student_age": 10, "situation": "won't start, afraid it won't be good"},
             "expect": "Normalize; fear of failure; 'bad first attempt' framing; don't push"},
            {"name": "perfectionist", 
             "input": {"role": "parent", "student_age": 12, "situation": "redoes frame 1 twenty times"},
             "expect": "Normalize perfectionism; rough-first approach; specific phrasing"},
            {"name": "skill_gap_frustration", 
             "input": {"role": "teacher", "student_age": 14, "situation": "vision exceeds skill, frustrated"},
             "expect": "Gap is normal; break into small wins; specific encouragement"},
            {"name": "burnout", 
             "input": {"role": "parent", "student_age": 16, "situation": "stopped having fun, pressure"},
             "expect": "Burnout signs; suggest break or side project; reduce pressure"},
            {"name": "progress_check", 
             "input": {"role": "parent", "student_age": 11, "situation": "is my kid actually learning?"},
             "expect": "Process-over-product; what learning looks like; positive signs"},
            {"name": "adult_fixes_it", 
             "input": {"role": "parent", "student_age": 10, "situation": "I keep fixing their animation for them"},
             "expect": "Stop taking the mouse; explain why; alternative approach"},
        ]
    },
    # Prompt 16: Story & Storyboard
    {
        "prompt_file": "16-story-storyboard.md",
        "tests": [
            {"name": "vague_idea_young", 
             "input": {"age": 10, "idea": "a cat does something funny"},
             "expect": "4-panel story; cat character; simple structure; 10-20 sec"},
            {"name": "has_character", 
             "input": {"age": 12, "idea": "", "characters": [{"name": "Blobby", "trait": "bouncy"}]},
             "expect": "6-panel story around Blobby; wants + obstacles"},
            {"name": "action_scene", 
             "input": {"age": 14, "idea": "parkour chase scene", "tool": "blender"},
             "expect": "8-panel action; varied camera; escalation; principle per shot"},
            {"name": "short_film", 
             "input": {"age": 16, "idea": "a robot learns to dance", "duration": 60},
             "expect": "Full 8-12 panel; story structure; pacing notes; staging"},
            {"name": "no_idea", 
             "input": {"age": 11, "idea": ""},
             "expect": "Asks 'what if' questions; offers 3 prompts to spark ideas"},
            {"name": "too_ambitious", 
             "input": {"age": 10, "idea": "full 10 minute movie"},
             "expect": "Gently scales down; 10 sec vs 10 min; start small"},
        ]
    },
    # Prompt 17: History & Inspiration
    {
        "prompt_file": "17-history-inspiration.md",
        "tests": [
            {"name": "learning_opentoonz", 
             "input": {"context": "learning-opentoonz"},
             "expect": "Studio Ghibli connection; same software; 'using Ghibli's tool'"},
            {"name": "anime_origins", 
             "input": {"question": "how did anime start"},
             "expect": "Tezuka + Astro Boy; limited animation as choice; connects"},
            {"name": "spider_verse_fan", 
             "input": {"context": "saw-spider-verse"},
             "expect": "12fps choice; rule-breaking; try-it: animate at 12fps on purpose"},
            {"name": "flipbook_curiosity", 
             "input": {"question": "what's the oldest animation"},
             "expect": "Thaumatrope/zoetrope/flipbook; persistence of vision; make-a-flipbook"},
            {"name": "no_question", 
             "input": {},
             "expect": "Picks inspiring fact for age; asks what they're curious about"},
            {"name": "discouraged_kid", 
             "input": {"situation": "discouraged"},
             "expect": "Story of how masters started; Glen Keane advice; connection"},
        ]
    },
    # Prompt 18: Workflow & File Management
    {
        "prompt_file": "18-workflow-file-management.md",
        "tests": [
            {"name": "getting_started_workflow", 
             "input": {"age": 12, "tool": "krita", "issue": "getting started"},
             "expect": "Folder structure; pre-flight checklist; Krita-specific setup"},
            {"name": "lost_file", 
             "input": {"age": 14, "tool": "blender", "issue": "lost a file"},
             "expect": "Search steps; empathy; naming fix for next time"},
            {"name": "dont_know_export", 
             "input": {"age": 11, "tool": "pencil2d", "issue": "don't know how to export"},
             "expect": "Exact menu path; format/fps/resolution settings"},
            {"name": "files_are_mess", 
             "input": {"age": 13, "tool": "any", "issue": "files are a mess"},
             "expect": "5-step cleanup plan; folder structure; naming pattern"},
            {"name": "general_workflow_young", 
             "input": {"age": 10, "issue": "general workflow"},
             "expect": "3 age-appropriate habits; simple; no folder tree overwhelm"},
            {"name": "scratch_export", 
             "input": {"age": 12, "tool": "scratch", "issue": "don't know how to export"},
             "expect": "Screen recording or TurboWarp; explains Scratch limitation"},
        ]
    },
]

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str) -> str:
    """Load a prompt file and extract just the prompt text (between ``` markers)."""
    path = PROMPTS_DIR / filename
    content = path.read_text()
    # Extract text between first ``` and last ```
    parts = content.split("```")
    if len(parts) >= 3:
        # Return the text between first pair of ``` markers
        # (strip language identifier if present)
        prompt_text = parts[1]
        if prompt_text.startswith("markdown\n"):
            prompt_text = prompt_text[9:]
        return prompt_text.strip()
    return content


def list_prompts():
    """List all prompts and their test cases."""
    for entry in TEST_CASES:
        print(f"\n{'='*60}")
        print(f"Prompt: {entry['prompt_file']}")
        print(f"{'='*60}")
        for i, test in enumerate(entry["tests"], 1):
            print(f"  Test {i}: {test['name']}")
            print(f"    Input:   {json.dumps(test['input'])}")
            print(f"    Expect:  {test['expect']}")


def run_tests(prompt_filter: str = None, interactive: bool = True):
    """Run test cases, optionally filtered by prompt number."""
    for entry in TEST_CASES:
        prompt_num = entry["prompt_file"][:2]
        if prompt_filter and prompt_filter != prompt_num:
            continue
        
        prompt_text = load_prompt(entry["prompt_file"])
        
        print(f"\n{'='*70}")
        print(f"PROMPT: {entry['prompt_file']}")
        print(f"{'='*70}")
        print(f"\n--- PROMPT TEXT ({len(prompt_text)} chars) ---\n")
        print(prompt_text[:500] + "..." if len(prompt_text) > 500 else prompt_text)
        
        for test in entry["tests"]:
            print(f"\n{'─'*50}")
            print(f"TEST: {test['name']}")
            print(f"INPUT: {json.dumps(test['input'], indent=2)}")
            print(f"EXPECTED: {test['expect']}")
            print(f"{'─'*50}")
            
            if interactive:
                print("\n[This is where you'd send the prompt + input to your LLM]")
                print("[Review the response against EXPECTED above]")
                input("\nPress Enter for next test case (Ctrl+C to stop)...")


def main():
    parser = argparse.ArgumentParser(description="Test harness for animation assistant prompts")
    parser.add_argument("--prompt", type=str, help="Run tests for a specific prompt (e.g., '03')")
    parser.add_argument("--list", action="store_true", help="List all prompts and test cases")
    parser.add_argument("--non-interactive", action="store_true", help="Print all tests without pausing")
    
    args = parser.parse_args()
    
    if args.list:
        list_prompts()
    else:
        run_tests(prompt_filter=args.prompt, interactive=not args.non_interactive)


if __name__ == "__main__":
    main()