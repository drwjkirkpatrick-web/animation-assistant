# Lesson Plan 4: The 12 Principles of Animation — Arcs with Kasa the Green Turtle

**Module Reference:** Prompt 4 — 04-principle-explainer.md  
**Duration:** 75 min  
**Age Group:** 12-17  
**Animation Tool:** Scratch (beginner), Krita (intermediate extension), Blender (advanced extension)  

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Animation Principles & Motion Theory |
| Core Competency | Critical Thinking & Problem Solving, Creativity & Imagination |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:

1. **Name** at least 6 of the 12 Principles of Animation and explain the **Arcs** principle in plain language using a real-world analogy.
2. **Demonstrate** the Arcs principle by animating **Kasa the Green Sea Turtle** swimming in a curved path through a coral reef, using at least two tools (Scratch + one other).
3. **Apply** the "Try It Now" physical demo to their own body and explain why nothing in nature moves in a straight line.

## Key Inquiry Question

> Kasa the Green Turtle's flippers trace wide, graceful curves through the water.
> Why does **nothing in nature move in a straight line** — and how do we put that
> into our animations?

---

## Resources

- Scratch (for the main hands-on project)
- Krita (for intermediate extension — drawing the arc path frame by frame)
- Blender (for advanced extension — 3D curve path animation, optional)
- Projector for principle demos
- Reference video of a green sea turtle swimming (Watamu Marine National Park footage — search "green sea turtle swimming slow motion")
- Printed "12 Principles" reference sheet (one per learner or one per group)
- Tennis ball or small rubber ball (for the physical demo)
- Paper and pencils for sketching arc paths
- Optional: Raspberry Pi with Scratch Desktop

---

## Local Context: Kenyan Ocean Animal

**Animal:** Green Sea Turtle (*Chelonia mydas*) — **Kasa** in Swahili  
**Habitat:** Seagrass beds of Watamu Marine National Park (Kilifi County) and
Diani-Chale Marine Reserve (Kwale County). Green sea turtles graze on seagrass
and nest on beaches at Watamu and Lamu. They are a flagship species for Kenya's
marine conservation efforts.  
**Why this animal?** A swimming green sea turtle is the **perfect arcs teacher**.
Its front flippers trace wide, sweeping curves with every stroke — you can see
the arc clearly in slow-motion footage. The turtle's body also rises and falls
in gentle arcs as it glides between strokes, rather than moving in a straight
line. This makes the Arcs principle immediately visible and relatable. The
reference guide categorises the green sea turtle under "Smooth Swimming (Arcs +
Timing)" — the ideal animal for this principle.  
**Conservation note:** Green sea turtles are **Endangered** (IUCN Red List). In
Kenya, they face threats from plastic pollution (turtles mistake plastic bags for
jellyfish), fishing net bycatch, and habitat loss as nesting beaches are
developed. KWS runs a nesting protection program at Watamu — rangers monitor
beaches during nesting season (March-June), relocate eggs to safe enclosures if
needed, and protect hatchlings on their way to the sea. Local organisations like
Local Ocean Conservation also run turtle rescue and release programs. Learners
should know that animating Kasa is also a way to tell her conservation story.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show a 30-second slow-motion video of a green sea turtle swimming at
Watamu. Ask learners to watch the flippers:

- *"What shape do the flippers trace through the water?"* (curves / arcs / circles)
- *"Does the turtle's body move in a straight line, or does it rise and fall?"*
  (rises and falls in gentle curves)
- *"What would it look like if the turtle moved in a perfectly straight line
  with stiff flippers?"* (robotic, dead, not alive)

Explain: **This is the Arcs principle — the 7th of the 12 Principles of
Animation.** Today we'll learn what it means, why it matters, see it in real
life, try it with our own bodies, and animate Kasa the Green Turtle swimming in
real arcs.

Show the full list of the 12 Principles on the board (briefly — we'll focus on
one today):

1. Squash & Stretch  2. Anticipation  3. Staging  4. Straight Ahead vs. Pose to
Pose  5. Follow Through & Overlapping Action  6. Slow In & Slow Out  7. **Arcs**
8. Secondary Action  9. Timing  10. Exaggeration  11. Solid Drawing  12. Appeal

### Step 1: Concept Introduction — The Arcs Principle Explained (15 min)

