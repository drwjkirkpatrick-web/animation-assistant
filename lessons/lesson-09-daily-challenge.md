# Lesson Plan 09: Daily Challenge Generator — Sparking Daily Practice

**Module Reference:** Prompt 09 — 09-daily-challenge.md  
**Duration:** 70 min  
**Age Group:** 10-14  
**Animation Tool:** Scratch (primary), Krita/Pencil2D (alternative), Stop Motion Studio (phone)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Animation & Motion Graphics |
| Core Competency | Creativity & Imagination; Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain what a daily animation challenge is and why short, constrained practice builds skill over time.
2. Generate and complete a self-contained 15-30 minute animation challenge focused on the **Squash & Stretch** principle using a jellyfish character.
3. Value daily creative practice and connect repeated small challenges to long-term growth.

## Key Inquiry Question

> "How does a jellyfish (*medusa*) pulse through the water — and how can we turn that into a 15-minute daily challenge that teaches squash & stretch?"

---

## Resources

- Scratch (offline or online at scratch.mit.edu) OR Krita/Pencil2D OR Stop Motion Studio on a phone
- Projector or large screen to show the jellyfish reference clip
- Short video of a jellyfish pulsing (search YouTube: "jellyfish swimming slow motion")
- Paper and pencils for learners sketching frame plans
- Optional: Raspberry Pi + camera for low-resource stop-motion setup
- Printed "Challenge Cards" (one per learner or pair) with the mission and constraints

---

## Local Context: Kenyan Ocean Animal

**Animal:** Jellyfish (Swahili: *Medusa*)  
**Habitat:** Found throughout Kenya's Indian Ocean waters — commonly seen in Watamu Marine National Park, Mombasa Marine National Park, and drifting near Diani reefs.  
**Why this animal?** The jellyfish bell naturally pulses — squashing as it expels water and stretching as it refills. This makes it the *perfect* character for teaching squash & stretch, the Monday warm-up principle in the weekly challenge rotation. Its translucent body and simple dome shape are also easy for beginners to animate.  
**Conservation note:** Jellyfish are not endangered, but they are affected by ocean plastic pollution — plastic bags drifting in the water look like jellyfish, and sea turtles (*kasa*) that eat jellyfish can die from swallowing plastic instead. KWS and local beach-cleanup groups at Watamu work to reduce plastic in the ocean. Animating a jellyfish is a chance to talk about keeping *bahari* (the ocean) clean.

---

## Lesson Development

### Introduction (8 min)

Show a 30-second slow-motion jellyfish video. Ask learners: "What shape does the jellyfish's body make when it moves? Does it stay the same shape, or does it change?"

Let 2-3 learners share what they notice. Guide them toward the idea that the bell *squashes* (flattens) when it pushes water out and *stretches* (tallens) when it refills.

Introduce the concept of a **daily challenge**: a short, focused animation exercise with clear rules and a time limit. Explain that today they will complete their first daily challenge — a Monday warm-up focused on squash & stretch, just like professional animators warm up with short exercises.

Connect to the weekly rotation: *Monday = Squash & Stretch, Tuesday = Timing & Spacing, Wednesday = Anticipation*, and so on.

### Step 1: Concept Introduction — Squash & Stretch + Challenge Format (12 min)

Teach squash & stretch using the jellyfish as the example. Draw (or display) three key shapes:

1. **Rest pose** — round dome (normal)
2. **Squash pose** — flattened, wider than tall (pushing water out)
3. **Stretch pose** — taller than wide (refilling, moving up)

Explain the golden rule of squash & stretch: **the volume stays the same.** When the bell squashes (gets shorter), it must get wider. When it stretches (gets taller), it must get thinner.

Then introduce the **challenge format** they will use:

> ### 🎬 Today's Challenge: The Pulsing Medusa
> **Principle:** Squash & Stretch  
> **Difficulty:** 🟢 Easy (warm-up)  
> **Time:** 20 minutes  
> **Tool:** Any (tips below for Scratch and Krita)
>
> ### The Mission
> Animate a jellyfish pulsing upward through the water. Show the bell squashing as it pushes water out and stretching as it refills and rises. Make it pulse at least 3 times.
>
> ### Constraints
> - Only 12 frames maximum
> - The jellyfish must change shape on every pulse (squash AND stretch — not just one)
> - Volume must stay constant: if it squashes wider, it gets shorter; if it stretches taller, it gets thinner
>
> ### Stretch Goal 🚀
> Add two tentacles that trail behind the bell with a 2-frame delay — that's your first taste of follow-through!

Show the Scratch code below and walk through it together.

**Scratch — Jellyfish Pulse (Squash & Stretch):**

```scratch
when [green flag] clicked
set [y position] to (-150)
set size to (100) %
forever
  // STRETCH phase — bell rises and elongates
  repeat (6)
    change [y position] by (10)
    set size to (80) %   // narrower = stretched
    wait (0.05) seconds
  end
  // SQUASH phase — bell flattens to push water out
  repeat (6)
    change [y position] by (-4)
    set size to (120) %  // wider = squashed
    wait (0.05) seconds
  end
end
```

> **Teacher note:** In Scratch, "set size to" scales the whole sprite uniformly, so to truly preserve volume you would use the costume editor to switch between pre-drawn squash/stretch costumes. The code above is a simplified version that changes size to *suggest* the effect. For the full effect, use the **costume-switch approach** shown in Step 2.

### Step 2: Guided Practice — Animating the Pulse Together (15 min)

Walk learners through building the jellyfish animation step by step.

**If using Scratch (costume-switch method — recommended for true squash & stretch):**

