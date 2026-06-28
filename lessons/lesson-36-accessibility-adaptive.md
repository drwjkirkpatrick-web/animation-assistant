# Lesson Plan 36: Accessibility & Adaptive Animation — Animation for Everyone

**Module Reference:** Prompt 36 — 36-accessibility-adaptive.md
**Duration:** 75 min
**Age Group:** 10-17
**Animation Tool:** Scratch + Stop Motion Studio (dual tool lesson)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Performing Arts — Animation and Digital Storytelling |
| Core Competency | Communication & Collaboration, Digital Literacy, Creativity & Imagination |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Identify at least three accessibility barriers in animation (motor, visual, cognitive) and describe an adaptive solution for each.
2. Use Scratch and/or Stop Motion Studio to create an accessible animation of a clownfish (Samaki Dart) that works for diverse abilities — using large shapes, high contrast, simple controls, or tactile materials.
3. Demonstrate empathy and inclusion by designing an animation workflow that a peer with different abilities could use successfully.

## Key Inquiry Question

> How can we make sure EVERYONE in our class can animate Samaki Dart the clownfish — whether they have trouble holding a pen, seeing small details, or staying focused — because animation is for everyone?

---

## Resources

- Scratch (offline or online at scratch.mit.edu) — block-based, no typing needed
- Stop Motion Studio (free app on phone/tablet) — tactile, physical animation
- Clay, LEGO, or paper cut-outs for physical animation (for stop motion)
- Bright colored paper and markers (high contrast materials)
- Tablets or phones with touchscreen (if available)
- Projector or large screen for demonstration
- Reference photos of clownfish (Samaki Dart) — bright orange with white stripes
- Optional: adaptive stylus or large-handle pen
- Optional: noise-cancelling headphones for sensory-sensitive learners
- Optional: Color Oracle (free software) for color-blindness simulation
- Optional: Raspberry Pi running Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Clownfish / Anemonefish (Samaki Dart)
**Habitat:** Coral reefs along Kenya's entire coastline — Mombasa Marine National Park, Malindi Marine National Park, Watamu Marine National Park, and Kisite-Mpunguti Marine Reserve. Clownfish live among sea anemones in shallow reef waters.
**Why this animal?** The clownfish is the PERFECT accessible animation character:
- **Simple shape:** An oval body with fins — easy to draw with large brushes, easy to sculpt in clay, easy to cut from paper. No complex anatomy required.
- **Bright, high-contrast colors:** Orange body with white stripes — naturally high contrast, visible to learners with low vision, and distinguishable even with some types of color blindness (orange/white has strong luminance contrast).
- **Small and friendly:** A character that feels approachable, not intimidating — perfect for learners who may feel anxious about animation.
- **Simple movement:** Darting and hovering — basic motion that can be achieved with just a few frames or simple Scratch blocks.
**Conservation note:** Clownfish depend on healthy coral reefs and sea anemones. Kenya's coral reefs are threatened by bleaching (caused by warming oceans), overfishing, and plastic pollution. KWS supports reef restoration projects at marine parks along the coast. When animating Samaki Dart, learners can tell stories about protecting coral reefs (mwamba wa makorali) so clownfish have a home.

---

## Lesson Development

### Introduction (8 min)

Ask the class: "If someone in our class had trouble holding a pen, or couldn't see small things on a screen, or lost focus easily — could they still animate? Should they be able to?"

Explain the core philosophy: **Animation is for everyone. If a kid wants to animate, there is a way. Adaptive animation is about ACCESS, not about making it easier — it's about making it POSSIBLE.**

Introduce three categories of accessibility needs (keep it positive, not clinical):

| Need Type | Example Challenge | Adaptive Approach |
|-----------|------------------|-------------------|
| Motor / Physical | Difficulty holding a pen or using a mouse | Touchscreen, large brushes, stop motion with clay, Scratch blocks (no drawing) |
| Visual | Low vision or color blindness | High contrast, large shapes, pixel art, stop motion (physical objects), color-blind safe palettes |
| Cognitive / Sensory | ADHD, autism, sensory sensitivity | Short projects, timer work, predictable workflow, written step-by-step instructions |

