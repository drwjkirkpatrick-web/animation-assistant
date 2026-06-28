# 🌊 Animation Assistant — Teaching Kids to Animate with Kenya's Ocean

> *Every kid in Mombasa, Kilifi, Kwale, and Lamu deserves to tell their stories through animation. This project makes that possible — using the marine animals swimming right outside their doorstep.*

An AI-powered animation teaching assistant for kids aged **10–17**, built around the **12 Principles of Animation**, localized for **Kenya's Indian Ocean coastline**, and aligned to the **Kenya CBC curriculum** and **Raspberry Pi Foundation computing standards**.

---

## What's Inside

### 📚 58 Prompt Modules (`prompts/`)
Testable system prompts covering everything from the bouncing ball to micro-expressions. Each prompt has a code block and a "What to Test" table with specific inputs and expected behaviors.

### 📝 58 Complete Lesson Plans (`lessons/`)
CBC-aligned, ready-to-teach lesson plans — one for every prompt module. Every lesson uses **Kenyan Indian Ocean marine animals** as animation characters. A teacher can pick up any lesson plan and teach it directly.

### 🧪 Test Harness (`tests/`)
341 test cases across all 58 prompts, with CLI for listing, focusing, and non-interactive review.

### 📊 Progress Tracker (`tracker/`)
SQLite-backed student tracker with 30 achievement badges across 5 tiers, printable HTML reports, and standards-aligned progress bars.

### 🔬 Research (`research/`)
- Animation tools landscape (7 tools for ages 10–17)
- Four-pass gap analysis (42 gaps identified and filled)
- Standards mapping (RPF 11-strand taxonomy + Kenya CBC 4-strand curriculum)
- **Kenya ocean animals reference** — 30+ species with animation movement categories

---

## Why Kenya's Ocean Animals?

Every lesson plan uses at least one animal from Kenya's **Marine Big Five** or reef ecosystem as the animation subject. This isn't decoration — it's pedagogy.

| Animal | Swahili Name | Animation Principle It Teaches |
|--------|-------------|-------------------------------|
| 🐢 Green Sea Turtle | Kasa | Weight shift, heavy vs light, quadruped locomotion |
| 🐬 Bottlenose Dolphin | Pomboo | Arcs, anticipation, breaching (jump physics) |
| 🦈 Whale Shark | Papa Shinga | Scale through timing, massive weight, slow momentum |
| 🐙 Octopus | Pweza | Secondary motion (8 tentacles = complex trailing) |
| 🪼 Jellyfish | — | Squash & stretch (pulsing bell), secondary motion (tentacle delay) |

Kids in Mombasa animate **Pomboo the Dolphin** leaping at Kisite-Mpunguti. Kids in Kilifi animate **Kasa the Turtle** nesting at Watamu. The animals are real, the locations are real, the conservation messages are real. Animation becomes a way to connect with and protect their own environment.

---

## Lesson Plan Structure (CBC-Aligned)

Every lesson plan follows the Kenya Competency-Based Curriculum format:

```
CBC Strand Mapping        → Which curriculum strand and sub-strand
Learning Outcomes         → 3 outcomes (knowledge, skill, value)
Key Inquiry Question      → The driving question for the lesson
Local Context             → The Kenyan ocean animal used + conservation note
Lesson Development        → 4 steps (intro → concept → guided → independent → sharing)
Assessment Table          → 4-level rubric (BE / AE / ME / EE)
Extended Activity         → Homework or follow-up project
Differentiation           → Support for struggling + challenge for advanced
Teacher Reflection        → Self-assessment checklist
```

**Assessment rubric levels:**
- **BE** = Below Expectation
- **AE** = Approaching Expectation
- **ME** = Meets Expectation
- **EE** = Exceeds Expectation

---

## The 58 Modules at a Glance

### Core Assistant (01–08)
| # | Module | Ocean Animal |
|---|--------|-------------|
| 01 | System Persona & Character Voice | 🐬 Dolphin (Pomboo) |
| 02 | Tool Routing — Right Software | 🐢 Turtle (Kasa) |
| 03 | Step-by-Step Project Guide | 🐙 Octopus (Pweza) |
| 04 | Principle Explainer — 12 Principles | 🪼 Jellyfish |
| 05 | Code-First Animation (Scratch/Python) | 🐠 Clownfish |
| 06 | Critique & Feedback | 🦈 Whale Shark (Papa Shinga) |
| 07 | Troubleshooting | 🐢 Turtle (Kasa) |
| 08 | Curriculum Planner | 🐬 Dolphin (Pomboo) |

