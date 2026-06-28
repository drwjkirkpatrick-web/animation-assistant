# Lesson Plan 34: Special Effects Animation — Fire, Water, Smoke & Magic

**Module Reference:** Prompt 34 — 34-special-effects.md
**Duration:** 75 min
**Age Group:** 12-17
**Animation Tool:** Scratch (primary) / Krita (optional extension)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Performing Arts — Animation and Digital Storytelling |
| Core Competency | Creativity & Imagination, Critical Thinking, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain how effects animation differs from character animation — effects follow physics, not anatomy, and use flows and cycles rather than key poses.
2. Animate at least two special effects (water splash + one other) using Scratch clone blocks or frame-by-frame drawing in Krita.
3. Apply the core principles of each effect (water is heavy and falls fast, fire always goes up, smoke expands and tumbles) to make effects feel realistic.

## Key Inquiry Question

> When Nyangumi the humpback whale breaches out of the Indian Ocean, how do we animate the splash so it looks like real water — heavy, fast, and powerful — instead of slow floating particles?

---

## Resources

- Scratch (offline or online at scratch.mit.edu) or Krita (free download)
- Projector or large screen for demonstration
- Reference video of humpback whale breaching (search "humpback whale breach slow motion")
- Reference video/photos of ocean splashes and waves
- Paper and pencils for sketching splash frames before animating
- Optional: Blender (for advanced learners wanting to try simulation)
- Optional: Raspberry Pi running Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Humpback Whale (Nyangumi)
**Habitat:** Migratory — humpback whales pass through Kenya's Indian Ocean waters from July to September each year, traveling from Antarctica to breed in warm tropical waters. They can be seen off the Kenya coast, especially around Watamu and Malindi.
**Why this animal?** A breaching humpback whale creates the MOST spectacular water splash in the ocean — a massive explosion of water and droplets when 40 tons of whale hits the surface. This makes Nyangumi the perfect character for teaching water splash effects: the splash has a crown shape, droplets fly in arcs, and ripples spread outward. The scale of a whale breach makes every effect principle visible and dramatic.
**Conservation note:** Humpback whales are classified as Least Concern and are recovering thanks to the global ban on commercial whaling, but they still face threats from ship collisions and ocean noise pollution. KWS monitors whales during migration season (July-September) as part of marine mammal protection along the Kenya coast. Learners can create awareness animations about keeping shipping lanes safe for migrating whales.

---

## Lesson Development

### Introduction (8 min)

Show a video of a humpback whale (Nyangumi) breaching in slow motion. Ask learners:
- "What do you notice about the splash?"
- "How is the water moving — is it floating gently or exploding?"

Explain that effects animation is DIFFERENT from character animation:
- Characters follow anatomy. Effects follow PHYSICS.
- Characters have key poses. Effects have flows and cycles.
- Effects should SUPPORT the scene, not steal focus.

