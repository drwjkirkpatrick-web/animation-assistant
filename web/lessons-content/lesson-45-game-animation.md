# Lesson Plan 45: Game Animation & Sprite Sheets — Animating for Games

**Module Reference:** Prompt 45 — 45-game-animation.md  
**Duration:** 80 min  
**Age Group:** 12-14  
**Animation Tool:** Scratch (primary), Piskel (sprite sheet creation, optional)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Computer Science |
| Sub-strand | Digital Animation & Game Design |
| Core Competency | Digital Literacy, Creativity & Imagination |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain the difference between film animation and game animation (looping, variable timing, sprite sheets).
2. Create at least two game animation loops (idle + walk) using Scratch costumes and time-based control.
3. Value the importance of seamless loops and frame-rate-independent animation in game design.

## Key Inquiry Question

> How do we make **Pweza the Octopus (pweza)** look alive when the player
> isn't pressing any buttons — and keep swimming smoothly when they do?

---

## Resources

- Scratch (scratch.mit.edu — browser-based, free) — one device per learner or pair
- Piskel (piskelapp.com — free, browser) for sprite sheet export (optional extension)
- Reference video: octopus swimming / idle footage (YouTube "octopus swimming slow motion")
- Printed or projected sprite sheet grid template (4 columns × 2 rows)
- Optional: Raspberry Pi with Scratch installed for low-resource offline settings
- Paper and pencils for learners to sketch frames before digitizing

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus — *Pweza* (Swahili)  
**Habitat:** Coral reefs of Watamu Marine National Park and Mombasa Marine National Park; rocky crevices along the Kenyan coast  
**Why this animal?** An octopus has a distinct idle state (sitting in a crevice, arms gently curling) and a clear locomotion state (jet-propulsion swimming with all arms trailing). This makes it perfect for teaching the two most important game animation loops: **idle** and **move/walk**. The eight arms also provide natural secondary motion that makes a loop feel "alive."  
**Conservation note:** Octopus populations on the Kenyan coast are under pressure from overfishing and habitat destruction of coral reefs (*mwamba wa makorali*). KWS and local community managed areas (BMUs — Beach Management Units) regulate octopus harvesting with seasonal closures to allow populations to recover. Healthy reefs mean healthy octopus populations.

---

## Lesson Development

### Introduction (8 min)

Show a short video clip of an octopus sitting still on a reef, then suddenly jetting away. Ask learners:

- "What does the octopus do when nothing is happening?" *(It breathes, its arms shift slightly, it watches.)*
- "What happens when it decides to move?" *(It jets — fast, all arms trail behind.)*

Explain: **In a video game, your character has these same two states.** When the player does nothing, the character plays an **idle loop** — it must look alive. When the player presses a key, the character plays a **move loop**. Today we animate **Pweza the Octopus** for a game.

### Step 1: Concept Introduction — Game Animation vs Film Animation (15 min)

Teach the core differences using a comparison on the board:

| Film Animation | Game Animation |
|----------------|----------------|
| Fixed timing — every frame planned | Variable timing — player controls the action |
| Plays start to finish | Loops endlessly (idle, walk) |
| Every frame is unique | Frames cycle through a sprite sheet / costumes |

**The 7 game animation loops every character needs** (brief overview):
1. **Idle** — standing still, "doing nothing" (MOST SEEN animation!)
2. **Walk** — loops while moving
3. **Run** — faster, fewer frames, forward lean
4. **Jump** — a sequence (not a loop): squat → launch → airborne → apex → fall → land → recover
5. **Attack/Hit** — anticipation → strike → recovery
6. **Hurt** — flinch backward, flash, recover (4-8 frames)
7. **Death/Faint** — collapse, last frame held

**The #1 rule: frame-rate independence.** In games, the frame rate varies (30fps, 60fps, 144fps). If you hard-code "change costume every 3 frames," the animation plays at different speeds on different computers. **Use TIME, not frames:**

> "Change costume every 0.1 seconds" — NOT "every 3 frames."

Show this Scratch code block structure on the projector:

```scratch
when green flag clicked
forever
  if <key [right arrow v] pressed?> then
    switch costume to [pweza-swim-1 v]
    wait (0.1) seconds
    switch costume to [pweza-swim-2 v]
    wait (0.1) seconds
    switch costume to [pweza-swim-3 v]
    wait (0.1) seconds
    switch costume to [pweza-swim-4 v]
    wait (0.1) seconds
  else
    switch costume to [pweza-idle-1 v]
    wait (0.3) seconds
    switch costume to [pweza-idle-2 v]
    wait (0.3) seconds
  end
end
```

**Explain the code:**
- When the right arrow is pressed → Pweza plays the **swim loop** (4 frames, 0.1s each = fast swimming)
- When no key is pressed (`else`) → Pweza plays the **idle loop** (2 frames, 0.3s each = slow breathing)
- `wait` blocks use **TIME** (seconds), not frames → this is frame-rate independent!
- The `forever` block makes the loops repeat endlessly

### Step 2: Guided Practice — Build Pweza's Idle & Swim Loops in Scratch (20 min)

Walk through the steps together. Learners follow along on their devices.

**Part A: Create the costumes (10 min)**

1. Open Scratch → create a new project
2. Delete the cat sprite → click "Choose a Sprite" → search "Octopus" (or draw your own pweza)
3. If drawing your own: click "Paint" → draw a simple octopus:
   - Round head, 8 arms, big eyes
   - Use the **Select** tool to duplicate and modify for each frame
