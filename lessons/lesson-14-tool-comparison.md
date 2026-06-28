# Lesson Plan 14: Tool Comparison — Choosing the Right Animation Tool

**Module Reference:** Prompt 14 — 14-tool-comparison.md  
**Duration:** 75 min  
**Age Group:** 12-16  
**Animation Tool:** Scratch + Stop Motion Studio + Krita (compare three; use any one for the build)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Computer Science / Creative Arts & Sports |
| Sub-strand | Digital Animation Tools — Selection & Evaluation |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Compare** at least three animation tools (Scratch, Stop Motion Studio, Krita) across key properties: animation style, tweening, onion skinning, frame-by-frame, learning curve, and export format.
2. **Select** the appropriate tool for a given animation goal and justify the choice using a comparison table.
3. **Appreciate** that there is no "best" tool — only the best tool *for a specific person and project*.

## Key Inquiry Question

> "If I want to animate Samaki Dart the Clownfish darting through a coral reef, should I use Scratch, Stop Motion Studio, or Krita — and how do I decide?"

---

## Resources

- Scratch (scratch.mit.edu) — browser, any device
- Stop Motion Studio (free app — iOS/Android/Windows/Mac) + phone or webcam + modelling clay or paper cutouts
- Krita (free, open-source — Windows/Mac/Linux) + drawing tablet or mouse
- Printed comparison table template (one per learner)
- Reference image of a clownfish (simple oval body, white stripes, orange color)
- Optional: Raspberry Pi running Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Clownfish / Anemonefish (*Samaki Dart*)  
**Habitat:** Coral reefs of Mombasa Marine National Park, Malindi Marine National Park, and Watamu — lives among the stinging tentacles of sea anemones for protection  
**Why this animal?** The clownfish is the **perfect first animation character**: a simple oval body, bright orange with white stripes, and a clear signature movement — darting and hovering. It's easy to draw in Krita, simple to build as a clay puppet for Stop Motion Studio, and straightforward to code in Scratch with glides and costume switches. One character, three tools — the ideal comparison subject.  
**Conservation note:** Clownfish depend on healthy coral reefs and sea anemones. Kenya's reefs are threatened by bleaching (caused by warming oceans), overfishing, and plastic pollution. KWS and community groups in Mombasa and Watamu run reef restoration projects — growing coral fragments in nurseries and transplanting them to damaged areas. Protect the *mwamba wa makorali* (coral reef), protect the clownfish.

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show three 5-second animations of the SAME character — a clownfish darting into an anemone — made in three different tools:
1. A Scratch project (code-driven glides)
2. A Stop Motion Studio clip (clay puppet moved frame by frame)
3. A Krita frame-by-frame drawing animation

Ask: *"These are all the same fish doing the same thing. But they were made in three different tools. Which one looks most real? Which one looks most fun to make? Which would YOU want to try?"*

Tally votes on the board. Say: *"Today you'll learn how to choose the right tool — not the 'best' tool, but the best one for YOU and your project."*

---

### Step 1: Concept Introduction — The Comparison Framework (15 min)

Introduce the comparison framework from Prompt 14. Explain that a good tool comparison has:

1. **Quick Verdict** — one sentence: which tool for which type of person
2. **Comparison Table** — side-by-side features
3. **Where Each Tool Wins** — 2-3 advantages
4. **The Tiebreaker** — one deciding question

Walk through the properties that matter when comparing tools:

| Property | What it means |
|----------|--------------|
| Animation style | Code-driven, frame-by-frame drawing, or physical puppet |
| Tweening | Does the computer fill in between your keyframes? |
| Frame-by-frame | Do you draw/move every single frame yourself? |
| Onion skin | Can you see nearby frames faintly (like tracing paper)? |
| Rigging | Can you build a skeleton/puppet to move parts? |
| Export | What file formats can you save? (MP4, GIF, etc.) |
| Learning curve | Low / Medium / High — how hard to learn? |
| Best age | Which age group is it designed for? |

Show the full 3-way comparison table below and explain each row:

