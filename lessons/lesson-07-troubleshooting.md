# Lesson Plan 7: Troubleshooting — When the Animation Goes Wrong

**Module Reference:** Prompt 07 — 07-troubleshooting.md  
**Duration:** 70 min  
**Age Group:** 12-14  
**Animation Tool:** Scratch (primary debugging lab); concepts transfer to Krita, Pencil2D, Blender

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Computer Science — Computer Software / Introduction to Programming |
| Sub-strand | 3.1 System Software (troubleshooting) / 4.1 Algorithms (debugging) |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy, Learning to Learn |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Categorize an animation problem into one of four types: principle issue, tool/technique gap, technical/software fault, or creative block (knowledge)
2. Apply a diagnostic checklist to find and fix bugs in a broken Scratch animation of a Kenyan ocean animal (skill/practical)
3. Value a systematic, calm approach to problems — debugging is normal, not a failure (value/attitude)

## Key Inquiry Question

> Pweza the octopus's animation is broken — it slides instead of crawls, the arms flap too fast, and it won't loop. How do we find and fix each problem?

---

## Resources

- **Scratch** — https://scratch.mit.edu (the debugging lab)
- Projector or large screen for demonstration
- The **"Broken Pweza" starter project** — teacher shares a Scratch project with 3 intentional bugs (or learners build it from the code in Step 2)
- Printed **Diagnostic Checklist** cards (one per pair) — see Step 1
- Optional: Krita or Pencil2D installed, to show how the same diagnostic thinking applies across tools
- Reference video of an octopus crawling and jet-propelling (search "octopus crawling underwater")

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus — Swahili: *Pweza*  
**Habitat:** Rocky reefs and coral crevices of **Watamu Marine National Park** and **Mombasa Marine National Park**; hides in holes during the day, hunts at night  
**Why this animal?** The octopus has **eight arms** — the ultimate test of **secondary motion**, **follow-through**, and **overlapping action**. With so many moving parts, an octopus animation has many ways to break: arms move in sync when they shouldn't, the body slides instead of gripping, the crawl won't loop. Pweza is the perfect troubleshooting subject because every common animation bug shows up clearly.  
**Conservation note:** Octopuses are highly intelligent — they solve puzzles and use tools. They face pressure from **overfishing** (octopus is a popular coastal food) and **habitat damage** to the reefs they hide in. KWS marine parks protect their reef habitat. Sustainable octopus fishing programs in some Kenyan coastal communities rotate harvest areas to let populations recover.

---

## Lesson Development

### Introduction (8 min)

Show a 20-second video of an octopus (pweza) crawling across a reef — arms gripping, body shifting, color changing. Then show the **"Broken Pweza"** animation: the octopus slides flatly across the screen, arms spasming at high speed, and it plays once then stops.

Ask: *"This octopus is broken. How many things can you spot that are wrong?"*

Let learners call out problems. Write them on the board. Then introduce the key idea: **Don't panic, diagnose.** Real animators and programmers spend a big part of their time fixing things that don't work. Debugging is a skill, not a sign of failure.

### Step 1: Concept Introduction — The Diagnostic Framework (12 min)

Teach the four-step troubleshooting approach from Prompt 07. Display it:

```
Animation Troubleshooting — "Diagnose Before You Fix"

STEP 1: WHAT KIND OF PROBLEM IS IT?
  A. "It doesn't look right"        → ANIMATION PRINCIPLE issue
  B. "The software won't do X"      → TOOL/TECHNIQUE knowledge gap
  C. "It's broken/crashing/won't export" → TECHNICAL/SOFTWARE issue
  D. "I don't know what to do next" → CREATIVE BLOCK / planning issue

STEP 2: ASK DIAGNOSTIC QUESTIONS BEFORE GIVING SOLUTIONS
  Don't assume. Get the key info first, then fix.

STEP 3: PRINCIPLE CHECKLIST (for "it doesn't look right")
  - Timing right?      (too fast = frantic, too slow = sluggish)
  - Squash & stretch?  (where the body compresses & extends)
  - Arcs correct?      (should be curved, not straight-line)
  - Anticipation?      (a wind-up before the main action)
  - Follow-through?    (parts keep moving AFTER the body stops)

STEP 4: APPLY THE FIX, THEN TEST
  Change ONE thing at a time. Re-run. Did it help?
```

Distribute the **Diagnostic Checklist** cards (printed version of the above). Learners will use these in Step 3.

### Step 2: Guided Practice — Meet the Broken Pweza (15 min)

Build (or load) the broken octopus animation together so everyone has the same buggy starting point. Here is the **intentionally buggy** Scratch code:

```
Scratch Blocks — "Broken Pweza" (3 bugs to find)

[Events]   when [green flag] clicked
[Looks]    switch costume to [pweza-arm1]
[Looks]    next costume
[Looks]    next costume
[Control]  wait [0.02] seconds                  ← BUG #1: way too fast
[Motion]   glide [3] secs to x:[200] y:[0]       ← BUG #2: one long flat glide = slides, no crawl
                                                    (no forever loop either!)
                                                    ← BUG #3: no "forever" wrapper = plays once, stops
```

Walk through the diagnosis as a class, modeling the framework:

