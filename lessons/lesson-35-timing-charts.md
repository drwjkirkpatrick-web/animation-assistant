# Lesson Plan 35: Timing Charts & Spacing Diagrams — Planning the Frames

**Module Reference:** Prompt 35 — 35-timing-charts.md
**Duration:** 70 min
**Age Group:** 12-17
**Animation Tool:** Scratch (primary) / Krita or OpenToonz (optional extension)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Performing Arts — Animation and Digital Storytelling |
| Core Competency | Critical Thinking, Creativity & Imagination, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain what a timing chart is and why planning spacing before animating produces better results than guessing.
2. Draw a timing chart for a falling/rising object using the Odd Rule (1, 3, 5, 7, 9) and identify the correct spacing pattern (ease in, ease out, ease in+out).
3. Apply a timing chart to animate Papa Shinga the whale shark drifting downward through the water column, using Scratch `wait` blocks or Krita key frames to control spacing.

## Key Inquiry Question

> How do we plan the frames BEFORE we animate so that Papa Shinga the whale shark feels truly massive and heavy — drifting slowly, then sinking faster — instead of moving at a constant robotic speed?

---

## Resources

- Scratch (offline or online at scratch.mit.edu) or Krita / OpenToonz (free downloads)
- Graph paper or plain paper for drawing timing charts
- Pencils and rulers
- Projector or large screen for demonstration
- Reference video of whale sharks swimming (search "whale shark slow motion swimming")
- Printed Odd Rule reference: 1, 3, 5, 7, 9 pattern
- Optional: Blender for advanced learners (Graph Editor demonstration)
- Optional: Raspberry Pi running Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Whale Shark (Papa Shinga)
**Habitat:** Open ocean along Kenya's coast, especially visible at Watamu Marine National Park and Diani-Chale Marine Reserve from October to February. Whale sharks come close to shore during plankton blooms.
**Why this animal?** The whale shark is the largest fish in the ocean — up to 18 meters long. Its massive size means it moves SLOWLY and gracefully, with each movement covering huge distance. This makes Papa Shinga the perfect character for teaching timing and spacing: a whale shark drifting downward through the water column naturally demonstrates acceleration (starts slow, speeds up due to gravity/sinking) — the Odd Rule in action. The contrast between a whale shark's slow drift and a small fish's quick dart makes the concept of spacing visible and dramatic.
**Conservation note:** Whale sharks are classified as Endangered by the IUCN. Main threats include boat strikes (they swim slowly at the surface), fishing, and plastic pollution. KWS runs a whale shark tagging program to track their movements along the Kenya coast, and there are tourism guidelines to keep boats at a safe distance. Learners can create animations that raise awareness about protecting Papa Shinga from boat traffic.

---

## Lesson Development

### Introduction (8 min)

Show a video or photo of a whale shark (Papa Shinga) swimming slowly at the Kenya coast. Ask learners:
- "How would you describe how this animal moves?"
- "If we animated it moving at a constant speed — the same amount every frame — would it look real? Why or why not?"

Explain the core concept: **"Spacing" = how far an object moves between frames.**
- Big gap between frames = FAST movement
- Small gap between frames = SLOW movement
- Equal gaps = constant speed (looks robotic/dead)
- Changing gaps = acceleration/deceleration (looks ALIVE)

Introduce the timing chart as a "map before you drive." You wouldn't drive across Kenya without planning your route — don't animate without planning your frames.

Connect to Papa Shinga: "A whale shark is so heavy that when it sinks in the water, it starts slowly and gets faster — just like gravity. Today we'll learn the Odd Rule that describes this, and we'll plan the frames BEFORE we animate."

### Step 1: Concept Introduction — The Odd Rule & Timing Charts (15 min)

**Teach the Odd Rule (Gravity Spacing):**

When something falls under gravity, the spacing follows the Odd Rule:
- Frame 1→2: move 1 unit
- Frame 2→3: move 3 units
- Frame 3→4: move 5 units
- Frame 4→5: move 7 units
- Frame 5→6: move 9 units

The pattern is **1, 3, 5, 7, 9** — odd numbers increasing by 2. The object STARTS SLOW and GETS FASTER. That's acceleration. That's gravity.

