# Lesson Plan 51: Balance, Weight Shift & Ground Contact — Keeping Characters Grounded

**Module Reference:** Prompt 51 — 51-balance-weight-shift.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Scratch (simple), Krita (frame-by-frame), Blender (advanced)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Integrated Science + Creative Arts & Sports |
| Sub-strand | Physics of Balance, Center of Gravity & Ground Contact |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Identify** the center of gravity (CoG) in a character and explain the golden rule: CoG must stay over the support foot or the character falls.
2. **Animate** a weight shift sequence showing the hips moving over the stance foot before the step.
3. **Distinguish** between grounded animation (feet plant, weight shifts, contact shadows) and floaty animation (sliding feet, no weight).

## Key Inquiry Question

> Why does a **sea turtle (Kasa)** look heavy when it crawls on the beach but weightless when it swims — and how do we show that weight in animation?

---

## Resources

- Scratch, Krita, or Blender
- Reference video of sea turtles on Kenyan beaches (Watamu nesting)
- Paper and pencils for CoG diagrams
- Optional: a physical object to balance (ruler on finger)
- Optional: Raspberry Pi with Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Green Sea Turtle (*Chelonia mydas*) — **Kasa** in Swahili  
**Habitat:** Seagrass beds in Watamu Marine National Park. Nests on beaches at Watamu and Tiwi (March-June).  
**Why this animal?** When a sea turtle comes onto land to nest, it weighs 150+ kg and moves against gravity. Every step is a massive weight shift — you can SEE the CoG moving over each flipper. In the water, the turtle is buoyant and weightless. This contrast is the perfect teaching tool for grounded vs floaty animation.  
**Conservation note:** Green sea turtles are Endangered. KWS and Local Ocean Trust patrol nesting beaches at night to protect females and eggs from poachers and predators.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Have a learner stand on one foot. Ask: *"What's keeping you from falling? Where is your balance point?"*

Explain: *Your belly button area is your center of gravity. If it's over your foot, you stay balanced. If it moves past your foot, you fall — or you take a step to catch yourself. This is THE most important thing for making characters look grounded.*

Show a video of a sea turtle crawling on a beach. Ask: *"Can you see the weight shifting? Each flipper plants, then the body shifts over it. That's grounded animation."*

### Step 1: The 5 Keys to Grounded Animation (20 min)

**Key 1: CoG Must Stay Over the Support Foot**
- Draw a vertical line from CoG straight down — it should land on or between the feet
- If it lands outside the feet → character falls or must step

**Key 2: Weight Shift Before Stepping**
- Before stepping with the right foot, shift weight to the LEFT foot first
- Hips slide over the stance foot → then the stepping foot lifts

**Key 3: Feet PLANT and Don't Slide**
- When a foot is on the ground, it stays in that spot
- Sliding feet = the #1 sign of amateur animation
- Fix: track each foot's position and keep it locked while planted

**Key 4: Ground Contact Shows Weight**
- Contact shadows under feet
- Slight compression of the foot/body at the contact point
- Dust or sand displaced at impact

**Key 5: Grounded vs Floaty**

| Grounded (heavy, real) | Floaty (light, fake) |
|------------------------|----------------------|
| Feet plant and grip | Feet slide |
| Weight shifts visibly | Body stays centered |
| Contact shadows | No shadows |
| Slow recovery from impact | Instant recovery |
| Body compresses on landing | Body stays same shape |

### Step 2: Turtle Weight Shift in Scratch (20 min)

Animate a heavy sea turtle shifting weight from one flipper to another:

```scratch
when [green flag] clicked
// Pose 1: Weight on left flipper, right flipper lifted
switch costume to [turtle-weight-left]
set x to (-100)
say [Shifting weight...] for (1) seconds

// Weight transfer: body slides RIGHT over the right flipper
glide (0.5) secs to x: (-80) y: (0)    ← Hips shift right
switch costume to [turtle-weight-transfer]
wait (0.3) seconds                       ← Settle over right flipper

// Now the left flipper can lift and step
switch costume to [turtle-weight-right]
set x to (-60)
say [Step!] for (0.5) seconds

// Contact: show sand displaced
switch costume to [turtle-contact-sand]
start sound [sand-sfx]
wait (0.5) seconds
```

**Key teaching:** The body MUST shift over the support flipper BEFORE the stepping flipper lifts. If both flippers lift at the same time, the turtle looks like it's floating (floaty).

### Step 3: Fix the Floaty Animation (20 min)

**Challenge:** Take a "floaty" animation and make it grounded.

Provide a simple floaty animation (or have learners create one):
- Character slides across screen without foot planting
- No weight shift
- No contact shadows
- Body doesn't compress

**Fix checklist:**
- [ ] Lock foot positions when planted (don't let them slide)
- [ ] Add weight shift before each step (hips move over stance foot)
- [ ] Add contact shadow under each planted foot
- [ ] Add body compression on landing (slight squash)
- [ ] Add sand/dust displacement at contact point
- [ ] Slow down the recovery (weight takes time to settle)

### Step 4: Sharing & Feedback (10 min)

Show before (floaty) and after (grounded) side by side. Discuss:
- *"Which one feels heavier? Why?"*
- *"Can you see the weight shift now?"*
- *"Do the contact shadows make a difference?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| CoG Understanding | Cannot identify center of gravity | Knows CoG exists but can't track it | Tracks CoG and checks it's over support foot | Tracks CoG + adjusts for one-foot balance + shows fall when CoG passes foot |
| Weight Shift | No weight shift (both feet lift together) | Some shift but timing is wrong | Weight shifts over stance foot before step | Weight shift + settle + breathing sway when still |
| Ground Contact | Feet slide | Feet plant but no shadows/compression | Feet plant + contact shadows + compression | Full contact: planting + shadows + compression + dust/sand + slow recovery |

---

## Extended Activity

**Turtle Nesting Animation:** Animate a 150kg sea turtle dragging itself up a Kenyan beach to lay eggs. Show EVERY principle of grounded animation: slow weight shifts, deep flipper prints in sand, heavy breathing, body compression with each step. End with the turtle laying eggs and a conservation message: "Protect nesting turtles — keep beaches dark and quiet at night."

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Use a simple ball instead of a character (ball rolls, weight shifts) | Use Blender: IK foot locking, weight-painted character, contact shadow setup |
| Focus on ONE fix (stop foot sliding) | Fix all 5 problems: sliding, weight shift, shadows, compression, recovery |
| Provide pre-drawn key poses to arrange | Animate a character catching their balance after a stumble (CoG passes foot, step to recover) |

---

## Teacher Reflection

- [ ] Did learners understand the CoG golden rule?
- [ ] Could they see the difference between floaty and grounded?
- [ ] Was the sea turtle on land vs in water an effective contrast?
- [ ] What exercise would help learners FEEL weight shift before animating it?