### Extended Modules (09–18)
| # | Module | Ocean Animal |
|---|--------|-------------|
| 09 | Daily Challenge Generator | 🦀 Crab |
| 10 | Reference Library Guide | 🐬 Dolphin (Pomboo) |
| 11 | Progress Tracker & Badges | 🐠 Parrotfish |
| 12 | Showcase & Exhibition | 🐢 Turtle (Kasa) |
| 13 | Animation Glossary | 🐙 Octopus (Pweza) |
| 14 | Tool Comparison Helper | 🦈 Whale Shark vs 🐠 Clownfish |
| 15 | Parent & Teacher Guide | 🐬 Dolphin (Pomboo) |
| 16 | Story & Storyboard Builder | 🐢 Turtle (Kasa) |
| 17 | Animation History & Inspiration | 🪼 Jellyfish |
| 18 | Workflow & File Management | 🐠 Butterflyfish |

### Gap-Fill Pass 1 (19–28)
| # | Module | Ocean Animal |
|---|--------|-------------|
| 19 | Color Theory & Visual Design | 🐠 Parrotfish |
| 20 | Sound & Audio Design | 🐬 Dolphin (Pomboo) |
| 21 | Rigging Deep Dive | 🐙 Octopus (Pweza) |
| 22 | Compositing & Rendering | 🪼 Jellyfish |
| 23 | Portfolio & Career Path | 🐢 Turtle (Kasa) |
| 24 | Animation Styles & Techniques | 🐠 Lionfish |
| 25 | Collaboration & Team Animation | 🐬 Dolphin pod |
| 26 | Raspberry Pi & Low-Resource | 🐠 Clownfish |
| 27 | Kid-Friendly FAQ | 🦀 Crab |
| 28 | Acting for Animation | 🐙 Octopus (Pweza) |

### Gap-Fill Pass 2 (29–38)
| # | Module | Ocean Animal |
|---|--------|-------------|
| 29 | Animation Physics & Weight | 🦈 Whale Shark (Papa Shinga) |
| 30 | Character Design & Shape Language | 🐢 Turtle (Kasa) |
| 31 | Camera & Cinematography | 🐬 Dolphin (Pomboo) |
| 32 | Advanced Body Mechanics | 🐢 Turtle (Kasa) |
| 33 | Facial Animation & Expressions | 🐙 Octopus (Pweza) |
| 34 | Special Effects Animation | 🪼 Jellyfish |
| 35 | Timing Charts & Spacing | 🐠 Clownfish |
| 36 | Accessibility & Adaptive Animation | 🐢 Turtle (Kasa) |
| 37 | Community & Online Etiquette | 🐬 Dolphin (Pomboo) |
| 38 | Contests, Festivals & Challenges | 🐠 Parrotfish |

### Gap-Fill Pass 3 (39–48)
| # | Module | Ocean Animal |
|---|--------|-------------|
| 39 | Animation Editing & Post-Production | 🐙 Octopus (Pweza) |
| 40 | Background & Environment Design | 🪸 Coral Reef |
| 41 | Anatomy & Figure Drawing | 🐢 Turtle (Kasa) |
| 42 | Voice Acting & Dialogue Recording | 🐙 Octopus (Pweza) |
| 43 | Music Synchronization & Beat Sync | 🐬 Dolphin (Pomboo) |
| 44 | Mixed Media & Experimental Techniques | 🪸 Coral Reef Ecosystem |
| 45 | Game Animation & Sprite Sheets | 🐠 Clownfish |
| 46 | Production & Project Management | 🦈 Whale Shark (Papa Shinga) |
| 47 | AI Ethics & Animation Tools | 🐙 Octopus (Pweza) |
| 48 | Pacing & Rhythm | 🐬 Dolphin (Pomboo) |

### Real-World Motion & Realism (49–58)
| # | Module | Ocean Animal |
|---|--------|-------------|
| 49 | Rotoscoping & Video Reference | 🐬 Dolphin (Pomboo) |
| 50 | Motion Capture & Mocap | 🐢 Turtle (Kasa) |
| 51 | Balance, Weight Shift & Ground Contact | 🐢 Turtle (Kasa) |
| 52 | Exaggeration vs Realism | 🦈 Whale Shark (Papa Shinga) |
| 53 | Cloth, Hair & Secondary Motion | 🪼 Jellyfish |
| 54 | Micro-Expressions & Subtle Performance | 🐙 Octopus (Pweza) |
| 55 | Stop Motion with Nature & Found Objects | 🐢 Turtle (Kasa, from beach stones) |
| 56 | Observational Sketching & Movement Studies | 🐬 Dolphin (Pomboo) |
| 57 | Photogrammetry & 3D Scanning | 🐚 Seashell from Watamu |
| 58 | Light, Shadow & Ambient Occlusion | 🐟 Manta Ray |

---

## Animation Tool Progression

```
Beginner (10-12)          Intermediate (12-14)         Advanced (14-17)
─────────────────────────────────────────────────────────────────────
Scratch ──────────────► Krita ──────────────────► OpenToonz
Stop Motion Studio ──► Pencil2D ───────────────► Blender (3D)
                        Synfig (tweening) ──────► Blender (Grease Pencil)
```

