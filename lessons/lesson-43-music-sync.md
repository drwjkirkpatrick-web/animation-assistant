# Lesson Plan 43: Music Synchronization & Beat Sync — Animating to Rhythm

**Module Reference:** Prompt 43 — 43-music-sync.md  
**Duration:** 80 min  
**Age Group:** 10-17  
**Animation Tool:** Scratch (beat-synced animation), Krita (audio waveform scrubbing)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Music & Animation — Rhythm, Beat Sync & Timing |
| Core Competency | Creativity & Imagination, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Find** the beat of a piece of music by tapping and mark beats on an animation timeline.
2. **Calculate** frames per beat from BPM and FPS (BPM ÷ 60 = beats/sec; FPS ÷ beats/sec = frames/beat).
3. **Sync** animation impacts (ball hits ground, character jumps) to land ON the beat, with anticipation between beats.

## Key Inquiry Question

> What if **Pomboo the Dolphin** could only jump on the drum beat — and what happens in the audience's brain when the splash hits exactly on the music?

---

## Resources

- Scratch (with sound import capability) or Krita (with audio import)
- Free music sources: YouTube Audio Library, Incompetech (Kevin MacLeod), Pixabay Music
- Phone or computer speakers
- Paper and pencils for beat mapping
- Optional: Audacity for finding BPM
- Optional: Raspberry Pi with Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Tursiops aduncus*) — **Pomboo** in Swahili  
**Habitat:** Kisite-Mpunguti Marine Reserve and Watamu Marine National Park.  
**Why this animal?** Dolphins are rhythmic animals — they leap in patterns, click and whistle in tempo, and swim in synchronized pods. A dolphin jumping ON the beat is the perfect image for music sync: the dive is anticipation, the leap is the action, the splash is the impact. When the splash hits on the downbeat, the audience FEELS it.  
**Conservation note:** Dolphins face threats from boat noise (disrupts communication), net bycatch, and plastic pollution. KWS regulates dolphin-watching at Kisite-Mpunguti — boats must keep 100m distance and cannot chase dolphins.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Play a song with a strong beat. Ask learners to tap their foot or clap on the beat. Then play the same song and clap OFF the beat (deliberately wrong). Ask: *"How did that feel? What felt different?"*

Explain: *When movement matches music, your brain says 'yes.' When it doesn't, your brain says 'something is wrong.' In animation, syncing to the beat is the difference between 'that looks professional' and 'something feels off.' Today we'll make Pomboo the Dolphin jump on the beat.*

### Step 1: Finding and Mapping the Beat (15 min)

**The Beat Marking Method:**
1. Import music into Scratch or Krita
2. Play it and TAP along with the beat (foot, finger, pencil)
3. Mark each beat on the timeline (keyframe, marker, or note)
4. Now you have a beat map — your timeline has rhythm markers

**BPM = Frames Per Beat:**

At 12fps (Scratch/cartoon standard):
| BPM (speed) | Frames per beat | Feel |
|-------------|----------------|------|
| 60 (slow) | 12 frames | Sad, emotional, dramatic |
| 90 (medium) | 8 frames | Walk cycle, conversation |
| 120 (medium-fast) | 6 frames | Dance, action, fun |
| 140 (fast) | ~5 frames | Chase, fight, comedy |

Formula: BPM ÷ 60 = beats per second. FPS ÷ beats per second = frames per beat.

```scratch
// In Scratch, we can use wait blocks timed to the beat
// At 120 BPM = 6 frames per beat = 0.5 seconds per beat

when [green flag] clicked
play sound [ocean-beats]            ← Start the music
wait (0.5) seconds                  ← Wait for one beat
broadcast [jump]                    ← Dolphin jumps ON the beat!
wait (0.5) seconds                  ← Wait for next beat
broadcast [splash]                  ← Splash lands ON the beat!
```

### Step 2: The Golden Pattern — Anticipation → Action → Follow-Through (20 min)

The beat sync pattern:

```
Between beats: Anticipation (dolphin dives deep — winding up)
ON the beat:   ACTION (dolphin leaps out of water — the big moment)
Between beats: Follow-through (dolphin falls, splash trails)
ON next beat:  Settle (splash settles, water calms)
```

