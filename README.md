# Animation Assistant

An AI-powered assistant that helps kids aged 10-17 learn computer animation. This repo contains 28 prompt designs, research, and a test harness for building and evaluating the assistant.

## What's Here

### `research/`
- **animation-tools-landscape.md** — Survey of 7 animation tools for ages 10-17, from Scratch to Blender, with learning progression paths and the 12 Principles framework.
- **gap-analysis.md** — Gap analysis comparing our modules to professional animation curricula, identifying 10 missing areas that were then built as modules 19-28.

### `prompts/`
Twenty-eight testable system prompts covering the full assistant experience:

#### Core Assistant (01-08)
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

#### Extended Modules (09-18)
| # | Prompt | What It Does |
|---|--------|-------------|
| 09 | Daily Challenge Generator | Constrained daily prompts — one principle per challenge, with stretch goals |
| 10 | Reference Library Guide | Real-world movement references — what to study, where to find it, how to observe |
| 11 | Progress Tracker & Badges | 6-level gamified system with 24+ badges — makes growth visible and motivating |
| 12 | Showcase & Exhibition | Helps kids present work with pride — quick-shares, portfolios, gallery labels |
| 13 | Animation Glossary | Kid-friendly term dictionary — every term in plain English with a try-it exercise |
| 14 | Tool Comparison Helper | Side-by-side feature comparisons when kids are torn between two tools |
| 15 | Parent & Teacher Guide | Module for adults supporting young animators — expectations, common mistakes, how to help |
| 16 | Story & Storyboard Builder | Pre-animation story development — character, structure, storyboard panels by age |
| 17 | Animation History & Inspiration | Fun facts from thaumatropes to Spider-Verse — links kids to the tradition |
| 18 | Workflow & File Management | Good digital habits — naming, versioning, folder structure, export settings, backups |

#### Gap-Fill Modules (19-28)
*Identified by gap analysis against professional curricula and animation FAQs*

| # | Prompt | What It Does |
|---|--------|-------------|
| 19 | Color Theory & Visual Design | Color schemes, composition, lighting — making scenes look professional |
| 20 | Sound & Audio Design | The 4 sound layers, SFX timing, free resources, DIY sound recording |
| 21 | Rigging Deep Dive | Pivot rigs to bone rigs to IK/FK — the bridge from drawing to puppet animation |
| 22 | Compositing & Rendering | Layering, shadows, effects, vignettes, export settings, pre-render checklist |
| 23 | Portfolio & Career Path | Demo reels, career paths, industry reality — for teens who want to go pro |
| 24 | Animation Styles & Techniques | 11 animation styles catalog — frame-by-frame to experimental, find your style |
| 25 | Collaboration & Team Animation | Buddy to studio model, animation pipeline, Pixar-style feedback rules |
| 26 | Raspberry Pi & Low-Resource | Animation on Pi, Chromebook, phone, old laptop — you don't need a gaming PC |
| 27 | Kid-Friendly FAQ | Answers to questions kids actually ask — "Do I need to draw?", "Can I make money?", "Can I use AI?" |
| 28 | Acting for Animation | Body language, eye acting, micro-expressions, the mirror exercise — the #1 animator skill |

### `tests/`
- **test_prompts.py** — Test harness with 160+ test cases across all 28 prompts.

```bash
python tests/test_prompts.py --list           # List all prompts and test cases
python tests/test_prompts.py --prompt 03      # Focus on one prompt
python tests/test_prompts.py                  # Interactive review mode
```

Each prompt file includes a "What to Test" table with specific inputs and expected behaviors.

## Animation Tool Progression

```
Beginner (10-12)          Intermediate (12-14)         Advanced (14-17)
─────────────────────────────────────────────────────────────────────
Scratch ──────────────► Krita ──────────────────► OpenToonz
Stop Motion Studio ──► Pencil2D ───────────────► Blender (3D)
                        Synfig (tweening) ──────► Blender (Grease Pencil)
```

Also supports: Raspberry Pi (Scratch, Python/Pygame, Pi Camera stop motion), Chromebook (Scratch, Piskel), phone/tablet (Stop Motion Studio, FlipaClip).

## Design Principles

1. **Age-calibrated everything** — tone, vocabulary, tool recommendations, and critique depth adjust based on student age
2. **The 12 Principles are the backbone** — every module ties back to foundational animation principles
3. **Project-based learning** — kids learn by making things (bouncing ball → walk cycle → short film)
4. **Process over product** — the assistant celebrates effort and learning, not just polished results
5. **Never dismiss a kid's ambition** — redirect to age-appropriate starting points without killing the dream
6. **Adults need help too** — parents and teachers get their own guidance for supporting without taking over
7. **Hardware equity** — kids with a Raspberry Pi or Chromebook can animate just as well as kids with gaming PCs
8. **Acting > drawing** — the #1 animator skill is performance, not illustration; the mirror exercise is the secret weapon

## License

MIT