**Going UP is the reverse:** 9, 7, 5, 3, 1 — starts fast, slows down, stops at the top.

**Fourth Down at Half Time:** For pose-to-pose animation, the breakdown frame (halfway in TIME between apex and ground) is only 1/4 of the DISTANCE down from the top. If the apex is at frame 0 and ground at frame 12, the breakdown at frame 6 is only 25% of the way down, not 50%. Things accelerate — they cover more ground later.

**Draw a timing chart together on the board:**

```
Frame 1  ●━━━ Key pose (Papa Shinga near surface — top)
         |
         |  (1 unit — slow start)
         |
Frame 3  ○━━━ Breakdown (only 1/4 down — Fourth Down at Half Time)
         |
         |  (3 units)
         |
         |  (5 units)
         |
         |  (7 units)
         |
Frame 8  ●━━━ Key pose (Papa Shinga deep — bottom, moving fast)
```

**Spacing patterns reference:**

| Pattern | Spacing | Use When |
|---------|---------|----------|
| Ease In (slow start) | Small → Big gaps | Object starting to move, anticipation release |
| Ease Out (slow stop) | Big → Small gaps | Object stopping, landing |
| Ease In+Out | Small → Big → Small | Most natural movement (slow fast slow) |
| Linear | Equal gaps | Robots, machines ONLY |
| Odd Rule | 1, 3, 5, 7, 9 | Falling under gravity |
| Reverse Odd | 9, 7, 5, 3, 1 | Rising against gravity (decelerating) |

**Code demonstration — the Odd Rule in Python:**

Show learners how the Odd Rule works computationally. This Python script generates the spacing values and shows where Papa Shinga should be on each frame:

```python
# PAPA SHINGA TIMING CHART — The Odd Rule
# Whale shark sinks from surface (y=0) downward
# Each frame, it moves more than the last (acceleration)

units_per_frame = [1, 3, 5, 7, 9, 11]  # The Odd Rule pattern
position = 0  # Start at the surface

print("PAPA SHINGA SINKING — Timing Chart")
print("=" * 45)
print(f"Frame 1: position = {position} (surface — START)")
print(f"         gap to next: {units_per_frame[0]} units (SLOW)")

for i, gap in enumerate(units_per_frame, start=2):
    position += gap
    speed = "SLOW" if gap <= 3 else ("MEDIUM" if gap <= 7 else "FAST")
    print(f"Frame {i}: position = {position} (gap: {gap} units — {speed})")

print("=" * 45)
print(f"Total distance: {position} units in {len(units_per_frame)+1} frames")
print()
print("KEY INSIGHT: Papa Shinga starts slow (1 unit/frame)")
print("and gets faster each frame. That's GRAVITY. That's ALIVE.")
print()
print("If we used EQUAL gaps (linear), it would look ROBOTIC.")
print("Try it: change units_per_frame to [5, 5, 5, 5, 5, 5]")
print("and see how wrong it looks!")
```

Run this script (or walk through the output on the board). Learners see the numbers grow: 1, 4, 9, 16, 25, 36, 47 — Papa Shinga covers more distance each frame.

**Scratch demonstration — applying the Odd Rule with wait blocks:**

```scratch
when [green flag] clicked
// PAPA SHINGA SINKS — Odd Rule spacing
// We use glide with INCREASING step distances
// Short glide = small gap = slow
// Long glide (same time) = big gap = fast

go to x: (0) y: (150)    // Start near surface (top of screen)

// Frame 1→2: move 1 unit (SLOW)
glide (0.2) secs to x: (0) y: (145)
// Frame 2→3: move 3 units
glide (0.2) secs to x: (0) y: (136)
// Frame 3→4: move 5 units
glide (0.2) secs to x: (0) y: (121)
// Frame 4→5: move 7 units
glide (0.2) secs to x: (0) y: (100)
// Frame 5→6: move 9 units
glide (0.2) secs to x: (0) y: (73)
// Frame 6→7: move 11 units (FAST now!)
glide (0.2) secs to x: (0) y: (40)
// Frame 7→8: move 13 units (FASTEST)
glide (0.2) secs to x: (0) y: (-20)

say [I am Papa Shinga. I am very heavy, so I sink faster and faster!] for (3) seconds
```

