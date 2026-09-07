# Lesson Plan 12: Showcase & Exhibition — Presenting Work with Pride

**Module Reference:** Prompt 12 — 12-showcase-exhibition.md  
**Duration:** 75 min  
**Age Group:** 10-17  
**Animation Tool:** Scratch (primary), Krita/Pencil2D (alternative), any tool learners have used

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Animation & Motion Graphics; Communication & Collaboration |
| Core Competency | Communication & Collaboration; Creativity & Imagination |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain why presenting and sharing animation work is an important part of being an animator.
2. Create a showcase presentation (studio presentation format) and an exhibition label for a finished animation using a clownfish character.
3. Value their own creative work and communicate about their process with pride and clarity.

## Key Inquiry Question

> "How does a clownfish (*samaki*) stand out on the reef with its bright colors — and how can we make our animations stand out by presenting them with context, pride, and good communication?"

---

## Resources

- Scratch or Krita/Pencil2D (learners' finished animation projects)
- Projector or large screen for the class exhibition
- Printed "Exhibition Label" cards (template provided in Step 1)
- Printed "Studio Presentation" template (template provided in Step 1)
- Paper and colored pencils for designing exhibition labels
- A classroom wall or board for the "gallery" display
- Optional: Phone to record learners presenting their work (for portfolio archive)
- Optional: Raspberry Pi + monitor for a digital gallery display in low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Clownfish (Anemonefish) (Swahili: *Samaki wa Anemone*)  
**Habitat:** Found in coral reefs along Kenya's coastline — particularly in Mombasa Marine National Park, Malindi Marine National Park, and Watamu Marine National Park. Clownfish live among the tentacles of sea anemones in shallow reef waters.  
**Why this animal?** The clownfish is one of the most recognizable fish in the ocean — its bright orange body with white stripes makes it stand out instantly on the reef. This is exactly what a great showcase does: it makes work **stand out**. The clownfish is also small but brave (it lives among stinging tentacles that would hurt other fish), which mirrors the courage it takes to present your work to others. In the animation reference guide, the clownfish is listed as the "perfect first character" because of its simple oval body and bright color — making it ideal for a showcase lesson where learners present their best work.  
**Conservation note:** Clownfish depend on healthy coral reefs and sea anemones for survival. Kenya's coral reefs (*mwamba wa makorali*) are **threatened** by coral bleaching (caused by rising ocean temperatures), overfishing, and anchor damage from boats. KWS and local organizations run **reef restoration projects** — growing coral fragments in nurseries and transplanting them to damaged reefs. When we showcase our clownfish animations, we also shine a spotlight on the reefs that need protection.

---

## Lesson Development

### Introduction (10 min)

Show two images side by side:
1. A dull, camouflaged fish blending into the reef
2. A bright orange clownfish with white stripes

Ask: "Which fish stands out more? Why?"

Learners will say the clownfish — because of its bright colors and bold pattern. Explain: "In the ocean, standing out helps the clownfish signal 'I'm here, this is my anemone.' In animation, **presenting your work with context and pride** is what makes it stand out. A bouncing ball animation is just a bouncing ball — until you tell people what principle you focused on, what was hard, and what you're proud of. Then it becomes *your* work."

Show an example of a **bad presentation**: Play a short animation silently, say nothing, walk away. Then show a **good presentation**: Play the same animation, then say:

> "This is 'Kasa's First Swim.' I made it in Scratch. I focused on timing — the turtle moves slowly to show it's heavy. The hard part was making the flippers look like they're really pushing water. I'm proud of the arc the turtle traces. Next time I'd add more bubbles."

Ask: "Which presentation made the animation feel more important? Why?"

Introduce the four showcase formats:
1. **Quick Share** — social media, friends (one-sentence description)
2. **Studio Presentation** — classroom, family (full process talk)
3. **Portfolio Entry** — long-term tracking (structured record)
4. **Exhibition Label** — like a museum! (gallery-style write-up)

Explain: "Today you will each create a **Studio Presentation** and an **Exhibition Label** for one of your finished animations, and we'll hold a class gallery exhibition at the end."

### Step 1: Concept Introduction — Showcase Formats & Artist's Voice (15 min)

Teach the four showcase formats in detail. Display the templates:

**Studio Presentation Template:**
```
Title: [name of the piece]
Tool: [software used and why you chose it]
Principle focus: [which of the 12 principles you worked on]
Challenge: [one thing that was hard and how you overcame it]
Improvement: [what you'd improve next time]
Time spent: [how long it took]
```

**Exhibition Label Template (museum-style):**
```
Title: [student-chosen name]
Animator: [name/age]
Tool: [software]
Duration: [X seconds]
Principle focus: [which of the 12]
Artist statement: [2-3 sentences in YOUR OWN WORDS about 
what you made and why]
```

**The Artist's Voice rule:** Always use your own words. If you said "I made a fish swim," use that — don't let someone else rewrite it as "I created a dynamic demonstration of aquatic locomotion." Your voice is what makes it yours.

**The Celebration rule:** Every presentation ends with a celebration of completion. Examples:
- "You turned a blank screen into something that moves. That's magic."
- "Every professional animator started with a bouncing ball. You're on the path."
- "You made something from nothing. That's what artists do."

**Demonstrate with a clownfish example:**

Show a simple clownfish animation (swimming/darting). Present it:

> **Exhibition Label:**
> Title: *Samaki Dart Goes Home*  
> Animator: [Teacher name], age [X]  
> Tool: Scratch  
> Duration: 8 seconds  
> Principle focus: Anticipation & Squash & Stretch  
> Artist statement: "I made a clownfish dart into its anemone when a shadow passes overhead. The fish pulls back first — that's anticipation — then squashes as it turns and zooms forward. I wanted to show how a small fish can be fast and brave."

**Scratch code for the clownfish dart (reference — show on screen):**

```scratch
when [green flag] clicked
set [x position] to (100)
set [y position] to (0)
// Wait, then shadow appears — fish anticipates
wait (1) seconds
// ANTICIPATION: pull back slightly
repeat (3)
  change [x position] by (-5)
  wait (0.05) seconds
end
// SQUASH: compress before the dash
switch costume to [squash]
wait (0.08) seconds
// STRETCH & DART: zoom forward into anemone
switch costume to [stretch]
repeat (5)
  change [x position] by (-30)
  wait (0.03) seconds
end
// Arrive at anemone — rest pose
switch costume to [rest]
say [Safe!] for (1) seconds
```

Explain: "This is a simple animation, but with a good presentation, it becomes a *story* — a small, brave fish protecting itself. That's what showcase skills do."

### Step 2: Guided Practice — Writing the Presentation Together (12 min)

As a class, pick one learner's completed animation (with their permission). Play it on the screen.

**Walk through the Studio Presentation template together:**

1. **Title:** Ask the learner: "What would you call this?" (Use their words. If they say "the fish one," suggest "the fish one" or help them find a slightly more descriptive name like "Swimming Fish" — but respect their voice.)
2. **Tool:** "What tool did you use? Why?" (E.g., "Scratch, because it's easy to make the fish move with blocks.")
3. **Principle focus:** "Which principle did you work on?" (Connect to previous lessons: squash & stretch, timing, arcs, etc.)
4. **Challenge:** "What was hard?" (E.g., "Making the fish not just slide — I wanted it to look like it was swimming, not gliding.")
5. **Improvement:** "What would you do better next time?"
6. **Time spent:** "How long did this take you?"

Write the completed presentation on the board.

**Now write the Exhibition Label together** using the same animation. Emphasize the **artist statement** — 2-3 sentences in the learner's own words. Ask: "In your own words, what did you make and why?"

> **Example Exhibition Label:**
> Title: *Swimming Fish*  
> Animator: [Learner name], age 12  
> Tool: Scratch  
> Duration: 6 seconds  
> Principle focus: Timing & Spacing  
> Artist statement: "I made a fish swim across the screen. I made it go fast in the middle and slow at the ends so it looks like it has weight. I like fish and I wanted to make one move."

Point out: "The artist statement doesn't need to be fancy. 'I like fish and I wanted to make one move' is a perfect artist statement. It's honest and it's theirs."

### Step 3: Independent Practice — Create Your Showcase (20 min)

Each learner chooses one finished animation (from any previous lesson or their own work) and creates:

1. **A Studio Presentation** — fill in the template (title, tool, principle, challenge, improvement, time)
2. **An Exhibition Label** — fill in the template including a 2-3 sentence artist statement in their own words
3. **Decorate the Exhibition Label** — use colored pencils to make it look like a museum plaque. Include a small drawing of their character.

Provide the printed templates. Walk around and help:
- Are learners using their **own words** in the artist statement? (Correct any overly formal language that doesn't sound like them.)
- Can they identify which principle they focused on? (Help them connect to the 12 principles from earlier lessons.)
- Are they including a **challenge** they overcame? (Every animation has a challenge — finding it is part of the presentation.)

**For learners who don't have a finished animation yet:** They can use the clownfish dart animation from Step 1 (provide the Scratch code) and create a showcase for it. Alternatively, they can create a very quick 2-frame animation right now and showcase that — "Even a 2-frame bouncing ball is a real animation that someone made."

### Step 4: Sharing & Feedback — The Gallery Exhibition (15 min)

Set up the classroom as a **gallery**:
- Learners place their decorated Exhibition Labels on their desks (or on a wall/board) with their animation playing on their screen.
- Half the class becomes **gallery visitors** and walks around viewing the work, reading the labels, and asking animators questions.
- After 7 minutes, switch: the other half becomes visitors.

**Visitors ask:**
- "What are you most proud of?"
- "What was the hardest part?"
- "Why did you choose this animal/character?"

After the gallery walk, gather the class. Select 2-3 learners to give their **Studio Presentation** to the whole class (standing up, speaking clearly, animation playing on the projector).

End each presentation with a **celebration note**:
- "You turned a blank screen into something that moves. That's magic."
- "You made something from nothing. That's what artists do."
- "Every professional animator started exactly where you are now."

Close the lesson: "Every animation deserves a moment in the spotlight. Even a 2-frame bouncing ball is a real animation that someone made. When you present your work with context and pride, you help people see it the way you see it. That's what artists do."

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Exhibition Label completion | Label is incomplete or missing artist statement | Label complete but artist statement is copied/paraphrased from teacher examples | Label complete with artist statement in learner's own words (2-3 sentences) | Label complete, own-voice artist statement, AND decorated like a museum plaque with character drawing |
| Studio Presentation delivery | Does not present or says only "I made this" | Presents but reads template mechanically without personal detail | Presents clearly, covers all template items (title, tool, principle, challenge, improvement) using own words | Presents clearly and confidently, covers all items, AND answers visitor questions thoughtfully |
| Understanding showcase purpose | Cannot explain why presenting work matters | Says "so people can see it" but not why context helps | Explains that presentation adds context (principle, process, challenge) that makes work feel meaningful | Explains the purpose AND connects it to the clownfish metaphor (standing out, being brave enough to show your work) |

---

## Extended Activity

**Portfolio Entry:** Create a portfolio entry for your showcased animation using the portfolio format:
```
Date completed: ___________
Tool: ___________
Project type: ___________
Principles demonstrated: ___________
What I learned: ___________
File name and location: ___________
Self-rating: Effort ___/5, Creativity ___/5, Execution ___/5
Goal for next project: ___________
```
Start a portfolio folder (physical or digital) and add this entry. Each future animation gets a new entry. Over time, you'll see your growth — like a turtle gliding forward, one stroke at a time.

**Conservation connection:** Create an exhibition label for a **conservation-themed animation**. Animate a clownfish returning to a restored coral reef (*mwamba wa makorali*). Research one reef restoration project in Kenya (Watamu, Mombasa, or Diani) and include a fact about it in your artist statement. Display it at school or share it online to raise awareness.

**Quick Share practice:** Write a 50-word "quick share" for social media about your animation:
> "I made [title] — a [character] that [does what]. I'm proud of [one thing]. I learned [one thing]. 🐟🎬 #AnimationKenya #Bahari"

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a fill-in-the-blank Exhibition Label template. Reduce artist statement to 1 sentence. Pair them with a partner to practice presenting before the gallery walk. | Create all 4 showcase formats (quick share, studio presentation, portfolio entry, exhibition label) for the same animation. Present to the whole class first as a model. Help a peer write their artist statement. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the clownfish metaphor effective for teaching showcase skills?
- [ ] Did learners use their **own words** in artist statements, or did they copy formal language?
- [ ] Did the gallery exhibition format feel celebratory and safe? Were all learners comfortable presenting?
- [ ] What would I change next time?