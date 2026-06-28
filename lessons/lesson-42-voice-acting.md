# Lesson Plan 42: Voice Acting & Dialogue Recording — Being the Voice

**Module Reference:** Prompt 42 — 42-voice-acting.md  
**Duration:** 80 min  
**Age Group:** 10-17  
**Animation Tool:** Phone voice memos, Scratch (dialogue integration), Audacity (free audio editing)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Performing Arts — Voice Acting & Audio Production |
| Core Competency | Communication & Collaboration, Creativity & Imagination |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Create** a character voice by matching pitch, texture, and energy to a character's personality and size.
2. **Record** dialogue using a phone or microphone with proper technique (mic distance, room tone, multiple takes).
3. **Direct** a peer's voice performance using descriptive direction ("more frustrated," "slower, like you're tired").

## Key Inquiry Question

> If **Pweza the Octopus** could talk, what would she sound like — and how does the voice you create tell the audience who she is before she even moves?

---

## Resources

- Phone with voice memos app (or USB mic if available)
- Scratch (for integrating dialogue into animation)
- Audacity (free download for audio editing — optional)
- Quiet room or closet (for recording)
- A sock (for pop filter — reduces "p-pops")
- Character design cards from Lesson 30 (reuse ocean animal characters)
- Optional: Raspberry Pi with USB mic for low-resource recording

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus (*Octopus cyanea*) — **Pweza** in Swahili  
**Habitat:** Coral reefs throughout Kenya's marine parks — Watamu, Mombasa, Diani. Octopuses hide in crevices and holes in the reef during the day and hunt at night.  
**Why this animal?** Octopuses are incredibly intelligent — they can solve puzzles, open jars, and change color to communicate. This makes them perfect for voice acting: what does a clever, secretive, shape-shifting creature sound like? Pweza could be whispery and sly, or bubbly and excited, or deep and thoughtful. The voice IS the personality. Also, octopuses have no bones — their movement is completely different from vertebrates, making the voice even more important for establishing character.  
**Conservation note:** Octopuses are not currently endangered but face pressure from overfishing and reef degradation. They are important predators in the reef ecosystem — keeping crab and shellfish populations balanced. Healthy reefs need octopuses.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Ask learners to close their eyes. Say the same sentence three different ways:
1. Happy: "I found it!" (high pitch, fast, energetic)
2. Angry: "I found it." (low pitch, forceful, clipped)
3. Sad: "I... found it..." (quiet, slow, breathy)

Ask: *"Same words. Different feeling each time. Why?"*

Answer: *Voice = personality. In animation, the voice tells the audience who a character IS before they even move. Today we're going to be the voices of our ocean characters.*

Show a photo of Pweza the Octopus. Ask: *"If this octopus could talk, what would she sound like? Clever? Sneaky? Friendly? Wise?"*

### Step 1: Finding the Voice (15 min)

Teach the voice creation process:

**4 Elements of a Character Voice:**

| Element | What It Means | Pweza Example |
|---------|--------------|---------------|
| Pitch | High or low? | Medium-low (octopuses are mysterious) |
| Texture | Smooth, raspy, breathy, nasal? | Whispery and smooth (sneaky reef dweller) |
| Energy | Fast/loud or slow/quiet? | Deliberate, unhurried (patient hunter) |
| Quirk | A catchphrase, laugh, verbal tic? | Makes a "blub" sound when excited |

**How to Create a Voice:**
1. Start with a FEELING — what emotion does this character live in?
2. Match pitch to size — big character = lower, small = higher
3. Find the texture — smooth, raspy, breathy, nasal?
4. Add a quirk — a laugh, a catchphrase, a verbal tic
5. Test it — say 3 sentences in the voice. Can you sustain it?

**Exercise:** "I didn't do it" — 5 ways
Have each learner say "I didn't do it" as:
1. Innocent (high, clear, confused)
2. Guilty (low, fast, nervous)
3. Angry (forceful, tight, loud)
4. Scared (high, wavering, breathy)
5. Bored (flat, slow, monotone)

### Step 2: Recording Setup & Technique (15 min)

**Equipment (free to cheap):**
- Phone voice memos app (free, good quality)
- Gaming headset mic (~$20-30 if available)
- USB mic (~$50-80 if available)