- **Bug #1 — Arms too fast:** "What category? It doesn't look right → principle issue. The checklist says check *timing*. 0.02 s wait = 50 flaps per second — that's a spasm, not a crawl. **Fix:** change `wait` to 0.2 s."
- **Bug #2 — Slides instead of crawls:** "Checklist says check *arcs* — should be curved, not straight. One long glide to (200, 0) is a flat line. A real octopus grips and pulls in stages. **Fix:** break it into several shorter glides with slight up/down offsets to create a crawling arc."
- **Bug #3 — Won't loop:** "Category: software/technique. The blocks aren't inside a `forever` block. **Fix:** wrap everything in `forever { … }`."

**Here is the FIXED version:**

```
Scratch Blocks — "Fixed Pweza" (crawls, flaps at the right speed, loops)

[Events]   when [green flag] clicked
[Looks]    switch costume to [pweza-arm1]
[Control]  forever                                  ← FIX #3: now it loops
[Looks]      next costume
[Control]    wait [0.2] seconds                      ← FIX #1: natural flap speed
[Motion]     glide [0.4] secs to x:[50]  y:[10]      ← FIX #2: crawl in stages
[Motion]     glide [0.4] secs to x:[100] y:[0]       ←   with slight arcs
[Motion]     glide [0.4] secs to x:[150] y:[12]      ←   (grip, pull, grip, pull)
[Motion]     glide [0.4] secs to x:[200] y:[0]
[Motion]     glide [2] secs to x:[-150] y:[0]        ← jet back to start (slow drift)
[Control]  end forever
```

**Key teaching point:** We changed **one thing at a time** and re-ran after each fix. That's how you know *which* change solved *which* problem.

### Step 3: Independent Practice — Debug Pweza's Reef (20 min)

Learners work in pairs. Each pair gets a **new broken project** (or creates one for another pair). The project has 3 bugs from this list — pairs must **diagnose using the checklist**, then fix:

**Bug menu (teacher assigns 3 per pair):**
| Bug | Symptom | Category | Fix |
|-----|---------|----------|-----|
| `wait` set to 0.01 | Arms blur/spasm | Principle — timing | Raise to 0.2-0.3 |
| No `forever` block | Plays once, stops | Software/technique | Wrap in `forever` |
| Single flat glide | Octopus slides, no crawl | Principle — arcs | Break into staged glides with arcs |
| All 8 arms switch costume together | Arms move in sync (no overlap) | Principle — follow-through/overlap | Offset arm costumes with separate `wait` values |
| Octopus starts off-screen | Can't see it at first | Tool/technique | Add `go to x:[0] y:[0]` at start |
| `next costume` missing | Arms don't flap at all | Software/technique | Add `next costume` in the loop |

Pairs fill out a **Debug Log** for each bug:

```
DEBUG LOG — Pair: ___________
Bug #___  Symptom I see: ____________________
Category (A/B/C/D): ___
My diagnostic question: ____________________
What I changed: ____________________
Did it work? (yes/no): ___
```

### Step 4: Sharing & Feedback (10 min)

Pairs demonstrate their **fixed** Pweza animation and read out one Debug Log entry — sharing the *diagnosis*, not just the result. The class guesses which bug it was.

Celebrate the thinking: *"The best fixers aren't the ones who never break things — they're the ones who can figure out why."*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Categorizes the problem | Cannot tell what type of problem it is | Identifies the category with prompting | Independently sorts the bug into the right category (A/B/C/D) | Categorizes correctly AND explains why other categories don't fit |
| Uses the diagnostic checklist | Guesses fixes randomly | Uses one checklist item with help | Runs through timing/arcs/loop checks systematically | Uses the full checklist + asks diagnostic questions before fixing |
| Fixes & verifies | Changes many things at once, can't tell what worked | Fixes one bug with guidance | Fixes bugs one at a time, re-runs to verify each | Fixes all bugs + explains the cause-and-effect of each change |

---

## Extended Activity

**Homework — Bug Hunter**
Find a real animation you made in an earlier lesson (or a friend's). Run the diagnostic checklist on it. Write down: one thing that's a **principle issue**, one that's a **tool/technique gap**, and the fix you'd try for each. Bring it next class.

**Conservation connection:** Add a "healthy reef" backdrop to Pweza's animation and a speech bubble: *"Pweza needs clean reefs to hide and hunt. Pick up plastic at the beach (pwani)!"*

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Give a **partially-fixed** project with only 1 bug remaining and the category already labeled. Provide the Bug Menu with the fix column pre-filled so they focus on *matching symptom to fix*. | Assign **all 6 bugs** in one project. Add a cross-tool challenge: recreate one bug in **Krita** (e.g., onion skin not showing → check the Onion Skin docker is enabled) and have them write the tool-specific fix steps. Introduce the concept of **overlapping action** — make the 8 arms flap with staggered timing (each arm's `wait` offset by 0.03 s) so they move in a wave, not in sync. |

---

## Teacher Reflection

- [ ] Did learners achieve the three outcomes?
- [ ] Was the octopus (pweza) a good subject for finding multiple bugs?
- [ ] Did learners diagnose before fixing, or jump straight to changing code?
- [ ] Did they change one thing at a time and re-test, or change everything at once?
- [ ] What would I change next time?