# Lesson Plan 10: Reference Library Guide — Study Real Movement

**Module Reference:** Prompt 10 — 10-reference-library.md  
**Duration:** 75 min  
**Age Group:** 12-17  
**Animation Tool:** Scratch (primary), Krita/Pencil2D (alternative), phone camera for recording reference

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Animation & Motion Graphics |
| Core Competency | Critical Thinking & Problem Solving; Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain why studying real movement ("you can't animate what you haven't observed") is essential to believable animation.
2. Apply the 3-Step Study Method (normal speed → 25% speed → frame-by-frame) to analyze dolphin movement and identify 3-4 key poses.
3. Value observation as a creative skill and respect real animal behavior as the foundation for animation.

## Key Inquiry Question

> "How does a bottlenose dolphin (*pomboo*) arc out of the water when it jumps — and how can studying real video make our animation look believable instead of fake?"

---

## Resources

- Scratch or Krita/Pencil2D
- Projector or large screen for video analysis
- Slow-motion dolphin video (search YouTube: "dolphin jumping slow motion" or "dolphin breach 240fps")
- Phone with slow-mo mode (most phones have 240fps) — one per group if available
- Printed "Reference Study Sheet" with the 3-Step Study Method and key frame sketch boxes
- Paper and pencils for sketching key frames
- Optional: Raspberry Pi + monitor for low-resource viewing (pre-download video files)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (Swahili: *Pomboo*)  
**Habitat:** Found in Watamu Marine National Park and Kisite-Mpunguti Marine Reserve (Kwale County). Dolphins are frequently spotted in pods near the coral reefs and open waters of Kenya's coast.  
**Why this animal?** The dolphin's breach — arcing out of the water and re-entering with a splash — is a perfect reference study subject. It contains anticipation (the deep dive before the jump), a clear arc trajectory through the air, and impact (the splash on re-entry). Studying real dolphin footage teaches learners how to observe and extract key poses from live movement.  
**Conservation note:** Dolphins face threats from bycatch (getting caught in fishing nets), pollution, and disturbance from unregulated boat tourism. KWS has established **dolphin-watching regulations** at Kisite-Mpunguti Marine Reserve to protect pods — boats must keep a respectful distance and avoid separating mothers from calves. When we study dolphins for animation, we also learn to appreciate why they need protection.

---

## Lesson Development

### Introduction (10 min)

Show a 15-second clip of a dolphin breaching at normal speed. Ask learners: "What did you see? How would you describe the jump in one sentence?"

Most learners will say something general: "It jumped out of the water and went back in."

Now show the **same clip at 25% speed**. Ask: "What do you notice now that you couldn't see before?"

Guide them to notice:
- The dolphin dives *down* first (anticipation) before going up
- The body traces a **curved arc** through the air — not a straight line up and down
- The splash on re-entry is bigger than expected
- The tail comes out of the water last

Introduce the golden rule of animation reference: **"You can't animate what you haven't observed."** Explain that professional animators always study real movement before they animate — they watch videos in slow motion, sketch key poses, and sometimes act out the movement themselves.

### Step 1: Concept Introduction — The 3-Step Study Method (15 min)

Teach the **3-Step Study Method** for studying any movement reference:

1. **Watch it 3 times at normal speed.** What's the overall feeling? What is the overall shape of the motion?
2. **Watch it at 25% speed.** What are the key poses? Where does movement start? Which body part leads?
3. **Watch it frame-by-frame.** Count frames between poses. Notice the arcs. See what happens in the transitions.

Apply the method to the dolphin breach using the dolphin video:

**Step 1 — Normal speed (watch 3 times):** The dolphin leaps in a graceful arc. It looks fast, powerful, and joyful.

**Step 2 — 25% speed (identify key poses):**

| Frame | Key Pose | Description |
|-------|----------|-------------|
| 1 | **Approach** | Dolphin swimming fast just below the surface, body angled upward |
| 2 | **Launch** | Body breaks the surface, nose first, momentum carrying it up and forward |
| 3 | **Apex** | Highest point — body is nearly horizontal, fully out of water, arc at its peak |
| 4 | **Descent** | Body angles downward, gravity pulling it back, nose pointing toward water |
| 5 | **Impact** | Body re-enters water, splash erupts, tail still above surface |
| 6 | **Submerge** | Dolphin disappears below, splash settles, bubbles remain |

**Step 3 — Frame-by-frame (count the transitions):**
- Frames 1→2: Fast — the launch is explosive (few frames = fast movement)
- Frames 2→3: Slowing — as it reaches the apex, it decelerates (more frames = slow-in)
- Frames 3→4: Speeding up — gravity takes over (fewer frames = accelerating)
- Frames 4→5: Fast impact — splash is sudden
- The **arc** is a smooth curve, not a triangle or V-shape

**Key observation:** Movement starts from the *head* — the nose leads the jump. The tail is the last thing to leave the water and the last to re-enter. This is **follow-through** in the dolphin's own body.

Show the Python/Scratch code below that demonstrates how to translate key poses into animation timing.

**Scratch — Dolphin Breach (Key Pose + Arc Approach):**

```scratch
when [green flag] clicked
set [y position] to (-100)
set [x position] to (-200)
// POSE 1: Approach — swimming just below surface, angled up
switch costume to [approach]
repeat (4)
  change [x position] by (15)
  change [y position] by (8)
  wait (0.05) seconds
end
// POSE 2: Launch — explosive, few frames = fast
switch costume to [launch]
repeat (3)
  change [x position] by (20)
  change [y position] by (35)
  wait (0.04) seconds
end
// POSE 3: Apex — slowing down at the top (slow-in = more frames, less movement)
switch costume to [apex]
repeat (5)
  change [x position] by (10)
  change [y position] by (5)
  wait (0.08) seconds
end
// POSE 4: Descent — gravity accelerating (fewer frames, more movement per frame)
switch costume to [descent]
repeat (4)
  change [x position] by (15)
  change [y position] by (-25)
  wait (0.05) seconds
end
// POSE 5: Impact — fast re-entry + splash
switch costume to [impact]
wait (0.15) seconds
// POSE 6: Submerge
switch costume to [submerge]
repeat (3)
  change [y position] by (-15)
  wait (0.06) seconds
end
```

