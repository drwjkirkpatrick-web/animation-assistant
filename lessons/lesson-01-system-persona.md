# Lesson Plan 1: System Persona & Character Voice

**Module Reference:** Prompt 1 — 01-system-persona.md  
**Duration:** 70 min  
**Age Group:** 10-14  
**Animation Tool:** Scratch (beginner); paper & pencils for offline warm-up  

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Character Design & Performance |
| Core Competency | Communication & Collaboration, Creativity & Imagination |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:

1. **Describe** what a "persona" is in animation and how it shapes a character's voice, movement, and personality.
2. **Design** a character persona for a Kenyan Indian Ocean marine animal using Scratch, including at least two personality traits expressed through dialogue and costume changes.
3. **Appreciate** the importance of an encouraging, playful tone when helping others learn — mirroring the animation assistant's teaching philosophy.

## Key Inquiry Question

> How do we give **Pomboo the Dolphin** a personality that shows in every line she
> speaks and every move she makes?

---

## Resources

- Scratch (online at scratch.mit.edu or offline desktop version)
- Projector or large screen for demonstration
- Reference photos/video of bottlenose dolphins leaping (Watamu/Kisite-Mpunguti)
- Printed "Persona Card" template (name, species, 3 traits, favourite phrase, fear, dream)
- Pencils and paper for the warm-up sketch
- Optional: Raspberry Pi running Scratch Desktop for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Tursiops aduncus*) — **Pomboo** in Swahili  
**Habitat:** Kisite-Mpunguti Marine Reserve (Kwale County) and Watamu Marine National
Park (Kilifi County). Dolphins live in pods of 10-30 and are frequently seen leaping
and playing in the warm coastal waters.  
**Why this animal?** Dolphins are playful, energetic, and social — the perfect
embodiment of the animation assistant's teaching philosophy: *encouraging, playful,
never condescending*. A dolphin's leaping arcs also introduce the idea that
personality drives movement.  
**Conservation note:** Bottlenose dolphins face threats from fishing net bycatch,
plastic pollution, and irresponsible dolphin-watching boats. KWS regulates
dolphin-watching tourism at Kisite-Mpunguti to keep boats at a safe distance.
Learners should know that loud boat engines stress dolphins and disrupt their
communication — a good persona trait for Pomboo could be "hates loud noise."

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show a 30-second video clip of bottlenose dolphins leaping at
Kisite-Mpunguti Marine Reserve. Ask learners:

- *"What words would you use to describe this dolphin's personality?"*
- *"If this dolphin could talk, what would she sound like?"*

Write learner responses on the board (playful, energetic, friendly, curious, fast,
acrobatic…). Explain that in animation, this list of traits is called a **persona** —
the character's personality that drives everything: how she moves, how she speaks,
how she reacts to problems.

Connect to the animation assistant: *"Just like our dolphin has a personality, our
animation teaching assistant has one too — it's always encouraging, playful, and
breaks things into small steps. Today we'll learn to design character personas."*

### Step 1: Concept Introduction — What Is a Persona? (15 min)

Teach the core concept using Pomboo as the example.

**A persona has four parts:**

1. **Identity** — name, species, where they live
2. **Traits** — 3-5 personality words (playful, brave, shy, clever…)
3. **Voice** — how they talk (short sentences? big words? jokes?)
4. **Behaviour** — how they move and react

Show learners a completed Persona Card for Pomboo on the board:

| Field | Value |
|-------|-------|
| Name | Pomboo |
| Species | Bottlenose Dolphin |
| Home | Kisite-Mpunguti Marine Reserve |
| Traits | Playful, encouraging, curious, hates loud noise |
| Voice | Short, energetic sentences. Uses "!" a lot. Always cheers you on. |
| Favourite phrase | "Jump higher! You've got this!" |
| Fear | Loud boat engines |
| Dream | To teach every fish in the reef how to jump |

Now demonstrate in Scratch how a persona becomes code. Open a new Scratch project
and create a dolphin sprite (use the Scratch library "Dolphin1" or draw a simple
one). Add these blocks:

```scratch
when [green flag] clicked
go to x: (0) y: (0)
switch costume to [dolphin-a]
say [Hello! I am Pomboo the Dolphin!] for (2) seconds
say [I live at Kisite-Mpunguti Marine Reserve!] for (2) seconds
say [I love to jump and play! What is YOUR name?] for (3) seconds
ask [Type your name:] and wait
say (join [Hi ] (join (answer) [! Let's animate together!])) for (3) seconds
switch costume to [dolphin-b]
say [Jump higher! You have got this!] for (2) seconds
```

**Teaching point:** Every `say` block reflects Pomboo's persona — short,
enthusiastic, encouraging. The costume switch shows her playful movement. If we
changed the words to long, boring sentences, she wouldn't feel like a dolphin
anymore.

### Step 2: Guided Practice — Build Pomboo's Persona in Scratch (15 min)

