# Lesson Plan 19: Color Theory & Visual Design — Making Scenes Look Great

**Module Reference:** Prompt 19 — 19-color-design.md  
**Duration:** 70 min  
**Age Group:** 10-14  
**Animation Tool:** Scratch (primary) — principles transfer to Krita/Pencil2D/Blender  

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Visual Arts — Colour, Composition & Design in Animation |
| Core Competency | Creativity & Imagination, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Identify primary, secondary, and complementary colours and choose a colour scheme (complementary, analogous, or monochromatic) for a scene.
2. Apply the 60-30-10 rule and the rule of thirds to compose an underwater scene so the character is the clear focal point.
3. Use colour to communicate emotion/mood and value the natural colour design of Kenya's reef animals as inspiration.

## Key Inquiry Question

> Why does a parrotfish *pop* against the blue reef — and how can you use the same colour trick to make your animation character the star of the scene?

---

## Resources

- Laptop or Raspberry Pi with Scratch (or Krita/Pencil2D)
- Coloured pencils/paper for the off-screen planning sketch
- Printed colour wheel (one per pair) or one projected
- Reference photos: a parrotfish on a reef, a reef scene with blue water + coral
- Projector to demo the 60-30-10 split and rule-of-thirds grid

---

## Local Context: Kenyan Ocean Animal

**Animal:** Parrotfish — *Samaki** (no widely used Swahili common name; learners may call it "samaki wa rangi" — the colourful fish)  
**Habitat:** Coral reefs of Watamu, Malindi, and Mombasa Marine National Parks; it chomps coral with its beak-like mouth.  
**Why this animal?** The parrotfish is one of the most vibrantly coloured fish on the Kenyan coast — blues, greens, pinks, oranges all on one body. It is the reference document's top pick for **colour theory**. Against blue reef water its warm colours *pop* naturally — a perfect real-world example of complementary colour contrast.  
**Conservation note:** Parrotfish are vital to the reef: they scrape algae off coral and produce much of the white beach sand (*mchanga*) at Diani and Watamu. Overfishing of parrotfish damages reefs. Protecting them protects the beach itself.

---

## Lesson Development

### Introduction (8 min)

Show a parrotfish photo on the blue reef. Ask: *"Why does this fish stand out so much?"* Let learners notice the warm colours (pink/orange/green) against cool blue water. Say: *"That's not an accident — it's colour theory. Today you'll learn the rules that nature already uses, and use them in your animation."*

### Step 1: Concept Introduction — Colour, Composition & the 60-30-10 Rule (15 min)

Teach three things, kid-version (from Prompt 19):

**A. The colour wheel is a menu, not a rule.**
- Primary: Red, Yellow, Blue
- Secondary (mix two primaries): Orange, Green, Purple
- **Complementary** = opposite colours (blue ↔ orange). Use for **contrast / "pop"** ← this is the parrotfish trick.
- **Analogous** = neighbours (blue → blue-green → green). Use for **calm / nature / harmony**.
- **Monochromatic** = one colour, different brightness. Use for **mood / fog / underwater / night**.

**B. Colour = emotion.**
- Warm (red/orange/yellow) = energy, happy, danger, daytime
- Cool (blue/green/purple) = calm, sad, mysterious, cold, night, **underwater**
- Saturation: bright = important/exciting; muted = calm/background
- The parrotfish is bright (saturated) = it's the star; the background is muted blue = it recedes.

**C. The 60-30-10 rule** (prevents "rainbow chaos"):

```text
60% of scene = dominant colour   (usually background → blue water)
30%           = secondary colour  (supports → green/brown coral)
10%           = ACCENT colour     (the focal point → YOUR parrotfish)

This is WHY the parrotfish pops: it's the 10% accent against 60% blue.
```

**D. Rule of thirds:** divide the frame into a 3×3 grid; put the character on a line or where lines cross — not dead centre. (Show on projector.)

### Step 2: Guided Practice — Build a Parrotfish Scene in Scratch (18 min)

Build it together so everyone has a working colour-designed scene.