1. Open Scratch and click **Choose a Sprite** → draw your own jellyfish or pick a round character.
2. In the **Costumes** tab, create 3 costumes:
   - `rest` — a round dome (equal height and width)
   - `squash` — flattened dome (wider than tall)
   - `stretch` — tall dome (taller than wide)
3. Use this code to cycle through costumes:

```scratch
when [green flag] clicked
set [y position] to (-140)
forever
  // Stretch up
  switch costume to [stretch]
  repeat (4)
    change [y position] by (12)
    wait (0.06) seconds
  end
  // Pause at top
  switch costume to [rest]
  wait (0.1) seconds
  // Squash down slightly
  switch costume to [squash]
  repeat (3)
    change [y position] by (-6)
    wait (0.06) seconds
  end
  // Brief rest
  switch costume to [rest]
  wait (0.08) seconds
end
```

4. Press the green flag. The jellyfish should pulse upward, squash, and repeat.
5. Check: Does the bell visibly change shape? Is the volume consistent (squash is wider AND shorter; stretch is taller AND thinner)?

**If using Krita/Pencil2D:**
1. Create a new canvas. Draw the jellyfish in 3 poses: rest, squash, stretch.
2. Frame 1: rest. Frame 3: stretch (moved up). Frame 5: squash (slightly lower). Frame 7: rest (back to start position).
3. Add in-between frames (2, 4, 6) to smooth the motion.
4. Play back at 8-12 fps.

**If using Stop Motion Studio (phone):**
1. Mold a jellyfish shape from clay or cut one from paper.
2. Photograph frame 1: round shape. Frame 2: press it flat (squash). Frame 3: stretch it tall and move it up. Frame 4: round again.
3. Repeat the cycle 3 times for 12 frames total.

Have all learners press play / preview at the same time. Ask: "Who can see the squash? Who can see the stretch?"

### Step 3: Independent Practice — The 20-Minute Challenge (20 min)

Hand out or display the Challenge Card. Learners work individually or in pairs to complete the challenge within 20 minutes.

**The Challenge:**
> Animate a jellyfish (*medusa*) pulsing upward through the water. Show the bell squashing as it pushes water out and stretching as it refills and rises. Make it pulse at least 3 times.
>
> **Constraints:** Max 12 frames. Bell must change shape on every pulse. Volume stays constant.
>
> **Stretch Goal 🚀:** Add two tentacles that trail behind with a 2-frame delay (follow-through).

Walk around the room. Check for:
- Are learners changing shape, not just position? (Common mistake: moving the jellyfish up and down without changing its shape.)
- Is volume being preserved? (If the squash is wider, is it also shorter?)
- Are fast finishers attempting the stretch goal?

**Code starter for the stretch goal (Scratch):**

```scratch
// Tentacle sprite — follows the bell with a delay
when [green flag] clicked
forever
  // Wait 2 frames before following = creates delay/follow-through
  wait (0.12) seconds
  glide (0.2) secs to x: ([x position] of [jellyfish v]) y: (([y position] of [jellyfish]) - (40))
end
```

### Step 4: Sharing & Feedback (10 min)

Learners pair up and show their jellyfish animation to a partner. Each partner answers these three questions:

1. **What works?** (Name one thing that looks good — e.g., "I can really see the squash when it pushes water out.")
2. **What's one thing to try next time?** (e.g., "Make the stretch a little taller so the contrast is bigger.")
3. **Did you try the stretch goal?** (Share follow-through attempts.)

Select 2-3 learners to project their animation for the whole class. Celebrate effort, completion, and creative choices (colors, tentacle designs, extra pulses).

End with the **Tomorrow's Teaser**: "Tomorrow we tackle **Timing & Spacing** — ever noticed how a turtle (*kasa*) moves slowly because it's heavy, but a small fish darts fast because it's light? That's timing. See you tomorrow!"

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Squash & Stretch principle | Jellyfish moves up/down but shape never changes | Shape changes but volume is inconsistent (squashes without getting wider) | Bell visibly squashes (wider+shorter) and stretches (taller+thinner) with consistent volume | Volume is consistent AND timing of squash/stretch feels natural and rhythmic |
| Challenge completion within time limit | Does not complete a pulsing animation | Completes animation but only 1-2 pulses or exceeds frame limit | Completes 3+ pulses within 12 frames and 20 minutes | Completes challenge with time to spare AND attempts stretch goal |
| Understanding daily challenge concept | Cannot explain what a daily challenge is | Explains that challenges are short exercises but not why constraints help | Explains that short, constrained daily practice builds skill over time and names the principle focused on | Explains the concept AND connects it to the weekly rotation (Monday = squash & stretch) and future principles |

---

## Extended Activity

**Home Challenge:** Create a **Tuesday challenge card** for yourself — focused on **Timing & Spacing**. Pick any Kenyan ocean animal (turtle = slow/heavy, clownfish = fast/light) and write a mission with 2-3 constraints. Animate it for 20 minutes at home. Bring it to the next class to share.

**Conservation connection:** Draw or animate a scene where a sea turtle (*kasa*) mistakes a plastic bag for a jellyfish. This connects squash & stretch practice to the real threat plastic pollution poses to turtles in Watamu Marine National Park.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Start with just 2 poses (rest + squash) and 6 frames. Provide a pre-drawn jellyfish sprite they can import into Scratch. Reduce to 2 pulses. | Attempt the stretch goal (trailing tentacles with delay). Try the challenge in Krita with hand-drawn frames instead of Scratch. Add a second jellyfish pulsing at a different rhythm (timing variation). |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the jellyfish example engaging? Did they connect it to squash & stretch?
- [ ] Did learners understand the daily challenge concept and the weekly rotation?
- [ ] Was the 20-minute time limit realistic, or did learners need more/less time?
- [ ] What would I change next time?