Introduce today's character: Samaki Dart the clownfish — a simple, bright, high-contrast character that is naturally accessible. "Today we'll learn how to make animation possible for EVERYONE, using Samaki Dart as our character."

### Step 1: Concept Introduction — Adaptive Approaches & Tool Features (15 min)

Walk through the adaptive approaches for each need type, using Samaki Dart as the example character.

**Motor / Physical Differences:**
- **Stop motion with clay or LEGO:** Sculpt a simple clownfish from orange clay (oval body, white stripes). No precise drawing needed — hands shape the clay. Move it slightly, capture a frame, repeat.
- **Scratch blocks (no drawing):** Use the built clownfish sprite (or a simple oval). Animation is done by dragging blocks — no pen or mouse precision required.
- **Large brush sizes:** In Krita, set brush size to 50+ pixels. Large brushes need less precision.
- **Cut-out animation:** Pre-draw clownfish body and fins as separate pieces. Move the pieces between frames instead of drawing from scratch.

**Visual Differences:**
- **High contrast:** Clownfish orange (#FF6600) on a dark blue ocean background (#003366) = strong contrast, visible to most low-vision learners.
- **Large shapes / pixel art:** Draw Samaki Dart as a 32×32 pixel sprite. Large pixels are easier to see than fine details.
- **Don't rely on color alone:** Add white stripes AND a distinct shape. If someone can't distinguish orange from another color, the stripe pattern still identifies the clownfish.
- **Stop motion:** Physical objects (clay clownfish) are easier to perceive than small screen elements.

**Cognitive / Sensory Differences:**
- **Short projects:** Today's project is 15-20 minutes — quick wins maintain engagement.
- **Predictable workflow:** Same steps, same order, every time. Write the steps on the board.
- **Written instructions:** Provide step-by-step text alongside verbal instructions. Some learners process written instructions better.
- **Timer work:** 10-minute focused sessions with short breaks.
- **Reduce visual noise:** Hide unused tools and panels. Simplify the workspace.

**Code demonstration — accessible Scratch animation of Samaki Dart:**

Show how to create a simple, accessible clownfish animation in Scratch with LARGE, CLEAR blocks and high contrast:

```scratch
when [green flag] clicked
// SAMAKI DART — Accessible Animation
// Simple, clear, high-contrast, few blocks

// Set high-contrast background
switch backdrop to [underwater dark blue]

// Clownfish starts at the left
go to x: (-200) y: (0)
set size to (150) percent  // LARGE sprite — easy to see
show

// Simple darting movement (3 darts — short project)
repeat (3)
  // Anticipation: small pull-back
  glide (0.2) secs to x: (x position - 20) y: (y position)
  // Dart forward (fast)
  glide (0.3) secs to x: (x position + 100) y: (pick random -50 to 50)
  // Brief hover
  wait (0.5) seconds
end

// Conservation message (clear, large text)
say [My home is the coral reef. Keep it clean!] for (4) seconds
```

Explain why this is accessible:
- **Large sprite (150% size):** Easy to see for low-vision learners
- **High contrast:** Orange clownfish on dark blue background
- **Few blocks:** Simple, predictable workflow — not overwhelming
- **No drawing required:** Uses a built-in or pre-made sprite
- **Short project:** Only a few blocks — achievable in 10-15 minutes
- **Clear conservation message:** Text is large and stays on screen long enough to read

### Step 2: Guided Practice — Two Paths, Same Character (15 min)

Learners choose ONE of two paths based on their preference (or the teacher assigns based on needs). Both paths animate Samaki Dart the clownfish.

**Path A: Scratch (for learners who prefer screen-based work)**

Walk through together:
1. Open Scratch. Choose or draw a clownfish sprite. To draw: orange oval, two or three white vertical stripes, a tail fin. Keep it SIMPLE — big shapes, no fine details.
2. Set the backdrop to a dark blue underwater scene (high contrast).
3. Set the sprite size to 150% (large and visible).
4. Build the script from Step 1 above. Test it.
5. Adjust: Does the clownfish dart clearly? Is it large enough to see? Could someone with low vision follow the action?

**Path B: Stop Motion Studio (for learners who prefer tactile/physical work)**

Walk through together:
1. Sculpt a simple clownfish from orange clay: oval body, press white clay stripes onto it, add a tail. OR cut a clownfish shape from orange paper and draw stripes with a white marker.
2. Set up a simple stage: a dark blue cloth or paper as the background (high contrast).
3. Place the clownfish at the left side of the stage.
4. Open Stop Motion Studio on a phone or tablet. Position the camera above or in front of the stage.
5. Capture frame 1. Move the clownfish slightly to the right. Capture frame 2. Repeat 10-15 times until the clownfish has "darted" across the stage.
6. Play back at 5-8 fps. The clownfish should appear to swim across the screen.

**Key teaching moment:** Both paths produce the SAME animation — Samaki Dart darting across the ocean. Different tools, same result. This is the heart of adaptive animation: **there is always a way.**

### Step 3: Independent Practice — Design an Accessible Animation (20 min)

Learners create their own Samaki Dart animation AND add at least one accessibility feature that makes it easier for a specific type of learner to use.

**Challenge:** Create a "Samaki Dart's Reef Home" animation that tells a short conservation story (clownfish looking for its anemone home, reef is clean, happy ending). Include at least ONE accessibility feature from the list below.

**Accessibility feature menu (choose at least 1):**

| Feature | Who it helps | How to implement |
|---------|-------------|------------------|
| Large sprite (150-200%) | Low vision | `set size to (200) percent` in Scratch, or make a bigger clay model |
| High contrast colors | Low vision, color blindness | Dark blue background + bright orange fish; test with Color Oracle |
| Audio cues | Low vision, cognitive | Add `play sound` blocks at key moments (splash, happy chime) |
| Simple blocks only (under 10) | Cognitive, learning | Keep the script short and linear — no nested loops or complex logic |
| Written step-by-step guide | Autism, dyslexia | Write out the steps on paper so someone else could follow them |
| Tactile materials (clay/paper) | Motor, visual, blind | Use stop motion with physical objects instead of screen drawing |
| Shape + pattern (not just color) | Color blindness | Give the fish distinct stripes AND a unique silhouette shape |
| Short duration (under 30 sec) | ADHD | Keep the animation to 20-30 seconds — quick win |

**Scratch starter code with accessibility features:**

```scratch
when [green flag] clicked
// SAMAKI DART'S REEF HOME — Accessible version
// Features: large sprite, high contrast, audio cues, few blocks

switch backdrop to [underwater dark blue]
go to x: (-200) y: (0)
set size to (180) percent  // ACCESSIBILITY: Large for low vision
show

// Samaki Dart looks for its anemone home
say [Where is my anemone?] for (2) seconds

// Dart right (searching)
play sound [blip]          // ACCESSIBILITY: Audio cue for movement
glide (0.4) secs to x: (0) y: (0)
wait (0.5) seconds

// Finds the anemone!
play sound [happy chime]   // ACCESSIBILITY: Audio cue for happy moment
say [There it is! My home!] for (2) seconds
glide (0.3) secs to x: (150) y: (0)

// Conservation message (large, clear, stays on screen)
say [Clean reefs = happy clownfish. Keep our ocean clean!] for (4) seconds
```

**For stop motion learners:**
1. Build a simple reef set: clay or paper anemone on the right side of the stage.
2. Animate Samaki Dart moving from left to right, "finding" the anemone.
3. Add a caption card at the end: "Keep our reef clean!" (large text, high contrast).
4. Keep it to 15-20 frames (short, achievable).

Teacher circulates and checks:
- Which accessibility feature did the learner choose? Can they explain who it helps?
- Is the animation achievable in the time given (not too complex)?
- Could a peer with different abilities follow this animation or use this workflow?

### Step 4: Sharing & Feedback — Empathy and Inclusion (10 min)

Learners present their animation AND explain the accessibility feature they added. Use this critique framework:
1. **What I see:** Describe the animation and the accessibility feature.
2. **Who does this help?** The presenter explains which type of learner their feature supports.
3. **One question:** "What if you also added…?" (e.g., "What if you added audio cues for low vision?" or "What if you made a written guide so someone else could recreate your animation?")

**Class discussion (5 min):**
- "What did you learn about making animation accessible?"
- "Was it hard to think about other people's needs? Was it rewarding?"
- "If someone in our class had trouble with [motor/visual/cognitive], which of our animations could they use?"

End with the key message: **The tool matters less than the kid's DESIRE to animate. If a kid wants to make things move, there is a way. Start with what they CAN do, not what they can't. Celebrate every frame.**

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Accessibility understanding | Cannot name any accessibility barriers or solutions | Names 1-2 barriers but cannot match solutions to needs | Identifies 3+ barriers (motor, visual, cognitive) and describes an adaptive solution for each | Identifies barriers across all categories AND explains trade-offs between different adaptive approaches |
| Accessible animation creation | Animation made but no accessibility features included | Includes 1 accessibility feature but cannot explain who it helps | Includes 1+ accessibility feature and can explain which need it addresses (e.g., "large sprite helps low vision") | Includes 2+ accessibility features from different categories AND the animation is genuinely usable by someone with that need |
| Empathy & inclusion | No consideration of others' needs; dismissive of accessibility | Acknowledges accessibility is important but doesn't apply it in practice | Designs animation with a specific peer's needs in mind; explains their choices thoughtfully | Proactively designs for multiple needs; helps a peer adapt their workflow; advocates for inclusion in the class |

---

## Extended Activity

**Homework / Follow-up project:** Create a "How to Animate Samaki Dart" guide for a specific learner. Choose a real or hypothetical peer with a specific need (motor, visual, cognitive, or sensory) and write/draw a step-by-step guide that shows them EXACTLY how to make their first clownfish animation. Include:
- Which tool to use (Scratch, stop motion, Krita) and why it fits their need
- Step-by-step instructions (written clearly, 1-2 sentences per step)
- What to do if they get stuck
- An encouraging message: "You CAN do this!"

**Conservation connection:** Research one action KWS or local communities take to protect Kenya's coral reefs. Add this as a fact card or dialogue in your animation: "Did you know? KWS supports reef restoration at [marine park name]. Healthy reefs mean happy clownfish!"

**Advanced option:** Use Color Oracle (free software) to test your animation for color blindness. Adjust the colors if needed so the clownfish is distinguishable in all color blindness types. Document what you changed and why.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Focus on Path B (stop motion with clay/paper). Tactile animation needs less fine motor control and is immediately accessible. Provide pre-cut clownfish shapes. Provide a written step-by-step card with 5 simple steps. Keep the animation to 10 frames. | Design an animation workflow that works for MULTIPLE need types simultaneously (e.g., a stop motion animation with audio narration for visual impairment AND a written guide for cognitive support). Research and test Color Oracle. Create a class "accessibility guide" that documents all the adaptations available. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Samaki Dart clownfish a good accessible character? Did its simple shape and bright colors help?
- [ ] Did learners genuinely engage with empathy and inclusion, or was it just an exercise?
- [ ] Were both paths (Scratch and stop motion) viable in my classroom setting?
- [ ] Did any learner discover an accessibility need of their own during this lesson?
- [ ] What would I change next time?