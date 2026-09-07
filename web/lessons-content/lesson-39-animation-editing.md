# Lesson Plan 39: Animation Editing & Post-Production — The Invisible Art

**Module Reference:** Prompt 39 — 39-animation-editing.md  
**Duration:** 75 min  
**Age Group:** 14-17  
**Animation Tool:** OpenShot (free video editor) + Scratch or Krita (for animation source)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Computer Science |
| Sub-strand | Media Production & Digital Content Creation |
| Core Competency | Critical Thinking & Problem Solving / Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain the "edit before you animate" principle and describe the three stages of animation editing (radio play, animatic, post-production).
2. Assemble a multi-shot animation in OpenShot by importing clips, arranging a timeline, syncing audio, and exporting a final MP4.
3. Apply basic editing concepts (cut on action, shot pacing, frame rate manipulation) to improve the flow and rhythm of a short animation.

## Key Inquiry Question

> A green sea turtle (*kasa*) glides through the water with perfect rhythm —
> every flipper stroke timed exactly, every turn smoothly anticipated. How can
> we edit our animations so they flow with the same natural rhythm as *kasa*
> swimming through the Watamu coral gardens?

---

## Resources

- Laptops with OpenShot installed (free: openshot.org) and Scratch or Krita
- Projector or large screen for demonstration
- Short video clip of a green sea turtle (*kasa*) swimming through coral (2-3 min, e.g., Watamu Marine National Park footage)
- Pre-made Scratch animation clips (3 short clips of a turtle swimming, turning, and resting — exported as separate MP4 files) OR learners' own animation clips from previous lessons
- Headphones (one per learner if possible) for audio editing
- Printed animatic storyboard template (6-panel)
- Optional: Raspberry Pi with OpenShot for low-resource groups (OpenShot runs on Linux)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Green Sea Turtle (*Kasa*)  
**Habitat:** Seagrass beds and coral reefs of Watamu Marine National Park (Kilifi County) and Diani-Chale Marine Reserve (Kwale County). Green sea turtles graze on seagrass and rest in coral caves along Kenya's coast.  
**Why this animal?** The green sea turtle is the master of **rhythm and pacing**. Its flipper strokes follow a steady, graceful pattern — slow-in, power stroke, glide, slow-out, repeat. This is exactly what good editing feels like: every cut timed perfectly, every shot flowing into the next with natural rhythm. A turtle doesn't rush; it glides. Good editing doesn't feel choppy; it flows. We'll use *kasa* as our editing subject — assembling three shots of turtle behavior into one smooth sequence that flows like the turtle itself.  
**Conservation note:** Green sea turtles are classified as **Endangered** by the IUCN. They face threats from plastic pollution (turtles mistake plastic bags for jellyfish), fishing bycatch, and habitat destruction of seagrass beds. Local Ocean Conservation (a Watamu-based NGO) and KWS run nesting protection programs — volunteers patrol beaches at night during nesting season to protect eggs from poachers. When you edit your turtle animation, consider adding a conservation message card: "Protect *kasa* — say no to plastic bags."

---

## Lesson Development

### Introduction (5-10 min)

Show the 2-3 minute video of a green sea turtle (*kasa*) swimming through Watamu's coral gardens. Ask learners:

- *"How would you describe the rhythm of the turtle's movement?"* (Answer: steady, smooth, unhurried, graceful)
- *"What happens when the turtle turns? Does it stop and start, or flow?"* (Answer: it flows — anticipates the turn, adjusts, glides into the new direction)
- *"Now imagine watching 5 video clips of this turtle stitched together randomly — would it feel as smooth?"* (Answer: no — the clips would feel choppy and disconnected)

Connect to the lesson: **Editing is the invisible art that makes your animation flow like *kasa* swimming.** In animation, you don't edit after — you edit BEFORE. The edit is the blueprint. Today we learn the three stages of animation editing and assemble our own multi-shot turtle sequence in OpenShot.

---

### Step 1: Concept Introduction — The Three Stages of Editing (15 min)

**The Golden Rule of Animation Editing:**

> *"In live-action, you shoot first and edit later. In animation, you edit first
> and shoot later."* — Ken Schretzmann (editor of Toy Story 3 and Cars)

This means: you plan the ENTIRE film's timing, pacing, and flow BEFORE you draw a single frame of final animation.