**Recording Setup:**
1. Find the quietest room (small room + soft things = less echo)
2. Put the mic 6-8 inches from your mouth (a fist's width)
3. Put a sock over the mic to reduce "p-pops" (plosives)
4. Record a 5-second test: "Peter Piper picked a peck of pickled peppers." Listen back.
5. Record 10 seconds of SILENCE (room tone — needed for editing)

**Recording Tips:**
- Project! Speak louder than feels natural
- Exaggerate! Animation voices are BIGGER than real speech
- Move! Voice actors act with their whole body — stand up, gesture
- Record each line 3 times — pick the best take
- Stay in character between takes — don't break the voice
- If your throat hurts, STOP. No voice is worth damaging your vocal cords.

### Step 3: Recording Pweza's Dialogue (20 min)

**Challenge:** Each learner records dialogue for their ocean animal character.

**Sample script for Pweza:**
```
Line 1: "Hello! I am Pweza. I live in the coral reef at Watamu."
Line 2: "You think you can hide from me? I have eight arms and I can see in every direction."
Line 3: "Oh! A plastic bag! That's not food. That's... dangerous. Be careful, little fish."
Line 4: "I may be soft, but I am clever. And clever beats strong every time."
```

**Recording checklist:**
- [ ] Found a quiet space
- [ ] Mic is 6-8 inches away
- [ ] Sock on mic (or pop filter)
- [ ] Recorded 10 seconds of room tone
- [ ] Said the line number before each take ("Line 1: Hello! I am Pweza...")
- [ ] Recorded 3 takes of each line
- [ ] Stayed in character the whole time
- [ ] Drank water between lines

### Step 4: Integrating Voice into Scratch Animation (20 min)

Import the recorded voice into Scratch:

```scratch
// First: File → Import sound → select your recording
// Then use it in your animation:

when [green flag] clicked
switch costume to [pweza-neutral]
play sound [pweza-line1] until done    ← "Hello! I am Pweza..."
switch costume to [pweza-clever]       ← Change expression to match voice
play sound [pweza-line2] until done    ← "You think you can hide..."
switch costume to [pweza-warning]
play sound [pweza-line3] until done    ← "Oh! A plastic bag!"
switch costume to [pweza-proud]
play sound [pweza-line4] until done    ← "I may be soft, but I am clever..."
```

**Key technique:** Switch costumes to MATCH the voice energy. When Pweza sounds clever, show a clever expression. When Pweza warns about plastic, show concern. The face and voice work TOGETHER.

**Peer directing exercise (in pairs):**
- Partner A records their character voice
- Partner B directs: "More frustrated!" "Slower, like you're really tired." "Bigger — this is a cartoon!"
- Swap roles

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Voice Creation | Uses own normal voice | Attempts different voice but inconsistent | Sustained character voice with pitch/texture/energy | Distinct voice + quirk + can do multiple emotions in character |
| Recording Quality | Echoey, too quiet, or too loud | Some issues (pops, distance) but usable | Clear, well-leveled, minimal noise, 3 takes | Professional quality + room tone + properly slated |
| Direction | Cannot give voice direction | Gives vague direction ("do it better") | Specific direction ("slower, lower, more energy") | Directs + demonstrates + gives emotional context |

---

## Extended Activity

**Conservation Radio Play:** Record a 60-second radio PSA about ocean conservation using multiple character voices (one learner does all the voices!). Characters: Pweza the Octopus (clever), Kasa the Turtle (wise), and a narrator. Message: "Don't litter our ocean — we live here." Edit in Audacity (free) — add ocean sound effects and background music.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-written scripts to read | Write their own scripts; voice multiple characters with distinct voices |
| Use phone only (simplest setup) | Use Audacity: noise reduction, normalize to -3dB, cut pauses, export as WAV |
| Focus on one character voice | Direct a friend: explain character, demonstrate, give energy notes, record 3 takes, be kind |
| Skip editing (record → import directly) | Add background music and SFX in Scratch or Audacity; sync to the dialogue |

---

## Teacher Reflection

- [ ] Did learners create distinct character voices (not just their normal voice)?
- [ ] Was the recording quality usable? What issues came up?
- [ ] Did the peer directing exercise work? Were learners kind to each other?
- [ ] Did learners connect voice personality to their character design from Lesson 30?