Introduce the 5 core effects: fire, water, smoke, explosions, and magic. Today we focus on **water & splashes** (using Nyangumi's breach) and one additional effect of the learner's choice.

Write the key rule on the board: **"Water is HEAVY. It falls fast. It doesn't float."**

### Step 1: Concept Introduction — How Water Splashes Work (15 min)

Teach the anatomy of a water splash using Nyangumi's breach as the example.

**The 6 phases of a splash:**

| Phase | Frames | What happens |
|-------|--------|-------------|
| Impact | Frame 0 | Object hits water — squash shape, water compresses |
| Crown | Frames 1-2 | Water splashes UP around the object like a flower opening |
| Droplets | Frames 3-5 | Droplets fly up and outward in ARCS (follow gravity) |
| Fall | Frames 6-10 | Droplets fall back down (Odd Rule: 1, 3, 5, 7, 9 units) |
| Ripples | Frames 8-15 | Ripples expand outward in circles from impact point |
| Calm | Frame 15+ | Surface calms, ripples fade |

**Key principles:**
- Droplets follow ARCS — each droplet is a tiny projectile affected by gravity
- The splash is FAST — 1-2 seconds total. Don't drag it out.
- Ripples spread outward in expanding circles
- Big splash (whale) = more droplets, bigger crown, longer ripples
- Small splash (fish) = fewer droplets, quick settle

**Scratch demonstration — splash particles with clones:**

```scratch
when [green flag] clicked
// NYANGUMI BREACH SPLASH
// When the whale hits the water, create splash particles
broadcast [whale_splash]
hide

when I receive [whale_splash]
// This sprite is a single water droplet
create clone of [myself]   // Create 15-20 droplets
repeat (18)
  create clone of [myself]
end

when I start as a clone
// Each droplet flies up and outward, then falls (gravity!)
show
set size to (pick random 30 to 80) percent
go to [Nyangumi whale sprite]
// Random launch angle and speed (upward and outward)
set [droplet_speed] to (pick random 4 to 10)
set [droplet_angle] to (pick random -60 to 60)
set [gravity] to (0.5)
set [vy] to (droplet_speed)      // Initial upward velocity
set [vx] to (droplet_angle / 10) // Horizontal spread
repeat until <touching [edge]?>
  change y by (vy)       // Move up (vy starts positive)
  change x by (vx)       // Move sideways
  change [vy] by (gravity * -1)  // Gravity pulls down over time
  // vy decreases each frame → droplet rises, slows, falls
  if <(vy) < (-12)> then
    delete this clone   // Droplet goes off screen
  end
end
delete this clone
```

Explain: each clone is a water droplet. It starts moving UP (positive vy), but gravity pulls it down (vy decreases each frame). Eventually vy goes negative and the droplet falls. This creates the ARC trajectory — just like real water. The `pick random` blocks make each droplet different, which looks natural.

### Step 2: Guided Practice — Animating Nyangumi's Breach Splash (15 min)

Walk through building the splash effect together in Scratch.

**Step-by-step:**

1. **Create the whale sprite:** Draw or import a simple whale shape. Place it below the stage (off-screen at the bottom). Animate it rising up and falling back:

```scratch
when [green flag] clicked
// Whale rises out of water (breach!)
set y to (-180)
glide (1) secs to x: (0) y: (50)    // Rise up
wait (0.3) seconds                   // Hang at the top (apex)
glide (0.5) secs to x: (0) y: (-100) // Fall back down FAST
// Trigger splash when whale hits the water!
broadcast [whale_splash]
glide (0.3) secs to x: (0) y: (-180) // Sink below surface
hide
```

2. **Create the droplet sprite:** Draw a small blue circle (the water droplet). This is the sprite that will be cloned.

3. **Add the clone script** (from Step 1 above) to the droplet sprite.

4. **Add ripples (optional but recommended):** Create a separate "ripple" sprite — an oval that starts small and grows:

```scratch
when I receive [whale_splash]
// Ripple 1
go to x: (0) y: (-100)
set size to (10) percent
show
repeat (20)
  change size by (8)
  // Ripple fades as it grows
  set [ghost] effect to ((size) / 3)
end
hide
```

5. **Play it back.** Ask learners:
   - "Does the splash look heavy and fast, or slow and floaty?"
   - "Do the droplets arc upward and then fall? That's gravity!"
   - "What would happen if we removed the gravity variable?" (Droplets would fly in straight lines forever — wrong!)

### Step 3: Independent Practice — Add a Second Effect (20 min)

Learners who have completed the whale splash choose a SECOND effect to add to the scene. Options:

**Option A: Smoke/Dust after the splash settles**
After the ripples fade, add a dust/mist cloud that rises and expands. Create 3-5 overlapping puff clones at different stages (the key to good smoke = LAYERING).

```scratch
when I receive [make_mist]
// Mist rises after the big splash settles
create clone of [myself]
wait (0.3) seconds
create clone of [myself]
wait (0.3) seconds
create clone of [myself]

when I start as a clone
go to x: (pick random -50 to 50) y: (-80)
set size to (20) percent
set [ghost] effect to (30)
show
repeat (25)
  change y by (1.5)        // Rise slowly
  change size by (3)        // Expand
  change [ghost] effect by (2) // Fade out
end
delete this clone
```

**Option B: Magic glow around Nyangumi as it breaches (bioluminescence)**
Make the whale glow with sparkling particles as it rises — representing bioluminescent plankton in the Indian Ocean water.

```scratch
when I receive [whale_glow]
// Sparkle particles around the whale as it rises
repeat (30)
  create clone of [myself]
end

when I start as a clone
go to [Nyangumi whale sprite]
set size to (pick random 10 to 40) percent
set [color] effect to (pick random 120 to 180) // Blue/green glow
show
repeat (15)
  change x by (pick random -3 to 3)  // Flicker
  change y by (pick random -2 to 4)  // Float up slightly
  change [ghost] effect by (5)       // Fade
end
delete this clone
```

**Option C: Fire (if learners want to try a different effect)**
Draw a 6-frame fire cycle in Krita — flame that grows tall, splits, shrinks, and loops. Fire ALWAYS goes up. Not for the whale scene, but as a separate practice (e.g., a beach campfire at the Kenya coast).

**Requirements:**
- The second effect must use a DIFFERENT animation technique than the splash
- The effect should SUPPORT the scene, not steal focus from Nyangumi
- Learners should be able to explain which physics principle their effect follows

Teacher circulates and checks:
- Are droplets/particles using gravity (arcs, not straight lines)?
- Is the effect the right speed (water = fast, smoke = slow)?
- Are there enough particles/layers for realism?

### Step 4: Sharing & Feedback (10 min)

Learners present their Nyangumi breach animation with effects. Use this critique framework:
1. **What I see:** Describe the effects you observed (splash, ripples, mist, glow, etc.).
2. **What works:** One effect that felt realistic — what made it work?
3. **One question:** "What if you tried…?" (e.g., "What if you added more droplets for a bigger splash?" or "What if the ripples lasted longer?")

Highlight learners whose effects SUPPORT the scene without stealing focus. The best effects are the ones the audience doesn't consciously notice — they just feel the scene is real.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Splash effect creation | Creates a splash but droplets float or move in straight lines | Creates a splash with some droplets but missing gravity/arcs | Creates a splash with droplets that arc up and fall (gravity applied); crown + ripples present | Full 6-phase splash: impact, crown, arcing droplets, fall, expanding ripples, calm; feels heavy and realistic |
| Second effect | No second effect attempted | Second effect exists but follows wrong physics (e.g., smoke falls, fire goes sideways) | Second effect follows correct physics (smoke rises & expands, magic glows & spirals, fire goes up) | Second effect uses layering (3-5 overlapping puffs/particles) AND supports the scene without stealing focus |
| Understanding of FX principles | Cannot explain how effects differ from character animation | Can name one difference (effects follow physics) | Can explain 2+ differences and name the key principle of each effect (water=heavy, fire=up, smoke=expands) | Explains differences fluently AND applies the Odd Rule to droplet falling; understands effects support, not steal |

---

## Extended Activity

**Homework / Follow-up project:** Create a complete "Nyangumi's Breach" scene with 3 effects: the splash (water), mist rising after (smoke), and a bioluminescent glow (magic) as the whale rises at night. Add a conservation message: "Nyangumi migrates to Kenya's coast from July to September. Keep the ocean quiet and clean so whales can breed safely." Research one fact about humpback whale migration and include it as a text caption in the animation.

**Advanced option (Blender):** For learners using Blender, try the smoke simulation: Add → Domain (container), Add → Flow (set to "Fire + Smoke"), bake at low resolution for testing, then render. Create a mist effect rising from the ocean surface after the breach.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-made droplet sprite and whale sprite. Learners only need to assemble the clone script and adjust the gravity variable. Start with just the splash (skip the second effect). Use fewer clones (5-8 instead of 18). | Try all 5 effects in one scene. Use Blender's smoke simulation for realistic mist. Add screen shake (shift the whole stage 2-3 pixels for 2 frames on impact). Experiment with the Odd Rule for droplet spacing: manually set vy to follow 1, 3, 5, 7, 9 pattern instead of smooth gravity. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Nyangumi whale breach example engaging? Did the scale of the splash help learners see the effect clearly?
- [ ] Did learners understand that water is heavy and falls fast (not floaty)?
- [ ] Were the Scratch clone blocks manageable, or did learners struggle with the clone lifecycle?
- [ ] What would I change next time?