Explain: each `glide` takes the SAME time (0.2 sec), but the DISTANCE increases (1, 3, 5, 7, 9...). This is the Odd Rule — the whale shark starts slow and accelerates. If all glides moved the same distance, it would look robotic.

### Step 2: Guided Practice — Drawing Papa Shinga's Timing Chart (15 min)

Walk through creating a timing chart on paper and then implementing it in Scratch or Krita.

**On paper:**
1. Draw a vertical line on graph paper (this is the water column).
2. Mark "Frame 1" at the top (Papa Shinga at the surface — key pose ●).
3. Mark "Frame 8" at the bottom (Papa Shinga deep — key pose ●).
4. Calculate positions using the Odd Rule:
   - Frame 1: 0 units (surface)
   - Frame 2: 1 unit down
   - Frame 3: 4 units down (1+3)
   - Frame 4: 9 units down (1+3+5)
   - Frame 5: 16 units down (1+3+5+7)
   - Frame 6: 25 units down (1+3+5+7+9)
   - Frame 7: 36 units down (1+3+5+7+9+11)
   - Frame 8: 49 units down (1+3+5+7+9+11+13)
5. Mark the **breakdown** (○) at Frame 4 — this is only 9/49 = ~18% of the way down, NOT 50%. This is the Fourth Down at Half Time principle.
6. Draw arrows showing the GAPS between marks: small at the top, large at the bottom.

**In Scratch (implementing the chart):**
1. Create or import a whale shark sprite (Papa Shinga).
2. Use the glide block script from Step 1 — adjust the y-values to match the chart.
3. Play it back. Ask: "Does Papa Shinga start slow and get faster? Can you SEE the acceleration?"

**In Krita (alternative):**
1. Create 8 key frames on the timeline.
2. On each frame, place Papa Shinga at the y-position from the chart (0, 1, 4, 9, 16, 25, 36, 49 units from the top).
3. Turn on onion skin — the gaps between onion skin shadows should be small at the top and large at the bottom.
4. Play back at 12 fps. The whale shark should visibly accelerate.

### Step 3: Independent Practice — Papa Shinga Rises Back Up (20 min)

Learners create the REVERSE animation: Papa Shinga rises from the deep back to the surface. This uses the **Reverse Odd Rule (9, 7, 5, 3, 1)** — starts fast (big gaps), slows down (small gaps), gently stops at the surface.

**Challenge:** Animate Papa Shinga rising from the deep ocean to the surface to feed on plankton. The whale shark should start fast (deep, heavy, pushing up) and slow down as it approaches the surface (decelerating).

**Requirements:**
- Draw a timing chart on paper FIRST showing the Reverse Odd Rule (9, 7, 5, 3, 1)
- Animate at least 6 frames following the chart
- The whale shark should clearly decelerate — fast at the bottom, slow at the top
- Add a small "settle" at the top (Papa Shinga gently bobbing at the surface)

**Scratch starter code:**

```scratch
when [green flag] clicked
// PAPA SHINGA RISES — Reverse Odd Rule (9, 7, 5, 3, 1)
// Starts FAST at the bottom, SLOWS DOWN approaching surface

go to x: (0) y: (-150)   // Start deep (bottom of screen)

// Frame 1→2: move 9 units (FAST — big gap)
glide (0.2) secs to x: (0) y: (-105)
// Frame 2→3: move 7 units
glide (0.2) secs to x: (0) y: (-68)
// Frame 3→4: move 5 units
glide (0.2) secs to x: (0) y: (-43)
// Frame 4→5: move 3 units
glide (0.2) secs to x: (0) y: (-28)
// Frame 5→6: move 1 unit (SLOW — small gap, gentle stop)
glide (0.2) secs to x: (0) y: (-22)

// Settle: gentle bob at the surface
say [Plankton! Time to eat.] for (2) seconds
repeat (3)
  glide (0.3) secs to x: (0) y: (-18)
  glide (0.3) secs to x: (0) y: (-26)
end
```

