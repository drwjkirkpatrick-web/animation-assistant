# Lesson Plan 13: Animation Glossary — Building Your Term Dictionary

**Module Reference:** Prompt 13 — 13-glossary.md  
**Duration:** 70 min  
**Age Group:** 10-14  
**Animation Tool:** Scratch (browser) + paper flipbooks (low-resource)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Animation & Motion Graphics — Terminology & Vocabulary |
| Core Competency | Communication & Collaboration, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Define** at least 10 core animation terms (frame, keyframe, inbetween, FPS, onion skinning, squash & stretch, anticipation, arcs, follow-through, timing) in plain language.
2. **Apply** glossary terms to a working Scratch animation of a Kenyan ocean animal, labeling where each term appears in the project.
3. **Value** precise vocabulary as a tool for talking about and improving their own animation work.

## Key Inquiry Question

> "If Pweza the Octopus (*pweza*) is squeezing through a coral gap, what animation words do we need to describe every part of that movement?"

---

## Resources

- Scratch (scratch.mit.edu) — one laptop or Raspberry Pi per pair of learners
- Printed glossary cards (one term per card) — or hand-written on index cards
- Short video clip of an octopus moving (YouTube: "octopus swimming jet propulsion") — optional
- Paper flipbooks (stack of sticky notes) for the low-resource "Try it" exercises
- Reference photo of an octopus for drawing the Scratch sprite

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus (*Pweza*)  
**Habitat:** Coral reefs and rocky crevices along the Kenyan coast — Watamu Marine National Park, Mombasa Marine National Park, Kisite-Mpunguti Marine Reserve  
**Why this animal?** An octopus is the ultimate glossary animal. Its 8 arms demonstrate **follow-through** and **overlapping action** (arms trail at different times). It **squashes & stretches** to squeeze through narrow coral gaps. It uses **anticipation** before jet-propulsion darts. It **crawls** with ground contact and **changes color** — a rich secondary action. One animal, a dozen terms.  
**Conservation note:** Octopuses are not currently endangered, but they face pressure from overfishing and coral reef degradation along the Kenyan coast. KWS and local community groups in Watamu run reef restoration projects that protect octopus habitat. Healthy reefs mean healthy *pweza* populations.

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show a 30-second video (or describe from photos) of an octopus squeezing through a tiny crack in coral, then darting away in a cloud of ink.

Ask learners: *"Use your own words — what is the octopus doing? How would you describe that to someone who can't see it?"*

Write their words on the board: "squishing," "sliding," "arms following," "zooming off."

Say: *"Every one of those words is correct — but animators have special words for each part. Today we build our animation dictionary so we can talk about movement like professionals."*

Introduce **Pweza the Octopus** as today's character.

---

### Step 1: Concept Introduction — The Glossary Framework (15 min)

Teach the glossary format using 5 anchor terms, each illustrated by Pweza.

Explain the format every glossary entry will follow:
- **Plain English** — explain so a 10-year-old understands
- **Why it matters** — when animators use this
- **Example** — from a tool or real life
- **Try it** — a 2-minute mini-exercise

Walk through these 5 terms aloud, connecting each to the octopus:

| Term | Plain English | Octopus Example |
|------|--------------|-----------------|
| **Frame** | One single picture in an animation, like one flipbook page | One drawing of Pweza with arms in one position |
| **Keyframe** | An important frame where you set a pose; the computer fills in between | Pweza arms-wide (start) and arms-tucked (end) |
| **Inbetween** | The frames between keyframes — drawn by hand or made by the computer | The 5 frames showing arms moving from wide to tucked |
| **Onion Skinning** | Seeing nearby frames faintly through the current frame, like tracing paper | Seeing last frame's arm position faintly so you draw the next one accurately |
| **Squash & Stretch** | Squishing and stretching a shape to show weight and impact | Pweza's body squashes flat to squeeze through a coral gap, then stretches long when jetting away |

Show the Scratch code below and explain how each block maps to a glossary term.

**Runnable Scratch code — Pweza Glossary Demo:**

```scratch
when [green flag] clicked
  // KEYFRAME: set the start pose — arms wide
  switch costume to [pweza-arms-wide]
  // HOLD: stay still for half a second (not everything moves all the time)
  wait (0.5) seconds
  // ANTICIPATION: pull back slightly before the big move
  change [y] by (-10)
  wait (0.2) seconds
  // TWEENING / INBETWEEN: the computer fills in the glide
  //   glide is Scratch's built-in tween — it creates the inbetween frames for us
  glide (1) secs to x: (100) y: (0)
  // SQUASH & STRETCH: switch to the squeezed costume mid-move
  switch costume to [pweza-squashed]
  wait (0.1) seconds
  // stretch back out after passing through the gap
  switch costume to [pweza-arms-tucked]
  // FOLLOW-THROUGH: arms keep drifting after the body stops
  repeat (6)
    change [x] by (3)
    wait (0.05) seconds
  end
  // ARCS: turn in a curve, not a straight line
  repeat (18)
    move (10) steps
    turn [clockwise] (10) degrees
  end
```