> **Teacher note:** Learners need to draw or find 6 dolphin costumes (approach, launch, apex, descent, impact, submerge). They can sketch these from the video stills. The key is that the *timing* — how many frames and how much wait time between poses — is based on what they observed in the reference, not guessed.

### Step 2: Guided Practice — Studying and Sketching Together (15 min)

Divide learners into groups of 3-4. Give each group a phone (or use the projector) with the slow-motion dolphin video.

**Task:** Complete a Reference Study Sheet together.

1. **Watch** the clip 3 times at normal speed. Each group member writes one word describing the feeling (e.g., "powerful," "graceful," "fast").
2. **Watch** at 25% speed. Pause at each key pose and **sketch** it in the boxes on the Reference Study Sheet. Label each sketch: approach, launch, apex, descent, impact, submerge.
3. **Frame-by-frame:** Count how many frames (or seconds) between the launch and the apex. Count between apex and impact. Notice: which part is slower? (Answer: approaching the apex is slower = slow-in. Descending is faster = slow-out.)

Walk around and check that groups are actually *sketching poses* — not just watching passively. The sketching is what builds observation skill.

**Common Reference Mistake to discuss:** Copying the reference too literally. Reference is a *guide*, not a trace. Real dolphins have complex body shapes; for animation, we simplify to the key poses and exaggerate slightly for clarity. The arc can be a bit higher, the splash a bit bigger — that's animation, not documentation.

### Step 3: Independent Practice — Animate the Breach (20 min)

Learners use their Reference Study Sheet sketches to animate the dolphin breach.

**In Scratch:**
1. Draw 6 costumes based on the sketches (or use a simple oval/dolphin shape in 6 angles).
2. Use the code from Step 1 as a starting point.
3. Adjust the timing based on what they observed: Did the apex feel slow? Add more `wait` time there. Was the launch fast? Reduce the repeat count.

**In Krita/Pencil2D:**
1. Draw the 6 key poses on frames 1, 5, 10, 14, 18, 22.
2. Add in-between frames to smooth the arc.
3. Play back at 12 fps. Does the arc look smooth? Is the timing believable?

**Challenge constraint:** The dolphin must follow a **visible arc path** — not a straight line up and down. If it goes straight up and straight down, that's wrong. Use the glide or position changes to create a curve.

Walk around and check:
- Are learners using their reference sketches, or animating from imagination? (The whole point is to use reference.)
- Is the arc curved, not V-shaped?
- Is the timing varied (slow at apex, fast at launch and impact)?

### Step 4: Sharing & Feedback (10 min)

Learners do a **gallery walk**: leave their animation playing on their screen and walk around to see others' work. Each learner writes down one observation on a sticky note and leaves it by someone's screen:

- "I can see the arc clearly."
- "The slow part at the top looks real."
- "The splash is dramatic!"

Gather the class and ask: "Whose animation felt the most believable? What made it believable?" Connect answers back to reference: the most believable animations are the ones that studied the real movement most carefully.

End with: "Next time you animate anything — a person walking, a fish swimming, a bird flying — **study the real thing first.** That's what professionals do."

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Reference study (3-Step Method) | Watches video but does not sketch or identify key poses | Sketches some poses but misses key ones (e.g., skips the approach or apex) | Completes all 3 steps, sketches 4+ key poses, labels them correctly | Completes all 3 steps AND notes frame counts/timing differences between poses |
| Animation from reference | Dolphin moves but no arc — goes straight up and down | Arc is present but timing is uniform (same speed throughout) | Dolphin follows a curved arc with varied timing (slow at apex, fast at launch/impact) | Arc + varied timing + at least one detail from reference (e.g., tail exits last, or splash on impact) |
| Understanding observation principle | Cannot explain why studying reference matters | Says "it makes it look better" but not why | Explains that observation reveals key poses, arcs, and timing you can't guess | Explains the principle AND identifies a common mistake (e.g., copying too literally, or animating without studying) |

---

## Extended Activity

**Home Study:** Pick any Kenyan ocean animal from the reference list (turtle, octopus, clownfish, jellyfish). Find a slow-motion video on YouTube. Complete a Reference Study Sheet: 3 viewings, 4-6 key pose sketches, frame counts. Bring it to the next class.

**Conservation connection:** Research how KWS regulates dolphin-watching tourism at Kisite-Mpunguti Marine Reserve. Write one paragraph: Why do boats need to keep their distance? How does noise from boat engines affect dolphins? How does studying dolphins for animation help us appreciate why they need protection?

**Recording your own reference:** If learners live near the coast or have access to a pool, they can film their own swimming or jumping motion in slow-mo (240fps) on a phone. Film from the side (profile view) to see the arc clearly.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-printed key pose sketches to trace. Reduce to 4 key poses (launch, apex, descent, impact). Use a pre-made dolphin sprite with costumes already drawn. | Study two animals and compare: How does a dolphin's arc differ from a humpback whale's (*nyangumi*) breach? Animate both and note the timing/weight differences. Try rotoscoping — trace over the video frames directly. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the dolphin breach a good reference subject? Did it engage learners?
- [ ] Did learners actually use the 3-Step Study Method, or did they skip to animating?
- [ ] Were the key pose sketches detailed enough to inform their animation?
- [ ] What would I change next time?