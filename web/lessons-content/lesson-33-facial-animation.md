# Lesson Plan 33: Facial Animation & Expressions — The Face That Tells the Story

**Module Reference:** Prompt 33 — 33-facial-animation.md
**Duration:** 70 min
**Age Group:** 12-17
**Animation Tool:** Scratch (primary) / Krita (optional extension)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Performing Arts — Animation and Digital Storytelling |
| Core Competency | Creativity & Imagination, Communication & Collaboration |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Identify the three zones of facial expression (eyes, brows, mouth) and explain how each contributes to showing emotion.
2. Create a character with at least four different facial expressions (happy, sad, surprised, angry) using costume switching in Scratch or frame-by-frame drawing in Krita.
3. Apply the 2-frame rule (eyes → brows → mouth) to sequence facial changes so the character's expression feels alive, not robotic.

## Key Inquiry Question

> How do we make Pomboo the dolphin look truly happy or surprised — not just by changing its mouth, but by moving its eyes and brows first?

---

## Resources

- Scratch (offline or online at scratch.mit.edu) or Krita (free download)
- Projector or large screen for demonstration
- Reference photos/video of bottlenose dolphins (Pomboo) — search "bottlenose dolphin face close-up"
- Printed expression reference sheet (the 6 universal expressions from the lesson)
- Paper and pencils for sketching expressions before animating
- Optional: Raspberry Pi running Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (Pomboo)
**Habitat:** Kisite-Mpunguti Marine Reserve (Kwale County), Watamu Marine National Park (Kilifi County) — dolphins live in pods along Kenya's south coast and are a major draw for responsible dolphin-watching tourism.
**Why this animal?** Dolphins have a natural curve to their mouth that looks like a smile — but a real smile also involves the eyes and brows. This makes Pomboo the perfect character for teaching that facial expression is about ALL three zones working together, not just the mouth. Dolphins are also highly social and expressive animals, making them emotionally rich animation subjects.
**Conservation note:** Bottlenose dolphins face threats from bycatch (getting caught in fishing nets), plastic pollution, and disturbance from irresponsible boat tourism. KWS (Kenya Wildlife Service) regulates dolphin-watching at Kisite-Mpunguti to keep boats at a safe distance. When animating Pomboo, learners can tell conservation stories about keeping the ocean clean and respecting dolphin space.

---

## Lesson Development

### Introduction (8 min)

Show a short video or photo of a bottlenose dolphin (Pomboo) at the Kenya coast. Ask learners:
- "What emotion do you think this dolphin is showing?"
- "How can you tell — is it just the mouth, or something else?"

Explain that the audience looks at a character's FACE 80% of the time. If the face is "dead," the whole character feels dead — even with great body animation. Introduce the three zones: **eyes, brows, mouth**. Write them on the board in order of movement: Eyes → Brows → Mouth.

Connect to Pomboo: "A dolphin's smile is famous. But a real expression of happiness also has the eyes squinting slightly and the brows relaxed. Today we'll learn how to make Pomboo's face truly express emotion."

### Step 1: Concept Introduction — The 3 Zones & 6 Universal Expressions (15 min)

Teach the three zones of facial expression using Pomboo as the example character.

**Zone 1: Eyes (Lead everything)**
- Eyes move FIRST in any reaction
- Eye darts: quick 1-2 frame snaps = searching, nervous
- Blinks: normal every 2-4 seconds; double blink = surprise; slow blink = skepticism
- Pupils dilate (get bigger) when surprised or scared

**Zone 2: Brows (The emotion amplifier)**
- Raised up = surprise, question, disbelief
- Furrowed (together/down) = anger, concentration
- Asymmetric (one up, one down) = skepticism, "really?"
- Brows move 2-3 frames BEFORE the mouth changes

**Zone 3: Mouth (The communicator)**
- Smile: corners up; big smile = cheeks push up, eyes squint
- Frown: corners down
- Open round: shock
- Pressed thin: determination
- Asymmetric smirk: hiding something