Teach the Arcs principle using the animation assistant's "Principle Explainer"
format. Walk through each section:

#### What It Means (plain language)

> **Think of throwing a ball.** When you throw a ball, it doesn't travel in a
> straight line — it curves up, reaches a peak, and curves back down. That curve
> is called an **arc**. Almost everything in nature moves in arcs: a bird's wing,
> a dolphin's jump, a turtle's flipper, your own arm when you reach for
> something. The Arcs principle says: **animate along curved paths, not straight
> ones, and your animation will look alive.**

#### Why It Matters

> If you animate something moving in a perfectly straight line, it looks robotic
> and mechanical — like a machine, not a living creature. Even a car turning a
> corner follows an arc. Straight-line movement is the #1 reason beginner
> animations look "wrong" without the learner knowing why.

#### See It In Real Life

> Watch **any Studio Ghibli film** (like *Spirited Away* or *Ponyo*) — the water,
> the hair, the fish, the characters' arms all move in beautiful arcs. Or watch
> a dolphin jump at Kisite-Mpunguti: the dolphin leaves the water in a perfect
> arc, not a straight line up and down. Even Spider-Man swinging through the city
> in *Spider-Verse* follows arcs — his web is the radius of the curve.

#### Try It Now (no software needed!)

> **Physical demo — do this right now:**
> 1. Stand up. Hold your arm out to the side.
> 2. Bring your hand to your opposite shoulder. **Don't think about it — just
>    reach naturally.**
> 3. Notice: your hand didn't travel in a straight line. It curved downward, then
>    back up. That's an arc.
> 4. Now try to do the same movement in a **perfectly straight line**. Feels
>    weird, right? That's what bad animation looks like.

Have 2-3 learners demonstrate the arm arc to the class. Everyone tries it.

#### Common Mistake

> The #1 mistake beginners make: **using `glide` blocks or keyframes that go in a
> straight line from point A to point B.** In Scratch, `glide 1 secs to x: 200 y:
> 0` moves in a straight line. To fix it, break the movement into multiple glide
> steps that trace a curve — or use the `turn` blocks to create circular motion.

**Now show the code.** Open Scratch and demonstrate the difference:

**BAD — straight line (looks robotic):**
```scratch
when [green flag] clicked
go to x: (-200) y: (0)
glide (2) secs to x: (200) y: (0)    // Straight line! No arc!
```

**GOOD — arc path (looks alive):**
```scratch
when [green flag] clicked
go to x: (-200) y: (0)
// Break the movement into an arc: rise, peak, descend
glide (0.5) secs to x: (-100) y: (50)   // Rising
glide (0.5) secs to x: (0) y: (80)      // Peak of the arc
glide (0.5) secs to x: (100) y: (50)    // Descending
glide (0.5) secs to x: (200) y: (0)     // Landing
```

Run both. The class will immediately see the difference — the arc version feels
like swimming; the straight version feels like a robot on a rail.

### Step 2: Guided Practice — Animate Kasa Swimming in Arcs (20 min)

Walk through the full turtle animation step by step.

**Setup:**

1. **Open Scratch** → New project. Delete the cat.
2. **Create the turtle sprite** → Paint a simple green sea turtle: an oval body
   (green), two flipper shapes on the sides, a small head at the front. Or search
   the Scratch sprite library for "Turtle."
3. **Make 2 costumes** → In the Costumes tab, duplicate the turtle. In the second
   costume, move the front flippers to a different angle (one up, one down) to
   simulate the swimming stroke. Name them `turtle-glide` and `turtle-stroke`.
4. **Set the backdrop** → Paint an underwater scene: blue gradient, some coral at
   the bottom (orange/purple), maybe a small fish or two for scale.

**Build the swimming animation with arcs:**

