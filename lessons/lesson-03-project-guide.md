# Lesson Plan 3: Step-by-Step Project Guide — The Bouncing Jellyfish

**Module Reference:** Prompt 3 — 03-project-guide.md  
**Duration:** 80 min  
**Age Group:** 10-14  
**Animation Tool:** Scratch (primary); Krita (extension for advanced learners)  

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Animation Techniques & Motion Principles |
| Core Competency | Creativity & Imagination, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:

1. **Follow** a structured, step-by-step project guide to create a complete bouncing animation in Scratch.
2. **Apply** the animation principles of **squash & stretch**, **timing**, and **arcs** by animating a jellyfish pulsing through the water column.
3. **Self-evaluate** their animation using a checklist of 4 questions and identify what to improve.

## Key Inquiry Question

> A jellyfish pulses by squashing its bell and pushing water out — so how do we
> animate **Tikwi the Jellyfish** bouncing through the reef so it looks like it's
> really alive?

---

## Resources

- Scratch (online at scratch.mit.edu or offline desktop)
- Projector for step-by-step demonstration
- Reference video of jellyfish pulsing (search "jellyfish swimming slow motion" — or use Watamu reef footage)
- Printed step-by-step guide (the instructions from Step 2 below, so learners can follow without looking at the projector)
- Pre-made jellyfish sprite with 3 costumes (available as a Scratch studio project, or learners draw their own)
- Optional: Krita (for advanced extension), Raspberry Pi running Scratch Desktop
- Paper and pencils for sketching the arc path

---

## Local Context: Kenyan Ocean Animal