4. Create **6 costumes total**:
   - `pweza-idle-1`: arms slightly curled, body normal
   - `pweza-idle-2`: arms slightly more open, body slightly bigger (breathing in)
   - `pweza-swim-1`: arms spread wide (start of jet)
   - `pweza-swim-2`: arms pulling inward
   - `pweza-swim-3`: arms compressed tight (jet propulsion)
   - `pweza-swim-4`: arms trailing behind (gliding)

**Part B: Program the loops (10 min)**

Type in this code exactly:

```scratch
when green flag clicked
set [animation_state v] to [idle v]
forever
  if <key [right arrow v] pressed?> then
    set [animation_state v] to [swim v]
    change x by (5)
  end
  if <key [left arrow v] pressed?> then
    set [animation_state v] to [swim v]
    change x by (-5)
  end
  if <not <<key [right arrow v] pressed?> or <key [left arrow v] pressed?>>> then
    set [animation_state v] to [idle v]
  end
  if <(animation_state) = [swim v]> then
    switch costume to [pweza-swim-1 v]
    wait (0.1) seconds
    switch costume to [pweza-swim-2 v]
    wait (0.1) seconds
    switch costume to [pweza-swim-3 v]
    wait (0.1) seconds
    switch costume to [pweza-swim-4 v]
    wait (0.1) seconds
  else
    switch costume to [pweza-idle-1 v]
    wait (0.3) seconds
    switch costume to [pweza-idle-2 v]
    wait (0.3) seconds
  end
end
```

**Test it:** Press the green flag. Pweza should breathe slowly when you do nothing, and swim when you press arrow keys. The octopus moves across the screen while swimming.

**Loop check:** Watch the transition from the last swim frame back to the first. Does it jump? If so, make `pweza-swim-4` flow naturally back into `pweza-swim-1` (arms should be in a similar position).

### Step 3: Independent Practice — Add a Hurt Animation (20 min)

**Challenge:** Add a **hurt/hit reaction** to Pweza. When the octopus touches a "danger" sprite (a jellyfish — *vipepeo* in some contexts, but let's use a simple red obstacle), Pweza should:
1. Flash (change color effect briefly)
2. Play a 3-frame hurt animation
3. Move backward slightly (knockback)
4. Return to idle

**Starter code for learners to complete:**

```scratch
when green flag clicked
forever
  if <touching [danger-jellyfish v]?> then
    set [color v] effect to (50)
    switch costume to [pweza-hurt-1 v]
    wait (0.1) seconds
    switch costume to [pweza-hurt-2 v]
    wait (0.1) seconds
    switch costume to [pweza-hurt-3 v]
    wait (0.1) seconds
    change x by (-20)
    set [color v] effect to (0)
  end
end
```

Learners must:
- Draw 3 `pweza-hurt` costumes (flinch back, squashed, recovering)
- Add a "danger" sprite (a jellyfish or rock) to the stage
- Test that the hurt animation triggers on contact
- Make sure Pweza returns to idle afterward

### Step 4: Sharing & Feedback (7 min)

Learners pair up and play each other's mini-games. Use the **critique framework** (from Prompt 06):
- **Say one thing that works:** "Your idle loop really looks like Pweza is breathing!"
- **Ask one question:** "How did you make the hurt animation so fast?"
- **Suggest one improvement:** "Could you add a sound effect when Pweza gets hurt?"

Celebrate the best idle loops — remind learners: **the idle is the most important game animation because players see it the most.**

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Understanding game vs film animation | Cannot explain any difference | Identifies 1 difference (e.g., "games loop") | Explains 2+ differences including looping and variable timing | Explains differences with examples and understands frame-rate independence |
| Creating animation loops in Scratch | Creates 1 loop but it does not loop smoothly | Creates idle OR swim loop that mostly works | Creates both idle and swim loops that cycle seamlessly | Creates idle + swim + hurt, all seamless, with smooth transitions between states |
| Frame-rate independent timing | Uses no wait blocks (frame-based) | Uses wait blocks but inconsistent times | Uses time-based `wait` blocks consistently (0.1s, 0.3s) | Uses time-based waits AND can explain why it matters across devices |

---

## Extended Activity

**Homework / follow-up project:** Create a full **Pweza's Reef Adventure** game in Scratch with:
- Idle, swim, and hurt animations
- A coral reef background (*mwamba wa makorali*)
- 3 obstacles (plastic bag, fishing net, jellyfish)
- A score counter for "coral saved"

Connect to conservation: plastic bags in the ocean look like jellyfish to octopuses and turtles — they eat them and get sick. Research what Watamu Marine Park does to reduce plastic pollution and include a "conservation fact" screen in your game.

**Next lesson connection:** Lesson 46 covers **production management** — how to actually plan and FINISH a project like this without giving up halfway.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-drawn octopus costume templates (6 frames ready to use); reduce to idle + swim only (skip hurt); pair with a peer for coding | Add a **jump animation** (sequence, not loop): squat → launch → airborne → fall → land; export a sprite sheet using Piskel; try the same loops in Pygame with `pygame.time.get_ticks()` for frame-rate-independent timing |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the octopus (pweza) example engaging? Did learners connect with the local animal?
- [ ] Did learners understand the difference between film and game animation?
- [ ] Did the Scratch code work on the available devices? Any technical issues?
- [ ] What would I change next time?