**The 3 Stages:**

```
STAGE 1: THE RADIO PLAY (Audio First)
─────────────────────────────────────
Before any visuals, build the audio:
  1. Record dialogue (or narration)
  2. Assemble all audio into a "radio play" — the full
     story in sound only
  3. Time out non-dialogue moments (act them out!)
  4. WHY? Because dialogue timing = how many frames you
     need. A 2-second line = 48 frames at 24fps. You
     can't animate without knowing the timing.
  5. This is the EASIEST place to make changes — cutting
     1 second here saves hours of animation later.

STAGE 2: THE ANIMATIC (Visual Blueprint)
────────────────────────────────────────
  1. Draw storyboard panels
  2. Time each panel to the audio
  3. Add temp music and SFX
  4. Watch it — does the story work? Is the pacing right?
  5. PRO RULES from professional editors:
     - Leave 4 extra frames at head and tail of every
       dialogue shot
     - Edit SLOWER than feels natural — animation speeds
       up when details are added
     - Never less than 2 seconds for establishing shots
     - This is your BLUEPRINT. Animate to match it.

STAGE 3: POST-PRODUCTION (Final Assembly)
─────────────────────────────────────────
After animation is done:
  1. Replace animatic frames with final animation
  2. Fine-tune cuts and timing
  3. Add final SFX, music, sound design
  4. Color correction
  5. Final render and export as MP4
```

**Editing concepts every animator should know:**

| Concept | What It Means | When to Use |
|---------|---------------|-------------|
| Hard cut | Instant change from one shot to another | Most common. Use for continuous action or energy |
| Soft cut (dissolve) | Gradual blend between shots | Time passing, dream sequences, mood change |
| Smash cut | Sudden, jarring cut | Shock, surprise, tonal shift |
| Match cut | Two shots linked by similar composition | Visual continuity |

**When to cut:**
- Cut ON action — cut during movement, not stillness
- Cut on dialogue — new speaker = new shot (usually)
- Don't cut too fast — each shot needs at least 1-2 seconds
- Don't hold too long — if nothing happens for 3+ seconds, the audience gets bored

---

### Step 2: Guided Practice — Assemble a Turtle Sequence in OpenShot (15 min)

Walk through assembling a 3-shot turtle animation in OpenShot. Demonstrate on the projector; learners follow along.

**Our project:** "Kasa's Journey" — a 3-shot sequence:
- **Shot 1 (5 sec):** Turtle swimming through coral (establishing shot)
- **Shot 2 (4 sec):** Turtle turning to graze on seagrass (action shot)
- **Shot 3 (3 sec):** Turtle resting in coral cave + conservation message (closing shot)

**Step-by-step in OpenShot:**

```
OPENSHOT WORKFLOW — "KASA'S JOURNEY"
══════════════════════════════════════════════════════════

1. IMPORT YOUR CLIPS
   - Open OpenShot
   - File → Import Files (or drag files into the Project Files panel)
   - Import: shot1_swim.mp4, shot2_turn.mp4, shot3_rest.mp4
   - Import: ocean_ambient.wav (background water sound)
   - Import: turtle_narration.wav (if you have voiceover)

2. ARRANGE ON TIMELINE
   - Drag shot1_swim.mp4 to Track 1 at position 0:00
   - Drag shot2_turn.mp4 to Track 1 right after shot1 ends
   - Drag shot3_rest.mp4 to Track 1 right after shot2 ends
   - Your timeline should look like:
     [==shot1 swim==][==shot2 turn==][==shot3 rest==]
      0:00           0:05            0:09      0:12

3. ADD AUDIO TRACK
   - Drag ocean_ambient.wav to Track 2 at position 0:00
   - Drag turtle_narration.wav to Track 3 at the right
     position (if using voiceover)
   - Timeline now has 3 tracks:
     Track 1: [==shot1==][==shot2==][==shot3==]
     Track 2: [========ocean ambient=========]
     Track 3:       [==narration==]

4. TRIM AND CUT
   - Hover over the edge of a clip → cursor becomes a double arrow
   - Click and drag to trim the clip's start or end
   - TIP: Cut ON action. If the turtle is mid-flipper-stroke
     at the end of shot1, cut there — the motion continues
     into shot2 and the cut feels invisible.

5. ADD A TRANSITION (optional)
   - Right-click between two clips → "Transition"
   - Choose "Dissolve" for a soft transition (time passing)
   - Use HARD CUTS for most edits. Dissolves only for
     mood/time changes.

6. ADD A TITLE CARD (conservation message)
   - Title → Title → "Title" in the top menu
   - Type: "Protect Kasa — say no to plastic bags.
           Support Local Ocean Conservation, Watamu."
   - Drag the title clip to Track 1 after shot3
   - Set duration to 4 seconds

7. PREVIEW
   - Press Spacebar to play from the beginning
   - Watch the full sequence. Does it flow like kasa swimming?
   - TIP: Edit SLOWER than feels natural. Animation speeds up
     when you add details.

8. EXPORT
   - File → Export Video
   - Profile: "MP4 (H.264)" — most universally accepted
   - Resolution: 1280 x 720 (or 1920 x 1080)
   - FPS: 24 (standard for animation)
   - Click "Export Video"
   - Save as: kasa_journey_v01.mp4
══════════════════════════════════════════════════════════
```

