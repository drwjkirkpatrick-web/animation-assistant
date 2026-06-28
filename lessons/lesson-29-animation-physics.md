# Lesson Plan 29: Animation Physics & Weight — Making Movement Believable

**Module Reference:** Prompt 29 — 29-animation-physics.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Scratch (demo), Krita (practice), Blender (advanced)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Integrated Science + Creative Arts & Sports |
| Sub-strand | Forces, Motion & Animation Physics |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Explain** how gravity, inertia, and momentum affect animated movement using the Odd Rule (spacing 1, 3, 5, 7, 9...).
2. **Apply** the 6 principles of animation physics to make a falling object look heavy and real in Scratch or Krita.
3. **Value** the connection between real physics and believable animation — understanding that animation physics = common sense physics.

## Key Inquiry Question

> Why does a **whale shark (Papa Shinga)** look heavy when it sinks and light when it glides — and how can we use the same physics rules to make our animations feel real?

---

## Resources

- Scratch (online or desktop) or Krita (for drawing-based animation)
- Tennis ball and crumpled paper (for physical demo)
- Projector for video reference
- Reference video of whale sharks at Watamu Marine National Park (Oct-Feb season)
- Optional: Raspberry Pi with Scratch Desktop for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Whale Shark (*Rhincodon typus*) — **Papa Shinga** in Swahili  
**Habitat:** Open ocean near Watamu Marine National Park, Kilifi County. Whale sharks visit Kenya's coast from October to February, feeding on plankton in the warm Indian Ocean waters.  
**Why this animal?** The whale shark is the largest fish in the ocean — up to 12 meters long and 20+ tons. Its massive weight makes it the perfect subject for studying how timing and spacing communicate weight. When a whale shark sinks, it falls slowly (water resistance). When it glides, it moves with momentum. The contrast between heavy and light is visible in every movement it makes.  
**Conservation note:** Whale sharks are classified as Endangered by the IUCN. Major threats include boat strikes (they swim slowly at the surface), fishing nets, and plastic pollution. KWS runs a tagging and monitoring program at Watamu. Tourists can swim with whale sharks but must follow strict guidelines — no touching, keep 3 meters away, no flash photography.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show a 30-second video clip of a whale shark gliding at Watamu. Ask learners:

- *"How heavy do you think this animal is?"* (Answer: up to 20 tons — as heavy as 3 elephants!)
- *"Does it look heavy when it moves? Why or why not?"*

Drop a tennis ball and a crumpled piece of paper from the same height. Ask: *"Which hit the ground first? Which bounced? That's weight. In animation, we control weight with TIMING and SPACING."*

Explain: *Today we'll learn the 6 simple physics rules that make animation look real. We'll use Papa Shinga the Whale Shark as our test subject.*

### Step 1: The 6 Principles of Animation Physics (20 min)

Teach each principle using whale shark examples:

**1. The Odd Rule (Timing & Spacing):**
When something falls under gravity, spacing between frames goes 1, 3, 5, 7, 9... (odd numbers). Things accelerate as they fall.

```
Frame 1: █                          ← 1 unit down
Frame 2: ███                        ← 3 units down (total: 4)
Frame 3: █████                      ← 5 units down (total: 9)
Frame 4: ███████                    ← 7 units down (total: 16)
Frame 5: █████████                  ← 9 units down (total: 25)
```

**Whale shark version:** If Papa Shinga dives from the surface, frame 1 moves 1 unit, frame 2 moves 3 more, frame 3 moves 5 more... The dive gets faster and faster.

**2. Law of Inertia:**
Things don't start or stop on their own. When a whale shark stops swimming, it doesn't stop instantly — it drifts forward. Body parts stop at different times: tail stops last (follow-through!).

**3. Momentum & Force:**
Momentum = mass × speed. A 20-ton whale shark moving slowly has enormous momentum. A small clownfish moving fast has very little.

**4. Center of Gravity:**
Every object has a balance point. A whale shark's CoG is near its belly. When it banks to turn, its body rotates around this point.

**5. Weight Gain & Loss:**
Heavy = more frames on impact, slow recovery, big squash. Light = bounces high, recovers fast, floats at top.

