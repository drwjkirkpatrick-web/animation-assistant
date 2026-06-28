# Animation Assistant

An AI-powered assistant that helps kids aged 10-17 learn computer animation. This repo contains 38 prompt designs, research, and a test harness for building and evaluating the assistant.

## What's Here

### `research/`
- **animation-tools-landscape.md** — Survey of 7 animation tools for ages 10-17, from Scratch to Blender, with learning progression paths and the 12 Principles framework.
- **gap-analysis.md** — Two-pass gap analysis comparing our modules to professional animation curricula, identifying 20 missing areas that were then built as modules 19-38.

### `prompts/`
Thirty-eight testable system prompts covering the full assistant experience:

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
| 09 | Daily Challenge Generator | Constrained daily prompts — one principle per challenge |
| 10 | Reference Library Guide | Real-world movement references — what to study, where to find |
| 11 | Progress Tracker & Badges | 6-level gamified system with 24+ badges |
| 12 | Showcase & Exhibition | Presenting work with pride — quick-shares, portfolios, gallery labels |
| 13 | Animation Glossary | Kid-friendly term dictionary with try-it exercises |
| 14 | Tool Comparison Helper | Side-by-side feature comparisons between tools |
| 15 | Parent & Teacher Guide | Adult support guidance — expectations, mistakes, how to help |
| 16 | Story & Storyboard Builder | Pre-animation story development and storyboard panels |
| 17 | Animation History & Inspiration | From thaumatropes to Spider-Verse — sparking wonder |
| 18 | Workflow & File Management | Good digital habits — naming, versioning, exports, backups |

#### Gap-Fill Modules — First Pass (19-28)
*Identified by first gap analysis against professional curricula and FAQs*

| # | Prompt | What It Does |
|---|--------|-------------|
| 19 | Color Theory & Visual Design | Color schemes, composition, lighting |
| 20 | Sound & Audio Design | 4 sound layers, SFX timing, DIY recording |
| 21 | Rigging Deep Dive | Pivot to bone to IK/FK rigs |
| 22 | Compositing & Rendering | Layering, effects, export cheat sheet |
| 23 | Portfolio & Career Path | Demo reels, career paths, industry reality |
| 24 | Animation Styles & Techniques | 11 animation styles — find your style |
| 25 | Collaboration & Team Animation | Buddy to studio model, Pixar feedback rules |
| 26 | Raspberry Pi & Low-Resource | Pi, Chromebook, phone animation |
| 27 | Kid-Friendly FAQ | Answers to questions kids actually ask |
| 28 | Acting for Animation | Body language, eye acting, mirror exercise |

#### Gap-Fill Modules — Second Pass (29-38)
*Identified by second gap analysis against physics curricula, character design guides, and festival resources*

| # | Prompt | What It Does |
|---|--------|-------------|
| 29 | Animation Physics & Weight | The Odd Rule, inertia, momentum, center of gravity |
| 30 | Character Design & Shape Language | Circles/squares/triangles, model sheets, silhouettes |
| 31 | Camera & Cinematography | Shot types, 180-degree rule, camera moves, composition |
| 32 | Advanced Body Mechanics | Run cycles, jumps, weight shift, quadruped locomotion |
| 33 | Facial Animation & Expressions | 3 zones, 6 universal expressions, lip sync, blend shapes |
| 34 | Special Effects Animation | Fire, water, smoke, explosions, magic — frame-by-frame and simulation |
| 35 | Timing Charts & Spacing | Dope sheets, Odd Rule spacing, graph editor, planning frames |
| 36 | Accessibility & Adaptive Animation | Motor, visual, cognitive, sensory adaptations — animation for everyone |
| 37 | Community & Online Etiquette | Sharing work, giving/receiving feedback, online safety |
| 38 | Contests, Festivals & Challenges | 11 Second Club, film festivals, preparation and submission |

### `tests/`
- **test_prompts.py** — Test harness with 220+ test cases across all 38 prompts.

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

Also supports: Raspberry Pi, Chromebook, phone/tablet, and adaptive/accessible tools.

## Design Principles

1. **Age-calibrated everything** — tone, vocabulary, tool recommendations, critique depth
2. **The 12 Principles are the backbone** — every module ties to foundational principles
3. **Project-based learning** — kids learn by making (bouncing ball → walk cycle → short film)
4. **Process over product** — celebrate effort and learning, not just polished results
5. **Never dismiss a kid's ambition** — redirect to age-appropriate starting points
6. **Adults need help too** — parents and teachers get their own guidance
7. **Hardware equity** — Pi, Chromebook, phone kids can animate just as well
8. **Acting > drawing** — the #1 animator skill is performance, not illustration
9. **Animation is for everyone** — adaptive tools for motor, visual, cognitive, sensory needs
10. **Physics makes it believable** — weight, momentum, and the Odd Rule ground animation in reality

## License

MIT