# Lesson Plan 25: Collaboration & Team Animation — Building Together

**Module Reference:** Prompt 25 — 25-collaboration-team.md  
**Duration:** 80 min  
**Age Group:** 12-14  
**Animation Tool:** Scratch (browser or Raspberry Pi)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Collaboration in Creative Projects |
| Core Competency | Communication & Collaboration |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Describe at least three roles in an animation team (director, animator, background artist, sound designer) and explain what each person contributes.
2. Work with a partner or small group to co-create a short Scratch animation featuring a Kenyan ocean animal, dividing tasks fairly.
3. Give and receive constructive feedback using the "start with what's working, then ask questions" method.

## Key Inquiry Question

> How do dolphins work together in a pod to hunt and play — and how can
> we work together like a pod to make a better animation than any one of
> us could make alone?

---

## Resources

- Scratch (scratch.mit.edu) — one account per team, or use Raspberry Pi desktop Scratch
- Projector or large screen to show the sample animation
- Reference video of a dolphin pod (Bottlenose Dolphins / *Pomboo*) — search "dolphin pod hunting cooperation" on YouTube
- Printed role cards (Director, Animator, Background Artist, Sound Designer) — one set per team
- Paper and pencils for storyboarding
- Optional: Raspberry Pi 4/5 with Scratch pre-installed for offline teams

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Pomboo*)  
**Habitat:** Kisite-Mpunguti Marine Reserve (Kwale County) and Watamu Marine National Park — dolphins live and hunt in pods of 10-30 individuals.  
**Why this animal?** Dolphins are the ocean's ultimate collaborators. They hunt in coordinated teams, take turns feeding, and communicate constantly — exactly how a good animation team works. Each dolphin has a role during a hunt: some herd the fish, some block the escape route, some drive the school into a tight ball. This maps perfectly onto animation team roles: the director herds the vision, the animator drives the movement, the background artist sets the scene, the sound designer adds the energy.  
**Conservation note:** Dolphins in Kenyan waters face threats from fishing nets (bycatch) and boat traffic. The Kenya Wildlife Service (KWS) regulates dolphin-watching tourism at Kisite-Mpunguti to keep boats a respectful distance away so the pods are not stressed. Always watch dolphins from a distance — never chase or surround them.

---

## Lesson Development

### Introduction (10 min)

Show the class a short video clip (1-2 minutes) of a Bottlenose Dolphin pod
hunting cooperatively — the "mud-ring feeding" or "ball-feeding" strategy
where dolphins circle a school of fish and take turns darting in to eat.

Ask learners:
- *"What do you notice about how the dolphins work together?"*
- *"Does one dolphin do everything, or do they have different roles?"*
- *"Could one dolphin catch this many fish alone?"*

Connect to animation: **One person can make a short animation, but a TEAM
makes a film.** Just like a dolphin pod, an animation team divides the work
so each person can focus on what they do best. Today, you'll work like a
dolphin pod to make an animation together.

Introduce the four roles using the role cards:

| Role | Dolphin Equivalent | What They Do |
|------|-------------------|--------------|
| Director | Pod leader — keeps the group coordinated | Decides what happens in the animation; keeps the vision; leads feedback |
| Animator | The dolphin that darts in to catch fish | Does the key character movement and frames |
| Background Artist | The dolphins that circle and set the trap | Draws the ocean, reef, and environment |
| Sound Designer | The dolphins that communicate with clicks and whistles | Finds or creates all sound effects and music |

### Step 1: Concept Introduction — The Animation Pipeline (15 min)

Explain the simplified animation pipeline that every team follows:

```
Story Meeting → Storyboard → Split the Work → Animation → Sound → Assembly → Review
```

Walk through each stage using the dolphin animation as the example:

1. **Story meeting (5 min):** The team agrees on the story. Example: *"Pomboo the dolphin swims through the reef, sees a school of fish, and does a happy jump."*
2. **Storyboard (10 min):** One person sketches 3-4 quick panels showing what happens in each shot.
3. **Split the work:** Background artist starts drawing the reef; animator starts building the dolphin sprite.
4. **Animation:** Animator creates the swimming and jumping motion.
5. **Sound:** Sound designer adds splash sounds and dolphin clicks.
6. **Assembly:** Director puts everything together in Scratch.
7. **Review:** The whole team watches it together and celebrates.

Show this Scratch starter project structure. The team will build on it
together. Each person works on their part:

```scratch
When [green flag] clicked
  // DIRECTOR sets up the scene
  switch backdrop to [underwater reef v]
  set [dolphin v] size to (60) %
  go to x: (-200) y: (0)
  
  // ANIMATOR creates the swim + jump
  repeat (10)
    glide (0.5) secs to x: (0) y: (0)  // swim across
  end
  glide (0.8) secs to x: (100) y: (120)  // jump up!
  glide (0.6) secs to x: (150) y: (0)   // splash back down
  
  // SOUND DESIGNER triggers audio
  broadcast [splash v]
  start sound [dolphin click v]
  
when I receive [splash v]
  // BACKGROUND ARTIST makes a splash effect on the water
  create clone of [splash ripple v]
```

Explain how the team splits this code: the Director assembles the main
script, the Animator writes the movement blocks, the Background Artist
designs the backdrop and splash sprite, the Sound Designer records or
finds the sound files and wires them in.

### Step 2: Guided Practice — Build the Pod Animation Together (20 min)

Divide the class into teams of 3-4. Give each team a set of role cards and
let them choose who does what (the teacher can help assign if needed).

Walk the whole class through building the first part together, step by step:

**Part A — Background Artist (5 min):**
1. In Scratch, click "Choose a Backdrop" → search "underwater" → pick one.
2. If using Raspberry Pi offline Scratch, use the Paint Editor to draw a
   simple blue ocean with a brown reef strip at the bottom.
3. Add 2-3 colorful coral shapes (mwamba wa makorali).

**Part B — Animator (5 min):**
1. Click "Choose a Sprite" → search "dolphin." If no dolphin sprite is
   available, use the Paint Editor to draw a simple dolphin: a curved
   gray-blue body, a triangle dorsal fin, and a tail fluke.
2. Name the sprite "Pomboo."
3. Add the glide blocks from the code above to make Pomboo swim from
   left to right, then jump up in an arc, then come back down.

**Part C — Sound Designer (5 min):**
1. Click the "Sounds" tab on the Pomboo sprite.
2. Click "Choose a Sound" → search "splash" → add it.
3. Search "water" or "bubble" → add a second sound.
4. Wire the sounds into the code using `start sound [splash v]` after
   the jump.

**Part D — Director (5 min):**
1. Review all parts together. Does the animation tell the story?
2. If the jump feels too fast, ask the Animator to increase the glide
   time from 0.6 to 0.9 seconds.
3. Test the project with the green flag. Celebrate the first version!

The teacher circulates during this time, helping teams that get stuck and
reminding each person to focus on their role.

### Step 3: Independent Practice — Add Your Pod's Story (20 min)

Now each team extends the animation with their own creative ideas.
Challenge: **Add a second scene where Pomboo meets another ocean animal
and they interact.**

Options:
- Pomboo meets **Kasa the Green Turtle** and they swim together
- Pomboo meets a **clownfish** (samaki) and plays tag
- Pomboo's pod works together to herd a school of fish (show 2-3 dolphin sprites cooperating)

Each team must:
1. Hold a 3-minute story meeting to agree on the new scene.
2. The storyboard artist (director can double here for small teams) sketches 2-3 panels.
3. The background artist adds a new backdrop or modifies the existing one.
4. The animator adds the new character and movement.
5. The sound designer adds at least one new sound effect.

**Code starter for a second character:**

```scratch
// When Pomboo meets Kasa the turtle
when I receive [meet turtle v]
  // Kasa sprite
  show
  go to x: (180) y: (-50)
  glide (2) secs to x: (0) y: (-50)   // Kasa swims over slowly (turtles are slow!)
  say [Karibu, Pomboo!] for (2) seconds  // "Welcome, Pomboo!" in Swahili
  glide (3) secs to x: (-200) y: (-50)  // they swim off together
```

Remind teams: **The director's job is to keep things moving. If you
disagree on an idea, the director makes the call. You can always make a
second version later.**

### Step 4: Sharing & Feedback — The Braintrust Way (10 min)

Each team shows their animation to the class (or to another team if the
class is large). Use the Pixar "Braintrust" feedback method adapted for
kids:

**Feedback rules (write these on the board):**
1. Start with what's WORKING: *"The jump arc looks really smooth — great timing!"*
2. Ask questions, don't command: *"What if Kasa swam a little slower?"* (not *"Make Kasa slower"*)
3. Be specific: *"The splash sound comes 2 frames after Pomboo hits the water"* (not *"the sound is off"*)
4. Pick only 1-2 things to improve — not a list of 10.
5. End with encouragement: *"This is a great start — the teamwork shows!"*

Each team gives feedback to one other team using these rules. The teacher
models the first feedback round so learners hear the right tone.

Celebrate every team's effort. Point out that NO animation is perfect on
the first try — even Pixar takes 3-5 years and hundreds of revisions.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Role分工 (Division of labor) | One person did most of the work; roles unclear | Roles assigned but not followed; some people idle | Each team member contributed to their assigned role | Each member excelled in their role AND helped others when needed |
| Animation quality | Dolphin does not move or movement is broken | Dolphin moves but jump arc is flat or timing feels off | Dolphin swims and jumps with a clear arc and reasonable timing | Dolphin movement is smooth with easing, and the second scene tells a clear story |
| Feedback (giving & receiving) | Did not give feedback or gave only negative comments | Gave vague feedback ("it looks good/bad") | Used "start with what's working, then ask a question" method | Gave specific, kind, actionable feedback AND used feedback to improve their own animation |

---

## Extended Activity

**Homework / Follow-up: The Conservation Podcast Animation**

Each team creates a 30-second animation about dolphin conservation in
Kenya. The story should show:
- A dolphin pod swimming happily in Kisite-Mpunguti Marine Reserve
- A threat arriving (a speeding boat, a fishing net, plastic pollution)
- A resolution (the boat slows down, a ranger removes the net, someone
  picks up the plastic)

This connects to the next lesson (Raspberry Pi & Low-Resource Animation)
where learners will explore how to make animations on limited hardware —
because conservation organizations in Kenya often use low-cost tools to
create educational content.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Work in a pair (buddy model) instead of 3-4; one person does the dolphin sprite and movement, the other does the background and sound. Provide a pre-made dolphin sprite so they focus on animation, not drawing. | Use the studio model with 5+ roles. Add a second ocean animal character with its own movement code. Try using broadcasts and variables to create a dialogue scene between two characters. Challenge: make the dolphin pod hunt cooperatively (3 dolphins, each with a different movement path). |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes? Could each team member explain their role?
- [ ] Was the dolphin pod metaphor effective for teaching collaboration?
- [ ] Did teams communicate well, or did one person dominate? How can I support better role-sharing next time?
- [ ] Was the Scratch code at the right difficulty level, or did learners spend too much time debugging?
- [ ] What would I change next time?