Walk through one example together. Learners follow along step by step.

1. **Open Scratch** → Create a new project. Delete the cat sprite.
2. **Add the dolphin sprite** → Click "Choose a Sprite" → search "Dolphin" →
   select it. (If no dolphin available, use the Scratch paint editor to draw a
   simple grey oval with a tail fin and a smile.)
3. **Add two costumes** → In the Costumes tab, duplicate the dolphin and modify
   the second costume so the tail is in a different position (up vs. down). Name
   them `dolphin-up` and `dolphin-down`.
4. **Add the dialogue blocks** → Recreate the code block from Step 1 in the Code
   tab.
5. **Test it** → Click the green flag. Pomboo should introduce herself, ask for
   the learner's name, and respond enthusiastically.
6. **Add a movement loop** → After the dialogue, add a forever loop that switches
   costumes every 0.3 seconds to make Pomboo's tail wiggle:

```scratch
when I receive [start swimming]
forever
    switch costume to [dolphin-up]
    wait (0.3) seconds
    switch costume to [dolphin-down]
    wait (0.3) seconds
end
```

7. **Broadcast the message** → Add `broadcast [start swimming]` at the end of the
   green-flag script so Pomboo starts swimming after introducing herself.

**Check:** Does Pomboo's dialogue match her personality traits? Is she
encouraging and playful? If the words feel stiff, change them!

### Step 3: Independent Practice — Design Your Own Ocean Character (20 min)

Learners create their own marine character persona and animate it.

**Challenge:** Choose any Kenyan Indian Ocean marine animal. Fill out a Persona
Card (on paper), then bring it to life in Scratch with at least:
- 3 `say` blocks that show the character's personality
- 1 `ask` block that interacts with the user
- 1 costume switch for movement

**Starter code template** (learners fill in the blanks):

```scratch
when [green flag] clicked
say [______] for (2) seconds      // Greeting in character's voice
say [______] for (2) seconds      // Something about where they live
ask [______] and wait             // A question that shows their personality
say (join [______] (answer)) for (3) seconds  // Encouraging response
switch costume to [______]        // Show a movement or emotion
say [______] for (2) seconds      // Final catchphrase
```

**Animal options from Kenya's coast** (write these on the board):
- **Kasa** the Green Sea Turtle — wise, patient, slow but steady
- **Pweza** the Octopus — clever, many arms, problem-solver
- **Papa Shinga** the Whale Shark — gentle giant, biggest in the ocean
- **Samaki Dart** the Clownfish — tiny but brave, darts through danger
- **Tikwi** the Jellyfish — calm, goes with the flow, pulses gently

### Step 4: Sharing & Feedback (10 min)

Learners present their character to the class (or in pairs if time is short).

**Critique framework (3 questions):**
1. *"Can you tell what the character's personality is from the dialogue alone?"*
2. *"Does the movement match the personality?"* (A slow turtle shouldn't zip
   across the screen; a darting clownfish shouldn't float slowly.)
3. *"What is one thing you love about this character?"*

Celebrate effort and creativity. Highlight learners who tried something unusual
— a shy whale shark, a brave jellyfish — and praise the risk-taking.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Persona design | Cannot describe what a persona is; no traits listed | Lists 1-2 traits but dialogue does not reflect them | Lists 3+ traits and dialogue clearly reflects the character's personality | Traits, voice, and movement all work together; personality is vivid and consistent |
| Scratch dialogue & interaction | No working `say` blocks; character does not speak | Character speaks but no `ask`/response interaction | Character speaks, asks a question, and responds to user input with personality | Multiple interactions, branching responses, or emotional costume changes |
| Movement via costume switch | No costume change; character is static | One costume change but timing is off or doesn't fit personality | Costume switches create visible movement that matches the character | Multiple costumes, smooth timing, movement enhances the personality |

---

## Extended Activity

**Homework: Pomboo's Conservation Message**

Add a second sprite (a fish friend or a boat) to your Scratch project. Write a
short dialogue scene where Pomboo explains to her friend why loud boat engines
are dangerous for dolphins. Use at least 4 `say` blocks. This connects to the
next lesson (Tool Routing) where learners will learn to choose the right tool
for different animation jobs — just as KWS chooses the right conservation
strategy for each animal.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-filled Persona Card with only the dialogue blanked out; they fill in the words | Add a second character and create a 4-line conversation between two ocean animals with different personalities |
| Use only 2 `say` blocks and 1 `ask` block; focus on getting one interaction working | Add `if/else` logic: if the user types "sad", Pomboo responds with encouragement; if "happy", she celebrates |
| Pair with a partner who has more Scratch experience | Record actual voice lines using a phone microphone and play them as sound blocks instead of `say` text |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the dolphin (Pomboo) example engaging and relatable?
- [ ] Did learners understand the connection between personality and animation?
- [ ] Was the Scratch code accessible for beginners, or did I need to spend too long on setup?
- [ ] What would I change next time?