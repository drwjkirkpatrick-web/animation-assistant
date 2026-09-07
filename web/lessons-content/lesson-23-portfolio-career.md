# Lesson Plan 23: Portfolio & Career Path — For Teens Who Want to Go Pro

**Module Reference:** Prompt 23 — 23-portfolio-career.md  
**Duration:** 60 min  
**Age Group:** 14-17  
**Animation Tool:** Any (Blender, Krita, OpenToonz, Scratch) + YouTube/ArtStation for hosting

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Computer Science |
| Sub-strand | Digital Animation — Portfolio Development & Career Planning |
| Core Competency | Communication & Collaboration, Digital Literacy, Self-Management |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Describe what a demo reel is, identify at least 3 career paths in animation, and explain why the reel matters more than a degree.
2. Assemble a portfolio plan and organize their animation work into a structured, dated folder system with a demo reel outline.
3. Value persistence and volume in skill-building, and understand how creative skills can serve conservation storytelling in Kenya.

## Key Inquiry Question

> If your demo reel is your resume in animation, how do we build a reel around **Pomboo the Dolphin** that shows range — swimming, jumping, and acting — and what career paths can it open for you?

---

## Resources

- A computer with internet access (for researching career paths and hosting portfolios)
- Learners' previous animation work (from Lessons 1-22 — bouncing balls, walk cycles, rigged characters, composited scenes)
- **YouTube** account (free, for hosting demo reels — unlisted is fine) or **ArtStation** account (free, industry standard)
- File organizer: a computer with folders, or USB drives / shared drive for low-resource settings
- Printed "Demo Reel Planning Sheet" (template provided in Step 2)
- Projector for showing example demo reels (search "student animation demo reel" on YouTube)
- *Optional:* Phone camera for recording a self-introduction video to accompany the reel

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin — *Pomboo* (Swahili)  
**Habitat:** Coastal waters of Watamu Marine National Park and Kisite-Mpunguti Marine Reserve, Kenya's Indian Ocean coast. Dolphins live in pods (family groups) and are frequently seen playing and jumping near the coast.  
**Why this animal?** The dolphin is the **ultimate range demonstrator** for a demo reel. A single dolphin character can show: a **swimming cycle** (body mechanics), a **breaching jump** (anticipation + arcs + weight), a **playful spin** (acting/personality), and a **pod interaction** (multiple characters). This is exactly what recruiters look for — **range** across different animation skills in one character. The dolphin's natural playfulness also makes portfolio-building fun rather than a chore.  
**Conservation note:** Dolphin populations in Kenya face threats from **bycatch** (getting caught in fishing nets) and **pollution**. The Kenya Wildlife Service (KWS) has established **dolphin-watching regulations** — boats must keep a respectful distance and avoid surrounding pods. **Class discussion:** Animators who can create compelling dolphin animations can support ecotourism education and conservation campaigns. Your creative skills have real-world impact — a well-made dolphin animation shown to tourists could teach them to respect dolphin-watching guidelines.

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show a professional animation demo reel (1-2 minutes, search "animation student demo reel" on YouTube). Then ask:

- "How long was that reel?" *(Answer: under 2 minutes)*
- "How many years of work did you see in those 2 minutes?" *(Answer: months to years!)*
- "Do you think this person got hired because of their degree or because of this reel?" *(Answer: the reel. In animation, your reel IS your resume.)*

Introduce the key concept: **A demo reel is a 1-2 minute video showing your BEST animation. It's more important than a degree. Studios hire based on reels, not resumes.**

**Connect to Pomboo:** "Today, we're going to plan a demo reel around Pomboo the Dolphin — a character that can show off everything you've learned: swimming cycles, jumping arcs, acting, and more. We'll also explore the career paths your animation skills can open."

**Quick career paths overview (display on board):**