```scratch
when [green flag] clicked
// --- SETUP ---
go to x: (-220) y: (0)
switch costume to [turtle-glide]
// --- SWIM IN AN ARC ACROSS THE SCREEN ---
forever
    // Arc segment 1: dip down slightly (turtle sinks between strokes)
    glide (0.4) secs to x: (-160) y: (-20)
    switch costume to [turtle-stroke]       // Flipper stroke!
    // Arc segment 2: rise up (turtle lifts with the stroke)
    glide (0.4) secs to x: (-100) y: (20)
    switch costume to [turtle-glide]        // Gliding
    // Arc segment 3: continue rising to peak
    glide (0.4) secs to x: (-40) y: (40)
    // Arc segment 4: descend
    glide (0.4) secs to x: (20) y: (20)
    switch costume to [turtle-stroke]       // Another stroke!
    // Arc segment 5: dip down
    glide (0.4) secs to x: (80) y: (-10)
    switch costume to [turtle-glide]
    // Arc segment 6: rise again
    glide (0.4) secs to x: (160) y: (20)
    glide (0.4) secs to x: (220) y: (0)
    // Reset to start (wrap around)
    go to x: (-220) y: (0)
end
```

**Teaching points as you build:**

| Step | What to do | Why (principle) | Try this |
|------|-----------|-----------------|----------|
| 1 | Set up the turtle at the left edge | Starting position for the swim | Try starting at a different y position |
| 2 | Break the swim into 6-8 glide segments with varying y values | **Arcs** — the turtle rises and falls in a wave pattern, not a straight line | Try making the arcs bigger (y: 60 instead of 40) |
| 3 | Switch costumes between `glide` and `stroke` | **Secondary Action** — flipper movement supports the body's arc | Try removing costume switches. Does it feel stiff? |
| 4 | Vary the glide times (some 0.4s, some 0.3s) | **Slow In & Slow Out** — the turtle speeds up during a stroke and slows during a glide | Try making all glides 0.4s. Does it feel mechanical? |
| 5 | Wrap around with `go to x: -220 y: 0` | Creates a continuous swimming loop | Try adding a `turn` block so the turtle banks into the arc |

**Test it!** Click the green flag. Kasa should swim across the screen in a
graceful wave pattern — rising and falling, flippers switching between glide and
stroke positions. The path should clearly look like a series of arcs, not a
straight line.

### Step 3: Independent Practice — Kasa's Coral Reef Journey (20 min)

Learners create their own version with a specific challenge.

**Challenge: Kasa navigates the reef**

Kasa needs to swim through the coral reef at Watamu Marine National Park. There
are coral pillars in the way. Animate Kasa swimming in arcs **around** the
obstacles, not through them.

**Requirements:**
1. Add 2-3 coral obstacle sprites placed at different x/y positions on the screen.
2. Plan Kasa's path on paper first — sketch the arc path around each obstacle.
3. Implement the path in Scratch using `glide` segments that curve around the
   coral (not through it).
4. Add at least one moment where Kasa has to **dip down sharply** to avoid a coral
   pillar — this creates a dramatic arc.
5. (Bonus) Add a piece of plastic pollution drifting in the water. Kasa must arc
   **around** it — not through it. This is the conservation message.

**Path sketch template** (have learners draw this on paper first):

```
Start → arc UP over coral 1 → arc DOWN under coral 2 → 
arc AROUND plastic bag → straight glide to exit
```

**Scratch starter for the obstacle avoidance:**

```scratch
when [green flag] clicked
go to x: (-220) y: (0)
// Swim UP and over the first coral pillar
glide (0.5) secs to x: (-150) y: (80)
glide (0.5) secs to x: (-80) y: (60)
// Dip DOWN to go under the second coral
glide (0.5) secs to x: (-20) y: (-40)
glide (0.5) secs to x: (40) y: (-20)
// Arc AROUND the plastic bag (conservation moment!)
glide (0.5) secs to x: (100) y: (40)
glide (0.5) secs to x: (160) y: (20)
// Exit the reef safely
glide (0.5) secs to x: (220) y: (0)
say [Safe! Remember: plastic bags look like jellyfish to turtles.] for (4) seconds
```

**Experiment ideas:**
- Add a second turtle swimming a different arc path — they cross paths naturally
- Add slow-in/slow-out by varying glide times (shorter at the peaks of arcs,
  longer during glides)
- Use the pen blocks to have Kasa **draw** her arc path as she swims, making the
  arcs visible as trails

**Tool tips (from the principle explainer format):**

| Tool | How to apply Arcs |
|------|-------------------|
| **Scratch** (beginner) | Break movement into multiple `glide` segments with varying y-values to create a curved path. Avoid single `glide` commands — they go in straight lines. |
| **Krita** (intermediate) | Draw a light arc path on the background layer. Animate the turtle along that path, frame by frame, placing each drawing ON the arc line. Use onion skin to check spacing. |
| **Blender** (advanced) | Create a Bezier curve path. Add a "Follow Path" constraint to the turtle model. The turtle will follow the exact curve. Adjust the curve handles to control the arc shape. |