```text
STEP-BY-STEP: Parrotfish reef scene in Scratch (colour + composition)

1. Choose a Backdrop:
   Backdrops → "Underwater2" (blue water = 60% dominant colour)
   OR paint your own: fill with BLUE (60%), add green-brown coral
   shapes at the bottom (30%).

2. Add the parrotfish sprite:
   Choose a Sprite → pick a fish, OR paint one with the Costume editor:
   - Body: warm colour (orange/pink) = your 10% ACCENT
   - Add a few bright spots (green/yellow) but keep it small
   - Keep the fish SMALL so it's 10%, not 50% of the screen

3. Composition — rule of thirds:
   Set the fish's X and Y so it sits on a grid cross-point,
   NOT in the dead centre. Try X = 80, Y = 40 (upper-right third).

4. Make the fish the FOCAL POINT:
   - Background is muted/darker blue (recedes)
   - Fish is bright/saturated (advances)
   → This is complementary contrast + saturation contrast.

5. Test the silhouette: imagine the fish as solid black —
   can you still tell it's a fish? If yes = good shape. If no = simplify.

CODE (Scratch blocks) — gentle drift so we can see the colour design:

  when [green flag] clicked
  go to x: 80 y: 40
  forever
      glide 2 secs to x: 100 y: 60
      glide 2 secs to x: 80  y: 40
  end
```

Run it. The bright fish against muted blue should *pop*. If it doesn't, fix the 60-30-10 balance (usually the fish is too big or the background too bright).

### Step 3: Independent Practice — Change the Mood (20 min)

Challenge: *"Take the parrotfish scene and make THREE versions with different MOODS by changing colour only — keep the same fish and motion."*

```text
VERSION A — HAPPY/DAYTIME
  Background: bright saturated blue + green coral (analogous cool, bright)
  Fish: bright warm accent (complementary pop)

VERSION B — SPOOKY/NIGHT
  Background: dark desaturated blue, almost grey (monochromatic, dark)
  Fish: dim the colours, maybe add a pale eerie rim
  Mood = cool, dark, mysterious

VERSION C — DANGER/ENERGY
  Background: shift toward dark teal/purple
  Fish: push saturation up, maybe add a red accent
  Mood = tense (warm accent in cool dark scene = conflict)

HOW (Scratch):
  For each version, use the Backdrop editor and the
  "Fill" tool to recolour. Duplicate the backdrop first so
  you keep all three. Switch backdrops with:
    switch backdrop to [Underwater2-night]
```

Learners should SEE that the *same* animation feels different with different colour — that's colour = emotion.

### Step 4: Sharing & Feedback (9 min)

Partners show their three versions (hidden labels). Viewer guesses the mood: *"happy / spooky / danger?"* If the guess matches the intent, the colour design worked. Use the critique frame: one thing that worked, one question, one connection to the colour rule that caused the feeling.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Colour theory | Cannot name primary/complementary colours | Names primary colours; vague on schemes | Names complementary & analogous; picks a correct scheme for the scene | Explains 3+ schemes (complementary, analogous, monochromatic, triadic) and justifies the choice |
| 60-30-10 + composition | No dominant/accent split; fish centred & lost | Roughly 2 colours used; fish off-centre by accident | Clear 60-30-10 balance; fish on a thirds line; fish is the focal point | 60-30-10 + rule of thirds + silhouette passes; can explain why the fish pops |
| Mood through colour | Same colours for all versions | Changes colours but moods read the same | 3 versions with clearly different moods; viewer can identify each | 3 distinct moods AND names the colour choice (e.g., "desaturated dark blue = scary") that creates each |

---

## Extended Activity

**Homework — "Nature's colour designer":** Find a photo of another Kenyan reef animal (butterflyfish, lionfish, clownfish) and identify its colour scheme using the wheel: is it complementary? analogous? What is its 10% accent? Sketch a 60-30-10 scene plan on paper using that animal. Bonus conservation link: parrotfish make the white sand at Diani beach — find out how, and add a one-line caption to your scene: *"Protect the parrotfish — it makes our sand."* This leads into the next lesson on adding sound to make the reef feel alive.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-painted backdrop and a fish costume to recolour only; reduce to ONE mood version; use the simplified colour wheel (just complementary vs analogous) | Require all 3 mood versions + a rim-light effect (lighter outline on the fish's top edge); use Krita/Blender for real lighting; challenge: design a monochromatic "deep ocean" scene and explain the mood |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the parrotfish a compelling example of colour in nature?
- [ ] Could learners see that colour changes mood, not just decoration?
- [ ] What would I change next time?