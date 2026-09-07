# Lesson Plan 32: Advanced Body Mechanics — Run Cycles, Jumps & Quadrupeds

**Module Reference:** Prompt 32 — 32-body-mechanics.md  
**Duration:** 80 min  
**Age Group:** 13-17  
**Animation Tool:** Scratch (basic), Krita (frame-by-frame), Blender (advanced rigging)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports + Integrated Science |
| Sub-strand | Body Mechanics, Locomotion & Biomechanics in Animation |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Distinguish** between walk and run cycles, identifying the flight phase as the key difference.
2. **Animate** a jump with 5 phases (anticipation, launch, flight, landing, recovery) using the Odd Rule for arc spacing.
3. **Apply** quadruped locomotion principles to animate a 4-legged Kenyan ocean animal (sea turtle swimming or crab walking).

## Key Inquiry Question

> How does a **green sea turtle (Kasa)** swim with four flippers — and what can we learn from its body mechanics to make our run cycles and jumps feel real?

---

## Resources

- Scratch, Krita, or Blender
- Reference video of sea turtles swimming at Watamu
- Reference video of crabs walking on Kenyan beaches
- Paper and pencils for pose planning
- Optional: Raspberry Pi with Scratch Desktop

---

## Local Context: Kenyan Ocean Animal

**Animal:** Green Sea Turtle (*Chelonia mydas*) — **Kasa** in Swahili  
**Habitat:** Seagrass beds in Watamu Marine National Park, Diani-Chale Marine Reserve. Turtles nest on Kenyan beaches at Watamu and Tiwi.  
**Why this animal?** Sea turtles are quadrupeds (four-limbed) but their locomotion is unique — they "fly" through water with all four flippers working in coordinated pairs. This makes them a perfect bridge between biped run cycles and quadruped mechanics. The flipper motion follows the same diagonal-pair principle as a dog walking, just adapted for swimming. Also, when a turtle comes onto land to nest, its slow, heavy movement is a perfect weight-and-balance study.  
**Conservation note:** Green sea turtles are Endangered. They eat plastic bags mistaking them for jellyfish. KWS and Local Ocean Trust protect nesting sites at Watamu — community volunteers patrol beaches at night during nesting season (March-June).

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show two videos side by side:
1. A human running (or a dog running)
2. A sea turtle swimming at Watamu

Ask: *"What's similar about how they move? What's different?"*

Key observations:
- Both use four limbs in diagonal pairs (front-right + back-left, then front-left + back-right)
- The turtle "flies" through water — its flippers stroke like wings
- On land, the turtle is heavy and slow — weight affects locomotion
- Both have a moment where all limbs are in motion (flight phase in running, glide phase in swimming)

*Today we'll learn how bodies move — running, jumping, and swimming with four limbs. We'll use Kasa the Sea Turtle and other ocean animals as our subjects.*

### Step 1: Run Cycle Mechanics (15 min)

Teach the run cycle using the turtle-to-dolphin comparison:

**Walk vs Run:**

| Element | Walk (Kasa on land) | Run (Pomboo jumping) |
|---------|--------------------|-----------------------|
| Speed | Slow | Fast |
| Body lean | Upright | Forward lean |
| Contact | 1-2 feet on ground | Moments of NO contact (flight!) |
| Key poses | 4 (contact, low, passing, high) | 4 (contact, down, push, flight) |

**Run cycle 4 key poses:**
1. **Contact:** Front foot reaches forward, about to hit ground. Body at mid-height.
2. **Down (Compression):** Front foot lands, leg compresses. Body is LOWEST. This is the squash.
3. **Push (Extension):** Front leg pushes body UP. Back leg swings forward. Body rising.
4. **Flight (Airborne):** Both feet off ground! Body is HIGHEST. Legs gathered under body.

In Scratch, simulate a run cycle with a dolphin sprite:
```scratch
when [green flag] clicked
forever
  // Pose 1: Contact — dolphin at mid-height, leaning forward
  switch costume to [dolphin-contact]
  change y by (0)
  wait (0.05) seconds

  // Pose 2: Down — dolphin compressed LOW
  switch costume to [dolphin-down]
  change y by (-10)              ← Body drops
  wait (0.05) seconds

  // Pose 3: Push — dolphin extending UP
  switch costume to [dolphin-push]
  change y by (20)               ← Body shoots up
  wait (0.05) seconds

  // Pose 4: Flight — dolphin at HIGHEST point, airborne
  switch costume to [dolphin-flight]
  change y by (5)                ← Still rising slightly
  wait (0.05) seconds
end
```

### Step 2: Jump with Physics (20 min)

Teach the 5-phase jump using a dolphin breaching:

| Phase | Description | Frames (12fps) | Animation Principle |
|-------|------------|----------------|---------------------|
| 1. Anticipation | Dolphin coils, points nose down | 6-10 | Anticipation |
| 2. Launch | Explosive tail push, body shoots up | 3-5 | Squash → stretch |
| 3. Flight | Parabolic arc up and over | 8-12 (use Odd Rule) | Arcs, slow in/out |
| 4. Landing | SPLASH back into water | 4-6 | Squash, weight |
| 5. Recovery | Settle, water calms | 6-10 | Follow-through |

**The Odd Rule for jump arc spacing (vertical):**
```
Going UP:    9, 7, 5, 3, 1  (decelerating — gets slower at peak)
Coming DOWN: 1, 3, 5, 7, 9  (accelerating — gets faster)
```

In Krita, draw 10 frames:
- Frame 1: Dolphin at water surface, nose down (anticipation)
- Frame 2: Body coiled tighter, tail flexed
- Frame 3: Tail pushes, body starts up (launch — stretched tall)
- Frame 4: Body rising, 9 units up from launch
- Frame 5: 7 more units up (decelerating)
- Frame 6: 5 more units up (peak approaching)
- Frame 7: 3 more units up (almost at peak)
- Frame 8: 1 unit up (PEAK — brief hang)
- Frame 9: 3 units down (starting to fall)
- Frame 10: 5 units down, body stretching toward water (landing imminent)

### Step 3: Quadruped Practice — Sea Turtle Swim Cycle (20 min)

**Challenge:** Animate Kasa the Sea Turtle swimming with four flippers.

**Quadruped walk/swim key poses (diagonal pairs):**
1. **Contact 1:** Front-right flipper strokes forward, back-left flipper pushes back. Spine neutral.
2. **Passing 1:** Front-right flipper is down (power stroke), back-left is lifting and swinging forward. Spine arches slightly.
3. **Contact 2:** Front-left flipper reaches forward, back-right pushes back. The OTHER diagonal pair.
4. **Passing 2:** Front-left is down, back-right swings forward. Spine arches.

In Scratch:
```scratch
when [green flag] clicked
forever
  // Pose 1: Front-right + back-left diagonal
  switch costume to [turtle-pose-1]
  wait (0.1) seconds

  // Pose 2: Transition — spine arches
  switch costume to [turtle-pose-2]
  wait (0.1) seconds

  // Pose 3: Front-left + back-right diagonal
  switch costume to [turtle-pose-3]
  wait (0.1) seconds

  // Pose 4: Transition — spine arches other way
  switch costume to [turtle-pose-4]
  wait (0.1) seconds
end
```

**Key tips:**
- The spine FLEXES: arches when back flippers come forward, dips when front flippers reach
- Head bobs slightly: down when front flippers stroke, up when they lift
- The shell doesn't change shape (it's rigid) — but it tilts and rotates
- Water resistance means everything moves slower than on land

### Step 4: Sharing & Feedback (15 min)

Learners present their run cycles, jumps, or swim cycles. Critique:
- *"Can you see the flight phase in the run? Both feet off ground?"*
- *"Does the jump arc follow the Odd Rule? Does it slow at the peak?"*
- *"Do the turtle's flippers move in diagonal pairs? Is the spine flexing?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Run Cycle | No flight phase; looks like fast walk | Has flight phase but timing is off | Clear 4-pose run cycle with flight phase and forward lean | Run cycle + weight shift + arm/flipper swing + head bob |
| Jump Physics | Jump has no anticipation or arc | Has arc but no Odd Rule spacing | 5 phases with parabolic arc and Odd Rule spacing | 5 phases + squash/stretch + splash impact + follow-through |
| Quadruped | Flippers move randomly | Flippers move together (wrong — should be diagonal pairs) | Diagonal pairs correct; spine flexes | Diagonal pairs + spine flex + head counterbalance + water resistance feel |

---

## Extended Activity

**Sea Turtle Nesting Animation:** Animate a heavy sea turtle dragging itself up a Kenyan beach to lay eggs. This is ALL about weight — the turtle is 150kg on land, moving against gravity. Show:
- Slow, laborious movement (weight)
- Deep footprints in sand (action-reaction)
- Heavy breathing (secondary action)
- Sand flying as she digs (impact reaction)
- The emotional weight of a conservation moment

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-drawn key poses to arrange in order | Use Blender: rig a quadruped with a bone skeleton, animate with IK (inverse kinematics) |
| Focus on run cycle only (skip jump and quadruped) | Animate all three: run cycle + jump + quadruped swim, then combine in one scene |
| Use 8 frames instead of 4 for run cycle (easier timing) | Add water splash particles on the dolphin landing (secondary action + effects) |

---

## Teacher Reflection

- [ ] Did learners understand the difference between walk and run (flight phase)?
- [ ] Could they apply the Odd Rule to the jump arc?
- [ ] Were the sea turtle and dolphin examples effective for teaching quadruped mechanics?
- [ ] Did learners connect body mechanics to real animal movement?