**The 2-Frame Rule:** When emotion changes, eyes move first, brows follow 2 frames later, mouth follows 2 frames after brows. This creates a natural cascade that feels alive.

Show the 6 universal expressions (recognized in every culture):

| Expression | Eyes | Brows | Mouth |
|-----------|------|-------|-------|
| Happy | Slightly squinted | Relaxed/up | Corners up (smile) |
| Sad | Downcast | Down and together (inner up) | Corners down (frown) |
| Angry | Narrowing | Down and together | Pressed or open shouting |
| Surprised | Wide open | High up | Open round |
| Fear | Wide | Up and together | Open slightly |
| Disgust | Narrowed | Furrowed | Asymmetric, nose wrinkled |

**Code Demonstration (Scratch):** Show how to draw 4 face costumes for Pomboo (neutral, happy, surprised, angry) and switch between them:

```scratch
when [green flag] clicked
switch costume to [neutral]
wait (1) seconds
say [I see a fish!] for (2) seconds
switch costume to [surprised]   // Eyes go wide FIRST
wait (0.1) seconds               // ~2 frames at 30fps
switch costume to [surprised-brows] // Brows react
wait (0.1) seconds
switch costume to [surprised-full]  // Mouth opens LAST
wait (1) seconds
switch costume to [happy]        // Now happy!
```

Explain: each `wait 0.1 seconds` is roughly 2-3 frames at Scratch's 30 fps. This creates the cascade: eyes → brows → mouth.

### Step 2: Guided Practice — Animating Pomboo's Reaction (15 min)

Walk through one example together as a class. Learners follow along step by step.

**In Scratch:**
1. Create a new sprite — draw a simple dolphin face (oval head, two eyes, a mouth curve). Name it "Pomboo."
2. Create 4 costumes by editing the face:
   - **Costume 1 "neutral":** Normal eyes, relaxed brows, slight smile
   - **Costume 2 "happy":** Squinted eyes (curved lines), brows up, big smile (curve up more)
   - **Costume 3 "surprised":** Wide round eyes, brows high up, mouth open as an "O"
   - **Costume 4 "angry":** Narrowed eyes, brows down and together, mouth pressed flat
3. Build this script together:

```scratch
when [green flag] clicked
switch costume to [neutral]
say [Hello! I am Pomboo.] for (2) seconds
// SCENE: Pomboo sees a plastic bag in the ocean
say [What is that?] for (1) seconds
switch costume to [surprised]       // Eyes wide — eyes lead!
wait (0.1) seconds
// (Brows already drawn into the surprised costume)
wait (0.1) seconds
// Mouth already in the surprised costume — cascade complete
say [Oh no! Plastic pollution!] for (2) seconds
switch costume to [angry]
say [We must keep the ocean clean!] for (2) seconds
switch costume to [happy]
say [Together we can do it! :] for (2) seconds
```

4. Play it back. Ask learners: "Does the expression change feel alive? What if we removed the `wait` blocks?"

**In Krita (alternative):**
1. Create 4 key frames on the timeline at frames 1, 8, 16, and 24.
2. Frame 1: Draw Pomboo with neutral face.
3. Frame 8: Draw Pomboo surprised (eyes wide, brows up, mouth open). Note: on frames 6-7, draw intermediate eyes-only change (eyes widen before brows/mouth).
4. Frame 16: Draw Pomboo angry. Again, eyes change first (frames 14-15), then full expression at frame 16.
5. Frame 24: Draw Pomboo happy.
6. Turn on onion skin to check that the face position stays consistent across expressions.

### Step 3: Independent Practice — Pomboo's Emotional Journey (20 min)

Learners create their own short animation of Pomboo going through at least 3 different emotions in a mini-story.

**Challenge:** Animate Pomboo reacting to an ocean event. Choose one:
- Pomboo finds a friend (surprised → happy)
- Pomboo encounters a plastic bag (curious → disgusted → angry)
- Pomboo gets separated from its pod (sad → afraid → happy when reunited)