| Career | What They Do | Key Skill |
|--------|-------------|-----------|
| Character Animator | Animate characters acting, walking, showing emotion | 12 Principles, body mechanics |
| Storyboard Artist | Draw the "comic book" version of a film before animation | Drawing, composition, storytelling |
| Rigger / TD | Build digital skeletons and controls for characters | Rigging, Python scripting, anatomy |
| Effects Animator | Animate fire, water, smoke, explosions | Physics simulation, particles |
| Motion Graphics Designer | Animated logos, titles, explainers | Typography, timing, design |
| Independent / Web Animator | Make own shorts, web series, YouTube content | Everything! |

---

### Step 1: Concept Introduction — Portfolio Building by Age (12 min)

Teach portfolio progression and what goes on a demo reel.

**Portfolio Progression:**

| Age | Stage | Goal |
|-----|-------|------|
| 14 | Foundation Building | Save everything; focus on fundamentals (bouncing ball, walk cycle, head turn); 5-10 pieces |
| 15-16 | First Demo Reel | Select 5-8 best pieces; keep under 90 seconds; best piece FIRST |
| 16-17 | Refined Portfolio | 60-90 seconds, all polished; show RANGE; create ArtStation; tailor to job type |

**What Goes On a Demo Reel:**

✅ **DO include:**
- Bouncing ball (squash & stretch + timing)
- Walk/swim cycle (body mechanics)
- Acting piece (character showing emotion through body language)
- One "passion piece" — something you made just because you wanted to
- For our class: a **Pomboo the Dolphin animation** showing swimming + jumping

