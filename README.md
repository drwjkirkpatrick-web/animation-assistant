# Animation Assistant

An AI-powered assistant that helps kids aged 10-17 learn computer animation. This repo contains 48 prompt designs, research, and a test harness for building and evaluating the assistant.

## What's Here

## Progress Tracker, Achievement System & Standards-Aligned Reports

### `tracker/`
- **progress_tracker.py** — Student progress tracker with achievement/badge system and printable HTML reports aligned to Raspberry Pi Foundation computing taxonomy and Kenya CBC Computer Science curriculum.

```bash
# Register students
python tracker/progress_tracker.py add_student --name "Amani" --age 13 --grade 8 --school "Mombasa Primary"

# Record module progress (CBC 4-level rubric: BE, AE, ME, EE)
python tracker/progress_tracker.py record --student-id S001 --module 3 --level ME --notes "Great walk cycle"

# View badges and RPF tier
python tracker/progress_tracker.py badges --student-id S001

# Generate printable HTML progress report
python tracker/progress_tracker.py report --student-id S001 --output report.html

# Generate class-level report
python tracker/progress_tracker.py class-report --output class_report.html

# List all students
python tracker/progress_tracker.py list-students
```

### Standards Alignment

The tracker maps all 48 modules to two standards frameworks:

- **Raspberry Pi Foundation Computing Taxonomy** — 11 content strands (programming, algorithms, creating media, safety, AI, etc.) + 5 Digital Making strands + 4 progression levels (Creator → Builder → Developer → Maker)
- **Kenya CBC Computer Science Curriculum** — 4 strands (Foundation, Networks, Software, Programming) + 7 core competencies + 4-level assessment rubric (BE/AE/ME/EE)

Full mapping in `research/standards-mapping.md`.

### Achievement System

30 badges across 5 tiers:
- **Creator** (3 badges) — first animation, tool exploration, first export
- **Builder** (4 badges) — squash, arcs, timing, weight
- **Developer** (6 badges) — walk cycle, anticipation, follow-through, mood, lip sync, voice
- **Maker** (11 badges) — storyboard, rigging, effects, sound, game animation, contests, Pi pioneer, physics master, mentor, style, short film
- **CBC Competency** (6 badges) — digital citizen, creative thinker, problem solver, collaborator, code creator, AI ethicist

Badges auto-award when a student reaches ME or EE on relevant modules. Reports are printable (CSS @media print) and show progress bars per strand.

### `research/`
- **animation-tools-landscape.md** — Survey of 7 animation tools for ages 10-17
- **gap-analysis.md** — Three-pass gap analysis identifying 30 missing areas (all built as modules 19-48)
- **standards-mapping.md** — Full alignment of all 48 modules to RPF taxonomy and Kenya CBC curriculum

### `prompts/`
Forty-eight testable system prompts covering the full assistant experience:

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
| 10 | Reference Library Guide | Real-world movement references |
| 11 | Progress Tracker & Badges | 6-level gamified system with 24+ badges |
| 12 | Showcase & Exhibition | Presenting work with pride |
| 13 | Animation Glossary | Kid-friendly term dictionary with try-it exercises |
| 14 | Tool Comparison Helper | Side-by-side feature comparisons |
| 15 | Parent & Teacher Guide | Adult support guidance |
| 16 | Story & Storyboard Builder | Pre-animation story development |
| 17 | Animation History & Inspiration | From thaumatropes to Spider-Verse |
| 18 | Workflow & File Management | Good digital habits — naming, versioning, exports |

#### Gap-Fill — First Pass (19-28)
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

#### Gap-Fill — Second Pass (29-38)
| # | Prompt | What It Does |
|---|--------|-------------|
| 29 | Animation Physics & Weight | Odd Rule, inertia, momentum, center of gravity |
| 30 | Character Design & Shape Language | Circles/squares/triangles, model sheets |
| 31 | Camera & Cinematography | Shot types, 180-degree rule, camera moves |
| 32 | Advanced Body Mechanics | Run cycles, jumps, quadruped locomotion |
| 33 | Facial Animation & Expressions | 3 zones, 6 universal expressions, lip sync |
| 34 | Special Effects Animation | Fire, water, smoke, explosions, magic |
| 35 | Timing Charts & Spacing | Dope sheets, Odd Rule spacing, graph editor |
| 36 | Accessibility & Adaptive Animation | Motor, visual, cognitive, sensory adaptations |
| 37 | Community & Online Etiquette | Sharing work, feedback, online safety |
| 38 | Contests, Festivals & Challenges | 11 Second Club, film festivals, submission |

#### Gap-Fill — Third Pass (39-48)
| # | Prompt | What It Does |
|---|--------|-------------|
| 39 | Animation Editing & Post-Production | Radio play, animatic, post — edit before you animate |
| 40 | Background & Environment Design | Perspective, depth layers, mood through environment |
| 41 | Anatomy & Figure Drawing | Skeleton, muscles, gesture drawing, construction |
| 42 | Voice Acting & Dialogue Recording | Character voices, recording setup, directing |
| 43 | Music Synchronization & Beat Sync | Marking beats, BPM to frames, sync levels |
| 44 | Mixed Media & Experimental Techniques | Collage, photo+drawing, 2D+3D, sand, typography |
| 45 | Game Animation & Sprite Sheets | Idle/walk/attack loops, sprite sheets, frame rate independence |
| 46 | Production & Project Management | Scoping, scheduling, the 2x rule, finishing projects |
| 47 | AI Ethics & Animation Tools | When AI helps vs hurts, learning test, portfolio honesty |
| 48 | Pacing & Rhythm | Fast/medium/slow, contrast, emotional wave, shot duration |

### `tests/`
- **test_prompts.py** — Test harness with 280+ test cases across all 48 prompts.

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

Also supports: Raspberry Pi, Chromebook, phone/tablet, game engines (Godot, Unity, Pygame), and adaptive/accessible tools.

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
11. **Done > perfect** — finishing projects matters more than perfecting them
12. **AI is a tool, not a replacement** — learn fundamentals first, use AI to assist

## License

MIT