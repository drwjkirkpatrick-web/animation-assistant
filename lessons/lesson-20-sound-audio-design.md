# Lesson Plan 20: Sound & Audio Design — The Other 50% of Animation

**Module Reference:** Prompt 20 — 20-sound-audio-design.md  
**Duration:** 75 min  
**Age Group:** 11-17  
**Animation Tool:** Scratch (primary) — extension with Audacity + Krita/OpenShot  

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Computer Science |
| Sub-strand | Multimedia — Sound Design for Animation |
| Core Competency | Creativity & Imagination, Digital Literacy, Communication & Collaboration |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Name the four sound layers (dialogue, SFX, music, ambient) and identify which layers an animation is missing.
2. Add at least two sound layers (SFX + ambient) to an animation, timed so the sound hits on the correct frame.
3. Value sound as half of the storytelling and record their own sound effects using everyday objects.

## Key Inquiry Question

> Watch a dolphin jump in silence — then watch the same jump with a splash, a whistle, and ocean waves. Which one feels real? Why is sound the other 50% of animation?

---

## Resources

- Laptop or Raspberry Pi with Scratch (with sound import enabled)
- Phone with a voice-memo app (for recording SFX) — one per group is enough
- Optional: Audacity (free) installed for editing recordings
- Optional: headphones (one per learner if possible)
- Free sound sources: freesound.org, YouTube Audio Library (ambient "ocean waves," "dolphin clicks")
- Reference video clip: a bottlenose dolphin jumping (Pomboo) at Kisite-Mpunguti

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin — *Pomboo*  
**Habitat:** Watamu Marine National Park and Kisite-Mpunguti Marine Reserve; playful pods that leap and splash.  
**Why this animal?** A dolphin jump is a SOUND showcase: the whistle/click before the jump (anticipation sound), the splash on re-entry (SFX), the wave hiss (ambient), and possible dolphin chatter (dialogue-ish). It naturally contains all four sound layers in one short action — perfect for teaching timing sound to animation.  
**Conservation note:** Dolphins face threats from bycatch (fishing nets) and pollution. KWS regulates dolphin-watching boats at Kisite-Mpunguti to keep distance and reduce stress. When we record "dolphin sounds," we also learn that noise from boats can disrupt how real dolphins communicate — protecting them means keeping the ocean quiet.

---

## Lesson Development

### Introduction (8 min)

Play a dolphin-jump clip **with sound off**. Ask: *"How did that feel?"* (Empty, flat.) Play it **with sound**. Ask: *"Now?"* (Exciting, real.) State the lesson's big idea: *"Bad sound ruins great animation. Good sound lifts simple animation. Sound is HALF of your story."* Tell them today they'll add the missing half to a dolphin jump.

### Step 1: Concept Introduction — The 4 Layers & Timing (15 min)

Teach the four sound layers (from Prompt 20) using the dolphin jump as the example:

```text
THE 4 SOUND LAYERS — mapped to a dolphin jump

1. DIALOGUE    → dolphin whistle/click "character voice"
2. SFX         → the SPLASH when it re-enters the water
3. MUSIC       → playful fast tune during the jump
4. AMBIENT     → ocean wave hiss (loops the WHOLE scene = makes it real)
```

**Timing rules (the pro secret):**
- **Hit the frame:** the splash sound lands ON the frame where the dolphin hits the water — not before, not after.
- **The 2-frame rule:** if a sound feels "off," shift it 2 frames earlier or later. Your ears are more sensitive than you think.
- **Anticipation sound:** a creak/wind-up *before* an action (a tiny whistle building before the jump).
- **Follow-through sound:** a splash ripple/ring *after* the dolphin lands.

> **Pro tip:** *Ambient/room tone makes everything feel real — even 10 seconds of ocean-hiss looped changes a scene from "vacuum" to "ocean."*

### Step 2: Guided Practice — Add Sound to a Dolphin Jump in Scratch (20 min)

Build the animation + sound together. First a simple dolphin jump, then layer the sounds.