Also supports: **Raspberry Pi**, Chromebook, phone/tablet, game engines, and adaptive/accessible tools. No kid is left out because of hardware.

---

## Progress Tracker & Achievement System

```bash
# Register a student
python tracker/progress_tracker.py add_student --name "Amani" --age 13 --grade 8 --school "Mombasa Primary"

# Record module progress (CBC rubric: BE, AE, ME, EE)
python tracker/progress_tracker.py record --student-id S001 --module 29 --level ME --notes "Great whale shark physics"

# View badges and RPF tier
python tracker/progress_tracker.py badges --student-id S001

# Generate printable HTML report
python tracker/progress_tracker.py report --student-id S001 --output report.html

# Class-level summary
python tracker/progress_tracker.py class-report --output class_report.html
```

**30 badges across 5 tiers:**
- 🌱 **Creator** (3) — first animation, tool exploration, first export
- 🔧 **Builder** (4) — squash, arcs, timing, weight
- 🎨 **Developer** (6) — walk cycle, anticipation, follow-through, mood, lip sync, voice
- 🏆 **Maker** (11) — storyboard, rigging, effects, sound, game animation, contests, Pi pioneer, physics master, mentor, style, short film
- 🇰🇪 **CBC Competency** (6) — digital citizen, creative thinker, problem solver, collaborator, code creator, AI ethicist

Badges auto-award when a student reaches **ME** or **EE** on relevant modules.

---

## Test Harness

```bash
python tests/test_prompts.py --list              # List all 58 prompts + 341 test cases
python tests/test_prompts.py --prompt 29          # Focus on the animation physics prompt
python tests/test_prompts.py --non-interactive    # Run without user prompts
```

---

## Standards Alignment

| Framework | Coverage |
|-----------|----------|
| **Raspberry Pi Foundation** | 11 content strands + 5 Digital Making strands + 4 progression levels (Creator → Builder → Developer → Maker) |
| **Kenya CBC** | 4 strands (Foundation, Networks, Software, Programming) + 7 core competencies + 4-level rubric (BE/AE/ME/EE) |

Full mapping in `research/standards-mapping.md`.

---

## Kenya's Marine Protected Areas (Used in Lessons)

| Park | County | Key Species | Lesson Reference |
|------|--------|-------------|-----------------|
| Watamu Marine National Park | Kilifi | Turtles, whale sharks, coral | Lessons 29, 30, 49, 51, 55, 57 |
| Kisite-Mpunguti Marine Reserve | Kwale | Dolphins, sea turtles | Lessons 01, 31, 43, 49, 56 |
| Malindi Marine National Park | Kilifi | Coral fish, sea turtles | Lesson 44 |
| Mombasa Marine National Park | Mombasa | Coral reef, diverse fish | Lessons 44, 53 |
| Diani-Chale Marine Reserve | Kwale | Whale sharks, dolphins | Lessons 51, 58 |
| Lamu Archipelago | Lamu | Dugongs, turtles, mangroves | (Reference) |

---

## Design Principles

1. **Age-calibrated everything** — tone, vocabulary, tools, critique depth
2. **The 12 Principles are the backbone** — every module ties to them
3. **Project-based learning** — kids learn by making (ball → walk cycle → short film)
4. **Process over product** — celebrate effort, not just polished results
5. **Never dismiss a kid's ambition** — redirect to age-appropriate starting points
6. **Hardware equity** — Pi, Chromebook, and phone kids can animate too
7. **Acting > drawing** — performance is the #1 animator skill
8. **Animation is for everyone** — adaptive tools for all needs
9. **Physics makes it believable** — weight, momentum, the Odd Rule
10. **Done > perfect** — finishing matters more than perfecting
11. **AI is a tool, not a replacement** — learn fundamentals first
12. **Local is powerful** — Kenya's ocean animals make animation relevant

---

## Quick Start for Teachers

1. **Read the lesson template:** `lessons/LESSON-TEMPLATE.md`
2. **Pick a lesson:** Any `lessons/lesson-NN-*.md` file — they're numbered by difficulty
3. **Check the ocean animal reference:** `research/kenya-ocean-animals.md`
4. **Gather resources:** Each lesson lists what you need (mostly free tools)
5. **Teach:** Follow the 4-step lesson development structure
6. **Assess:** Use the BE/AE/ME/EE rubric table in each lesson
7. **Track progress:** Use `tracker/progress_tracker.py` to record and badge

**Recommended starting point for beginners:** Lesson 01 (System Persona) → Lesson 04 (Principles) → Lesson 29 (Physics with whale sharks)

---

## License

MIT — free to use, modify, and share. Built for the kids of Kenya's coast and beyond. 🌊

---

*This project is part of a growing movement to make animation education accessible to every child, regardless of hardware, budget, or geography. From Watamu to Lamu, from Mombasa to Diani — the ocean is our classroom, and every animal is a character waiting to be animated.*