```markdown
### Comparison Table: Scratch vs Stop Motion Studio vs Krita

| Feature            | Scratch              | Stop Motion Studio       | Krita                    |
|--------------------|----------------------|--------------------------|--------------------------|
| Animation style    | Code-driven          | Physical (clay/paper)    | Frame-by-frame drawing   |
| Tweening           | No (manual via code) | No                       | No (drawing-focused)     |
| Frame-by-frame     | Costume switching    | Yes (core method)        | Yes (core method)        |
| Onion skin         | No                   | Yes (overlay)            | Yes (excellent docker)   |
| Rigging            | No                   | N/A (physical)           | No                       |
| Drawing tools      | Basic sprite editor  | N/A                      | Excellent brushes        |
| 3D                 | No                   | No                       | No                       |
| Export             | Screen record needed | MP4, GIF                 | MP4, GIF, image sequence |
| Learning curve     | Very low             | Very low                 | Low-Medium               |
| Best age           | 10-13                | 10-14                    | 12-16                    |
| Cost               | Free                 | Free / $5 pro            | Free                     |
```

**Where Scratch wins:** Code-curious kids who want to learn programming AND animation. Huge community for sharing. Works on any browser — even a Raspberry Pi.

**Where Stop Motion Studio wins:** Tactile learners who learn by touching and moving real objects. You can use clay, paper, or LEGO. Great for kids who say "I can't draw."

**Where Krita wins:** Kids who love to draw and want professional-quality brushes. Onion skinning is excellent. If you already love art, this feels like home.

**The Tiebreaker:** *"Do you want to CODE your fish, BUILD your fish with your hands, or DRAW your fish?"*
- Code → Scratch
- Build → Stop Motion Studio
- Draw → Krita

---

### Step 2: Guided Practice — The 15-Minute Mini-Project Test (20 min)

The best way to choose a tool is to try it. Learners spend **5 minutes in each of two tools** making the SAME thing: Samaki Dart the Clownfish darting from left to right across the screen.

**Mini-project A: Scratch (5 min)**

```scratch
when [green flag] clicked
  // ANIMATION STYLE: code-driven — we tell the fish where to go
  go to x: (-200) y: (0)
  // ANTICIPATION: small pull-back before the dart
  change [x] by (-15)
  wait (0.2) seconds
  // TWEENING (manual): glide fills in the movement
  glide (0.4) secs to x: (200) y: (0)
  // SQUASH & STRETCH via costume switch
  switch costume to [clownfish-stretched]
  wait (0.1) seconds
  switch costume to [clownfish-normal]
  // STOP in the anemone
  say [Safe in my anemone!] for (2) seconds
```

**Mini-project B: Stop Motion Studio (5 min)**

Step-by-step tool instructions:
1. Open Stop Motion Studio. Tap "New Movie."
2. Place your clownfish paper cutout (or clay figure) on the left side of the stage.
3. Tap the capture button (camera icon) — that's **frame 1**.
4. Move the fish 2 cm to the right. Tap capture — **frame 2**.
5. Move 2 cm right. Capture — **frame 3**. Repeat until the fish reaches the right side (about 10 frames).
6. Tap the onion-skin icon (overlapping squares) to see the previous frame faintly — this helps you keep movement smooth.
7. Press play. Your fish darts across!
8. Tap Export → GIF to save it.

> **Low-resource alternative:** If no phones are available, use a stack of sticky notes. Draw the fish in a slightly different position on each page. Flip the pages = same principle as stop motion.

After both mini-projects, learners answer: *"Which one felt more fun? Which one felt easier?"*

---

### Step 3: Independent Practice — Make the Choice and Build (20 min)

Learners **choose ONE tool** based on their mini-project experience and the tiebreaker question. They then build a **10-second clownfish animation** in their chosen tool with these requirements:

- The clownfish **darts** from one side to the other (anticicipation → dart → stop)
- It arrives at an **anemone** (a simple circle of wavy lines) and **hovers** (small up-down movement)
- The animation demonstrates **at least one principle**: anticipation, squash & stretch, or arcs

**For Scratch choosers — code starter with arcs (curved path):**

