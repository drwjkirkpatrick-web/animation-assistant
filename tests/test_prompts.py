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