```text
STEP-BY-STEP: Dolphin jump with 4 sound layers (Scratch)

PART A — the animation (dolphin = Pomboo)
  Sprite: choose "Dolphin" (or paint a simple dolphin shape)

  when [green flag] clicked
  go to x: -120 y: -100        ← start in the water (left)
  forever
      // anticipation: dip down first
      glide 0.5 secs to x: -120 y: -140
      // the jump (arc up and over)
      glide 1 secs to x: 120 y: 100
      // re-enter water
      glide 0.5 secs to x: 160 y: -100
      // pause before looping
      wait 1 secs
      go to x: -120 y: -100
  end

PART B — add the sound layers

  Layer 4 — AMBIENT (ocean waves, loops forever):
    Sounds tab → Choose a Sound → search "Ocean Waves" (or record
    your own: blow gently past a microphone = wave hiss)
    In the code:
      when [green flag] clicked
      forever
          play sound [Ocean Waves] until done
      end

  Layer 2 — SFX (splash on re-entry):
    Record a splash: slap your hand on a cup of water, or
    crumple paper quickly. Save as "Splash".
    Use a broadcast to TIME it to the landing frame:
      In the jump code, the moment the dolphin reaches the water,
      add:  broadcast [splash]
      Separate script:
      when I receive [splash]
      play sound [Splash] until done

  Layer 1 — DIALOGUE (dolphin whistle):
    Record a whistle with your mouth, or search "dolphin" sounds.
    Play it at the TOP of the jump (broadcast [whistle] at y: 100).

  Layer 3 — MUSIC (optional, keep QUIET):
    Import a short playful tune. Set volume lower so it doesn't fight:
      set volume to 30
      play sound [Playful Tune]   ← "play sound" (no "until done") = background
```

Run it. The scene should now feel like a *real ocean*, not a vacuum. If the splash feels early/late, shift the `broadcast` by a frame or two (the 2-frame rule).

### Step 3: Independent Practice — Record Your Own SFX (20 min)

Challenge: *"Replace at least TWO sounds with ones you RECORD yourself using everyday objects. Keep the timing correct."*

Give the DIY sound-effects list and a recording plan:

```text
DIY SOUND EFFECTS (record with phone voice-memo, then import to Scratch)

SPLASH      → slap your hand flat on a cup/bowl of water
WAVE HISS   → blow gently across the phone mic, or shake rice in a box
DOLPHIN WHISTLE → whistle high then low with your mouth
BUBBLES     → blow through a straw into a glass of water
JUMP CREAK (anticipation) → rub a balloon slowly
IMPACT      → bang a textbook flat on a desk

RECORDING PLAN:
  [ ] Record 3 sounds (ambient, SFX, dialogue) as .wav or .mp3
  [ ] In Scratch: Sounds tab → "Upload Sound" → load each file
  [ ] Trim long silences at the start (Scratch: select + delete)
  [ ] Re-time: use broadcast so each sound hits the right frame
  [ ] CHECK: play with eyes closed — can you "see" the dolphin jump?
```

**Free-resource note:** no phone/no recording? Use freesound.org (search "ocean waves", "splash", "dolphin") or YouTube Audio Library — import the file into Scratch the same way.

### Step 4: Sharing & Feedback (10 min)

Partners play their animation. **First with sound ON, then with sound OFF** — so the class hears the difference. Use the critique frame:
- **One layer that worked** (e.g., "the splash hit exactly on the landing")
- **One missing layer** (e.g., "no ambient — felt like a vacuum")
- **One timing fix** (e.g., "the whistle came 2 frames late — shift it")

Celebrate the best DIY sound effect of the class (the funniest homemade splash/whistle).

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Sound layers knowledge | Cannot name the 4 layers | Names 1–2 layers | Names all 4 layers and identifies which an animation is missing | Names all 4, identifies missing ones, and explains what each adds to the story |
| Adding & timing sound | No sound added, or 1 untimed sound | 1–2 layers added; timing noticeably off | 2+ layers (SFX + ambient) added; splash hits on the correct frame | 3–4 layers added; all timed to frame; uses anticipation/follow-through sounds |
| DIY recording | Uses only stock sounds; no recording | Records 1 sound but messy/untimed | Records 2+ own sounds, cleaned & imported correctly | Records 2+ sounds, edited (trimmed), AND can teach a peer the import+timing steps |

---

## Extended Activity

**Homework — "Sound conservation story":** Record a 10-second ambient soundscape of your environment (school, home, or if near the coast, the beach/shore). Import it into your dolphin animation as the ambient layer. Then add a ONE-LINE conservation message as a text frame or voice line: *"Keep the ocean quiet — noise harms Pomboo."* (Boat noise disrupts dolphin communication.) For advanced learners: mix all 4 layers in OpenShot or Audacity, set music volume low, and export a final MP4. This builds toward a finished portfolio piece combining animation, colour (Lesson 19), and sound.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Start with just AMBIENT + one SFX (2 layers); provide pre-recorded sounds to import; use the simple "play sound until done" block only | Require all 4 layers; use `broadcast` for precise timing; record + edit in Audacity (trim, normalise); mix layers in OpenShot/DaVinci Resolve with volume control |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the dolphin jump a clear example of all four sound layers?
- [ ] Could learners hear that sound changes how the animation *feels*?
- [ ] What would I change next time?