> **Teacher note:** Before the lesson, create 3 octopus costumes in the Scratch sprite editor: `pweza-arms-wide` (arms spread), `pweza-squashed` (body flattened), `pweza-arms-tucked` (arms trailing). Learners can draw these in 5 minutes — simple ovals with 8 wiggly lines for arms.

---

### Step 2: Guided Practice — Build a Living Glossary (15 min)

Learners open Scratch and recreate the Pweza demo script above, adding **comment blocks** (right-click any block → "add comment") that label each term.

Walk the class through the first 3 blocks together:

1. *"Add the green flag block. Add a comment that says 'KEYFRAME — start pose.' This is your important frame."*
2. *"Add the glide block. Add a comment: 'TWEENING — computer creates inbetween frames.' See how you didn't draw every step? The computer did."*
3. *"Add the squash costume switch. Comment: 'SQUASH & STRETCH — body compresses through the gap.'"*

Then release learners to label the rest (hold, follow-through, arcs) using their glossary cards as reference.

Circulate and ask: *"Which term is this block showing? Can you find it on your glossary card?"*

---

### Step 3: Independent Practice — The Pweza Glossary Challenge (20 min)

**Challenge:** Each learner (or pair) must add **3 new terms** to their Pweza animation that are NOT yet in the demo script. They choose from:

- **Timing** — change the glide duration to show how more seconds = slower movement
- **Spacing** — use two glides with different distances to show big gap = fast, small gap = slow
- **Overlapping Action** — add a second sprite (a small fish) that starts moving 0.3 seconds AFTER Pweza, not at the same time
- **Secondary Action** — add a sound effect (ink squirt) or color change when Pweza squashes
- **Exaggeration** — make the squash costume extra-flat, beyond what's realistic

**Glossary card template** (learners fill one out for each new term they add):

```
Term: ___________________________
Plain English: _____________________________________________
Why it matters: ___________________________________________
Example in my Pweza animation: ______________________________
Try it (2-minute exercise): __________________________________
```

**Code starter for the Timing + Spacing extension:**

```scratch
when [green flag] clicked
  // TIMING: more seconds = slower
  glide (2) secs to x: (-100) y: (0)    // slow drift
  glide (0.5) secs to x: (100) y: (0)   // fast dart
  // SPACING: big distance in short time = fast
  //          small distance in long time = slow
```

---

### Step 4: Sharing & Feedback (12 min)

Learners pair up and do a **"Glossary Tour"**: they play their animation and narrate it using only glossary terms.

Example narration: *"Pweza starts in a keyframe, holds, anticipates, then the computer tweens the glide. See the squash costume? That's squash & stretch. The arms keep moving after — follow-through."*

Partner gives feedback using the **"I notice… I wonder…"** framework from the critique guide:
- *"I notice you used timing really well — the slow drift felt heavy."*
- *"I wonder if the follow-through could last one more repeat?"*

Celebrate learners who used the most terms correctly and those who tried the hardest new term.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| **Term definitions** | Defines fewer than 5 terms; definitions are vague or copy-pasted | Defines 5-7 terms in own words but misses key ideas | Defines 8-10 terms correctly in plain, own words | Defines 10+ terms; explains relationships between terms (e.g., keyframe → inbetween → tweening) |
| **Term application in Scratch** | Recreates the demo script but cannot label terms with comments | Labels most demo terms but added no new terms | Labels all demo terms AND adds 1-2 new terms with correct code | Adds 3+ new terms; code clearly demonstrates each term; comments are accurate |
| **Vocabulary in feedback** | Uses informal words only ("it looks cool/weird") | Attempts glossary terms but uses some incorrectly | Uses 5+ glossary terms correctly while narrating a peer's animation | Uses terms precisely and helps a peer identify which term could improve their animation |

---

## Extended Activity

**Homework — "Glossary in the Wild":** Watch any short animated clip (Looney Tunes, a Scratch project, or a nature documentary) and write down 5 glossary terms you can spot in the animation. For each, write one sentence: *"I saw [term] when [what happened on screen]."*

**Conservation connection:** Research one threat to octopus habitat on the Kenyan coast (overfishing, coral bleaching, plastic pollution). Write 2 sentences about it. We will share these next lesson.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-made octopus costumes so they focus on code and labeling, not drawing. Give them a printed glossary with definitions already filled in for the 5 anchor terms — their job is to match terms to code blocks. | Challenge them to add a **Graph Editor** analog: use Scratch's "glide" with custom ease by breaking a glide into 4 segments with increasing/decreasing wait times to simulate slow-in/slow-out. Have them define this as a new glossary entry. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes — can they define and use 10+ terms?
- [ ] Was Pweza the Octopus an engaging character for illustrating these terms?
- [ ] Did the Scratch demo make the abstract terms concrete, or did learners struggle to connect code to vocabulary?
- [ ] What would I change next time? (Consider: more flipbook "Try it" exercises before Scratch, or more peer narration time.)