This creates: wind-up → HIT → recover → rest. Wind-up → HIT → recover → rest. It feels like dancing.

**What to sync ON the beat (exactly):**
- Impacts: splash hits water ON the downbeat
- Direction changes: dolphin starts jump ON the beat
- Reveals: character appears ON a big drum hit

**What goes BETWEEN beats:**
- Travel/movement: dolphin rises between beats
- Anticipation: dive happens between beats
- Recovery: splash settles between beats

### Step 3: Beat-Synced Dolphin Jump in Scratch (20 min)

**Challenge:** Animate Pomboo jumping on the beat with music.

**Setup:**
1. Find a 120 BPM song (search YouTube Audio Library or Incompetech for "120 BPM")
2. Import into Scratch as a sound
3. At 120 BPM = 0.5 seconds per beat

```scratch
when [green flag] clicked
// Start music
play sound [ocean-dance-120bpm]

// Beat 1: Dolphin at surface (anticipation starts)
set y to (-50)
switch costume to [dolphin-surface]
wait (0.5) seconds                  ← One beat

// Beat 2: Dive deep (anticipation — between beats)
glide (0.25) secs to x: (0) y: (-150)   ← Half a beat down
switch costume to [dolphin-dive]
wait (0.25) seconds                 ← Half a beat hold

// Beat 3: LEAP! (ACTION — ON the beat!)
glide (0.25) secs to x: (0) y: (150)    ← Shoot up to peak
switch costume to [dolphin-leap]
wait (0.25) seconds                 ← Brief hang at peak

// Beat 4: Fall (between beats)
glide (0.25) secs to x: (0) y: (0)
switch costume to [dolphin-falling]

// Beat 5: SPLASH! (Impact — ON the beat!)
switch costume to [dolphin-splash]
set size to (120) %                 ← Splash = bigger!
start sound [splash-sfx]
wait (0.25) seconds

// Beat 6: Settle (follow-through)
set size to (100) %
switch costume to [dolphin-calm]
wait (0.25) seconds
```

**Sync checklist:**
- [ ] Music starts at the same time as animation
- [ ] The LEAP happens ON a beat (not between)
- [ ] The SPLASH happens ON a beat (the impact!)
- [ ] Anticipation (dive) happens BETWEEN beats
- [ ] Recovery (settle) happens BETWEEN beats

### Step 4: Sharing & Feedback (15 min)

Play each animation WITH the music. Then play it WITHOUT the music.

Ask: *"Does it still feel good without the music? Why or why not?"*

Key insight: *When animation is properly synced, it feels rhythmic even without the music. The beat is IN the animation itself.*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Beat Finding | Cannot identify the beat | Finds beat but inconsistent | Consistently marks beats on timeline | Marks beats + identifies downbeats vs upbeat |
| Frame Calculation | Cannot calculate frames/beat | Gets formula but arithmetic errors | Correct frames/beat for given BPM+FPS | Can adjust for any BPM/FPS combination |
| Sync Quality | Animation has no relation to music | Some moments align but most don't | Big impacts land ON the beat | All impacts + direction changes + accents on beat; anticipation between |

---

## Extended Activity

**Ocean Conservation Music Video:** Create a 30-second animated music video about dolphin conservation. Find a song at 90-120 BPM. Sync at least 5 animation moments to the beat. End with the message: "Keep 100m away — let Pomboo play in peace." Share it with the class.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Sync only ONE moment (the splash) to the beat | Sync small accents too: eye blinks on hi-hat ticks, head turns on snare hits |
| Use pre-marked timeline (teacher provides beat markers) | Try counter-rhythm: dolphin moves slightly off-beat during a tense scene, then catches up |
| Use very clear, simple 4/4 music with strong drums | Use complex music with tempo changes; adjust frame timing mid-animation |
| Provide the Scratch code template (fill in the blanks) | Use Krita: import audio, see waveform, scrub to find exact beat frames, mark with keyframes |

---

## Teacher Reflection

- [ ] Could learners find and mark the beat?
- [ ] Did they understand the difference between "on the beat" and "between beats"?
- [ ] Did the dolphin jump feel more satisfying when synced to music?
- [ ] Would more time on beat-finding exercises help before the animation phase?