**Animal:** Jellyfish (various species including box jellyfish and moon jellyfish) —
**Tikwi** in Swahili (informal coastal term)  
**Habitat:** Found throughout Kenya's Indian Ocean waters, especially in Mombasa
Marine National Park and Watamu Marine National Park. Jellyfish drift with ocean
currents and pulse their bells to move through the water column.  
**Why this animal?** A jellyfish's **pulsing bell** is nature's squash & stretch.
When it squeezes (squash), water shoots out and the jellyfish moves. When it
relaxes (stretch), the bell opens and it drifts. This is exactly what a bouncing
ball does — squash on impact, stretch on rebound. The tentacles also provide a
perfect opportunity to teach **follow-through** (the tentacles lag behind the
bell's movement). The project guide module's first project is the "bouncing ball"
— the jellyfish is our marine Kenyan version of that same fundamental exercise.  
**Conservation note:** Jellyfish populations are actually *increasing* in some
areas due to overfishing (fewer fish predators) and warming waters. However,
jellyfish blooms can disrupt fishing communities on the Kenya coast by clogging
nets. KWS monitors jellyfish populations as part of reef health surveys.
Learners should understand that even "simple" animals play a role in the reef
ecosystem — and that an imbalance (too many jellyfish) signals a problem.

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show a 20-second slow-motion video of a jellyfish pulsing. Ask learners:

- *"What shape does the bell make when it squeezes?"* (flattened / squashed)
- *"What shape does it make when it relaxes?"* (round / stretched tall)
- *"What do the tentacles do after the bell moves?"* (they trail behind — lag)

Explain: **This is the bouncing ball of the ocean.** The jellyfish squashes and
stretches with every pulse, just like a ball squashes when it hits the ground and
stretches when it bounces up. Today we'll follow a step-by-step guide to animate
Tikwi the Jellyfish bouncing through the reef — and in doing so, we'll learn the
three most important principles of animation: **squash & stretch**, **timing**,
and **arcs**.

### Step 1: Concept Introduction — The Project Guide Format (12 min)

Teach the structure that the animation assistant's project guide module uses.
Every project guide has the same parts:

| Section | What it tells you |
|---------|-------------------|
| **Overview** | What you'll make, what you'll learn, how long it takes |
| **Setup** | Canvas size, frame rate, layers |
| **Steps** | Numbered instructions — each has: What to do, Why (which principle), Try This (variation) |
| **Check Your Work** | 3-4 self-evaluation questions |
| **Next Challenge** | One extension to push further |
| **Export** | How to save and share |

Show today's project overview on the board:

> **Project: Bouncing Jellyfish**
> **What you'll make:** A jellyfish that pulses (squashes and stretches) as it
> floats up and down through the water.
> **What you'll learn:** Squash & Stretch, Timing, Arcs
> **Time:** ~50 minutes
> **Tool:** Scratch

Now introduce the three principles with the jellyfish:

1. **Squash & Stretch** — The bell flattens when it pulses (squash) and elongates
   when it relaxes (stretch). This makes it look alive, not like a stiff circle.
2. **Timing** — How fast the pulse happens. A slow pulse = calm, drifting
   jellyfish. A fast pulse = panicked, escaping jellyfish. Frame count controls
   this.
3. **Arcs** — The jellyfish doesn't move in a straight line. It drifts in gentle
   curves, carried by the current. We'll use a curved path, not straight up-and-down.

### Step 2: Guided Practice — Build the Bouncing Jellyfish Step by Step (25 min)

Walk through the build together. Learners follow each step.

**Setup:**

1. **Open Scratch** → New project. Delete the cat sprite.
2. **Create the jellyfish sprite** → Click "Choose a Sprite." If no jellyfish
   exists, click "Paint" and draw a simple semi-circle (the bell) with 3-4 wiggly
   lines underneath (tentacles). Use light blue or pink.
3. **Make 3 costumes** in the Costumes tab:
   - `jellyfish-normal` — round bell (default)
   - `jellyfish-squash` — flattened/wide bell (squished down)
   - `jellyfish-stretch` — tall/narrow bell (stretched up)
4. **Set the backdrop** → Choose "Underwater" or paint a blue gradient with some
   coral at the bottom.
5. **Create a variable** → Variables tab → "Make a Variable" → name it `y_velocity`.

**Now build the animation code:**

```scratch
when [green flag] clicked
// --- SETUP ---
set [y_velocity] to (0)
go to x: (0) y: (0)
switch costume to [jellyfish-normal]
// --- MAIN LOOP ---
forever
    // Apply gravity (pulls down)
    change [y_velocity] by (-0.5)
    // Move the jellyfish
    change y by (y_velocity)
    // --- SQUASH when hitting the bottom ---
    if <(y_position) < (-140)> then
        set [y_velocity] to (12)          // Bounce up
        switch costume to [jellyfish-squash]  // SQUASH on impact!
        wait (0.1) seconds
        switch costume to [jellyfish-stretch]  // STRETCH on the way up!
        wait (0.1) seconds
        switch costume to [jellyfish-normal]   // Back to normal
    end
    // --- Add a gentle side-to-side drift (ARCS, not straight line) ---
    change x by (pick random (-1) to (1))
end
```

**Step-by-step explanation (teach each as you build):**

| Step | What to do | Why (principle) | Try this |
|------|-----------|-----------------|----------|
| 1 | Set `y_velocity` to 0 and position at center | Setup — defines starting state | Try starting at y: 100 instead |
| 2 | Add `change y_velocity by -0.5` in forever loop | **Timing** — gravity controls speed. Smaller number = slower, floatier jellyfish | Change -0.5 to -1.0. What happens? |
| 3 | Add `change y by y_velocity` | Moves the jellyfish based on velocity | Try removing this line. What happens? |
| 4 | Add the bottom-hit `if` block with bounce | **Squash & Stretch** — the bell flattens on impact and stretches on rebound | Try removing the costume switches. Does it look dead? |
| 5 | Add `change x by pick random -1 to 1` | **Arcs** — adds drift so it doesn't move in a straight vertical line | Try `pick random -3 to 3`. Does it drift too much? |

**Test it!** Click the green flag. Tikwi should:
- Fall down, squashing when it hits the bottom
- Bounce back up, stretching as it rises
- Drift slightly side to side (arcs)
- Return to normal bell shape at the top of the bounce

### Step 3: Independent Practice — Customise Your Jellyfish (20 min)

Learners create their own version with a specific challenge.

**Challenge: Tikwi's Escape**

A predator (a lionfish or moray eel) is approaching! Make Tikwi pulse *faster*
to escape upward, then slow down and drift gently when safe.

**Requirements:**
1. Add a second sprite (the predator) on the left side of the screen.
2. Make the predator slowly move toward the center.
3. When the predator gets close (use `distance to` block), Tikwi should:
   - Switch to fast pulsing (increase bounce velocity)
   - Change colour to show alarm (use `change color effect by`)
4. When the predator is far away, Tikwi returns to normal slow drifting.

**Starter code for the predator sprite:**

```scratch
when [green flag] clicked
go to x: (-200) y: (0)
forever
    glide (1) secs to x: (pick random (-180) to (-50)) y: (pick random (-100) to (100))
end
```

**Starter code to add to Tikwi (inside the forever loop, before the gravity line):**

```scratch
// --- ESCAPE MODE when predator is near ---
if <(distance to [predator v]) < (100)> then
    set [y_velocity] to (y_velocity + 1)   // Extra upward push!
    change [color v] effect by (10)         // Flash with alarm colour
else
    change [color v] effect by (0)          // Calm colour
end
```

**Experiment ideas:**
- Add sound effects: a "boing" sound when Tikwi bounces (use `play sound` block)
- Add a second jellyfish with different timing (one pulses fast, one slow)
- Make Tikwi leave a trail of bubbles behind (use `stamp` or pen blocks)

### Step 4: Sharing & Feedback (10 min)

Learners present their bouncing jellyfish animation.

**Self-evaluation checklist (from the project guide format — "Check Your Work"):**

1. **Does Tikwi look alive?** The squash and stretch should be visible. If the
   bell never changes shape, it looks like a stiff circle floating — not a
   jellyfish.
2. **Is the timing right?** A calm jellyfish pulses slowly. A scared jellyfish
   pulses fast. Does the speed match the mood?
3. **Does Tikwi move in an arc?** If it only goes straight up and down, add more
   sideways drift. Real jellyfish drift with the current.
4. **Do the tentacles look like they follow the bell?** This is a bonus — if you
   animated the tentacles separately, do they lag behind the bell's movement?

**Peer critique:** After each presentation, one classmate answers: *"What is one
thing that looks great, and one thing that could be even better?"*

Celebrate effort — especially learners who experimented with timing, colour, or
sound, even if the result wasn't perfect. **Happy accidents** are part of
animation!

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Following the project guide | Cannot follow the steps; project does not run | Follows most steps but animation is incomplete or buggy | Completes all steps; jellyfish bounces with visible squash and stretch | Completes all steps AND customises with extra features (sound, colour change, second character) |
| Animation principles applied | No squash/stretch; movement is linear and stiff | Squash OR stretch is present but not both; timing is flat | Squash on impact + stretch on rebound + timing that feels natural | All three principles (squash/stretch, timing, arcs) are clearly visible AND timing changes with the situation (escape mode) |
| Self-evaluation | Cannot identify what is wrong with their animation | Identifies problems but cannot suggest fixes | Uses the 4-question checklist to identify issues and proposes fixes | Uses checklist, identifies issues, fixes them, AND helps a peer evaluate their work |

---

## Extended Activity

**Homework: Tikwi's Krita Version (for 12-14 year-olds) or Paper Flipbook (for 10-12 year-olds)**

**For Krita users:** Open Krita. Create a new animation canvas (640×480, 12 fps).
Draw Tikwi the Jellyfish in 12 frames:
- Frames 1-3: Bell squashing (impact at bottom)
- Frames 4-6: Bell stretching (rising)
- Frames 7-9: Bell normal (drifting at top)
- Frames 10-12: Bell starting to squash again (falling)

Use **onion skin** (the light ghost of the previous frame) to keep the jellyfish
consistent. Export as a GIF or MP4.

**For paper flipbook users:** Take a small notebook (or staple 12-15 pages
together). Draw Tikwi on each page, slightly changing the bell shape and position
on each page. Flip the pages with your thumb to see the animation. This is the
original "frame-by-frame" animation — no computer needed!

This connects to the next lesson (Principle Explainer) where we'll dive deeper
into **why** squash & stretch works and practice the principle with hands-on demos.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-made Scratch project with the jellyfish sprite and 3 costumes already created; task is to assemble the code blocks | Remove the starter code; learners must write the entire bouncing animation from scratch using only the principle descriptions |
| Reduce to 2 costumes (normal + squash only); remove the stretch costume | Add tentacle follow-through: create a second sprite for the tentacles that moves on a 2-frame delay behind the bell |
| Pair with a partner; one handles the code, the other tests and gives feedback | Move to Krita and do the frame-by-frame version (12 frames, 12 fps) for a deeper understanding of timing |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the jellyfish (Tikwi) an effective substitute for the bouncing ball? Did it feel local and relevant?
- [ ] Could learners follow the step-by-step guide format, or did they get lost?
- [ ] Did the squash & stretch read clearly on screen, or were the costume changes too subtle?
- [ ] Was 80 minutes enough time, or did I need to cut the independent practice short?
- [ ] What would I change next time?