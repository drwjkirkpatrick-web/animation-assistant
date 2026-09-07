# Lesson Plan 54: Micro-Expressions & Subtle Performance — The Details That Matter

**Module Reference:** Prompt 54 — 54-micro-expressions.md  
**Duration:** 80 min  
**Age Group:** 14-17  
**Animation Tool:** Krita (frame-by-frame), Scratch (simplified)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Advanced Facial Animation & Subtle Performance |
| Core Competency | Creativity & Imagination, Communication & Collaboration |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Identify** 6 micro-expressions (half-blink, micro-squint, suppressed smile, lip press, nostril flare, jaw clench) and their emotional meanings.
2. **Animate** a micro-expression lasting 2-4 frames that reveals a hidden emotion.
3. **Create** a character performance where the character pretends one emotion but a micro-expression leaks the true feeling.

## Key Inquiry Question

> What is **Pweza the Octopus** REALLY feeling when she says "I'm fine" — and how can a 3-frame half-blink tell the audience she's lying?

---

## Resources

- Krita or Scratch (for frame-by-frame facial animation)
- Phone camera (for recording your own micro-expressions)
- Mirror (for studying your own face)
- Reference: Dr. Paul Ekman's micro-expression research (simplified for class)
- Character designs from Lesson 30 (reuse ocean animal characters)
- Optional: Raspberry Pi with Krita

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus (*Octopus cyanea*) — **Pweza** in Swahili  
**Habitat:** Coral reefs throughout Kenya's marine parks.  
**Why this animal?** Octopuses are masters of disguise — they change color and texture to hide what they really are. This makes them the perfect metaphor for micro-expressions: the character shows one thing on the surface, but a tiny flash reveals the truth underneath. Pweza says "I'm fine" but a half-blink reveals she's actually worried about the plastic in the reef.  
**Conservation note:** Octopuses face pressure from overfishing and reef degradation. They are important predators keeping reef ecosystems balanced.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Ask learners to record themselves on their phone saying "I'm fine, everything is great" — but THINK about something that worries them. Play it back in slow motion.

Ask: *"Can you see anything in your face that betrays your words? A tiny eye movement? A lip press? That's a micro-expression — a 2-4 frame flash of true emotion."*

Explain: *This is the advanced companion to Module 33 (big expressions). Module 33 covered the 6 universal emotions: happy, sad, angry, scared, surprised, disgusted. Today we cover the SUBTLE stuff — the half-blinks and suppressed smiles that make a character feel like a real person with an inner life.*

### Step 1: The 6 Micro-Expressions (20 min)

| Micro-Expression | What It Looks Like | Duration | Meaning |
|-----------------|-------------------|----------|---------|
| Half-Blink | Lid drops 60% (not 100%), then rises | 1-2 frames down, 1-2 up | Skepticism, doubt, processing |
| Micro-Squint | Barely visible narrowing of eyes | 2-3 frames | Suspicion, concentration |
| Suppressed Smile | Corner of mouth rises 1-2px, then controls back | 2-3 frames | Hiding joy, suppressing happiness |
| Lip Press | Lips thin slightly, press together | 2-4 frames | Holding back anger, controlling response |
| Nostril Flare | Nostrils widen briefly | 1-2 frames | Anger, or attraction/interest |
| Jaw Clench | Jaw tightens slightly, neck cords visible | 2-4 frames | Tension, suppressed frustration |

**Timing is everything:** Micro-expressions are 2-4 frames. That's 0.08-0.16 seconds at 24fps. They are FAST. If you hold them too long, they become regular expressions.

**The "mask and leak" principle:**
- Character puts on a mask (pretends to be fine)
- A micro-expression LEAKS through the mask for 2-3 frames
- The mask returns
- The audience subconsciously registers the leak
- Result: the audience knows the character is lying without knowing HOW they know

### Step 2: Animating a Half-Blink (20 min)

**Animate Pweza the Octopus doing a half-blink:**

In Krita, draw 5 frames:
```
Frame 1: Normal eyes (fully open) — the "mask"
Frame 2: Lids drop to 60% — the micro-expression STARTS
Frame 3: Lids at 60% — the micro-expression PEAKS (only 1 frame!)
Frame 4: Lids rising back — the micro-expression ends
Frame 5: Normal eyes again — the mask returns
```

