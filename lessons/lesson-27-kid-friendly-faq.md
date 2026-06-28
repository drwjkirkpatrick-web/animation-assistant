# Lesson Plan 27: Kid-Friendly FAQ — Answering Animation Questions Like a Pro

**Module Reference:** Prompt 27 — 27-kid-friendly-faq.md  
**Duration:** 70 min  
**Age Group:** 10-12  
**Animation Tool:** Scratch (browser, Raspberry Pi, or any computer)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Communication Through Digital Media |
| Core Competency | Communication & Collaboration |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Answer at least five common beginner animation questions in a clear, kid-friendly way (direct answer first, then explanation, then "try this").
2. Create an interactive Scratch FAQ project where an octopus character (*Pweza*) answers questions when the user clicks on different buttons.
3. Evaluate whether an answer is helpful by checking: Does it give the answer first? Is it easy to understand? Does it suggest something to try?

## Key Inquiry Question

> An octopus (*Pweza*) has eight arms and a big brain — it's the cleverest
> animal on the reef. How can we build an interactive FAQ animation where
> Pweza answers the questions that young animators actually ask?

---

## Resources

- Scratch (scratch.mit.edu) — one account per learner or pair
- Projector or large screen for demonstration
- Printed FAQ question cards (see Step 1 for the list — print one set per group)
- Reference image or video of an octopus (search "octopus camouflage color change" on YouTube — shows how octopuses are clever and responsive)
- Optional: Raspberry Pi with Scratch for offline use
- Paper and pencils for drafting answers

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus (*Pweza*)  
**Habitat:** Coral reefs and rocky areas along the entire Kenyan coast — commonly found in Watamu Marine National Park, Mombasa Marine National Park, and the Lamu archipelago. Octopuses hide in crevices in the reef (mwamba) and come out to hunt at night.  
**Why this animal?** The octopus is the reef's problem-solver. It has the largest brain of any invertebrate, can solve puzzles, open jars, and change color and texture to communicate. It's the perfect mascot for a FAQ project — an octopus is the "wise guide" who answers questions. Just as *Pweza* adapts to whatever situation it faces, a good FAQ answer adapts to the questioner's needs. The octopus's ability to change color also connects to Scratch: the character can change costumes (colors) to show different "moods" for different answers.  
**Conservation note:** Octopuses are sensitive to overfishing and reef degradation. In Kenya, they are harvested by coastal communities for food and income, but over-harvesting can deplete local populations. Sustainable fishing practices and reef protection (like the marine parks at Watamu and Mombasa) help maintain healthy octopus populations. A healthy reef needs its cleverest resident — if the octopus disappears, the reef ecosystem loses a key predator that keeps populations of crabs and small fish in balance.

---

## Lesson Development

### Introduction (10 min)

Show a short video (1-2 minutes) of an octopus solving a puzzle or changing
color to camouflage. Ask learners:
- *"What did the octopus do that surprised you?"*
- *"Why do people say octopuses are the smartest animals on the reef?"*
- *"If an octopus could talk, what kind of questions do you think it could answer?"*

Introduce the concept: **Today, Pweza the Octopus is going to be our FAQ
guide. We're going to build an interactive animation in Scratch where Pweza
answers the questions that young animators actually ask.**

