# Animation Assistant

An AI-powered assistant that helps kids aged 10-17 learn computer animation. This repo contains the prompt designs, research, and test harness for building and evaluating the assistant.

## What's Here

### `research/`
- **animation-tools-landscape.md** — Survey of 7 animation tools appropriate for ages 10-17, from Scratch to Blender, with learning progression paths and the 12 Principles of Animation framework.

### `prompts/`
Eight testable system prompts covering the full assistant experience:

| # | Prompt | What It Does |
|---|--------|-------------|
| 01 | System Persona | Core identity, teaching philosophy, tone |
| 02 | Tool Routing | Recommends the right software for a student's age/interests |
| 03 | Project Guide | Step-by-step lessons for specific animation projects |
| 04 | Principle Explainer | Teaches the 12 Principles with kid-friendly analogies |
| 05 | Code-First Animation | Scratch and Python-based animation instruction |
| 06 | Critique & Feedback | Gentle, age-calibrated review of student work |
| 07 | Troubleshooting | Diagnoses "it looks wrong" problems with tool-specific fixes |
| 08 | Curriculum Planner | Builds week-by-week learning paths tailored to goals |

### `tests/`
- **test_prompts.py** — Test harness with 40+ test cases across all 8 prompts. List, filter, and review prompts against expected behaviors.

```bash
python tests/test_prompts.py --list           # List all prompts and test cases
python tests/test_prompts.py --prompt 03      # Focus on one prompt
python tests/test_prompts.py                  # Interactive review mode
```

## Animation Tool Progression

```
Beginner (10-12)          Intermediate (12-14)         Advanced (14-17)
─────────────────────────────────────────────────────────────────────
Scratch ──────────────► Krita ──────────────────► OpenToonz
Stop Motion Studio ──► Pencil2D ───────────────► Blender (3D)
                        Synfig (tweening) ──────► Blender (Grease Pencil)
```

## License

MIT