```scratch
// In Scratch, use costume switching for micro-expressions
when [green flag] clicked
switch costume to [pweza-normal]       ← The mask: "I'm fine"
say [I'm fine, everything is great.] for (2) seconds

// Micro-expression: half-blink (FAST — only 0.2 seconds total)
wait (0.5) seconds                       ← After speaking, a pause
switch costume to [pweza-halfblink-60]   ← Lid drops to 60%
wait (0.08) seconds                      ← 1 frame at 12fps
switch costume to [pweza-halfblink-peak] ← Peak of doubt
wait (0.08) seconds                      ← 1 frame
switch costume to [pweza-normal]         ← Mask returns
say [Really, don't worry about me.] for (2) seconds
```

**Key teaching:** The half-blink takes only 3 frames (0.24 seconds at 12fps). It's barely visible — but the audience FEELS it. They know Pweza is worried, even if they can't articulate why.

### Step 3: The Mask-and-Leak Performance (20 min)

**Challenge:** Animate a character saying one thing while a micro-expression reveals the opposite.

**Scenario options:**
1. **Pweza the Octopus** says "The reef is beautiful today" but a micro-squint reveals she's worried about plastic pollution
2. **Kasa the Turtle** says "I'm not scared of the nets" but a lip press reveals she's terrified
3. **Pomboo the Dolphin** says "I don't mind the boat noise" but a nostril flare reveals anger

**Steps:**
1. Record or write the dialogue
2. Animate the "mask" expression (the pretended emotion)
3. Insert ONE micro-expression (2-4 frames) at a key moment
4. Return to the mask
5. Play it back — does the audience feel the lie?

**Checklist:**
- [ ] Character has a clear "mask" expression (pretended emotion)
- [ ] One micro-expression is inserted (2-4 frames only)
- [ ] Micro-expression is the OPPOSITE emotion from the mask
- [ ] Mask returns immediately after the leak
- [ ] The timing feels natural (not forced)

### Step 4: Sharing & Feedback (10 min)

Show animations to the class. Ask the audience (without telling them what to look for):
- *"What is this character really feeling?"*
- *"Did anything feel 'off' about their performance?"*

If the audience picks up on the hidden emotion → success! The micro-expression worked subconsciously.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Micro-Expression Knowledge | Cannot name any | Names 1-2 | Names 3+ with meanings | Names all 6 + knows timing + knows when to use each |
| Animation Timing | Micro-expression too long (regular expression) | Too short (invisible) | 2-4 frames — visible but fleeting | Perfect timing + varies speed for different emotions |
| Mask-and-Leak | No contrast between mask and leak | Leak is same emotion as mask (no contrast) | Clear contrast: mask = one emotion, leak = opposite | Full performance: mask + leak + return to mask + audience feels the lie |

---

## Extended Activity

**Conservation Two-Face:** Animate a character giving a speech about ocean conservation. They say "we must protect the reef" with a confident smile (mask), but insert a suppressed smile when they mention that their organization is actually helping — revealing genuine joy leaking through the professional mask. This shows that micro-expressions aren't just for lies — they reveal genuine feelings people try to hide, including positive ones.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Focus on ONE micro-expression (half-blink is easiest) | Combine 2 micro-expressions in one performance (half-blink + lip press) |
| Use Scratch (costume switching is simpler than drawing) | Use Krita: draw subtle lid changes frame by frame (only 1-2px movement) |
| Hold the micro-expression for 4-5 frames (more visible) | Try 2-frame micro-expressions at 24fps (extremely subtle, very advanced) |
| Provide pre-drawn expression frames to arrange | Record yourself doing micro-expressions, study frame by frame, then animate |

---

## Teacher Reflection

- [ ] Did learners understand the difference between micro-expressions and regular expressions?
- [ ] Were the 2-4 frame flashes visible enough to register but subtle enough to feel "micro"?
- [ ] Did the mask-and-leak exercise work? Could the audience feel the hidden emotion?
- [ ] Was the octopus metaphor (disguise + reveal) effective for teaching this concept?