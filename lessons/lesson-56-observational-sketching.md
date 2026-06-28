# Lesson Plan 56: Observational Sketching & Movement Studies — Training Your Eye

**Module Reference:** Prompt 56 — 56-observational-sketching.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Sketchbook + pencils (primary), no software needed

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Observational Drawing, Gesture Sketching & Movement Studies |
| Core Competency | Creativity & Imagination, Critical Thinking |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Create** 30-second gesture drawings capturing the line of action of a moving subject.
2. **Distinguish** between drawing from life (primary — trains eye-brain-hand) and drawing from video (secondary — useful but less effective).
3. **Start** a movement sketchbook with dated pages, practicing the same subject multiple times to track improvement.

## Key Inquiry Question

> If you want to animate a **dolphin (Pomboo)** jumping, should you watch a video — or should you go to **Kisite-Mpunguti Marine Reserve** and SEE one jump in real life? Why does drawing from life make your animation more believable?

---

## Resources

- Sketchbook (dedicated book — one per learner)
- Pencils (2B or softer for gesture work)
- Timer/phone (for 30-second intervals)
- Access to outdoor space (schoolyard, park, or ideally a zoo/aquarium)
- Reference photos of Kenyan ocean animals (as secondary reference)
- Optional: Line of Action website (line-of-action.com) for timed photo reference practice

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Tursiops aduncus*) — **Pomboo** in Swahili  
**Habitat:** Kisite-Mpunguti Marine Reserve, Watamu Marine National Park.  
**Why this animal?** Dolphins are fast, dynamic, and leap in clear arcs — perfect for gesture drawing. While most learners can't visit the marine reserve during class, they can study dolphin movement from video reference, then draw HUMANS doing similar motions (jumping, diving) from life. The connection: *your brain processes 3D space, depth, and weight differently when the subject is real and in front of you.* For schools near the coast, a beach trip to observe real marine life is the ideal application.  
**Conservation note:** Dolphins face threats from boat noise and net bycatch. KWS regulates dolphin-watching at Kisite-Mpunguti.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Ask learners to close their eyes and imagine a dolphin jumping. Now open eyes and draw it in 30 seconds.

Now show a VIDEO of a dolphin jumping. Draw it again in 30 seconds.

Now (if possible) have a learner JUMP in the classroom. Draw them mid-jump in 30 seconds.

Ask: *"Which drawing felt different? Which one captured the MOVEMENT better?"*

Explain: *Drawing from life is PRIMARY. Your brain processes 3D space, depth, and weight differently when the subject is real and in front of you. Video is SECONDARY — useful but less effective. Today we train our eyes to see real movement so our animation feels believable.*

### Step 1: Gesture Drawing Technique (15 min)

**What gesture drawing IS:**
- Quick sketches — 30 seconds to 2 minutes each
- NOT drawing details — no eyes, no fingers, no shading
- Capturing the LINE OF ACTION — the main flow of energy through the pose
- One sweeping line from head through spine to the furthest limb
- Think of it as catching the "feeling" of the pose, not the "look"

**3 Levels of Observation:**

| Level | Name | Time | What You Capture |
|-------|------|------|-----------------|
| 1 | Look-Memorize-Draw | 60 sec | Look for 5 sec, memorize the pose, then draw from memory |
| 2 | Quick Continuous Gesture | 30 sec | Draw continuously without looking at your paper — hand follows eye |
| 3 | Detailed Structural Study | 2-5 min | Build the figure using construction (skeleton → shapes → muscles, from Lesson 41) |

**Demo:** Teacher draws a 30-second gesture of a learner standing in a dynamic pose. Show the line of action as a single sweeping curve first, then add minimal body mass around it.

### Step 2: 20 Gestures in 10 Minutes (20 min)

**Exercise:** 20 gesture drawings at 30 seconds each.

**Subjects (adapt to available environment):**

If outdoors:
1-5: People walking (classmates or people in the area)
6-10: Birds flying or perching
11-15: Trees swaying in wind
16-20: Free choice (anything moving)

If indoors (using video/photo reference as secondary):
1-5: Dolphin jumping (video, paused at different points)
6-10: Turtle swimming (video)
11-15: Octopus crawling (video)
16-20: Learner doing dynamic poses (live — primary reference)