> **Teacher note:** If learners don't have pre-made clips, they can export 3
> short Scratch animations as separate MP4s (File → Save as video in Scratch
> or use a screen recorder). The focus is on the EDITING process, not the
> animation quality of the source clips.

---

### Step 3: Independent Practice — Edit Your Own Multi-Shot Sequence (20 min)

Learners create their own edited sequence using OpenShot.

**Task: Create a 15-20 second edited animation featuring a Kenyan ocean animal**

Requirements:
1. **Minimum 3 shots** (different scenes/angles of your animal)
2. **Audio track** (background sound, narration, or music)
3. **At least one hard cut** on action
4. **One title card** with your animal's name and a conservation message
5. **Export as MP4 H.264**

**Choose your animal:**
- *Kasa* (green sea turtle) — swimming, turning, resting
- *Pomboo* (dolphin) — swimming, jumping, splashing
- *Pweza* (octopus) — crawling, jetting, color change
- *Papa Shinga* (whale shark) — gliding, filter feeding, diver encounter
- Clownfish — hovering, darting, returning to anemone

**Version control naming convention (display on board):**

```
FILE NAMING — NEVER delete a version!
─────────────────────────────────────
  kasa_journey_v01.mp4   ← first attempt
  kasa_journey_v02.mp4   ← after fixing timing
  kasa_journey_v03.mp4   ← after adding sound
  kasa_journey_final.mp4 ← the one you submit

  WHY? You might want v01 back after v03 isn't better.
  Keep EVERY version until the project is finalized.
```

**Python script for frame rate analysis (for advanced learners):**

If learners want to understand frame rate manipulation, here is a Python script (runs on Raspberry Pi or any Python environment) that analyzes how many unique frames are in a sequence:

```python
# frame_rate_analyzer.py
# Analyzes frame timing in an animation sequence
# Run: python3 frame_rate_analyzer.py

# Standard frame rates for animation
frame_rates = {
    "on_1s": 24,   # 24 unique frames/sec — smooth, expensive
    "on_2s": 12,   # 12 unique frames/sec — classic cartoon look
    "on_3s": 8,    # 8 unique frames/sec — choppy, deliberate style
}

print("=== Animation Frame Rate Analyzer ===")
print()

# Input: how long is your shot?
shot_duration = float(input("Enter shot duration in seconds: "))

print()
print(f"For a {shot_duration}-second shot:")
print()

for style, fps in frame_rates.items():
    frames_needed = int(shot_duration * fps)
    print(f"  {style:>6}: {frames_needed} unique drawings needed "
          f"({fps} fps)")

print()
print("TIP: 'On 2s' (12 fps) is the most common for TV animation.")
print("     'On 1s' (24 fps) is for smooth, theatrical-quality animation.")
print("     'On 3s' (8 fps) is for stylized, choppy looks (anime action).")
print()

# Speed manipulation
print("=== Speed Manipulation ===")
print("To SPEED UP: remove every other frame (2s → 1s feel)")
print("To SLOW DOWN: duplicate frames (1s → 2s), no interpolation artifacts")
print("To RAMP (accelerate): transition from 2s to 1s")
print("To RAMP (decelerate): transition from 1s to 2s")
```