**6. Action-Reaction:**
Every action has an equal and opposite reaction. When a whale shark's tail sweeps right, water pushes left — the shark moves forward.

### Step 2: Guided Practice — Falling Whale Shark in Scratch (20 min)

Walk through creating a physics-based falling animation in Scratch:

```scratch
when [green flag] clicked
set [y_position] to (180)          ← Start at top of screen
set [fall_speed] to (0)            ← Start with no speed
set [gravity] to (1)               ← Gravity acceleration
forever
  change [fall_speed] by (gravity)  ← Speed increases each frame (Odd Rule!)
  change y by (fall_speed)          ← Move down by current speed
  if <(y_position) < (-160)> then   ← Hit the "ocean floor"
    say [Oof! That was heavy!] for (2) seconds
    stop [all]
  end
end
```

**Key teaching point:** The `change [fall_speed] by (gravity)` line IS the Odd Rule in code. Each frame, the speed increases by 1 — so the shark falls 1, then 2, then 3, then 4... (accumulating like 1, 3, 6, 10, 15...). This makes the fall feel real.

**Variation for Krita:** Draw the whale shark at 5 positions with increasing spacing:
- Frame 1: top of canvas, 1cm below start
- Frame 2: 3cm below frame 1
- Frame 3: 5cm below frame 2
- Frame 4: 7cm below frame 3
- Frame 5: 9cm below frame 4 (hitting the bottom with a squash!)

### Step 3: Independent Practice — Heavy vs Light (20 min)

**Challenge:** Animate TWO objects falling — one heavy (whale shark) and one light (jellyfish bell). Use different timing to make them feel different.

| Object | Frames to Fall | Squash on Landing | Bounce? |
|--------|---------------|-------------------|---------|
| Whale Shark (heavy) | 8 frames | Big squash, slow recovery | No — thud |
| Jellyfish (light) | 16 frames | Tiny squash | Yes — bounces 3 times |

Learners choose Scratch or Krita. Provide a checklist:

- [ ] Heavy object falls fast (fewer frames, Odd Rule spacing)
- [ ] Light object falls slowly (more frames, floaty spacing)
- [ ] Heavy object squashes big on impact
- [ ] Light object bounces after landing
- [ ] Heavy object has dust/impact reaction
- [ ] Light object has no impact reaction (too light)

### Step 4: Sharing & Feedback (10 min)

Learners present their falling animations. Use the critique framework:
- **What's working:** "Your whale shark really feels heavy — great use of the Odd Rule!"
- **One thing to try:** "I wonder what would happen if you added 2 more frames of squash on impact..."
- **Question:** "Does your jellyfish feel lighter than your whale shark? What makes the difference?"

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Physics Understanding | Cannot explain the Odd Rule | Explains Odd Rule but cannot apply it | Explains and applies Odd Rule to falling object | Explains all 6 principles and applies multiple |
| Weight Communication | Heavy and light look the same | Some timing difference but not convincing | Clear weight difference through timing/spacing | Weight difference plus squash, impact reaction, follow-through |
| Code/Tool Application | Cannot create falling animation | Creates basic fall but no acceleration | Creates fall with acceleration (Odd Rule) | Creates fall + squash + impact + bounce for both objects |

---

## Extended Activity

**Conservation Animation Project:** Create a 10-second animation showing a whale shark swimming through Watamu Marine Park, dodging plastic pollution. Use physics principles to make the shark's movement feel real — momentum when it turns, inertia when it slows down, weight when it dives. Add a conservation message at the end: "Protect Papa Shinga — say no to plastic."

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-drawn whale shark sprite/frames; focus only on timing | Add water resistance (drag) to the physics — falling through water is slower than air. Add a variable for `drag` that reduces acceleration. |
| Use only 4 frames instead of 8 | Add a third object (sea turtle) with different weight and animate all three falling together |
| Work in pairs on one computer | Use Blender's graph editor to create a physics-accurate fall curve (bezier interpolation) |

---

## Teacher Reflection

- [ ] Did learners understand the Odd Rule? (Can they explain 1, 3, 5, 7, 9?)
- [ ] Was the whale shark example engaging? Did they connect weight to the animal?
- [ ] Could learners see the difference between heavy and light in their animations?
- [ ] What would I change next time? (Consider more physical demos before screen work)