**For Krita users:** Draw the timing chart showing Reverse Odd Rule positions. Create 6 key frames placing Papa Shinga at each position. The onion skin gaps should be LARGE at the bottom and SMALL at the top. Add 2-3 "settle" frames at the surface where Papa Shinga bobs gently (ease out).

**Extension for advanced learners:** Animate BOTH the sinking (Odd Rule) and rising (Reverse Odd Rule) in one continuous sequence. Papa Shinga sinks → hits the bottom → pushes off → rises back up. The transition at the bottom should have a small squash (impact) and anticipation (coiling before pushing up).

Teacher circulates and checks:
- Did learners draw the timing chart BEFORE animating?
- Does the rising animation clearly decelerate (big gaps → small gaps)?
- Is there a settle/bob at the top?

### Step 4: Sharing & Feedback (10 min)

Learners present their timing chart (on paper) and their animation. Use this critique framework:
1. **What I see:** Describe the spacing — does the whale shark start fast and slow down (rising) or start slow and speed up (sinking)?
2. **Check the chart:** Compare the animation to the paper chart. Do the positions match?
3. **One question:** "What if you tried…?" (e.g., "What if you added more frames for a smoother deceleration?" or "What if you compared your animation to a linear version — which feels heavier?")

Celebrate learners who planned before animating. The key insight: **planned animation is better than guessed animation.** The timing chart is the plan.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Timing chart creation | No chart drawn; animates directly without planning | Draws a chart but spacing is equal/linear or pattern is wrong | Draws a correct Odd Rule chart (1,3,5,7,9) with key poses and breakdowns marked | Draws both Odd Rule AND Reverse Odd Rule charts; marks Fourth Down at Half Time; chart is clean and readable |
| Spacing application in animation | Animation moves at constant speed (linear/robotic) | Animation has some speed change but doesn't follow the chart | Animation follows the chart — whale shark clearly accelerates (sinking) or decelerates (rising) | Animation follows chart precisely AND includes settle/bob at the end; spacing visible in onion skin or playback |
| Understanding of spacing concepts | Cannot explain the difference between spacing and timing | Can explain that big gaps = fast, small gaps = slow | Can explain the Odd Rule, identify ease in/out patterns, and explain why linear looks robotic | Can explain Odd Rule, Reverse Odd, Fourth Down at Half Time, AND teach the concept to a peer |

---

## Extended Activity

**Homework / Follow-up project:** Create a timing chart for a COMPLETE Papa Shinga scene: the whale shark drifts down (Odd Rule), hits the seafloor (squash impact), pauses (anticipation), then rises back up (Reverse Odd Rule). Draw the full timing chart on paper with all key poses (●), breakdowns (○), and inbetweens. Then animate it. This connects sinking (gravity) and rising (deceleration) into one continuous performance.

**Conservation connection:** Add a fact card to the animation: "Papa Shinga (whale shark) is Endangered. Boat strikes are a major threat because whale sharks swim slowly at the surface. KWS tags whale sharks to track their movements and protect them along the Kenya coast." Include this as a say block or text caption.

**Advanced option (Blender):** For learners using Blender, open the Graph Editor after keyframing Papa Shinga's descent. Show how the F-curve shape represents spacing: a curved (ease in/out) line = natural acceleration, while a straight (linear) line = robotic. Try modifying the curve handles to change the spacing visually.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-printed timing chart template with frame numbers already marked. Learners only need to calculate and fill in the positions. Start with just 4 frames instead of 8. Use the provided Scratch starter code and just adjust the y-values. | Create a timing chart for a BOUNCE: Papa Shinga sinks (Odd Rule), hits the seafloor (squash), then bounces back up (Reverse Odd Rule) but not as high (energy loss). Try the horizontal timing chart format for a swim cycle. Use Blender's Graph Editor to shape F-curves. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Papa Shinga whale shark example effective for teaching weight and spacing?
- [ ] Did learners actually draw the timing chart BEFORE animating, or did they skip to animation?
- [ ] Did the Odd Rule (1, 3, 5, 7, 9) make sense to learners, or was it too abstract?
- [ ] What would I change next time?