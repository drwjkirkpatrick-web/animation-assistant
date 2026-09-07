# Lesson Plan 15: Reflection & Feedback — Supporting Yourself and Others as an Animator

**Module Reference:** Prompt 15 — 15-parent-teacher-guide.md  
**Duration:** 70 min  
**Age Group:** 12-16  
**Animation Tool:** Scratch (browser) + paper reflection journal

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Life Skills |
| Sub-strand | Animation — Self-Assessment, Peer Feedback & Resilience |
| Core Competency | Communication & Collaboration, Self-Affirmation & Emotional Intelligence |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Explain** the five core principles of supporting animation learning: process over product, don't take the mouse, frustration is normal, the 12 Principles are vocabulary, and comparison kills creativity.
2. **Apply** these principles by giving constructive peer feedback using animation vocabulary and by self-assessing their own progress against their past work (not against others).
3. **Value** resilience and self-reflection as essential animator skills — recognising that struggle is part of learning, not a sign of failure.

## Key Inquiry Question

> "When Pomboo the Dolphin (*pomboo*) doesn't jump the way I imagined, how do I talk about what's wrong — and how do I help a classmate whose animation is struggling — without making anyone feel bad?"

---

## Resources

- Scratch (scratch.mit.edu) — one device per pair
- Printed "Feedback Phrase Bank" cards (see Step 1)
- Paper reflection journals (or notebooks)
- Short video of a bottlenose dolphin jumping (YouTube: "dolphin breach slow motion") — optional
- Reference image of a dolphin arc (the curve from water → air → water)
- Optional: Python on Raspberry Pi for the self-assessment tool (low-resource: use the paper version)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Pomboo*)  
**Habitat:** Coastal waters of Watamu Marine National Park and Kisite-Mpunguti Marine Reserve — often seen in pods playing and jumping near the reef  
**Why this animal?** A dolphin's jump is the perfect "gap between vision and skill" project. Every learner **imagines** a beautiful arc. But animating that arc — getting the anticipation (the deep dive before the jump), the arc trajectory through the air, and the splash impact — is genuinely hard. The moment a learner's dolphin doesn't jump like they pictured is the moment this lesson's principles come alive: frustration is normal, the 12 Principles give us the words to diagnose what's off, and comparing to your own past work (not to a nature documentary) keeps you going.  
**Conservation note:** Dolphins in Kenyan waters face threats from fishing bycatch, plastic pollution, and disturbance from unregulated boat tourism. KWS regulates dolphin-watching at Kisite-Mpunguti — boats must keep distance and avoid chasing pods. Sustainable dolphin tourism helps local communities earn income while protecting *pomboo*.

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show a 10-second video of a real dolphin breaching — a perfect arc from water to air and back.

Then show a 10-second Scratch animation of a dolphin jumping that is clearly **not perfect** — the arc is flat, the timing is off, there's no splash.

Ask: *"What's the difference? Why does the real one look amazing and this one looks… off?"*

Write learner responses: "it's too straight," "no splash," "too fast," "doesn't feel heavy."

Say: *"Today we're not fixing the dolphin. We're learning how to TALK about what's off — using the right words — and how to support ourselves and our classmates when animation gets frustrating. Because it will. And that's normal."*

Introduce **Pomboo the Dolphin** as today's character.

---

### Step 1: Concept Introduction — The Five Principles (15 min)

Teach the five core principles from the Parent & Teacher Guide, reframed for **learners supporting themselves and each other**.

| Principle | What it means for YOU as a learner |
|-----------|-----------------------------------|
| **1. Process over product** | A 2-hour struggle with a jump arc teaches more than a flashy 10-second GIF from a tutorial. Praise your own effort, not just the result. |
| **2. Don't take the mouse** | When helping a classmate, don't grab their device and fix it. Ask: "What do you think looks off?" Let them fix it themselves. |
| **3. Frustration is normal** | Animation is hard. Coming back after a break is a skill, not a weakness. If you're stuck, take 5 minutes, then try again. |
| **4. The 12 Principles are your vocabulary** | Instead of "it looks weird," say "I think the timing is off" or "it needs anticipation." The right words help you diagnose problems. |
| **5. Comparison kills creativity** | Never compare your work to a professional animation or a classmate's. Compare to your OWN past work: "My arc is better than my first attempt!" |

Introduce the **Feedback Phrase Bank** — specific phrases learners will use when giving peer feedback:

```
GOOD feedback phrases:
  "I notice your dolphin really anticipates before the jump — great wind-up!"
  "I wonder if the arc could be rounder? Right now it looks a bit flat."
  "Your timing on the splash is much better than your first version."
  "What if you added a frame where the dolphin hangs at the top of the arc?"

BAD feedback phrases (NEVER use these):
  "That looks wrong."               → too vague, no vocabulary
  "Mine is better than yours."      → comparison kills creativity
  "Let me just fix it for you."     → don't take the mouse
  "Why is it so bad?"               → shaming, not helpful
```

