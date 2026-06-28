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
    # Prompt 19: Color Theory & Visual Design
    {
        "prompt_file": "19-color-design.md",
        "tests": [
            {"name": "color_combos", 
             "input": {"age": 12, "question": "what colors look good together"},
             "expect": "Color wheel basics; complementary/analogous; 60-30-10 rule; try-it"},
            {"name": "flat_scenes", 
             "input": {"age": 14, "tool": "krita", "question": "my scenes look flat"},
             "expect": "Rule of thirds; foreground/middle/background; silhouette test; Krita tips"},
            {"name": "lighting_basics", 
             "input": {"age": 15, "tool": "blender", "question": "how do I light a scene"},
             "expect": "Light direction = mood; rim light; Blender lamp tips; ball try-it"},
            {"name": "mood_color", 
             "input": {"age": 13, "scene": "sad character walking"},
             "expect": "Cool colors; desaturated; dark; analogous blues/greys; try-it"},
            {"name": "rainbow_chaos", 
             "input": {"age": 10, "scene": "rainbow character"},
             "expect": "60-30-10 rule; one accent color; rainbow chaos fix; try-it"},
            {"name": "silhouette_test", 
             "input": {"age": 16, "question": "how do I know if my pose is good"},
             "expect": "Silhouette test; fill black; if you can't read it, redo"},
        ]
    },
    # Prompt 20: Sound & Audio Design
    {
        "prompt_file": "20-sound-audio-design.md",
        "tests": [
            {"name": "feels_empty", 
             "input": {"age": 13, "question": "feels empty"},
             "expect": "Identifies missing layers; quick win = footsteps; free resources"},
            {"name": "ball_sound", 
             "input": {"age": 11, "tool": "scratch", "scene": "ball bouncing"},
             "expect": "Scratch sound blocks; boing vs thud = different story; try-it"},
            {"name": "lip_sync_audio", 
             "input": {"age": 15, "tool": "krita", "question": "how to add voices"},
             "expect": "Record with phone; import audio; waveform; Krita steps"},
            {"name": "chase_music", 
             "input": {"age": 14, "question": "what music for a chase scene"},
             "expect": "Fast tempo; doesn't fight action; free sources; volume guidance"},
            {"name": "no_sound", 
             "input": {"age": 10, "scene": "scratch cat walking"},
             "expect": "4 layers explained simply; start with SFX; Scratch import"},
            {"name": "diy_sfx", 
             "input": {"age": 12, "question": "how do I make sound effects"},
             "expect": "DIY sound list; phone recording; Audacity for editing"},
        ]
    },
    # Prompt 21: Rigging Deep Dive
    {
        "prompt_file": "21-rigging-deep-dive.md",
        "tests": [
            {"name": "first_rig", 
             "input": {"age": 13, "tool": "synfig", "level": "recommend"},
             "expect": "Level 1-2; Synfig skeleton steps; simple character advice"},
            {"name": "blender_rig", 
             "input": {"age": 16, "tool": "blender", "level": 3},
             "expect": "IK/FK; weight painting; constraints; Blender-specific"},
            {"name": "should_i_rig", 
             "input": {"age": 12, "character": "bouncing ball"},
             "expect": "No — frame-by-frame better for squash & stretch; explains why"},
            {"name": "walk_cycle_rig", 
             "input": {"age": 14, "tool": "opentoonz", "level": 2},
             "expect": "Bone rig steps; OpenToonz skeleton + plastic; hip importance"},
            {"name": "pivot_scratch", 
             "input": {"age": 11, "tool": "scratch", "level": 1},
             "expect": "Sprite-per-part; turn blocks; pivot = costume center"},
            {"name": "rig_broken", 
             "input": {"age": 15, "tool": "blender", "issue": "arm moves torso"},
             "expect": "Weight painting fix; common mistake; re-bind steps"},
        ]
    },
    # Prompt 22: Compositing & Rendering
    {
        "prompt_file": "22-compositing-rendering.md",
        "tests": [
            {"name": "unfinished", 
             "input": {"age": 14, "question": "looks unfinished"},
             "expect": "Compositing: vignette + contact shadow; quick polish; layering"},
            {"name": "krita_export", 
             "input": {"age": 13, "tool": "krita", "question": "export"},
             "expect": "Render Animation menu path; MP4 settings; FPS + resolution"},
            {"name": "blender_lost", 
             "input": {"age": 16, "tool": "blender", "question": "where did my render go"},
             "expect": "Output path check; Blender /tmp default; pre-render checklist"},
            {"name": "scratch_export_comp", 
             "input": {"age": 11, "tool": "scratch", "question": "export"},
             "expect": "Screen record or TurboWarp; Scratch limitation; 30fps"},
            {"name": "add_effects", 
             "input": {"age": 15, "tool": "blender", "question": "compositing", "scene": "dusty room"},
             "expect": "Particle dust; atmosphere layer; compositing nodes in Blender"},
            {"name": "first_render", 
             "input": {"age": 12, "tool": "pencil2d", "question": "render"},
             "expect": "Export Movie steps; format/fps; pre-render checklist; encouragement"},
        ]
    },
    # Prompt 23: Portfolio & Career
    {
        "prompt_file": "23-portfolio-career.md",
        "tests": [
            {"name": "14yo_beginner", 
             "input": {"age": 14, "experience": "beginner", "interest": "character-animation"},
             "expect": "Foundation building; save everything; focus on fundamentals; no reel yet"},
            {"name": "16yo_intermediate", 
             "input": {"age": 16, "experience": "intermediate", "interest": "not-sure"},
             "expect": "Career paths overview; try different types; start first demo reel"},
            {"name": "17yo_reel", 
             "input": {"age": 17, "experience": "advanced", "interest": "effects", "current_work": "some fire animations"},
             "expect": "Refine reel; effects-specific; ArtStation; Houdini; 11 Second Club"},
            {"name": "indie_path", 
             "input": {"age": 15, "interest": "independent"},
             "expect": "Everything-skill path; YouTube/Patreon; make shorts monthly; build audience"},
            {"name": "rigging_career", 
             "input": {"age": 16, "interest": "rigging"},
             "expect": "Rigger/TD path; Python mention; rigging reel; Blender tutorials"},
            {"name": "school_question", 
             "input": {"age": 17, "question": "do I need animation school"},
             "expect": "Both paths valid; reel > degree; school = connections; honest comparison"},
        ]
    },
    # Prompt 24: Animation Styles & Techniques
    {
        "prompt_file": "24-styles-techniques.md",
        "tests": [
            {"name": "drawing_kid", 
             "input": {"age": 13, "interest": "drawing"},
             "expect": "Frame-by-frame + rotoscope; Krita; Ghibli examples; bouncing ball try-it"},
            {"name": "lego_kid", 
             "input": {"age": 11, "interest": "lego"},
             "expect": "Stop motion + cut-out; Stop Motion Studio; Wallace & Gromit; LEGO try-it"},
            {"name": "coding_kid", 
             "input": {"age": 12, "interest": "coding"},
             "expect": "Motion graphics + pixel art; Scratch/Piskel; game examples; name animation"},
            {"name": "3d_interest", 
             "input": {"age": 15, "interest": "3d"},
             "expect": "3D animation; Blender; Spider-Verse; cube bounce try-it"},
            {"name": "not_sure_style", 
             "input": {"age": 14, "interest": "not sure"},
             "expect": "3 diverse styles; try all; low-commitment try-its for each"},
            {"name": "all_styles", 
             "input": {"age": 16, "question": "what styles are there"},
             "expect": "All 11 styles summarized; deep dive on 2; style mixing note"},
        ]
    },
    # Prompt 25: Collaboration & Team
    {
        "prompt_file": "25-collaboration-team.md",
        "tests": [
            {"name": "two_friends", 
             "input": {"age": "10-12", "group_size": 2, "project": "short animation"},
             "expect": "Buddy model; one character/one background; swap roles; Scratch/stop motion"},
            {"name": "team_of_4", 
             "input": {"age": 13, "group_size": 4, "project": "30 second scene"},
             "expect": "Small team roles; director/animator/BG/sound; pipeline; feedback rules"},
            {"name": "animation_club", 
             "input": {"age": 15, "group_size": 8, "project": "short film"},
             "expect": "Studio model; full roles; weekly check-ins; pipeline; quality consistency"},
            {"name": "solo_looking", 
             "input": {"age": 14, "group_size": "solo looking"},
             "expect": "Online communities; 11 Second Club; Reddit; Scratch remix collaboration"},
            {"name": "style_clash", 
             "input": {"age": 12, "conflict": "our drawings look different"},
             "expect": "Character sheet solution; one does character one does environment"},
            {"name": "slacker_member", 
             "input": {"age": 15, "conflict": "one person isn't doing their part"},
             "expect": "Director talks to them; reassign; producer role; honest communication"},
        ]
    },
    # Prompt 26: Raspberry Pi & Low-Resource
    {
        "prompt_file": "26-raspberry-pi-low-resource.md",
        "tests": [
            {"name": "pi4_beginner", 
             "input": {"age": 12, "hardware": "raspberry-pi-4", "experience": "none"},
             "expect": "Scratch on Pi; Pi Foundation projects; performance note; cooling tip"},
            {"name": "pi5_camera", 
             "input": {"age": 14, "hardware": "raspberry-pi-5", "has_camera": True, "interest": "stop-motion"},
             "expect": "Push-button stop motion; picamzero + ffmpeg; install commands; project"},
            {"name": "pi3_limits", 
             "input": {"age": 15, "hardware": "raspberry-pi-3", "interest": "3d"},
             "expect": "Honest: Blender won't run; Python/Pygame or Scratch; upgrade path"},
            {"name": "chromebook", 
             "input": {"age": 13, "hardware": "chromebook", "interest": "drawing"},
             "expect": "Scratch + Piskel in browser; no desktop tools; what works vs doesn't"},
            {"name": "old_laptop", 
             "input": {"age": 14, "hardware": "old-laptop", "experience": "some"},
             "expect": "Pencil2D + Scratch; install Linux if slow; performance expectations"},
            {"name": "phone_only", 
             "input": {"age": 11, "hardware": "phone-tablet", "experience": "none"},
             "expect": "Stop Motion Studio + FlipaClip; phone is a real animation tool; first project"},
        ]
    },
    # Prompt 27: Kid-Friendly FAQ
    {
        "prompt_file": "27-kid-friendly-faq.md",
        "tests": [
            {"name": "cant_draw", 
             "input": {"age": 12, "question": "do I need to be good at drawing"},
             "expect": "No! Lists non-drawing styles; stop motion, 3D, motion graphics; module 24"},
            {"name": "what_computer", 
             "input": {"age": 11, "question": "what computer do I need"},
             "expect": "Almost anything; Scratch in browser; Stop Motion on phone; module 26"},
            {"name": "how_long", 
             "input": {"age": 13, "question": "how long does it take to make an animation"},
             "expect": "Honest time estimates; patience is core skill; bouncing ball = 30 min"},
            {"name": "sliding_walk", 
             "input": {"age": 14, "question": "my character slides when walking"},
             "expect": "Contact frame explanation; foot planting; module 07"},
            {"name": "make_money", 
             "input": {"age": 15, "question": "can I make money from animation"},
             "expect": "Yes; YouTube, freelance, commissions, career; passion first; module 23"},
            {"name": "use_ai", 
             "input": {"age": 16, "question": "can I use AI to animate"},
             "expect": "Learning: no. Product: limited. AI is tool not replacement; joy is in making"},
            {"name": "not_in_faq", 
             "input": {"age": 13, "question": "what's the best tablet for animation"},
             "expect": "Answers in same style; honest recommendation; notes not in FAQ; adds to knowledge"},
        ]
    },
    # Prompt 28: Acting for Animation
    {
        "prompt_file": "28-acting-for-animation.md",
        "tests": [
            {"name": "robotic", 
             "input": {"age": 14, "question": "my character looks robotic"},
             "expect": "No thought process; see-think-act chain; eyes lead; weight shift; mirror"},
            {"name": "sad_walk_act", 
             "input": {"age": 13, "emotion": "sad", "scene": "walking"},
             "expect": "Hunched posture; slow shuffling; eyes down; hands close; mirror; table"},
            {"name": "angry_reaction", 
             "input": {"age": 15, "emotion": "angry", "scene": "character finds broken vase"},
             "expect": "Jaw clench; forward lean; sharp movement; nostril flare; 3-frame pause"},
            {"name": "eye_acting", 
             "input": {"age": 16, "question": "how do I make eyes expressive"},
             "expect": "Eyes lead body; dart/hold/look away; blink on thought change; 70/30 rule"},
            {"name": "first_acting", 
             "input": {"age": 12, "experience": "beginner", "question": "general"},
             "expect": "Mirror exercise first; eyebrow + mouth = 80%; permission to be silly"},
            {"name": "dialogue_scene", 
             "input": {"age": 16, "scene": "two characters arguing"},
             "expect": "Eye contact 70/30; thought pauses; micro-expressions; silence as power"},
        ]
    },
    # Prompt 29: Animation Physics & Weight
    {
        "prompt_file": "29-animation-physics.md",
        "tests": [
            {"name": "floaty_animation", 
             "input": {"age": 14, "problem": "looks floaty"},
             "expect": "Weight gain/loss; add frames at impact; Odd Rule spacing; squash"},
            {"name": "ball_too_light", 
             "input": {"age": 12, "scene": "bouncing ball", "problem": "too light"},
             "expect": "Odd Rule for fall; Fourth Down at Half Time; heavy = more ground frames"},
            {"name": "character_slides", 
             "input": {"age": 15, "problem": "sliding"},
             "expect": "Inertia: body parts stop at different times; weight shift; friction"},
            {"name": "falling_character", 
             "input": {"age": 16, "scene": "character jumps off roof"},
             "expect": "Scale = timing; 12 frames = 4 feet; Odd Rule; impact reaction"},
            {"name": "push_heavy", 
             "input": {"age": 14, "scene": "pushing a boulder"},
             "expect": "Momentum + force; lean into it (CoG); feet push ground; slow start"},
            {"name": "run_stop", 
             "input": {"age": 15, "scene": "character stops running"},
             "expect": "Inertia: feet stop first, then knees, hips, shoulders, head; stumble"},
        ]
    },
    # Prompt 30: Character Design & Shape Language
    {
        "prompt_file": "30-character-design.md",
        "tests": [
            {"name": "friendly_hero", 
             "input": {"age": 12, "personality": "brave, kind, loyal"},
             "expect": "Circles dominant; Baymax/Totoro; silhouette test; simple model sheet"},
            {"name": "villain_design", 
             "input": {"age": 14, "personality": "cunning, dangerous, elegant"},
             "expect": "Triangles dominant; Maleficent; sharp features; dark/saturated color"},
            {"name": "comic_relief", 
             "input": {"age": 11, "personality": "clumsy, funny, loyal"},
             "expect": "Mixed circles + squares; big body small head; goofy proportions"},
            {"name": "first_character", 
             "input": {"age": 10, "concept": "I want to make a character"},
             "expect": "Start with personality; pick shape; silhouette first; 2-3 colors"},
            {"name": "anime_style", 
             "input": {"age": 15, "style": "anime", "concept": "a samurai girl"},
             "expect": "Shape language applies; mix triangles + circles; model sheet"},
            {"name": "pixel_char", 
             "input": {"age": 13, "style": "pixel-art"},
             "expect": "16x16 or 32x32; limited colors; readable silhouette; shape in pixels"},
        ]
    },
    # Prompt 31: Camera & Cinematography
    {
        "prompt_file": "31-camera-cinematography.md",
        "tests": [
            {"name": "boring_shots", 
             "input": {"age": 14, "question": "my shots are boring"},
             "expect": "Vary shot types; rule of thirds; add close-ups; try push-in"},
            {"name": "conversation", 
             "input": {"age": 15, "scene": "two characters talking"},
             "expect": "180-degree rule; over-shoulder; medium close-ups; screen direction"},
            {"name": "chase_scene", 
             "input": {"age": 13, "scene": "character running"},
             "expect": "Tracking shots; lead room; screen direction; wide for action"},
            {"name": "flat_2d", 
             "input": {"age": 12, "tool": "krita", "question": "feels flat"},
             "expect": "Parallax layers; foreground framing; depth; Krita layer technique"},
            {"name": "blender_camera", 
             "input": {"age": 16, "tool": "blender", "question": "how do cameras work"},
             "expect": "Add camera; Track To; Numpad 0; focal length; graph editor"},
            {"name": "first_plan", 
             "input": {"age": 11, "tool": "scratch", "scene": "cat walks to a door"},
             "expect": "3-shot plan: wide to medium to close-up; Scratch simulation tips"},
        ]
    },
    # Prompt 32: Advanced Body Mechanics
    {
        "prompt_file": "32-body-mechanics.md",
        "tests": [
            {"name": "first_run_cycle", 
             "input": {"age": 14, "topic": "run-cycle", "experience": "can walk cycle"},
             "expect": "4 key poses; flight phase; forward lean; frame counts"},
            {"name": "jump_physics", 
             "input": {"age": 13, "topic": "jump"},
             "expect": "5 phases; squat determines height; parabolic arc; Odd Rule; landing squash"},
            {"name": "weight_shift", 
             "input": {"age": 15, "topic": "weight-shift"},
             "expect": "Why it matters; 4-step sequence; when to show; breathing sway"},
            {"name": "dog_walk", 
             "input": {"age": 16, "topic": "quadruped", "character": "dog"},
             "expect": "Diagonal pairs; spine flexes; head counterbalance; 4 key poses"},
            {"name": "cant_walk_yet", 
             "input": {"age": 12, "topic": "run-cycle", "experience": "none"},
             "expect": "Redirect to module 03; learn walk before run"},
            {"name": "gallop", 
             "input": {"age": 17, "topic": "quadruped", "character": "horse galloping"},
             "expect": "Gallop gait; back then front; big flight phase; spine arch"},
        ]
    },
    # Prompt 33: Facial Animation & Expressions
    {
        "prompt_file": "33-facial-animation.md",
        "tests": [
            {"name": "blank_face", 
             "input": {"age": 14, "question": "my character's face is blank"},
             "expect": "3 zones; start with eyes; brows lead; 6 universal expressions"},
            {"name": "surprise", 
             "input": {"age": 13, "emotion": "surprised"},
             "expect": "Brows up, eyes wide, mouth open; eyes first; 2-frame rule"},
            {"name": "lip_sync_basics", 
             "input": {"age": 15, "dialogue": "hello world"},
             "expect": "6-8 mouth shapes; open 2 frames early; group sounds; tool steps"},
            {"name": "blender_face_rig", 
             "input": {"age": 16, "tool": "blender", "question": "how to rig a face"},
             "expect": "Shape keys; base + targets; animate values; bone-driven option"},
            {"name": "eye_darts", 
             "input": {"age": 15, "question": "how do eyes move"},
             "expect": "Dart = 1-2 frame snap; 3-5 frame hold; tracking exception; 70/30 rule"},
            {"name": "mixed_emotion", 
             "input": {"age": 17, "emotion": "betrayed"},
             "expect": "Blend sad + angry; brows down + frown + tension; asymmetric"},
        ]
    },
    # Prompt 34: Special Effects Animation
    {
        "prompt_file": "34-special-effects.md",
        "tests": [
            {"name": "first_fire", 
             "input": {"age": 13, "effect": "fire", "tool": "krita"},
             "expect": "Frame-by-frame; 6-12 frame cycle; always goes up; flicker; layering"},
            {"name": "water_splash", 
             "input": {"age": 14, "effect": "water", "scene": "ball drops in water"},
             "expect": "Crown splash; droplets in arcs; ripples; 1-2 seconds total"},
            {"name": "explosion", 
             "input": {"age": 15, "effect": "explosion", "tool": "blender"},
             "expect": "3 phases; flash to fire to smoke; debris in arcs; screen shake"},
            {"name": "magic_spell", 
             "input": {"age": 12, "effect": "magic", "scene": "character casts a spell"},
             "expect": "Charge to release to impact to dissipate; glow; spiral; particles"},
            {"name": "smoke", 
             "input": {"age": 16, "effect": "smoke", "scene": "campfire"},
             "expect": "Tumbles; expands; fades; 3-5 overlapping puffs; opacity"},
            {"name": "scratch_particles", 
             "input": {"age": 11, "effect": "magic", "tool": "scratch"},
             "expect": "Clone blocks; random direction; fireworks or sparkles; lifetime"},
        ]
    },
    # Prompt 35: Timing Charts & Spacing
    {
        "prompt_file": "35-timing-charts.md",
        "tests": [
            {"name": "ball_chart", 
             "input": {"age": 13, "scene": "bouncing ball", "tool": "krita"},
             "expect": "Odd Rule spacing chart; 1,3,5,7 falling; snap up; draw the chart"},
            {"name": "walk_chart", 
             "input": {"age": 14, "scene": "walk cycle"},
             "expect": "Horizontal chart; contact/passing; equal-ish spacing; breakdowns"},
            {"name": "constant_speed", 
             "input": {"age": 12, "problem": "looks robotic"},
             "expect": "Linear spacing; switch to ease in/out; linear = robotic"},
            {"name": "blender_graph", 
             "input": {"age": 16, "tool": "blender", "question": "how to use graph editor"},
             "expect": "F-curves; shape = spacing; ease in/out curves; avoid linear"},
            {"name": "first_chart", 
             "input": {"age": 11, "question": "what is a timing chart"},
             "expect": "Simple explanation; map before drive; key frames first"},
            {"name": "jump_spacing", 
             "input": {"age": 15, "scene": "character jump"},
             "expect": "5 phases; Odd Rule for fall; Fourth Down at Half Time; ease out"},
        ]
    },
    # Prompt 36: Accessibility & Adaptive Animation
    {
        "prompt_file": "36-accessibility-adaptive.md",
        "tests": [
            {"name": "motor_difficulty", 
             "input": {"age": 12, "need": "motor", "specific": "trouble holding pen"},
             "expect": "Touchscreen, stop motion, large brushes, Scratch blocks; tactile"},
            {"name": "low_vision", 
             "input": {"age": 14, "need": "visual", "specific": "low vision"},
             "expect": "High contrast, large UI, zoom, pixel art, stop motion"},
            {"name": "adhd", 
             "input": {"age": 13, "need": "cognitive", "specific": "ADHD, loses focus"},
             "expect": "Short projects, timer work, daily challenges, one tool, badges"},
            {"name": "autism", 
             "input": {"age": 15, "need": "sensory", "specific": "autism, sensory sensitive"},
             "expect": "Reduce visual noise, predictable workflow, written instructions, interests"},
            {"name": "one_hand", 
             "input": {"age": 16, "need": "motor", "specific": "only one hand works"},
             "expect": "Keyboard shortcuts, one-handed tablet, cut-out/tweening, Blender"},
            {"name": "parent_asking", 
             "input": {"role": "parent", "need": "motor", "age": 10, "question": "can my kid animate"},
             "expect": "Yes! Stop motion, Scratch, touchscreen; start with what they CAN do"},
        ]
    },
    # Prompt 37: Community & Online Etiquette
    {
        "prompt_file": "37-community-etiquette.md",
        "tests": [
            {"name": "first_share", 
             "input": {"age": 12, "question": "where do I share my animation"},
             "expect": "Scratch first; safe moderated; how to title; include context"},
            {"name": "wants_feedback", 
             "input": {"age": 14, "platform": "reddit", "question": "how to ask for feedback"},
             "expect": "Specific questions; humble; sandwich method; one thing at a time"},
            {"name": "harsh_comment", 
             "input": {"age": 13, "situation": "someone said it looks bad"},
             "expect": "Separate work from self; vague negativity = ignore; step away"},
            {"name": "giving_feedback", 
             "input": {"age": 15, "question": "how do I give good feedback"},
             "expect": "Sandwich method; specific; one thing; suggest dont command; principle names"},
            {"name": "posting_anxiety", 
             "input": {"age": 11, "situation": "scared to post"},
             "expect": "Start with Scratch; family first; fear is normal; every pro started beginner"},
            {"name": "safety", 
             "input": {"role": "parent", "age": 11, "question": "is it safe to post"},
             "expect": "Scratch moderated; privacy settings; teach online safety; check comments"},
        ]
    },
    # Prompt 38: Contests, Festivals & Challenges
    {
        "prompt_file": "38-contests-festivals.md",
        "tests": [
            {"name": "first_contest", 
             "input": {"age": 13, "experience": "beginner", "interest": "contest"},
             "expect": "School/Scratch first; 11 Second Club next; start small"},
            {"name": "11_second_club", 
             "input": {"age": 15, "interest": "challenge", "experience": "intermediate"},
             "expect": "Monthly; audio provided; 11 seconds; any tool; submit MP4; forum feedback"},
            {"name": "film_festival", 
             "input": {"age": 16, "interest": "festival", "experience": "advanced"},
             "expect": "FilmFreeway search; free student festivals; submission package; synopsis"},
            {"name": "env_theme", 
             "input": {"age": 14, "interest": "contest", "theme": "environment"},
             "expect": "One Earth Young Filmmakers; 45s-8min; environmental action; free; annual"},
            {"name": "dont_know_where", 
             "input": {"age": 12, "interest": "not-sure"},
             "expect": "Scratch Design Studio; school art show; PTA Reflections; start local"},
            {"name": "didnt_win", 
             "input": {"age": 14, "situation": "entered and didn't win"},
             "expect": "Finishing IS winning; watch winners; learn; enter next; persistence > talent"},
        ]
    },
    # Prompt 39: Animation Editing & Post-Production
    {
        "prompt_file": "39-animation-editing.md",
        "tests": [
            {"name": "first_edit", 
             "input": {"age": 14, "question": "how do I put shots together"},
             "expect": "OpenShot workflow; import shots; arrange timeline; add audio; export"},
            {"name": "planning_stage", 
             "input": {"age": 15, "stage": "planning", "project": "short film"},
             "expect": "Radio play first; animatic; edit before animate; 4 extra frames"},
            {"name": "post_prod", 
             "input": {"age": 16, "stage": "post-production", "tool": "blender"},
             "expect": "VSE; replace animatic with finals; SFX/music; color; render"},
            {"name": "frame_rate_q", 
             "input": {"age": 14, "question": "what does on 2s mean"},
             "expect": "1s vs 2s vs 3s; 12 drawings/sec; classic cartoon look; speed manipulation"},
            {"name": "when_to_cut", 
             "input": {"age": 13, "question": "when should I cut between shots"},
             "expect": "Cut on action; new speaker=new shot; 1-2 sec minimum; don't hold too long"},
            {"name": "version_ctrl", 
             "input": {"age": 16, "question": "how do I manage different versions"},
             "expect": "Keep all versions; compare; combine; naming convention; don't delete"},
        ]
    },
    # Prompt 40: Background & Environment Design
    {
        "prompt_file": "40-background-design.md",
        "tests": [
            {"name": "boring_bgs", 
             "input": {"age": 13, "question": "my backgrounds are boring"},
             "expect": "3-layer depth; atmosphere perspective; foreground silhouette; clutter"},
            {"name": "first_room", 
             "input": {"age": 12, "scene_type": "interior", "tool": "krita"},
             "expect": "1-point perspective; window light; furniture; clutter; Krita layers"},
            {"name": "outdoor_peaceful", 
             "input": {"age": 14, "scene_type": "exterior", "mood": "peaceful"},
             "expect": "2-point perspective; atmosphere perspective; warm colors; rounded shapes"},
            {"name": "fantasy_world", 
             "input": {"age": 15, "scene_type": "fantasy", "tool": "blender"},
             "expect": "3D environment; unusual architecture; grounded lighting; Blender setup"},
            {"name": "abstract_bg", 
             "input": {"age": 11, "scene_type": "abstract"},
             "expect": "Gradient + vignette; character IS the scene; minimal = focus on character"},
            {"name": "scary_mood", 
             "input": {"age": 14, "mood": "scary"},
             "expect": "Dark colors; sharp angles; low angle; minimal light; sharp shadows"},
        ]
    },
    # Prompt 41: Anatomy & Figure Drawing
    {
        "prompt_file": "41-anatomy-figure-drawing.md",
        "tests": [
            {"name": "stiff_chars", 
             "input": {"age": 14, "question": "my characters look stiff"},
             "expect": "Spine S-curve; gesture drawing; construction from skeleton; line of action"},
            {"name": "arms_wrong", 
             "input": {"age": 13, "area": "arms", "question": "arms look broken"},
             "expect": "Elbow hinge one way; bicep/tricep pairs; deltoid; construction"},
            {"name": "first_anatomy", 
             "input": {"age": 12, "experience": "none", "question": "where do I start"},
             "expect": "Gesture drawing 30sec; simple skeleton; joints not bone middles; mirror"},
            {"name": "cartoon_anatomy", 
             "input": {"age": 15, "style": "cartoon", "question": "do I need anatomy for cartoons"},
             "expect": "Yes but simplified; know rules to break them; Chuck Jones; exaggeration"},
            {"name": "legs_walking", 
             "input": {"age": 14, "area": "legs", "question": "how do legs work"},
             "expect": "Hip ball joint; knee hinge; quad/hamstring pairs; calves; weight shift"},
            {"name": "cute_props", 
             "input": {"age": 11, "style": "cute", "question": "how to draw cute characters"},
             "expect": "2-3 heads tall; big head; short legs; rounded; child proportions"},
        ]
    },
    # Prompt 42: Voice Acting & Dialogue Recording
    {
        "prompt_file": "42-voice-acting.md",
        "tests": [
            {"name": "first_voice", 
             "input": {"age": 12, "question": "how do I voice my character"},
             "expect": "Find feeling; match pitch to size; exaggerate; move whole body; phone"},
            {"name": "grumpy_cat", 
             "input": {"age": 13, "character": "grumpy cat who secretly loves everyone", "role": "voicing"},
             "expect": "Low pitch, raspy; soft underneath; act angry but warm; try-it exercise"},
            {"name": "recording_setup", 
             "input": {"age": 14, "role": "recording", "question": "how do I record"},
             "expect": "Phone/USB mic; 6-8 inches; sock for plosives; quiet room; 3 takes; room tone"},
            {"name": "directing_friend", 
             "input": {"age": 15, "role": "directing", "character": "excited robot"},
             "expect": "Explain character; demonstrate; bigger—this is a cartoon; 3 takes; be kind"},
            {"name": "dialogue_editing", 
             "input": {"age": 16, "role": "editing", "question": "how to clean up audio"},
             "expect": "Audacity; noise reduction; normalize -3dB; cut pauses; keep breaths; WAV"},
            {"name": "voice_hurts", 
             "input": {"age": 13, "question": "my throat hurts from doing voices"},
             "expect": "STOP; too high/low/forced; drink water; 15min on 5min off; don't damage"},
        ]
    },
    # Prompt 43: Music Synchronization & Beat Sync
    {
        "prompt_file": "43-music-sync.md",
        "tests": [
            {"name": "first_sync", 
             "input": {"age": 12, "question": "how do I animate to music"},
             "expect": "Beat marking method; flash test; sync big hits first; try-it"},
            {"name": "walk_to_beat", 
             "input": {"age": 13, "scene": "walk cycle", "music_bpm": 120, "tool": "krita"},
             "expect": "12fps: 6 frames/beat; step on beat; import audio; waveform; scrub"},
            {"name": "chase_scene", 
             "input": {"age": 15, "scene": "chase", "question": "what tempo"},
             "expect": "120-140 BPM; fast impacts on downbeats; free sources; YouTube Audio Library"},
            {"name": "off_beat", 
             "input": {"age": 14, "question": "my animation doesn't feel right with music"},
             "expect": "Check beat alignment; impacts off beat; re-mark beats; sync big moments"},
            {"name": "blender_sync", 
             "input": {"age": 16, "tool": "blender", "music_bpm": 140},
             "expect": "Markers (M key); ~8.5 frames/beat at 24fps; VSE audio; graph editor"},
            {"name": "slow_emotional", 
             "input": {"age": 14, "scene": "sad scene", "question": "what BPM"},
             "expect": "60-80 BPM; slow impacts; hold between beats; Incompetech free music"},
        ]
    },
    # Prompt 44: Mixed Media & Experimental
    {
        "prompt_file": "44-mixed-media.md",
        "tests": [
            {"name": "something_diff", 
             "input": {"age": 13, "interest": "something different"},
             "expect": "2-3 approaches; collage or photo+drawing; try-it; inspiring examples"},
            {"name": "phone_only", 
             "input": {"age": 12, "tools": ["phone"], "interest": "mixed media"},
             "expect": "Stop motion collage; material animation; Stop Motion Studio; physical"},
            {"name": "photo_drawing", 
             "input": {"age": 14, "interest": "photo and drawing", "tool": "krita"},
             "expect": "Photo as background; draw on top; surreal contrast; Krita layers"},
            {"name": "two_d_three_d", 
             "input": {"age": 16, "interest": "2D 3D mix", "tool": "blender"},
             "expect": "Render 3D with alpha; composite 2D on top; Spider-Verse reference"},
            {"name": "typography", 
             "input": {"age": 13, "interest": "text animation", "tool": "scratch"},
             "expect": "Sprite per letter; bounce/stretch/morph; time to beat; movie titles"},
            {"name": "experimental", 
             "input": {"age": 15, "interest": "experimental", "question": "break the rules"},
             "expect": "Eyes-closed drawing; random sounds; one color/shape; destroy and rebuild"},
        ]
    },
    # Prompt 45: Game Animation & Sprite Sheets
    {
        "prompt_file": "45-game-animation.md",
        "tests": [
            {"name": "first_game_anim", 
             "input": {"age": 12, "tool": "scratch", "animation_type": "idle"},
             "expect": "Scratch costumes; idle = breathe + sway; 4-12 frames; loop; most seen"},
            {"name": "walk_platformer", 
             "input": {"age": 13, "tool": "pygame", "animation_type": "walk", "game_type": "platformer"},
             "expect": "8-12 frames; loop; side view; sprite sheet export; pygame blit"},
            {"name": "jump_anim", 
             "input": {"age": 14, "tool": "godot", "animation_type": "jump"},
             "expect": "Not a loop; 5 phases; 10-20 frames; responsive; Godot AnimationPlayer"},
            {"name": "attack_speed", 
             "input": {"age": 15, "tool": "unity", "animation_type": "attack"},
             "expect": "2-3 anticipation, 1-2 strike, 4-6 recovery; fast=responsive; slice"},
            {"name": "sprite_sheet_creation", 
             "input": {"age": 13, "tool": "krita", "question": "how do I make a sprite sheet"},
             "expect": "Export PNG sequence; frame size; packer tool; or Piskel direct export"},
            {"name": "frame_rate_issue", 
             "input": {"age": 14, "question": "animation plays different speeds"},
             "expect": "Frame rate independence; use time not frames; Scratch wait blocks; Pygame ticks"},
        ]
    },
    # Prompt 46: Production & Project Management
    {
        "prompt_file": "46-production-management.md",
        "tests": [
            {"name": "never_finishes", 
             "input": {"age": 14, "problem": "I keep not finishing things"},
             "expect": "Scope check; done definition; done > perfect; 2x rule; daily check-in"},
            {"name": "first_big_project", 
             "input": {"age": 13, "project": "30 second short film", "experience": "first time"},
             "expect": "Scope check; have they finished 10s first?; 3-week timeline; start smaller"},
            {"name": "overscoped", 
             "input": {"age": 12, "project": "10 minute movie", "experience": "first time"},
             "expect": "Scope to 30 seconds; 10 min = months; start small; done > perfect"},
            {"name": "deadline_pressure", 
             "input": {"age": 15, "deadline": "1 week", "project": "30s scene"},
             "expect": "Compressed timeline; cut scope to fit; prioritize; what to cut"},
            {"name": "no_plan", 
             "input": {"age": 13, "project": "walk cycle", "question": "how do I plan"},
             "expect": "3 phases; pre-production first; storyboard; time estimate with 2x rule"},
            {"name": "stuck", 
             "input": {"age": 14, "problem": "stuck on one shot for hours"},
             "expect": "Move on; block everything first; come back to problems; daily check-in"},
        ]
    },
    # Prompt 47: AI Ethics & Animation Tools
    {
        "prompt_file": "47-ai-ethics.md",
        "tests": [
            {"name": "generate_everything", 
             "input": {"age": 14, "stance": "tempted to use AI for everything"},
             "expect": "Learning test; can you make it without AI?; fundamentals matter; joy is making"},
            {"name": "ai_for_reference", 
             "input": {"age": 13, "question": "can I use AI for reference images"},
             "expect": "Yes; AI as tool; generate reference, study it, animate yourself; ethical"},
            {"name": "ai_portfolio", 
             "input": {"age": 16, "question": "can I put AI animation in my portfolio"},
             "expect": "No; recruiters can tell; can't animate live; claim skill you don't have"},
            {"name": "school_project", 
             "input": {"age": 15, "school_context": True, "question": "can I use AI for school animation"},
             "expect": "Check school policy; AI for reference OK; generation probably not; be honest"},
            {"name": "anti_ai", 
             "input": {"age": 14, "stance": "anti-AI"},
             "expect": "Validate concern; AI as tool is fine; replacement is the problem; learn either way"},
            {"name": "industry_question", 
             "input": {"age": 16, "question": "will AI replace animators"},
             "expect": "Fundamentals survive tech change; AI assists not replaces; acting = human"},
        ]
    },
    # Prompt 48: Pacing & Rhythm
    {
        "prompt_file": "48-pacing-rhythm.md",
        "tests": [
            {"name": "feels_boring", 
             "input": {"age": 14, "question": "my animation is boring"},
             "expect": "Pacing issue: not enough contrast; speed map; cut 30% of shots; add fast"},
            {"name": "action_pacing", 
             "input": {"age": 15, "scene_type": "action", "length": "20 seconds"},
             "expect": "70/20/10 split; short shots; build to climax; decelerate; cut on action"},
            {"name": "comedy_timing", 
             "input": {"age": 13, "scene_type": "comedy", "question": "jokes don't land"},
             "expect": "Setup to buildup to punchline to HOLD; hold is where laugh is; 1 frame matters"},
            {"name": "emotional_pacing", 
             "input": {"age": 16, "scene_type": "emotional", "question": "how to pace sadness"},
             "expect": "60% slow; long shots; minimal cuts; let face tell it; audience needs time"},
            {"name": "no_contrast", 
             "input": {"age": 14, "current_pacing": "same speed throughout"},
             "expect": "Golden rule: contrast; slow before fast, fast before slow; speed map"},
            {"name": "too_fast", 
             "input": {"age": 12, "question": "everything feels rushed"},
             "expect": "Add slows; hold shots longer; establish before action; decelerate after climax"},
        ]
    },
    # Prompt 49: Rotoscoping & Video Reference
    {
        "prompt_file": "49-rotoscoping.md",
        "tests": [
            {"name": "first_rotoscope", "input": {"age": 12, "tool": "Krita", "question": "how do I start"}, "expect": "Record phone video; import to Krita; trace every 2nd-3rd frame; add style; keep under 5 sec"},
            {"name": "every_frame_mistake", "input": {"age": 14, "tool": "Krita", "motion": "running"}, "expect": "Trace key frames not every frame; every 2nd for fast; 24-36 frames not 72"},
            {"name": "should_i_rotoscope", "input": {"age": 11, "motion": "blink"}, "expect": "Hand-animate; too simple for rotoscope; save for complex motion"},
            {"name": "dance_sequence", "input": {"age": 15, "tool": "Blender", "motion": "dance"}, "expect": "Grease Pencil; every 3rd frame; trace timing then exaggerate in-betweens"},
            {"name": "scratch_rotoscope", "input": {"age": 10, "tool": "Scratch", "motion": "waving"}, "expect": "Screenshot key frames; import as backdrops; trace; 8-12 fps"},
            {"name": "stiff_trace_fix", "input": {"age": 16, "tool": "Krita", "problem": "stiff"}, "expect": "Add style; simplify lines; exaggerate poses beyond video; trace is starting not finish"},
        ]
    },
    # Prompt 50: Motion Capture & Mocap
    {
        "prompt_file": "50-motion-capture.md",
        "tests": [
            {"name": "foot_sliding_mocap", "input": {"age": 14, "problem": "feet sliding"}, "expect": "Foot plant fix; IK lock; keyframe foot position; release on lift-off"},
            {"name": "stiff_mocap", "input": {"age": 15, "problem": "stiff"}, "expect": "Add exaggeration; push key poses; bigger arcs; amplify anticipation/follow-through"},
            {"name": "jittery_data", "input": {"age": 13, "problem": "jittery"}, "expect": "Smooth curves; average spikes; re-key; tracking noise explanation"},
            {"name": "when_to_mocap", "input": {"age": 16, "question": "when should I use mocap"}, "expect": "Realistic human motion; complex actions; hand-animate for cartoon; mocap=90% polish=10%"},
            {"name": "free_tools", "input": {"age": 12, "question": "free mocap tools"}, "expect": "Rokoko Vision; DeepMotion; Blender cleanup; bvh/fbx export"},
            {"name": "performer_credit", "input": {"age": 17, "question": "do I credit my friend"}, "expect": "Yes; mocap performers are actors; acknowledge the performer"},
        ]
    },
    # Prompt 51: Balance, Weight Shift & Ground Contact
    {
        "prompt_file": "51-balance-weight-shift.md",
        "tests": [
            {"name": "floaty_walk", "input": {"age": 14, "problem": "floaty"}, "expect": "Weight shift: hips over stance foot; no shift=gliding; contact shadows; feet plant"},
            {"name": "sliding_feet", "input": {"age": 15, "problem": "sliding"}, "expect": "Lock planted foot; body moves over foot; heel strike to flat to toe push-off"},
            {"name": "no_weight", "input": {"age": 13, "problem": "no weight"}, "expect": "Foot compression; ankle bends; weight distribution to stance foot; contact shadow"},
            {"name": "one_foot_balance", "input": {"age": 12, "scene": "one foot"}, "expect": "CoG over single support foot; hips shift; 3 points of balance"},
            {"name": "fake_walk", "input": {"age": 16, "problem": "walk fake"}, "expect": "Hips shift side to side; walking=controlled falling; arm swing counterbalances"},
            {"name": "general_balance", "input": {"age": 13, "question": "general"}, "expect": "5 keys overview; stand-on-one-foot demo; CoG over support; feet plant"},
        ]
    },
    # Prompt 52: Exaggeration vs Realism
    {
        "prompt_file": "52-exaggeration-realism.md",
        "tests": [
            {"name": "comedy_style", "input": {"age": 14, "project": "comedy"}, "expect": "Level 4 cartoon; big squash/stretch; physics still apply; consistent"},
            {"name": "photoreal_vfx", "input": {"age": 16, "project": "VFX"}, "expect": "Level 1 photorealistic; minimal exaggeration; 100% real physics; Odd Rule"},
            {"name": "spider_verse", "input": {"age": 15, "reference": "Spider-Verse"}, "expect": "Level 3 stylized; selective amplification; follows physics; consistent baseline"},
            {"name": "jump_three_levels", "input": {"age": 13, "scene": "jumping"}, "expect": "Exercise: animate at Levels 2,3,4; keep Odd Rule; change scale only"},
            {"name": "broke_believability", "input": {"age": 14, "problem": "looks wrong"}, "expect": "Check: still accelerating? weighted recovery? amplified not ignored; dial back"},
            {"name": "inconsistent_scene", "input": {"age": 16, "problem": "disjointed"}, "expect": "Pick one baseline; spike up for beats only; story decides; don't jump levels"},
        ]
    },
    # Prompt 53: Cloth, Hair & Secondary Motion
    {
        "prompt_file": "53-cloth-hair-simulation.md",
        "tests": [
            {"name": "cloth_stiff", "input": {"age": 14, "tool": "hand-drawn", "problem": "cape stiff"}, "expect": "Delay principle; body leads, cape follows 2-4 frames; arcs; wind ripple"},
            {"name": "hair_floating", "input": {"age": 13, "problem": "hair floating"}, "expect": "Gravity: hair hangs down; lighter strands move more; lags head turns 2-3 frames"},
            {"name": "blender_cape", "input": {"age": 16, "tool": "Blender", "problem": "glitch"}, "expect": "Bake simulation before render; check pin group; rebake after body changes"},
            {"name": "cloth_same_time", "input": {"age": 15, "problem": "glued"}, "expect": "Offset cloth 3-4 frames after body; body is PRIMARY, cloth is SECONDARY"},
            {"name": "no_settle", "input": {"age": 12, "problem": "hair stops instantly"}, "expect": "Follow-through: hair overshoots 4-6 frames, swings back, settles; head first, hair last"},
            {"name": "general_cloth", "input": {"age": 14, "question": "how real cloth"}, "expect": "Secondary after primary; hand-drawn=body then arcs; Blender=cloth sim+pin+bake"},
        ]
    },
    # Prompt 54: Micro-Expressions & Subtle Performance
    {
        "prompt_file": "54-micro-expressions.md",
        "tests": [
            {"name": "blank_face", "input": {"age": 15, "problem": "face dead"}, "expect": "Half-blink on thought; 60% lid, 1-2 frames; at listening beat; verify full speed"},
            {"name": "hidden_emotion", "input": {"age": 16, "problem": "subtext not landing"}, "expect": "Mask-and-leak; hold calm, flash sadness 3 frames, control back 6; baseline first"},
            {"name": "too_obvious", "input": {"age": 14, "problem": "too obvious"}, "expect": "Reduce to 2-4 frames; don't hold; flash faster, control back slower; check full speed"},
            {"name": "suspicious", "input": {"age": 17, "scene": "lied to"}, "expect": "Micro-squint + half-blink; slow head turn; the 'not buying it' read"},
            {"name": "anger_held", "input": {"age": 15, "scene": "argument"}, "expect": "Lip press + nostril flare + micro-squint; calm mask; leak on trigger line"},
            {"name": "suppressed_joy", "input": {"age": 16, "scene": "good news"}, "expect": "Corner 1-2px up 2-3 frames, control back 4-6; under-eye compression; serious mask"},
        ]
    },
    # Prompt 55: Nature & Found Objects Stop Motion
    {
        "prompt_file": "55-nature-found-objects.md",
        "tests": [
            {"name": "outdoor_beginner", "input": {"age": 10, "setting": "outdoor", "materials": "leaves stones"}, "expect": "Respectful collecting; stone+leaf character; lock focus; embrace wind; 10-min exercise"},
            {"name": "found_object_char", "input": {"age": 12, "materials": "keys coins buttons"}, "expect": "Object-to-character mapping; personality from material; small increments; stabilize with wax"},
            {"name": "lifecycle", "input": {"age": 14, "goal": "lifecycle"}, "expect": "Seed to sprout to plant to flower; swapping pieces; science tie-in; plan beats"},
            {"name": "pi_timelapse", "input": {"age": 16, "tool": "Raspberry Pi", "goal": "timelapse"}, "expect": "picamera loop; frame interval; ffmpeg; weatherproof; STEM crossover"},
            {"name": "wind_problem", "input": {"age": 13, "problem": "wind"}, "expect": "Sheltered spot or windbreak; embrace movement; cloudy days for even light; short sessions"},
            {"name": "env_message", "input": {"age": 15, "goal": "environmental message"}, "expect": "Trash-as-character; pollution narrative; deforestation theme; end card message"},
        ]
    },
    # Prompt 56: Observational Sketching
    {
        "prompt_file": "56-observational-sketching.md",
        "tests": [
            {"name": "stiff_gestures", "input": {"age": 14, "problem": "stiff"}, "expect": "Line of action first; 30s gestures; stop details; Level 2 continuous"},
            {"name": "where_to_start", "input": {"age": 12, "question": "where to start"}, "expect": "Zoo or dog park; 30s gestures; Level 1 look-memorize-draw; carry sketchbook"},
            {"name": "animals_fast", "input": {"age": 15, "subject": "dogs"}, "expect": "Level 1 look-memorize-draw; watch full cycle; draw same action 5 times; dogs repeat"},
            {"name": "cant_memory", "input": {"age": 13, "problem": "cant draw from memory"}, "expect": "Level 1 training; 3-sec observation then draw; memory builds with practice"},
            {"name": "life_vs_video", "input": {"age": 16, "question": "can I use video"}, "expect": "Life is primary; trains eye-brain-hand in 3D; video flattens; use video to supplement"},
            {"name": "people_walking", "input": {"age": 14, "subject": "people walking"}, "expect": "Cafe; catch stride line of action in 2 sec; Level 2 continuous; note weight shift"},
        ]
    },
    # Prompt 57: Photogrammetry & 3D Scanning
    {
        "prompt_file": "57-photogrammetry.md",
        "tests": [
            {"name": "first_scan", "input": {"age": 14, "object": "shoe", "goal": "animate"}, "expect": "RealityScan app; 40 photos all angles; even light; OBJ export; Blender import"},
            {"name": "shiny_object", "input": {"age": 15, "object": "trophy"}, "expect": "Shiny won't scan; matte spray or different object; expect holes"},
            {"name": "game_env", "input": {"age": 16, "object": "rock", "goal": "game env"}, "expect": "RealityCapture or Meshroom; 50+ photos; FBX export; Blender import; no rig needed"},
            {"name": "transparent", "input": {"age": 13, "object": "glass"}, "expect": "Transparent won't work; explain why; suggest solid alternative like clay"},
            {"name": "toy_movie", "input": {"age": 15, "goal": "scan toys"}, "expect": "RealityScan each toy; 30-40 photos; OBJ; Blender; rig with armature; animate cast"},
            {"name": "food_dancing", "input": {"age": 14, "object": "banana", "goal": "dance"}, "expect": "Scan banana (matte); 35 photos; OBJ; Blender; keyframe rotation; animate dancing"},
        ]
    },
    # Prompt 58: Light, Shadow & Ambient Occlusion
    {
        "prompt_file": "58-light-shadow-study.md",
        "tests": [
            {"name": "char_floats", "input": {"age": 14, "problem": "floats"}, "expect": "Contact shadow; dark patch at feet; sharpest at contact, softens outward"},
            {"name": "looks_flat", "input": {"age": 13, "problem": "flat"}, "expect": "Ambient occlusion in crevices; under chin, between fingers; soft darkness in folds"},
            {"name": "shadows_wrong", "input": {"age": 15, "problem": "shadows wrong"}, "expect": "Shadow color=complement of light; warm light=blue shadows; never black; reflected light"},
            {"name": "no_separation", "input": {"age": 16, "problem": "blends into bg"}, "expect": "Three-point lighting; rim light from behind; key/fill/rim explained"},
            {"name": "where_start", "input": {"age": 12, "question": "how to learn lighting"}, "expect": "Observation: white egg on white paper under one lamp; find 5 zones; photograph; move lamp"},
            {"name": "fake_render", "input": {"age": 17, "tool": "blender", "problem": "fake"}, "expect": "AO pass + contact shadows; colored shadows not black; fill light; bounce light settings"},
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