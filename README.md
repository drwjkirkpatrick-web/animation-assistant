# Animation Assistant

An AI-powered assistant that helps kids aged 10-17 learn computer animation. This repo contains the prompt designs, research, and test harness for building and evaluating the assistant.

## What's Here

### `research/`
- **animation-tools-landscape.md** — Survey of 7 animation tools appropriate for ages 10-17, from Scratch to Blender, with learning progression paths and the 12 Principles of Animation framework.

### `prompts/`
Eighteen testable system prompts covering the full assistant experience:

#### Core Assistant
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

#### Extended Modules
| # | Prompt | What It Does |
|---|--------|-------------|
| 09 | Daily Challenge Generator | Constrained daily prompts that keep kids practicing — one principle per challenge, with stretch goals |
| 10 | Reference Library Guide | Curated real-world movement references — what to study, where to find it, how to observe |
| 11 | Progress Tracker & Badges | 6-level gamified system with 24+ badges — makes growth visible and motivating |
| 12 | Showcase & Exhibition | Helps kids present work with pride — quick-shares, portfolios, gallery labels |
| 13 | Animation Glossary | Kid-friendly term dictionary — every term explained in plain English with a try-it exercise |
| 14 | Tool Comparison Helper | Side-by-side feature comparisons when kids are torn between two tools |
| 15 | Parent & Teacher Guide | Module for adults supporting young animators — expectations, common mistakes, how to help |
| 16 | Story & Storyboard Builder | Pre-animation story development — character, structure, storyboard panels by age |
| 17 | Animation History & Inspiration | Fun facts and connections from thaumatropes to Spider-Verse — links kids to the tradition |
| 18 | Workflow & File Management | Good digital habits — naming, versioning, folder structure, export settings, backups |

### `tests/`
- **test_prompts.py** — Test harness with 80+ test cases across all 18 prompts. List, filter, and review prompts against expected behaviors.

```bash
python tests/test_prompts.py --list           # List all prompts and test cases
python tests/test_prompts.py --prompt 03      # Focus on one prompt
python tests/test_prompts.py                  # Interactive review mode
```

Each prompt file includes a "What to Test" table with specific inputs and expected behaviors, so you can evaluate responses systematically.

## Animation Tool Progression

```
Beginner (10-12)          Intermediate (12-14)         Advanced (14-17)
─────────────────────────────────────────────────────────────────────
Scratch ──────────────► Krita ──────────────────► OpenToonz
Stop Motion Studio ──► Pencil2D ───────────────► Blender (3D)
                        Synfig (tweening) ──────► Blender (Grease Pencil)
```

## Design Principles

1. **Age-calibrated everything** — tone, vocabulary, tool recommendations, and critique depth all adjust based on the student's age
2. **The 12 Principles are the backbone** — every module ties back to the foundational animation principles
3. **Project-based learning** — kids learn by making things (bouncing ball → walk cycle → short film)
4. **Process over product** — the assistant celebrates effort and learning, not just polished results
5. **Never dismiss a kid's ambition** — redirect to age-appropriate starting points without killing the dream
6. **Adults need help too** — parents and teachers get their own guidance for supporting without taking over

## License

MIT