### Step 4: Sharing & Feedback (10 min)

Learners present their Kasa animation. Use the critique framework:

**Critique questions:**
1. *"Can you see the arcs? Trace Kasa's path with your finger in the air — is it
   curved or straight?"*
2. *"Does the turtle feel alive or robotic? What makes the difference?"*
3. *"Did Kasa avoid all the obstacles? Did the path feel natural?"*
4. *"Bonus: Did the plastic bag avoidance land as a conservation message?"*

**Celebration:** Highlight learners who:
- Sketched their path on paper first (good planning)
- Varied the glide times for slow-in/slow-out (advanced principle application)
- Added the conservation element (plastic bag)
- Made the arcs dramatic (big curves feel more alive)

**Connect to the 12 Principles:** Remind learners that today we focused on
**Arcs (#7)** but they also used **Slow In & Slow Out (#6)** by varying glide
times, and **Secondary Action (#8)** with the flipper costume switches. Animation
principles work together — you rarely use just one.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Principle understanding | Cannot name any of the 12 principles or explain what an arc is | Names 1-2 principles; can explain arcs vaguely but not with an analogy | Names 6+ principles; explains arcs clearly with a real-world analogy (throwing a ball, arm movement) | Names 8+ principles; explains arcs with analogy AND can explain how arcs relate to other principles (timing, slow in/out) |
| Arc animation execution | Turtle moves in a straight line; no visible curves | Turtle has slight curves but path is mostly straight or arcs are too small to notice | Turtle swims in clearly visible arcs; path rises and falls naturally | Turtle swims in smooth, dramatic arcs with varied timing (slow-in/out) AND avoids obstacles with purposeful curved paths |
| Physical demo & self-awareness | Did not participate in the physical demo; cannot relate body movement to animation | Participated in demo but cannot explain the connection to arcs | Participated in demo AND can explain why natural body movements follow arcs | Participated in demo, explained the connection, AND applied the body-awareness to their animation (e.g., traced their own arm arc as a reference path) |

---

## Extended Activity

**Homework: The 12 Principles Gallery**

Choose **one more principle** from the 12 (not Arcs). Create a 10-second Scratch
animation that demonstrates that principle using **any Kenyan ocean animal**.

Suggested pairings:
- **Squash & Stretch** → Pweza the Octopus squeezing through a gap in the coral
- **Anticipation** → Nyangumi the Humpback Whale diving deep before breaching
- **Follow-Through** → Lionfish fins trailing behind the body as it turns
- **Timing** → Papa Shinga the Whale Shark drifting slowly (heavy) vs. a small
  wrasse darting fast (light)
- **Staging** → A single clownfish lit in the foreground while the reef blurs
  behind it

Bring your animation to the next class for a "Principle Gallery Walk" — everyone
displays their animation on their screen and the class walks around trying to
guess which principle each one demonstrates.

**Conservation extension:** Add a text card at the end of your animation with one
fact about your animal's conservation status from the reference sheet.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide the full guided-practice code from Step 2; task is to run it, test it, and make ONE change (e.g., bigger arcs) | Remove the starter code; learners must plan the arc path on paper and implement it independently |
| Use only 3 glide segments instead of 6-8; focus on making the curve visible | Move to Krita: draw the arc path as a guide layer and animate frame-by-frame along the curve at 12 fps |
| Pair with a partner who understands the concept; one sketches the path, one codes it | Move to Blender: create a Bezier curve path, add a Follow Path constraint to a turtle model, and render a 5-second swim cycle |
| Focus on the physical demo and the "what it means" explanation rather than the code | Research and present on how Arcs work differently in 2D vs. 3D animation (path constraints vs. hand-drawn frames) |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the green sea turtle (Kasa) an effective example for the Arcs principle?
- [ ] Did the physical demo (arm arc) help learners feel the concept in their bodies?
- [ ] Could learners see the difference between straight-line and arc movement in Scratch?
- [ ] Did the conservation message (plastic bags = jellyfish to turtles) land, or did it feel forced?
- [ ] Was the 12-principle overview too much information at once, or was it a useful preview?
- [ ] What would I change next time?