Write "FAQ" on the board and explain: **FAQ = Frequently Asked Questions.**
It's a list of common questions with answers. Good FAQ answers follow a
pattern:
1. **Give the answer FIRST** (1-2 sentences — don't make them wait)
2. **Explain WHY** (1-2 more sentences, in kid-friendly language)
3. **Give a "Try this"** (an action they can take right now)

Show an example on the board:

> **Q: Do I need to be good at drawing to animate?**
> 
> **A:** No! Lots of animation styles don't need drawing at all — stop
> motion (use LEGO or clay), 3D animation (move digital models), and
> code animation (Scratch sprites) all work without drawing.
>
> **Try this:** Open Scratch and make a sprite move using only glide
> blocks — no drawing required!

### Step 1: Concept Introduction — The FAQ Answer Formula (15 min)

Divide learners into small groups (3-4 per group). Give each group a set
of printed FAQ question cards. These are real questions that kids ask
about animation:

| # | Question | Answer Summary |
|---|----------|----------------|
| 1 | "Do I need to be good at drawing to animate?" | No — stop motion, 3D, code animation all work without drawing |
| 2 | "What computer do I need to start?" | Almost anything! Scratch runs in a browser. A Raspberry Pi works too |
| 3 | "How long does it take to make an animation?" | Longer than you think! A 3-second bounce = 30 min. Patience is key |
| 4 | "Why does my animation look janky/jittery?" | Usually: inconsistent spacing, too few frames, or no easing |
| 5 | "How do I get better at animation?" | Practice every day, study reference, get feedback, redo old work |
| 6 | "Can I animate on my phone?" | Yes! Stop Motion Studio and FlipaClip both work on phones |
| 7 | "What FPS should I use?" | Start at 12 FPS (classic cartoon look). Move to 24 for smoother results |
| 8 | "Can I make money from animation?" | Yes — YouTube, freelance, commissions. But start by making what you love |

For each card, the group practices writing the answer using the formula:
**Answer first → Explain why → Try this.** Give them 5 minutes to draft
answers to 2-3 questions on paper.

The teacher walks around and checks: *"Does the answer come first? Is it
kid-friendly? Is there a 'try this'?"*

Share 2-3 group answers with the whole class. Celebrate clear, direct
answers and gently redirect answers that bury the main point.

Now show the class how this becomes a Scratch project. *Pweza* the octopus
will be the guide. When the user clicks a question button, Pweza changes
color (costume) and speaks the answer.

### Step 2: Guided Practice — Build the FAQ Scratch Project (15 min)

Walk the class through building the first FAQ entry together. Open Scratch
and follow these steps:

**Step A: Create the Octopus Character (Pweza)**

1. Click "Choose a Sprite" → search for "Octopus." If no octopus sprite is
   available, use the Paint Editor to draw a simple octopus:
   - A large circle for the head (purple or reddish-brown)
   - 4-5 wavy lines below for tentacles
   - Two white circles with black dots for eyes
2. Name the sprite "Pweza."
3. Create 3 costumes by duplicating and changing the color:
   - Costume 1: "normal" (purple) — for general answers
   - Costume 2: "happy" (pink) — for positive answers
   - Costume 3: "thinking" (blue) — for technical answers

**Step B: Create a Question Button**

1. Click "Choose a Sprite" → search "Button" or draw a simple rectangle.
2. Name it "Q1-Button."
3. Add text on the costume: "Do I need to draw?"
4. Position it on the left side of the stage.

**Step C: Write the Code**

For the button sprite:
```scratch
when this sprite clicked
  broadcast [ask-drawing v]

when this sprite clicked
  // Change color briefly to show it was clicked
  switch costume to [button-pressed v]
  wait (0.2) seconds
  switch costume to [button-normal v]
```

For Pweza the octopus:
```scratch
when I receive [ask-drawing v]
  // Pweza answers the question!
  switch costume to [thinking v]          // blue = technical answer
  say [No! You don't need to draw to animate.] for (3) seconds
  say [Stop motion, 3D, and code animation all work without drawing!] for (4) seconds
  switch costume to [happy v]             // pink = encouraging
  say [Try this: Open Scratch and make a sprite glide — no drawing needed!] for (5) seconds
  switch costume to [normal v]            // back to purple
```

Test it! Click the button and watch Pweza answer the question with a
color change and three speech bubbles.

Explain the pattern: **broadcast → receive → switch costume → say answer
→ say explanation → say "try this" → switch back to normal.** Every FAQ
entry follows this same pattern. Once they have one working, the rest are
just copies with different text.

### Step 3: Independent Practice — Build Your Own FAQ (15 min)

Challenge each learner (or pair) to add at least **3 more FAQ entries** to
their project. They pick questions from the card set (or make up their own)
and build:
1. A new button sprite for each question
2. A new broadcast message (e.g., `ask-computer`, `ask-time`, `ask-phone`)
3. Pweza's answer code following the same pattern

**Code template they can copy and modify:**

```scratch
// BUTTON: "What computer do I need?"
when this sprite clicked
  broadcast [ask-computer v]

// PWEZA answers:
when I receive [ask-computer v]
  switch costume to [thinking v]
  say [Almost any computer works!] for (3) seconds
  say [Scratch runs in a web browser. A Raspberry Pi can animate too.] for (4) seconds
  switch costume to [happy v]
  say [Try this: Open Scratch in your browser right now — it's free!] for (5) seconds
  switch costume to [normal v]

// BUTTON: "Can I animate on my phone?"
when this sprite clicked
  broadcast [ask-phone v]

// PWEZA answers:
when I receive [ask-phone v]
  switch costume to [normal v]
  say [Yes! Your phone is a real animation tool.] for (3) seconds
  say [Stop Motion Studio and FlipaClip are free apps for iOS and Android.] for (4) seconds
  switch costume to [happy v]
  say [Try this: Download Stop Motion Studio and film a pencil moving!] for (5) seconds
  switch costume to [normal v]

// BUTTON: "Why does my animation look janky?"
when this sprite clicked
  broadcast [ask-janky v]

// PWEZA answers:
when I receive [ask-janky v]
  switch costume to [thinking v]
  say [Usually one of three things: spacing, frame count, or easing.] for (4) seconds
  say [Things move unevenly, or there are too few frames, or no slow-in/slow-out.] for (5) seconds
  switch costume to [happy v]
  say [Try this: Turn on onion skinning to see your previous frames!] for (4) seconds
  switch costume to [normal v]
```

Learners can also add:
- A **backdrop** showing an underwater reef scene (mwamba) where Pweza lives
- **Sound effects**: a bubble sound when Pweza starts talking
- **Animation**: make Pweza's tentacles wiggle while it talks using a
  simple `repeat` + `turn` loop

```scratch
// Add tentacle wiggle while talking:
when I receive [ask-drawing v]
  switch costume to [thinking v]
  repeat (10)
    turn right (5) degrees
    wait (0.1) seconds
    turn left (5) degrees
    wait (0.1) seconds
  end
  say [No! You don't need to draw to animate.] for (3) seconds
```

### Step 4: Sharing & Peer Testing (10 min)

Learners swap computers (or share their screen) with a partner. The
partner plays the FAQ project — clicks each button, reads Pweza's answers,
and evaluates using the "3 checks":

1. **Does the answer come FIRST?** (Before the explanation?)
2. **Is it kid-friendly?** (Would a 10-year-old understand it?)
3. **Is there a "Try this"?** (An action, not just theory?)

The partner gives feedback using the sandwich method:
- ✅ What's working: *"Pweza's color change makes it clear when the answer
  changes"*
- 💡 One suggestion: *"What if the 'try this' was more specific — like
  telling them exactly which block to use?"*

The creator then makes one improvement based on the feedback.

If time allows, have 2-3 learners show their project to the whole class
on the projector. Celebrate creative answers, funny Pweza costumes, and
clear explanations.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| FAQ answer quality | Answers are unclear or missing the "answer first" pattern | Answers follow the pattern but explanations are vague or too long | Each FAQ gives the answer first, explains why in kid-friendly language, and includes a "try this" | Answers are clear, concise, and engaging; "try this" is specific and actionable; tone is encouraging throughout |
| Scratch project functionality | Project does not run; buttons don't trigger answers | At least 1 button works and Pweza gives an answer | 3+ buttons work; Pweza changes costume and speaks for each question | All buttons work; Pweza has animated movement (tentacle wiggle), sound effects, and a themed backdrop; project is polished |
| Peer feedback | Did not test a partner's project or gave no useful feedback | Tested the project but feedback was vague ("it's good") | Used the 3 checks to evaluate; gave specific "what's working" + one suggestion | Gave specific, kind, actionable feedback AND the creator used it to improve their project |

---

## Extended Activity

**Homework / Follow-up: Pweza's Conservation FAQ**

Add 2 more FAQ entries to the project — but this time about ocean
conservation, answered by Pweza:

| Question | Answer Summary |
|----------|----------------|
| "Why are sea turtles (*kasa*) important for the reef?" | Turtles eat jellyfish and seagrass — without them, jellyfish overpopulate and seagrass overgrows. Balance! |
| "What can I do to help Kenyan marine life?" | Reduce plastic use, don't touch coral when swimming, support marine parks like Watamu, share what you learn! |

This connects to the next lesson (Acting for Animation) where learners will
learn to give their characters emotions and personality — Pweza will go
from a static answer-giver to a character who FEELS things while answering.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-built Scratch project with Pweza and one button already working. They just need to add the text for 2 more questions by modifying the `say` blocks. Give them the printed answer summaries from Step 1 so they don't have to write answers from scratch. | Challenge them to add a "search" feature: a text input where the user types a keyword and Pweza answers the matching question (using Scratch's `ask and wait` block + `if answer contains` logic). Extra challenge: add a variable to track how many questions the user has asked, and have Pweza comment on it ("You've asked 3 questions — you're curious like an octopus!"). |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes? Could they write clear FAQ answers using the formula?
- [ ] Was Pweza the octopus an engaging character for this project?
- [ ] Did learners understand the broadcast/receive pattern in Scratch, or did they struggle with it?
- [ ] Were the FAQ questions relevant and interesting to the learners?
- [ ] What would I change next time?