Show the Scratch dolphin-jump code below and walk through which principles and terms apply:

```scratch
when [green flag] clicked
  // PRINCIPLE 4: Use vocabulary to label your code
  //   ANTICIPATION: dolphin dives deep before the jump
  go to x: (0) y: (-100)
  glide (0.5) secs to x: (0) y: (-150)   // deep dive
  wait (0.2) seconds                       // hold = builds tension
  //   ARCS: jump in a curve, not a straight line
  //     break into 3 glides to create an arc shape
  glide (0.2) secs to x: (30) y: (0)
  glide (0.2) secs to x: (60) y: (80)     // peak of the arc
  glide (0.2) secs to x: (90) y: (0)
  //   IMPACT: splash on re-entry
  switch costume to [dolphin-splash]
  start sound [splash]
  wait (0.3) seconds
  switch costume to [dolphin-normal]
  //   FOLLOW-THROUGH: ripples after the splash
  repeat (4)
    change [y] by (-5)
    wait (0.1) seconds
  end
```

> **Teacher note:** Create 2 dolphin costumes: `dolphin-normal` and `dolphin-splash` (dolphin with water splashing around it). A simple gray crescent shape works for the body.

---

### Step 2: Guided Practice — Diagnose with Vocabulary (15 min)

Learners open Scratch and build the dolphin jump script above. Then, in pairs, they play their animation and **diagnose it together using only animation vocabulary**.

Walk through one example as a class:

1. Play the animation. Ask: *"Using our vocabulary, what's working?"*
   - Expected answer: *"The anticipation is good — it dives before jumping."*
2. Ask: *"What's not working yet?"*
   - Expected answer: *"The arc is too flat — the three glides make a triangle, not a smooth curve."* or *"The timing is too fast — 0.2 seconds per glide makes it look rushed."*

Give pairs 5 minutes to diagnose each other's animations using the Feedback Phrase Bank. Circulate and model the language:

- *"I notice your splash costume appears at the right moment. I wonder if the follow-through ripples could last one more repeat?"*
- *"Compare this to your first attempt — is the arc better? Yes? Then you're improving."*

**Key rule:** No one touches anyone else's device. You can point, you can suggest, you can ask questions — but **you don't take the mouse.**

---

### Step 3: Independent Practice — Reflection Journal + Fix One Thing (20 min)

**Part A: Reflection Journal (10 min)**

Each learner writes in their journal using this template (also available as a Python tool below):

```
ANIMATION REFLECTION — [Date]
Character: Pomboo the Dolphin

1. What was I TRYING to make?
   _________________________________________________

2. What actually happened?
   _________________________________________________

3. Using animation vocabulary, what is ONE thing that's off?
   (Choose from: timing, spacing, arcs, anticipation,
    squash & stretch, follow-through, staging)
   The ___________________ is off because _______________

4. Compare to my LAST animation (not someone else's):
   "My ____________ is better than last time because __________"

5. What is ONE thing I will fix next?
   I will fix: _______________________________________

6. How am I feeling? (circle one)
   Frustrated / Okay / Proud / Excited to try again
   → If frustrated: that's NORMAL. Animation is hard.
     Take a 5-minute break, then come back.
```

**Runnable Python self-assessment tool (for Raspberry Pi / learners who like code):**

```python
#!/usr/bin/env python3
# animation_reflection.py — Self-assessment journal for young animators
# Run: python3 animation_reflection.py

import datetime

def main():
    print("=" * 50)
    print("  🐬 Animation Reflection Journal 🐬")
    print("  Pomboo the Dolphin — Self-Assessment Tool")
    print("=" * 50)

    name = input("\nYour name: ")
    date = datetime.date.today().strftime("%d %B %Y")

    print(f"\nDate: {date}")
    print("Answer each question. Take your time.\n")

    trying = input("1. What were you TRYING to make?\n   > ")
    happened = input("2. What actually happened?\n   > ")

    vocab = ["timing", "spacing", "arcs", "anticipation",
             "squash & stretch", "follow-through", "staging"]
    print(f"\n3. What is ONE thing that's off? Choose from: {', '.join(vocab)}")
    term = input("   The term: > ")
    why = input("   ...because: > ")

    better = input("\n4. Compare to your LAST animation (not someone else's!)\n"
                   "   My ____ is better than last time because...\n   > ")

    fix = input("\n5. What is ONE thing you will fix next?\n   > ")

    print("\n6. How are you feeling?")
    print("   1) Frustrated  2) Okay  3) Proud  4) Excited to try again")
    feeling = input("   Choose 1-4: > ")
    feelings = {"1": "Frustrated", "2": "Okay", "3": "Proud", "4": "Excited"}
    feel_word = feelings.get(feeling, "Unknown")

    if feel_word == "Frustrated":
        print("\n💡 Frustration is NORMAL. Animation is hard.")
        print("   Take a 5-minute break, then come back.")
        print("   Every animator feels this. You're not alone.")

    # Save the reflection
    entry = f"""
{'=' * 50}
ANIMATION REFLECTION — {date}
Animator: {name}
Character: Pomboo the Dolphin
{'=' * 50}

TRYING TO MAKE: {trying}
WHAT HAPPENED:  {happened}
DIAGNOSIS:      The {term} is off because {why}
SELF-COMPARISON: My {better} is better than last time.
NEXT FIX:       {fix}
FEELING:        {feel_word}
{'=' * 50}
"""
    filename = f"reflection_{datetime.date.today().isoformat()}.txt"
    with open(filename, "w") as f:
        f.write(entry)
    print(f"\n✅ Saved to {filename}")
    print("\nRemember: Process over product. You're learning. 🐬")

if __name__ == "__main__":
    main()
```