> **Teacher note:** Run this script together on the projector for advanced
> learners. It helps them understand WHY editing decisions about frame rate
> matter before they start animating.

---

### Step 4: Sharing & Feedback (10 min)

Learners present their edited sequences to the class or in small groups.

**Screening format (each presentation = 2 min):**
1. Play the final exported MP4
2. Name one editing decision they're proud of (e.g., "I cut on action when the turtle's flipper was mid-stroke")
3. Name one thing they'd improve next time (e.g., "The audio is too loud compared to the narration")

**Feedback using the Sandwich Method** (from Lesson 37):
- 🍞 Positive: "The pacing flows really well — the turtle feels like it's genuinely swimming"
- 🧀 Constructive: "The cut between shot 1 and shot 2 is a bit abrupt — try cutting during the flipper stroke instead of the glide"
- 🍞 Encouragement: "Your conservation title card is a great touch. Keep editing!"

**Closing discussion:**
- *"Did editing feel different from animating? How?"*
- *"Which stage was hardest — planning (radio play/animatic) or post-production?"*
- *"Did anyone discover that editing slower than feels natural actually works?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Editing concepts (3 stages, cut types) | Cannot describe the 3 stages or any cut types | Describes 1-2 stages or cut types with confusion | Describes all 3 stages (radio play, animatic, post-production) and 2+ cut types (hard cut, dissolve, etc.) with correct examples | Describes all 3 stages and multiple cut types with examples, AND explains "edit before you animate" with reasoning |
| Practical editing (OpenShot assembly) | Does not import/arrange clips; no final export | Imports clips but timeline is disorganized or no audio track; export attempted | Imports 3+ clips, arranges on timeline, adds audio, trims/cuts, exports MP4 H.264 successfully | Imports 3+ clips, arranges timeline with cuts on action, adds audio + title card, uses version naming, exports clean MP4 with correct resolution/fps |
| Pacing & rhythm | Sequence feels random or choppy; no sense of timing | Sequence has some flow but cuts are too fast or too slow; pacing inconsistent | Sequence flows with consistent pacing; cuts feel intentional; rhythm is steady | Sequence flows naturally like the turtle swimming; pacing varies intentionally for dramatic effect; cuts are invisible |

---

## Extended Activity

**Homework: Build a Radio Play**

Before animating your next project, build a radio play first:
1. Write a 30-second narration or dialogue for your ocean animal animation (e.g., *Kasa* swimming, *Pomboo* jumping)
2. Record it on your phone (voice memos app)
3. Listen to it. Time each line.
4. Write down: "Line 1 = 3 seconds = 72 frames at 24fps. Line 2 = 2 seconds = 48 frames."
5. Bring your timing notes to the next class

**This is Stage 1 of editing — audio first.** You now know exactly how many frames you need to animate before you draw a single frame. That's the invisible art.

**Conservation connection:** Add a 5-second conservation card to your final edit. Use a real fact about green sea turtles from Local Ocean Conservation (localocean.co) — they protect turtle nests on Watamu beaches. Your animation can educate viewers while entertaining them.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-exported Scratch clips (the teacher's demo clips) so they skip animation and focus purely on editing | Have them build a full animatic first (storyboard panels timed to audio in OpenShot) before assembling final clips |
| Reduce to 2 shots instead of 3; skip the audio track and focus on visual editing only | Challenge them to use frame rate manipulation — animate one shot "on 1s" and another "on 2s" and compare the feel |
| Walk through the OpenShot steps as a paired activity (two learners on one laptop) | Introduce DaVinci Resolve (free, pro-level) as a step up from OpenShot; have them try color correction on their turtle clips |
| Use the Python frame rate analyzer script as a math cross-connection (calculate frames needed for different durations) | Have them write a second Python script that generates a version control log — automatically creating v01, v02, v03 filenames |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the green sea turtle's swimming rhythm an effective metaphor for editing pacing?
- [ ] Did learners understand "edit before you animate," or did they still think of editing as something done at the end?
- [ ] Was OpenShot accessible for all learners, or did technical issues (crashes, slow laptops) create barriers?
- [ ] Did any learner struggle with the concept of frame rate? How can I support them next time?
- [ ] What would I change next time?