```scratch
when [green flag] clicked
  go to x: (-200) y: (-50)
  // ANTICIPATION
  change [x] by (-10)
  wait (0.15) seconds
  // ARCS: dart in a curve, not a straight line
  //   break the glide into 3 segments to create an arc
  glide (0.15) secs to x: (-80) y: (20)
  glide (0.15) secs to x: (20) y: (-10)
  glide (0.15) secs to x: (120) y: (30)
  // ARRIVE at anemone — hover with small loops
  forever
    change [y] by (5)
    wait (0.1) seconds
    change [y] by (-5)
    wait (0.1) seconds
  end
```

**For Krita choosers — step-by-step:**
1. File → New → set width 800, height 600, frame rate 12 FPS.
2. Draw the clownfish on the left (frame 1). Use a simple orange oval + white stripes.
3. Turn on onion skin (View → Show Onion Skin).
4. Add a new frame (Animation docker → "+" button). Draw the fish slightly right and slightly up — this creates an **arc**.
5. Repeat for 8-10 frames, tracing the onion skin to keep movement smooth.
6. Add the anemone on the right side (on a separate layer).
7. For the hover: add 4 frames with the fish moving up-down-up-down by small amounts.
8. Render → Animation → export as GIF.

**For Stop Motion Studio choosers:** Continue from the mini-project. Add an anemone made of pipe cleaners or paper. After the dart, do 4 frames of small up-down movement for the hover. Export as GIF.

---

### Step 4: Sharing & Feedback (12 min)

Learners display their animations (screen share, pass the phone, or pass the laptop). The class does a **"Tool Fair"**:

- Each learner states which tool they chose and **one sentence why**: *"I chose Krita because I love drawing and the onion skin helped me keep the arc smooth."*
- Peers respond with **"I notice…"** feedback: *"I notice your anticipation — the fish pulled back before darting. That made it feel alive."*

End with a class discussion: *"Did anyone regret their tool choice? Did anyone discover they liked a tool they didn't expect?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| **Comparison table completion** | Fills in fewer than half the cells; properties are inaccurate | Completes most cells but confuses 2+ properties (e.g., tweening vs onion skin) | Completes the full comparison table accurately for 3 tools | Completes table AND adds relevant properties not given in class (e.g., audio support, community size) |
| **Tool selection justification** | Chooses a tool but cannot explain why | States a preference ("it's fun") but does not tie it to tool properties | Justifies choice using 2+ specific tool properties (e.g., "I chose Stop Motion because I'm a tactile learner and it has onion skin") | Justifies choice using properties AND acknowledges the trade-off (e.g., "I lose tweening, but I gain hands-on control") |
| **Animation build quality** | Fish moves but no animation principles are visible | Shows one principle (e.g., the dart) but it's rough or unclear | Shows anticipation + dart + hover clearly; the fish reads as alive | Shows 3+ principles (anticipation, arcs, squash & stretch); movement is smooth and the anemone hover loops seamlessly |

---

## Extended Activity

**Homework — "Tool Hunter":** Find one animation tool NOT covered in class (e.g., Pencil2D, Synfig Studio, OpenToonz, Blender). Research it and fill in the same comparison table properties. Bring your findings next lesson — we'll build a class "Tool Wall" with all tools ranked.

**Conservation connection:** Design your clownfish animation to include a **threat** — a piece of plastic drifting toward the reef, or rising water temperature shown as the coral turning white (bleaching). Add a final frame with a conservation message: *"Linda mwamba wa makorali — protect the coral reef."* Share it with your family.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Assign them the tool that matches their mini-project preference and provide the full code starter / step list so they can follow along without getting stuck on tool navigation. Reduce the requirement to just the dart (skip the hover). | Challenge them to try all THREE tools for the 10-second animation and then write a 150-word comparison: which tool produced the best result, which was most enjoyable, and which they'd recommend to a friend their age. Introduce Synfig as a 4th option for tweening. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes — can they compare tools and justify a choice?
- [ ] Was the clownfish a good character for cross-tool comparison? Did it work equally well in all three tools?
- [ ] Did the 15-minute mini-project test help learners decide, or did it overwhelm them?
- [ ] What would I change next time? (Consider: pre-installing all tools before class, or assigning tool-stations rather than free choice.)