**Requirements:**
- At least 3 different facial expressions
- The 2-frame rule applied (eyes change before the full expression)
- A short story told through the face and simple dialogue (say blocks or speech bubbles)

**Scratch starter code for learners:**

```scratch
when [green flag] clicked
switch costume to [neutral]
// YOUR STORY BEGINS HERE
// 1. Add a say block with Pomboo's first line
// 2. Switch to the first emotion costume (eyes change first!)
// 3. Add a short wait (0.1 sec = ~2-3 frames)
// 4. Switch to the full expression costume
// 5. Add dialogue for that emotion
// 6. Repeat for at least 2 more emotion changes
// 7. End with Pomboo back to neutral or happy

// EXAMPLE STRUCTURE:
say [I am swimming with my pod.] for (2) seconds
switch costume to [surprised]
wait (0.1) seconds
say [Wait — where did everyone go?] for (2) seconds
switch costume to [sad]
wait (0.1) seconds
say [I am all alone...] for (2) seconds
// Add your own ending!
```

**For Krita users:** Create 6-8 key frames telling the same emotional journey. Use onion skin to keep Pomboo's face positioned correctly. Remember: on the frame BEFORE each new expression, change only the eyes to preview the emotion coming.

Teacher circulates and checks:
- Are learners changing eyes first?
- Are the expressions distinct enough to read?
- Is the story clear through the face alone?

### Step 4: Sharing & Feedback (10 min)

Learners present their Pomboo animation to a partner or the class. Use this critique framework:
1. **What I see:** Describe the emotions you observed in order.
2. **What works:** One thing that made the expression feel alive.
3. **One question:** "What if you tried…?" (e.g., "What if Pomboo blinked before looking surprised?")

Celebrate effort and creativity. Highlight learners who applied the 2-frame rule successfully. Note: the face tells the story — if the class can guess the emotion just from watching, the animation works.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Expression creation | Creates 1-2 expressions; faces are unclear or identical | Creates 2-3 expressions; some distinction but hard to read | Creates 3+ clear, distinct expressions using eyes, brows, and mouth | Creates 4+ expressions with subtle blending (e.g., happy+surprised); all clearly readable |
| 2-frame rule application | All features change simultaneously; no sequencing | Attempts sequencing but timing is wrong (mouth first) | Eyes change before brows and mouth; timing feels natural | Uses 2-frame rule consistently AND adds eye darts or blinks for extra life |
| Storytelling through face | No story; random expression changes | Basic story but expressions don't match the events | Clear story where expressions match what's happening | Rich emotional journey with expression blending; story understandable from face alone |

---

## Extended Activity

**Homework / Follow-up project:** Add a second character to the scene — a sea turtle (Kasa) or a clownfish. Animate a conversation between Pomboo and the new character. Practice the **70/30 rule**: in dialogue, Pomboo's eyes look at the other character 70% of the time and look away 30% of the time while "thinking." Add at least one eye dart (quick 1-2 frame eye shift) when Pomboo is searching or nervous.

**Conservation connection:** Add a conservation message to the story — Pomboo and friends cleaning up plastic pollution in Watamu Marine National Park. Research one real action KWS takes to protect dolphins and include it in the dialogue.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-drawn Pomboo face templates — learners only need to modify the eyes and mouth for each costume. Start with just 2 expressions (happy + surprised). Use longer `wait` blocks (0.3-0.5 sec) to make the changes easier to see. | Try expression blending: create a "happy+surprised" (wow!) face and a "sad+angry" (betrayed) face. Attempt simple lip sync by animating mouth shapes for a short dialogue line ("Keep the ocean clean!"). Use Krita for frame-by-frame work with onion skin. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Pomboo dolphin example engaging? Did learners connect with the character?
- [ ] Did learners understand and apply the 2-frame rule (eyes → brows → mouth)?
- [ ] Were the 6 universal expressions clear, or should I spend more time on specific ones?
- [ ] What would I change next time?