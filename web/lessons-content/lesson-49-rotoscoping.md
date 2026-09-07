# Lesson Plan 49: Rotoscoping & Video Reference — Tracing Real Motion

**Module Reference:** Prompt 49 — 49-rotoscoping.md  
**Duration:** 80 min  
**Age Group:** 10-17  
**Animation Tool:** Phone (video recording), Krita (rotoscoping), Scratch (simple version)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports + Integrated Science |
| Sub-strand | Observation, Video Reference & Rotoscoping Technique |
| Core Competency | Creativity & Imagination, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Record** video reference of a real motion using a phone, choosing appropriate frame rate and framing.
2. **Rotoscope** key frames (every 2nd or 3rd frame, NOT every frame) in Krita, tracing real motion to build believable animation.
3. **Add personal style** on top of rotoscoped frames so the result is original art, not a stiff copy.

## Key Inquiry Question

> How do you turn a video of someone swimming like a **dolphin (Pomboo)** into animation — without tracing every single frame?

---

## Resources

- Phone with video camera
- Krita (free, for rotoscoping) or Scratch (simpler version)
- Tripod or phone stand (for stable video)
- Reference video of dolphins at Kisite-Mpunguti (optional)
- Paper and pencils for planning
- Optional: Raspberry Pi with Krita for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Tursiops aduncus*) — **Pomboo** in Swahili  
**Habitat:** Kisite-Mpunguti Marine Reserve, Watamu Marine National Park.  
**Why this animal?** Dolphins have graceful, clear-motion arcs — perfect for rotoscoping. But instead of tracing a dolphin, learners record THEMSELVES doing dolphin-like movements (swimming motion, jumping, diving) and rotoscope that. The connection: *your body moves like a dolphin when you swim — rotoscoping your own motion teaches you how real movement becomes animation.*  
**Conservation note:** Dolphins face threats from boat noise, net bycatch, and plastic pollution. KWS regulates dolphin tourism at Kisite-Mpunguti — boats must keep 100m distance.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show a short clip of Disney's Snow White dancing. Explain: *"Disney filmed a real actress dancing, then traced over her frame by frame. That technique is called rotoscoping — and it's 100 years old. Today you can do it with a phone and free software."*

Ask: *"Have you ever wished your animation looked more realistic? Rotoscoping is the shortcut — but it has a golden rule..."*

### Step 1: The Golden Rule & Setup (15 min)

**The Golden Rule: Trace KEY frames, not every frame.**
- At 24fps, a 3-second clip = 72 frames. Tracing all 72 = exhaustion + stiff animation.
- Instead trace every 2nd or 3rd frame → 24-36 drawings.
- Fast action (running, jumping) = every 2nd frame.
- Slow action (walking, head turn) = every 3rd frame.

**Recording the reference:**
1. Find a clear space (classroom or outdoor area)
2. Record a 3-second video of a learner doing a "dolphin jump" motion (crouch down, leap up, land)
3. Keep the camera still (use a tripod or prop the phone)
4. Frame the whole body — head to feet

### Step 2: Rotoscoping in Krita (25 min)

**Import video as animation background:**
1. Open Krita → New Animation (1280×720, 12fps)
2. Import the video: Layer → Import Animation Frames → select video file
3. The video frames appear as a background layer

**Trace every 3rd frame (for a slow motion):**
- Frame 1: Trace the crouch (anticipation pose)
- Frame 4: Trace the launch (body extending up)
- Frame 7: Trace the peak (highest point)
- Frame 10: Trace the fall (coming down)
- Frame 13: Trace the landing (impact + squash)

```
Frame  1:     Frame  4:     Frame  7:     Frame 10:     Frame 13:
   crouch  →    launch  →     peak   →     fall    →    landing
     O           |O           | O          | O           O
    /|\         /|          / |          / |          /|\
    / \         / \         /  \         / \          / \  ←squash!
   ===        ===          ===          ===          ===
```

**Add personal style:**
- Don't trace exactly — exaggerate the squash on landing
- Make the character an ocean animal (add fins, tail)
- Change the proportions (bigger head = cuter character)
- Add motion lines or effects

```scratch
// Simple Scratch version: use video frames as backdrops
// Upload 5 key video frames as backdrops
// Trace over them with the sprite editor

when [green flag] clicked
switch backdrop to [frame-1-crouch]
wait (0.3) seconds
switch backdrop to [frame-4-launch]
wait (0.3) seconds
switch backdrop to [frame-7-peak]
wait (0.3) seconds
switch backdrop to [frame-10-fall]
wait (0.3) seconds
switch backdrop to [frame-13-landing]
say [Splash!] for (1) seconds
```

### Step 3: Independent Practice (20 min)

**Challenge:** Record a 3-second video of an ocean animal movement and rotoscope it.

**Movement options:**
- **Dolphin jump:** crouch → leap → land (like a dolphin breaching)
- **Turtle swim:** slow arm strokes (like turtle flippers)
- **Octopus crawl:** wiggling fingers while moving forward (like tentacles)
- **Crab walk:** sideways scuttling

**Checklist:**
- [ ] Recorded 3-second video with phone (camera still)
- [ ] Imported into Krita as background
- [ ] Traced every 2nd or 3rd frame (NOT every frame)
- [ ] Added personal style (exaggerated, changed character, added effects)
- [ ] Played back — does it feel alive?

### Step 4: Sharing & Feedback (10 min)

Show the original video side by side with the rotoscoped animation. Discuss:
- *"What did rotoscoping give you that hand-animating wouldn't?"*
- *"What did your personal style add that the raw trace didn't have?"*
- *"How many frames did you trace? Was it manageable?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Frame Selection | Traced every frame (exhausting) | Traced too few frames (jumpy) | Traced every 2nd/3rd frame correctly | Adjusted frame rate for fast vs slow sections |
| Tracing Quality | Traces are loose/inaccurate | Traces match video but are stiff | Accurate traces with energy preserved | Accurate + exaggerated + personal style added |
| Style Addition | Pure copy of video — no originality | Minor changes (color only) | Clear personal style on top of real motion | Transformed into original character with exaggerated motion |

---

## Extended Activity

**Ocean Conservation Rotoscope:** Record yourself pretending to pick up plastic from a beach. Rotoscope the motion, then draw yourself as a sea turtle collecting plastic bags instead. The real motion grounds the animation; the character transformation tells the conservation story.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-recorded video to trace | Record multiple angles and rotoscope a 360° turn |
| Trace every 4th frame (fewer drawings) | Use Blender's Grease Pencil to rotoscope in 3D space with depth |
| Use Scratch (simpler than Krita) | Add color, shadows, and effects on top of the rotoscope |

---

## Teacher Reflection

- [ ] Did learners understand the "trace key frames, not every frame" rule?
- [ ] Was the video recording setup smooth? Did they keep the camera still?
- [ ] Did they add personal style, or just copy the video exactly?
- [ ] Would a pre-recorded dolphin video work better than self-recording?