# Lesson Plan 5: Code-First Animation — Scratch & Programmatic Animation

**Module Reference:** Prompt 05 — 05-code-first-animation.md  
**Duration:** 80 min  
**Age Group:** 10-14  
**Animation Tool:** Scratch (primary), Python/turtle (extension for 13+)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Computer Science — Introduction to Programming |
| Sub-strand | 4.3 Visual Programming (Scratch) / 4.4 Text-based Programming (Python) |
| Core Competency | Digital Literacy, Creativity & Imagination, Algorithmic Thinking (Critical Thinking & Problem Solving) |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain how animation can be created using code — loops, variables, and conditions — and describe coding as "controlling time" (knowledge)
2. Build a working Scratch animation using costume-switch and glide blocks to animate a Kenyan Indian Ocean animal (skill/practical)
3. Appreciate the link between programming logic and creative storytelling, and value the marine life that inspires the work (value/attitude)

## Key Inquiry Question

> How can we use code to make Samaki the clownfish dart and flap around its anemone home on the Mombasa reef?

---

## Resources

- **Scratch** — https://scratch.mit.edu (browser-based, free; also runs offline via the Scratch app on Raspberry Pi)
- Projector or large screen for live demonstration
- Reference video of a clownfish hovering and darting in an anemone (search "clownfish anemone behavior")
- Pre-made clownfish sprite with 2 costumes (fin-up / fin-down) — teacher shares via a Scratch studio or learners draw their own
- Optional: Raspberry Pi + monitor for low-resource settings (Scratch runs natively)
- **Unplugged fallback:** paper flipbook (2 drawings) for classrooms without computers

---

## Local Context: Kenyan Ocean Animal

**Animal:** Clownfish (Anemonefish) — Swahili: *Samaki*  
**Habitat:** Coral reefs (mwamba wa makorali) of **Mombasa Marine National Park** and **Malindi Marine National Park**, sheltering among sea-anemone tentacles  
**Why this animal?** The clownfish has a simple oval body and bright orange color — perfect as a first coded character. Its darting movement (quick direction changes) and constant fin-flapping hover map directly onto Scratch's **costume-switch** (Level 1) and **glide** (Level 2) patterns.  
**Conservation note:** Clownfish cannot survive without healthy coral reefs. Kenya's reefs are threatened by bleaching, overfishing, and plastic pollution. KWS and community groups run **reef restoration projects** in Mombasa and Watamu, replanting coral and policing fishing. When learners animate Samaki, they are animating an animal whose home needs protection.

---

## Lesson Development

### Introduction (8 min)

Show a 30-second video clip of a clownfish hovering and darting in an anemone. Ask learners:
- "What do you notice about how the fish moves?" *(hovers in place, fins flap constantly, suddenly darts to a new spot)*
- "Could we make a computer do this? What would we tell it to do?"

Introduce the big idea: **Coding IS animation. Every animated effect is a loop, a variable, and a condition.** Today we *control time with code* to bring Samaki the clownfish to life.

### Step 1: Concept Introduction — Costume-Switch Animation (15 min)

Teach **Level 1: Costume-Switch Animation.** In Scratch, the simplest animation = switching costumes inside a loop with a `wait` block. This teaches **frame rate** and **timing**.

