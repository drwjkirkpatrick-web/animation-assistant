# Lesson Plan 53: Cloth, Hair & Secondary Motion — Things That Trail

**Module Reference:** Prompt 53 — 53-cloth-hair-simulation.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Krita (hand-drawn trailing), Scratch (simple), Blender (cloth simulation)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Secondary Motion, Cloth & Hair Animation |
| Core Competency | Creativity & Imagination, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Explain** the golden rule of secondary motion: secondary ALWAYS starts AFTER primary (never at the same time, never before).
2. **Animate** trailing elements (jellyfish tentacles, lionfish fins) with a 2-4 frame delay after the body moves.
3. **Identify and fix** common secondary motion mistakes (cloth moving same time as body, hair floating not falling).

## Key Inquiry Question

> Why do a **jellyfish's** tentacles trail behind its bell — and how does the "delay principle" make everything from cloth to hair to tentacles feel real?

---

## Resources

- Krita or Scratch (Blender for advanced cloth simulation)
- Reference video of jellyfish pulsing at Kenyan reef
- Reference video of lionfish swimming with flowing fins
- Paper and pencils for planning delay frames
- Optional: a scarf or piece of fabric (for physical demo)
- Optional: Raspberry Pi with Krita

---

## Local Context: Kenyan Ocean Animal

**Animal:** Jellyfish (various species) — common in Kenya's Indian Ocean waters  
**Habitat:** Drifting in currents throughout Kenya's marine parks. Often seen at Mombasa Marine Park and Watamu.  
**Why this animal?** The jellyfish is THE perfect secondary motion teaching tool. Its bell (the round top) pulses — that's the PRIMARY motion. Its tentacles trail behind — that's the SECONDARY motion. The tentacles NEVER move first. The bell contracts, THEN the tentacles follow with a delay. This is the delay principle in nature, visible in every jellyfish.  
**Conservation note:** Jellyfish populations are increasing in some areas due to overfishing (their predators and competitors are being removed). They are important indicators of ocean health. Jellyfish stings can be painful — respect them in the water.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Wave a scarf in the air. Stop your hand suddenly. Ask: *"Did the scarf stop when my hand stopped? No — it kept going. That's secondary motion. Things that trail ALWAYS follow the body, never lead."*

Show a video of a jellyfish pulsing. Point out: *"The bell moves first. The tentacles follow. If the tentacles moved at the same time, it would look like a rigid plastic toy. The delay is what makes it feel alive."*

### Step 1: The Golden Rule & How Things Trail (15 min)

**The Golden Rule:** Secondary motion ALWAYS starts AFTER primary motion.
- Body moves first → cloth follows
- Head turns first → hair follows
- Bell pulses first → tentacles follow
- NEVER the other way around

**How cloth/hair/tentacles move:**

| Element | How It Trails | Key Principle |
|---------|-------------|---------------|
| Cloth | Follows body with 2-4 frame delay | Never initiates; folds at joints |
| Hair | Lags head turns by 2-3 frames | Falls with gravity; lighter strands move more |
| Jellyfish tentacles | Lag bell pulse by 3-5 frames | Water resistance slows the trailing |
| Lionfish fins | Lag body direction change by 2-4 frames | Fins are thin = more delay |

**Common mistakes:**
1. Cloth moves at SAME time as body → looks glued on (no delay)
2. Hair FLOATS instead of falling → gravity forgotten
3. No wind on loose fabric → everything moves the same way
4. All tentacles move identically → no overlap (they should stagger)

### Step 2: Jellyfish Pulse in Krita (25 min)

**Animate a jellyfish with proper delay:**

Draw 6 frames at 12fps:

```
Frame 1: Bell is relaxed (round), tentacles hanging straight
Frame 2: Bell starts contracting (slightly oval), tentacles STILL straight (no movement yet!)
Frame 3: Bell fully contracted (flat oval), tentacles JUST STARTING to move upward
Frame 4: Bell expanding back, tentacles trailing UPWARD (delayed reaction)
Frame 5: Bell fully relaxed, tentacles at highest point (maximum delay)
Frame 6: Bell still, tentacles falling back down (gravity pulls them)
```

**Key timing:** The tentacles start moving on Frame 3 — the bell started on Frame 2. That 1-frame delay is what makes it feel real.

```scratch
// Simple Scratch jellyfish with delay
when [green flag] clicked
// Bell sprite (primary motion)
// Tentacle sprite (secondary motion - follows with delay)

// Bell contracts first
broadcast [bell-contract]
wait (0.1) seconds              ← THE DELAY! Tentacles don't move yet
broadcast [tentacles-follow]    ← NOW tentacles react

// When bell expands:
broadcast [bell-expand]
wait (0.1) seconds              ← Delay again
broadcast [tentacles-settle]
```

### Step 3: Fix the Broken Secondary Motion (20 min)

**Challenge:** Take a "broken" animation where the tentacles move at the same time as the bell, and fix it by adding delay.

**Problems to fix:**
- [ ] Tentacles and bell move at the same time → add 2-3 frame delay to tentacles
- [ ] Tentacles are floating (not falling back) → add gravity frames
- [ ] All tentacles move identically → stagger them (different tentacles delay by different amounts)
- [ ] No overlap → tentacles should still be settling when the bell starts the next pulse

**Advanced option (Blender cloth simulation):**
1. Add a plane (cloth) to a character
2. Add Cloth physics modifier
3. Pin the attached points (where cloth connects to body)
4. Set gravity and wind
5. Press Play — the computer simulates the cloth with proper delay
6. Bake the simulation to save it

### Step 4: Sharing & Feedback (10 min)

Show the before (same-time) and after (delayed) side by side:
- *"Which one feels more alive? Why?"*
- *"Can you see the delay? How many frames is it?"*
- *"Do the tentacles feel like they're in water?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Delay Principle | No delay (everything moves together) | Small delay but inconsistent | Clear 2-4 frame delay on all secondary elements | Varied delays per element + overlap between tentacles |
| Gravity/Weight | Tentacles float (no gravity) | Some falling but too slow | Tentacles fall with gravity and settle | Gravity + water resistance + drag + settle with follow-through |
| Common Mistakes | Has all 4 mistakes | Fixed 1-2 mistakes | Fixed 3+ mistakes | No mistakes + added wind variation + tentacle overlap |

---

## Extended Activity

**Lionfish Fin Animation:** Animate a lionfish swimming with its flowing fins trailing behind. The body changes direction first, then each fin follows with a different delay (dorsal fin 2 frames, pectoral fins 3 frames, anal fin 4 frames). The staggered delays create overlapping action. Add a conservation message: lionfish are an invasive species in some reefs — but in Kenya's Indian Ocean they are native and important.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Animate only 2 elements (bell + 1 tentacle) | Use Blender cloth simulation on a character's clothing |
| Use 6 frames instead of 12 | Add wind force variation — gusts that affect trailing elements |
| Focus on the delay concept only (skip gravity) | Animate a full character with hair, clothing, AND tail — all with different delays |
| Use Scratch (broadcast delay is simple to understand) | Use Krita: draw each tentacle on a separate layer with staggered keyframes |

---

## Teacher Reflection

- [ ] Did learners understand the delay principle (secondary AFTER primary)?
- [ ] Could they see the difference between same-time and delayed motion?
- [ ] Was the jellyfish an effective teaching example?
- [ ] Would a physical demo (scarf on a stick) help reinforce the concept?