```python
# Timer script for gesture drawing sessions
# Run on Raspberry Pi or any Python device

import time
import os

num_gestures = 20
gesture_time = 30  # seconds per gesture

print(f"Gesture Drawing Timer: {num_gestures} gestures, {gesture_time}s each")
print("Press Enter to start...")

input()

for i in range(1, num_gestures + 1):
    print(f"\nGesture {i}/{num_gestures} — DRAW NOW!")
    for remaining in range(gesture_time, 0, -1):
        print(f"\r  Time: {remaining}s", end="", flush=True)
        time.sleep(1)
    print(f"\n  TIME! Next pose in 3 seconds...")
    time.sleep(3)

print(f"\nDone! You drew {num_gestures} gestures. Look at your improvement!")
```

**Rules during gesture drawing:**
- Don't look at your paper much (Level 2: continuous gesture)
- Don't erase — just draw over mistakes
- Don't draw details — capture the MOVEMENT
- Use loose, flowing lines
- Find the line of action FIRST, then add body mass

### Step 3: Animal Movement Study (20 min)

**Draw the same subject 5 times:**

Choose an animal (from video reference if live animals aren't available):
- **Dolphin:** easiest to study — clear arc motions, repeated jumps
- **Turtle:** slow, graceful — good for studying weight
- **Octopus:** complex — many tentacles, good for studying overlap

Draw the same animal 5 times from different angles or different moments in its movement:
1. First drawing: just starting to move
2. Second drawing: mid-motion
3. Third drawing: peak of action
4. Fourth drawing: coming down
5. Fifth drawing: recovery/settling

**Key observation:** Each drawing should show a DIFFERENT line of action. The line changes as the animal moves through its motion arc.

**Where to sketch (for future practice):**

| Location | What to Sketch | Why |
|----------|---------------|-----|
| Zoo/aquarium | Animals in motion | Real 3D movement (primary reference) |
| Beach (Kenya coast) | Crabs, birds, fish in tide pools | Local marine life |
| Cafe/market | People walking, sitting, talking | Human body mechanics |
| Park | Dogs, birds, trees in wind | Varied movement |
| Mirror | Yourself in poses | You're always available |

### Step 4: Building a Movement Sketchbook (15 min)

**Start a dedicated sketchbook TODAY.**

**Sketchbook rules:**
1. **Dedicated book** — only for movement studies, not general drawing
2. **Date every page** — track your improvement over time
3. **Draw the same subject multiple times** — repetition reveals movement patterns
4. **Mix life and video** — life is primary, video is secondary
5. **Don't tear out "bad" pages** — they show your progress

**How observational sketching improves animation:**
- You internalize real movement by SEEING and DRAWING it
- When you animate, your brain recalls the felt movement
- Animation becomes believable because YOU experienced the movement
- The line of action in your sketches becomes the arcs in your animation

**Commitment:** Each learner commits to 10 minutes of gesture drawing per day for the next week. Write the commitment in the front of the sketchbook.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Gesture Quality | Stiff, detailed, no movement | Some looseness but no line of action | Clear line of action; loose and energetic | Dynamic line of action + weight + energy in every gesture |
| Life vs Video | Cannot distinguish | Knows difference but doesn't apply | Chooses life when available, video as backup | Actively seeks life drawing; explains why it's better |
| Sketchbook | Not started | Started but undated | Dated, organized, multiple subjects | Dated + multiple subjects + same subject repeated + visible improvement |

---

## Extended Activity

**Coastal Sketchbook Project:** If the school is near the coast (or plans a field trip), take sketchbooks to Watamu Beach or Mombasa Marine Park. Spend 30 minutes doing gesture drawings of real marine life: crabs scuttling, birds diving, fish in tide pools. Date each page. After the trip, compare life drawings to video drawings — the life drawings will have more energy and weight. This is why professional animators always study from life.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Use 60-second gestures instead of 30 | Use 15-second gestures — pure line of action, no body mass |
| Provide photo reference (easier than video or life) | Draw from life only — no photo or video reference at all |
| Focus on human figures (easier than animals) | Study Aaron Blaisé's animal gesture technique (online tutorials) |
| Draw 10 gestures instead of 20 | Build a 30-day daily gesture habit — 20 gestures every day for a month |

---

## Teacher Reflection

- [ ] Did learners understand the difference between gesture drawing and detailed drawing?
- [ ] Were the 30-second gestures loose and energetic, or tight and detailed?
- [ ] Did they understand why life drawing is primary and video is secondary?
- [ ] Will they actually maintain the sketchbook? How can I check next week?