Demonstrate these Scratch blocks (described by palette color and label, per the module's convention):

```
Scratch Blocks — Clownfish Fin Flap (Level 1: Costume Switch)

[Events]   when [green flag] clicked
[Looks]    switch costume to [clownfish-fin-up]
[Control]  forever
[Control]    wait [0.2] seconds
[Looks]      next costume
[Control]    wait [0.2] seconds
[Control]  end forever
```

**Line-by-line explanation:**
- `when green flag clicked` — starts the animation when we press Go
- `switch costume to [clownfish-fin-up]` — sets the starting frame so the animation always begins the same way
- `forever` — the loop; this is what makes the animation play continuously (our "infinite timeline")
- `wait [0.2] seconds` — the timing between frames. 0.2 s = about 5 frames per second. **This number controls speed.**
- `next costume` — switches to the next costume (fin-up → fin-down → fin-up…)
- The second `wait` keeps the timing even on both costumes

**Key teaching point:** The `wait` number *is* the animator's timing, expressed as code. Try 0.1 for nervous, fast flapping; 0.4 for slow, lazy fins. Ask: *"Which number makes Samaki look calm? Which makes it look scared?"*

### Step 2: Guided Practice — Glide Animation (15 min)

Now teach **Level 2: Glide & Move Animation.** Samaki doesn't just flap — it darts around its anemone. We use `glide [secs] to x:[ ] y:[ ]` for smooth motion, which teaches **easing** and **arcs**.

Walk through together — learners follow step by step on their own machines:

```
Scratch Blocks — Samaki Darting Around the Anemone (Level 2: Glide)

[Events]   when [green flag] clicked
[Control]  forever
[Motion]     glide [0.3] secs to x:[80]  y:[40]     ← dart right-up (fast)
[Motion]     glide [0.5] secs to x:[-60] y:[-20]    ← drift left-down (slower = ease)
[Motion]     glide [0.2] secs to x:[20]  y:[60]     ← quick dart up
[Motion]     glide [0.6] secs to x:[-80] y:[0]      ← long slow glide back
[Control]  end forever
```

**Line-by-line explanation:**
- Each `glide` moves Samaki to a new position over a set time — no teleporting, the sprite *travels*
- **Short glide time (0.2 s) = fast dart** — the clownfish zips
- **Long glide time (0.6 s) = slow drift** — the clownfish eases through the water (this is slow-in/slow-out!)
- The four positions trace a path that *orbits* the anemone at center (0, 0) — connect them and you get curved **arcs**, not straight lines
- **Combine with Step 1:** right-click the flap script → "duplicate," then run both at once so Samaki flaps *while* gliding

**Teacher tip:** Have learners add an "anemone" backdrop or a second sprite at center (0, 0) so the glide points visibly orbit around it.

### Step 3: Independent Practice — Samaki's Reef Challenge (20 min)

**Challenge:** Make Samaki the clownfish dart around its anemone, flap its fins, AND react when danger appears.

Give learners this starter and have them complete the `???` sections:

```
Scratch Blocks — Starter (learners fill in the ??? sections)

[Events]   when [green flag] clicked
[Looks]    switch costume to [clownfish-fin-up]
[Control]  forever
[Looks]      next costume
[Control]    wait [???] seconds            ← choose your flap speed
[Control]  end forever

[Events]   when [??? key] pressed          ← pick a key, e.g. "space"
[Motion]    glide [???] secs to x:[???] y:[???]   ← dart away to safety!
[Looks]     say [Watch out — papa! A shark!] for [2] seconds
```

**Tasks:**
1. Set the flap timing (try 0.15 for nervous, fast flapping when scared)
2. Choose a key that triggers a "dart to safety" glide
3. Add a **second sprite** — a shark (*papa*) — that glides in from the edge
4. Make Samaki say something in Swahili or English when it escapes to the anemone

**Extension for ages 13+:** If learners finish early, introduce the Python `turtle` version (see Differentiation).

### Step 4: Sharing & Feedback (10 min)

Learners present their Scratch projects to a partner or the class. Use the critique framework from Prompt 06:
- **Start positive:** "Your fin-flap timing really looks alive — great sense of timing!"
- **One "I wonder":** "I wonder what would happen if Samaki glided *slower* when escaping — would it feel more dramatic?"
- Celebrate that learners **coded** an animation — they didn't just draw it, they programmed time.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Costume-switch loop | Cannot build the flap loop even with help | Builds the loop with guidance; timing may be uniform or off | Builds a working flap loop independently; controls speed via `wait` | Builds loop + tests multiple `wait` values to find the best timing |
| Glide animation | Cannot use glide blocks | Uses glide but motion is jerky or all the same speed | Uses glide with varied times to show darting vs. drifting | Combines glide points into visible arcs; adds deliberate direction changes |
| Combining scripts & interactivity | Single script only | Two scripts but they conflict or overlap | Runs flap + glide together smoothly | Adds key-press trigger + second sprite + character dialogue |

---

## Extended Activity

**Homework — Samaki's Day at the Reef**
Add a second scene to the Scratch project: Samaki meets **Kasa the green turtle** gliding past the reef. Use `broadcast` messages (Level 3: Broadcast Choreography) to switch between scenes. Research **one fact** about why coral reefs (mwamba) in Mombasa are disappearing, and display it as a sprite "speech-bubble" fact in the animation. Share at the start of next lesson.

**Conservation connection:** Post the finished project to the class Scratch studio titled **"Bahari ya Hindi — Our Ocean."**

---

## Differentiation

| For learners who need more support | For advanced learners (ages 13+) |
|-------------------------------------|----------------------------------|
| Provide a pre-made clownfish sprite with 2 costumes already drawn; reduce the challenge to just the flap loop + one glide line. Use 0.3 s waits so timing is forgiving. | Graduate from Scratch to text-based code. Run this complete Python `turtle` program — it does the same darting animation in code: |

```python
# Samaki the Clownfish — Python Turtle Animation
# Ages 13+: graduate from Scratch to real code.
# Run:  python3 samaki_turtle.py
# (No install needed — turtle is part of Python's standard library.)

import turtle
import time

screen = turtle.Screen()
screen.bgcolor("deep sky blue")
screen.title("Samaki the Clownfish - Code-First Animation")

samaki = turtle.Turtle()
samaki.shape("circle")
samaki.color("orange")
samaki.penup()
samaki.speed(0)            # 0 = instant move, we control timing ourselves

# Each tuple = (x, y, glide_seconds)
# Shorter time = faster dart  (just like Scratch's glide secs)
path = [
    (80,  40, 0.3),    # dart right-up      (fast)
    (-60, -20, 0.5),   # drift left-down    (slower = ease)
    (20,  60, 0.2),    # quick dart up      (fast)
    (-80, 0,  0.6),    # long slow glide back (slowest)
]

print("Press Ctrl+C to stop the animation.")
try:
    while True:                       # forever loop — just like Scratch!
        for x, y, secs in path:
            samaki.goto(x, y)         # glide to position
            time.sleep(secs)          # wait = our timing control
except KeyboardInterrupt:
    print("Samaki says: Tutaonana! (See you later!)")

screen.bye()
```

> **Tweak challenge:** Add a 5th waypoint to the `path` list so Samaki loops in a bigger arc. Change one timing value and predict how the feel changes before you run it.

---

## Teacher Reflection

- [ ] Did learners achieve the three outcomes?
- [ ] Was the clownfish example engaging and locally relevant?
- [ ] Did learners understand that `wait` time = animation timing?
- [ ] Did older learners successfully transition to Python where attempted?
- [ ] What would I change next time?