❌ **DON'T include:**
- Everything you've ever made (curate ruthlessly — 1 great piece beats 5 mediocre)
- Unfinished work (unless it's a visible wireframe/breakdown)
- Tutorial results where you followed step-by-step (recruiters recognize these)
- Copyright music

**The #1 rule:** Best piece goes FIRST. Recruiters may only watch 10 seconds.

**Code Block — Portfolio Organization Script (Python/Bash):**

```python
# === PORTFOLIO ORGANIZER SCRIPT ===
# Run this Python script to create a structured portfolio folder
# for your animation journey. Works on any computer with Python.

import os
from datetime import datetime

# Set your portfolio root folder (change this path!)
portfolio_root = "/home/student/MyAnimationJourney"

# Create the main folder
os.makedirs(portfolio_root, exist_ok=True)

# Create subfolders for each type of work
folders = [
    "01_Fundamentals",        # bouncing ball, timing exercises
    "02_WalkCycles_and_Swim", # walk cycles, swim cycles (Kasa, Pomboo)
    "03_Acting_and_Emotion",  # character performance pieces
    "04_Rigging",             # rig tests and breakdowns
    "05_Composited_Scenes",   # finished, rendered animations
    "06_DemoReel",            # final demo reel exports
    "07_Reference",           # reference videos, images
    "08_WIP",                 # work in progress (not ready for reel)
]

print(f"Creating portfolio structure at: {portfolio_root}")
for folder in folders:
    path = os.path.join(portfolio_root, folder)
    os.makedirs(path, exist_ok=True)
    print(f"  ✓ {folder}")

# Create a README file with today's date
readme_path = os.path.join(portfolio_root, "README.txt")
with open(readme_path, "w") as f:
    f.write("My Animation Journey\n")
    f.write(f"Started: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    f.write("Folder Guide:\n")
    f.write("01_Fundamentals — basic exercises (bouncing ball, timing)\n")
    f.write("02_WalkCycles_and_Swim — locomotion (turtle swim, dolphin jump)\n")
    f.write("03_Acting_and_Emotion — character performance\n")
    f.write("04_Rigging — rig tests and breakdowns\n")
    f.write("05_Composited_Scenes — finished rendered animations\n")
    f.write("06_DemoReel — your final demo reel exports\n")
    f.write("07_Reference — videos and images you study from\n")
    f.write("08_WIP — work in progress, not ready for the reel yet\n\n")
    f.write("RULE: Save EVERYTHING. Even bad animations show growth.\n")
    f.write("Date every file: YYYY-MM-DD_projectname.mp4\n")

print(f"\n✓ README created at {readme_path}")
print("\nPortfolio structure ready!")
print("Next: Move your existing animations into the right folders.")
print("Name each file with the date: 2026-06-28_dolphin-jump.mp4")
```

---

### Step 2: Guided Practice — Plan Your Pomboo Demo Reel (15 min)

Walk through planning a demo reel together. Learners fill out their Demo Reel Planning Sheet.

**Demo Reel Planning Sheet (print and distribute):**

```text
═══════════════════════════════════════════════
       MY DEMO REEL PLANNING SHEET
       Featuring: Pomboo the Dolphin
═══════════════════════════════════════════════

Name: _______________________
Date: _______________________
Reel Title: "Demo Reel 2026 — [Your Name]"

TOTAL TARGET TIME: 60-90 seconds
RULE: Best piece goes FIRST!

PIECE 1 (0:00-0:15) — BEST PIECE
  What: _______________________ 
  (e.g., "Pomboo breach jump — anticipation + arc + splash")
  Skill it shows: ______________
  Status: [ ] Done  [ ] Needs polish  [ ] Not started

PIECE 2 (0:15-0:30)
  What: _______________________
  (e.g., "Pomboo swimming cycle — body mechanics")
  Skill it shows: ______________
  Status: [ ] Done  [ ] Needs polish  [ ] Not started

PIECE 3 (0:30-0:45)
  What: _______________________
  (e.g., "Kasa the Turtle walk on beach — weight + contact")
  Skill it shows: ______________
  Status: [ ] Done  [ ] Needs polish  [ ] Not started

PIECE 4 (0:45-0:60)
  What: _______________________
  (e.g., "Acting piece — Pomboo curious about a camera")
  Skill it shows: ______________
  Status: [ ] Done  [ ] Needs polish  [ ] Not started

PIECE 5 (0:60-0:75) — PASSION PIECE
  What: _______________________
  (something you made just for fun)
  Skill it shows: ______________
  Status: [ ] Done  [ ] Needs polish  [ ] Not started

TITLE CARD: Name, email, "Demo Reel 2026"
MUSIC: [ ] No music  [ ] Instrumental only (NO vocals)
HOSTING: [ ] YouTube (unlisted)  [ ] ArtStation  [ ] Both

═══════════════════════════════════════════════
```

**Walk through together:**
1. Have learners list every animation they've made so far in this course (bouncing ball, turtle swim, whale shark composite, etc.).
2. Help them identify which piece is their **strongest** — that goes first.
3. Check for **range**: Do they have body mechanics (swim/walk cycle)? Acting (emotion)? Effects (water splash)?
4. If they're missing a category, that becomes their next project.

**Key advice:**
- "If you only have 3 pieces, that's fine — 3 great pieces beat 8 mediocre ones."
- "Your Pomboo dolphin jump is a perfect Piece 1 — it shows anticipation, arcs, and weight all at once."
- "If you don't have an acting piece yet, your next project should be one: Pomboo looking curious, surprised, or playful."

---

### Step 3: Independent Practice — Organize & Research Careers (15 min)

Learners do two things independently:

**Part A: Run the portfolio organizer script and sort their work**

1. Run the Python script from Step 1 (or create the folders manually if Python isn't available).
2. Move their existing animation files into the appropriate folders.
3. Rename each file with the date format: `YYYY-MM-DD_projectname.mp4`
4. Identify which pieces are reel-ready and which need more work.

**Part B: Research a career path**

Learners pick one career path that interests them and research it:

```text
=== CAREER PATH RESEARCH SHEET ===

Career I'm interested in: _____________________

1. What does this person do day-to-day?
   ___________________________________________

2. What skills do they need?
   ___________________________________________

3. What tools do they use?
   ___________________________________________

4. What's the career path? (junior → senior)
   ___________________________________________

5. What's ONE thing I can do this month to move
   toward this career?
   ___________________________________________

Free resources for this career:
- _________________________________________
- _________________________________________
```

**Career reality check (share with the class):**
> "Animation is competitive. Your reel competes with people who've been doing this for years. That's why **volume matters** — make one short piece every month. The first year is hard. Everything you make will feel not good enough. That's normal. Keep going."

---

### Step 4: Sharing & Feedback (10 min)

Learners share their demo reel plan and career research in pairs or small groups.

**Pair share protocol:**
1. **Show your plan:** Share your Demo Reel Planning Sheet. What's your Piece 1?
2. **Get feedback:** Partner uses the critique framework:
   - "I notice your reel shows swimming and jumping — good range."
   - "I wonder if you have an acting piece? Recruiters look for that."
   - "What if you added a breakdown showing your rig?"
3. **Share your career path:** Which career interests you and why?

**Class discussion:**
- "How many of you discovered you're missing a category in your reel? What will you make next?"
- "Which career path surprised you? Did anyone discover a path they didn't know existed?"
- "How could your animation skills serve conservation in Kenya?" *(Answers: conservation campaign videos, ecotourism education, KWS awareness content, school programs)*

**One thing to do this month (every learner states theirs out loud):**
- "I will finish my Pomboo jump animation and render it."
- "I will create an ArtStation account and upload my best piece."
- "I will make one new 5-second animation this month."
- "I will study a dolphin video at 0.25x speed and count the frames."

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Portfolio Organization | Files are scattered, unorganized, no folder structure | Some files organized but no clear system; files not dated | Structured folder system created; files sorted and dated; reel-ready pieces identified | Organized system with clear categories, dated files, AND a written plan for what to create next to fill gaps |
| Demo Reel Planning | No reel plan; cannot identify which pieces are strongest | Basic reel plan but missing range or pieces are not ordered by quality | Complete reel plan with 3-5 pieces ordered by quality, showing range across at least 2 skill types, under 90 seconds | reel plan shows range across 3+ skills (mechanics, acting, effects), includes title card, hosting plan, and a passion piece |
| Career Understanding | Cannot name animation career paths or explain what a demo reel is | Can name 1-2 career paths and knows what a demo reel is | Can describe 3+ career paths, explains why the reel matters more than a degree, and has researched one path in depth | Describes multiple career paths with tools/skills for each, has a personal next-step plan, AND can connect animation skills to conservation or local opportunities in Kenya |

---

## Extended Activity

**Homework/Project: Create Your First Demo Reel (if you have enough pieces)**

If you have 3+ finished animations:
1. Use a free video editor (OpenShot, Shotcut, or even your phone's editor) to combine your best pieces.
2. Order them: best piece first.
3. Add a title card: your name, email, "Demo Reel 2026."
4. Keep it under 90 seconds.
5. Add instrumental music only (or no music).
6. Upload to YouTube (unlisted is fine) or ArtStation.
7. Share the link with your teacher and classmates.

**If you don't have enough pieces yet:**
Your homework is to make ONE new animation this month. Suggestion: Animate **Pomboo the Dolphin** breaching out of the water — showing anticipation (the deep dive before the jump), the arc through the air, and the splash on return. This single piece demonstrates three principles at once and would be a strong demo reel opener.

**Conservation connection:** Research dolphin-watching guidelines in Kisite-Mpunguti Marine Reserve. Create a 10-second animated public service announcement: "Keep your distance — dolphins need space too." This could be a portfolio piece AND a conservation tool.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide the folder structure pre-made on a USB drive. Give them a simplified reel plan with just 3 slots. Focus on organizing existing work rather than planning new pieces. Help them identify their single best animation. | Build a full ArtStation portfolio page with a demo reel, individual piece posts with descriptions, and a breakdown showing the rig and keyframes. Research a specific studio or animation school and tailor the reel to their requirements. Learn basic video editing in OpenShot or Shotcut for reel assembly. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Pomboo the Dolphin example effective for demonstrating range in a demo reel?
- [ ] Did learners engage with the career paths, or was it overwhelming? Should I focus on fewer paths next time?
- [ ] Was the portfolio organizer script helpful, or should I provide pre-made folders instead?
- [ ] What would I change next time? (Consider: bringing in a guest animator from Kenya, showing more diverse demo reels, or spending more time on the "one thing to do this month" commitment)
- [ ] Did the conservation connection — using animation for dolphin awareness — resonate with learners? Did any learners express interest in conservation animation as a career?