**Part B: Fix One Thing (10 min)**

Based on their reflection, learners go back to Scratch and fix **just one thing** they identified. Not everything — one. This teaches the principle of **small steps** and prevents perfectionism paralysis.

Examples:
- *"I said the arc is flat. I'll change my 3 glides to 5 glides with a higher peak."*
- *"I said the timing is too fast. I'll change 0.2 seconds to 0.4 seconds."*

---

### Step 4: Sharing & Feedback (12 min)

Learners pair up (different partner from Step 2) and do a **"Before & After" share**:

1. Show your animation **before** the fix and **after** the fix.
2. Your partner responds using the Feedback Phrase Bank and the self-comparison principle:
   - *"I notice your arc is rounder after the fix — the peak is higher now."*
   - *"Compared to your before version, your timing really improved."*
3. The sharer says one sentence from their reflection: *"The thing I diagnosed was [term], and I fixed it by [action]."*

Celebrate: the learner who gave the most specific vocabulary feedback, and the learner who showed the most improvement over their own past work.

Close with the key message: *"Animation is hard. Frustration is normal. The words help. Comparing to your own past work keeps you going. And you never take someone's mouse — you give them the words to fix it themselves."*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| **Principle understanding** | Names fewer than 2 principles; cannot explain them | Names 3+ principles but explanations are vague | Names and explains all 5 principles in own words | Explains all 5 principles AND connects each to a specific moment in their own animation experience |
| **Vocabulary-based feedback** | Gives feedback using only vague words ("looks good/bad") | Uses 1-2 animation terms but some incorrectly | Uses 3+ animation terms correctly in peer feedback (e.g., "your arcs are flat") | Uses terms precisely AND helps a peer diagnose a specific problem using vocabulary ("I think your timing is off — the glide is too fast for a heavy dolphin") |
| **Self-reflection quality** | Reflection is incomplete or compares to others | Completes the journal but diagnosis is vague ("it looks weird") | Completes journal; identifies one specific issue using animation vocabulary; compares to own past work | Completes journal; identifies issue with vocabulary; compares to past work; AND fixes one thing that demonstrably improves the animation |

---

## Extended Activity

**Homework — "Be the Mentor":** Teach one animation principle to a family member or younger sibling. Show them your dolphin animation and explain one term (e.g., "This is anticipation — the dolphin dives deep before it jumps, like when you bend your knees before you jump"). Write 2 sentences about how it went. Did they understand? Did you feel like a teacher?

**Conservation connection:** Write a short paragraph: *"If I were a dolphin-watching guide in Kisite-Mpunguti, what rules would I set for tourists to protect pomboo?"* Research KWS dolphin-watching regulations and compare your rules to theirs.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide the reflection journal template with sentence starters already filled in for questions 1-3. Reduce the vocabulary list to 3 terms (timing, arcs, anticipation). Pair them with a patient partner who models the feedback phrases. | Challenge them to write a full "Peer Feedback Guide" for the class — a one-page document with do's and don'ts, sample phrases, and a checklist. They can also add a second animation principle fix (not just one) and document both in their reflection. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes — can they use vocabulary to give and receive feedback?
- [ ] Was Pomboo the Dolphin a good project for teaching about frustration and the vision-skill gap?
- [ ] Did learners actually practice "don't take the mouse" during peer feedback, or did they grab devices?
- [ ] Did the reflection journal help learners self-assess, or did they treat it as busywork?
- [ ] What would I change next time? (Consider: more time on the Feedback Phrase Bank role-play, or introduce the Python tool earlier for code-loving learners.)