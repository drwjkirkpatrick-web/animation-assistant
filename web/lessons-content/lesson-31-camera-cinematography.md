# Lesson Plan 31: Camera & Cinematography for Animation — Directing the Eye

**Module Reference:** Prompt 31 — 31-camera-cinematography.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Scratch (camera simulation), Krita (layer-based parallax), Blender (advanced)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Film & Animation — Camera, Composition & Visual Storytelling |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Identify** six camera shot types (extreme wide, wide, medium, medium close-up, close-up, extreme close-up) and explain when to use each.
2. **Apply** the rule of thirds, lead room, and the 180-degree rule to compose animation shots featuring a Kenyan ocean animal.
3. **Create** a 3-shot animated sequence with varied camera angles using Scratch or Krita, simulating at least one camera move (pan, push-in, or parallax).

## Key Inquiry Question

> If you were filming **Pomboo the Dolphin** jumping at Kisite-Mpunguti Marine Reserve, where would you put the camera — and why does the camera position change how the audience feels about the jump?

---

## Resources

- Scratch or Krita (Blender for advanced learners)
- Projector for demonstrating shot types
- Reference video of dolphins at Kisite-Mpunguti Marine Reserve
- Printed shot-type reference cards (wide, medium, close-up examples)
- Paper and pencils for storyboard planning
- Optional: Raspberry Pi with Scratch for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Bottlenose Dolphin (*Tursiops aduncus*) — **Pomboo** in Swahili  
**Habitat:** Kisite-Mpunguti Marine Reserve (Kwale County) and Watamu Marine National Park. Dolphins live in pods of 10-30 and are frequently seen leaping and playing in the warm coastal waters.  
**Why this animal?** Dolphins are fast, dynamic, and leap out of the water — perfect for demonstrating camera choices. A wide shot shows the whole leap arc. A close-up shows the splash. A tracking shot follows the dolphin as it swims. The same action feels completely different depending on where you put the camera.  
**Conservation note:** Bottlenose dolphins face threats from fishing net bycatch and irresponsible dolphin-watching tourism. KWS regulates dolphin-watching at Kisite-Mpunguti — boats must keep 100 meters away and cannot chase or surround dolphins. Loud boat engines stress dolphins and disrupt their communication.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show the same dolphin jumping video three times, cropped differently:
1. **Wide shot** — dolphin is tiny in the vast ocean (feels: epic, lonely, grand)
2. **Medium shot** — dolphin fills half the frame (feels: energetic, exciting)
3. **Close-up** — just the splash as it lands (feels: dramatic, impactful)

Ask: *"Same dolphin, same jump. Why does it feel different each time?"*

Answer: *The camera is you. In animation, YOU decide where the audience looks. Today we learn to direct the eye.*

### Step 1: Shot Types & Camera Moves (20 min)

Teach shot types using dolphin examples:

| Shot Type | What We See | When to Use | Dolphin Example |
|-----------|------------|-------------|-----------------|
| Extreme Wide | Dolphin is a dot in the ocean | Establishing scale, isolation | Pomboo alone in the vast Indian Ocean |
| Wide | Full dolphin + environment | Show the full leap arc | Complete jump from water to splash |
| Medium | Dolphin fills half the frame | Action, energy | Mid-jump, body and tail visible |
| Medium Close-Up | Chest up (if dolphin had a chest!) | Reaction, emotion | Dolphin's face as it breaks the surface |
| Close-Up | Face fills frame | Key emotional moment | Dolphin's eye — joy or fear |
| Extreme Close-Up | One feature | Tension, detail | Just the splash droplets hitting water |

**Camera moves for Scratch:**

```scratch
// PAN: Move the background horizontally to simulate camera turning
when [green flag] clicked
set [bg_x] to (240)
forever
  change [bg_x] by (-2)        ← Background scrolls right to left = camera pans left
  go to x: (bg_x) y: (0)       ← Apply to backdrop or background sprite
end

// PUSH-IN: Gradually scale the sprite up to simulate camera moving closer
when [green flag] clicked
set size to (50) %
repeat (60)
  change size by (1)           ← Slowly zoom in over 60 frames
end

// PARALLAX: Foreground moves faster than background = depth illusion
// Sprite 1 (foreground coral): change x by (-4)
// Sprite 2 (midground water):  change x by (-2)
// Sprite 3 (background sky):   change x by (-1)
```

**The 180-degree rule:** When two characters face each other (say, a dolphin and a sea turtle), keep the camera on one side. Dolphin is always screen-LEFT, turtle is always screen-RIGHT. If you cross the line, they swap sides and the audience gets confused.

### Step 2: Guided Practice — 3-Shot Dolphin Sequence (20 min)

Plan and animate a 3-shot sequence of Pomboo the Dolphin jumping:

**Shot Plan:**
1. **Wide Shot** — Pomboo swimming toward the jump point (establish the scene) — 3 seconds
2. **Medium Shot** — Pomboo leaps out of the water (the action) — 2 seconds
3. **Close-Up** — Splash as Pomboo lands (the impact) — 1 second

In Scratch:
```scratch
// Shot 1: Wide — dolphin small, full ocean visible
when [green flag] clicked
switch backdrop to [ocean-wide]
set size to (40) %              ← Small = far away
glide (3) secs to x: (0) y: (-50)

// Shot 2: Medium — dolphin larger, mid-leap
switch backdrop to [ocean-medium]
set size to (80) %              ← Larger = closer
glide (1) secs to x: (0) y: (100)  ← Jump up
glide (1) secs to x: (0) y: (-50)  ← Come down

// Shot 3: Close-up — splash only
switch backdrop to [ocean-closeup]
set size to (150) %             ← Very large = very close
switch costume to [splash]
say [SPLASH!] for (1) seconds
```

**Composition checklist:**
- [ ] Rule of thirds: dolphin is NOT in the center — it's on a thirds line
- [ ] Lead room: when dolphin faces right, there's space to the right
- [ ] Shot variety: no two consecutive shots are the same type
- [ ] 180-degree rule: if another character appears, they stay on their side

### Step 3: Independent Practice — Your Ocean Scene (20 min)

**Challenge:** Plan and animate a 3-5 shot sequence featuring any Kenyan ocean animal.

Options:
- **Sea turtle laying eggs on the beach** (wide → medium → close-up on eggs)
- **Octopus escaping a predator** (tracking shot → close-up on tentacles → wide escape)
- **Whale shark feeding on plankton** (extreme wide → push-in → close-up on mouth)

Learners plan on paper first (storyboard with 3-5 boxes), then animate in Scratch or Krita.

### Step 4: Sharing & Feedback (10 min)

Learners present their sequences. Class analyzes:
- *"Which shot was your favorite and why?"*
- *"Did the camera choices help tell the story?"*
- *"Was there a shot that felt too long or too short?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Shot Types | Uses only one shot type (usually wide) | Uses 2 shot types | Uses 3+ shot types with clear purpose | Uses 4+ shot types + varied camera moves |
| Composition | Subject centered in every shot | Some off-center but no rule of thirds | Rule of thirds applied; lead room considered | Rule of thirds + lead room + foreground framing + parallax |
| Storytelling | Shots feel random/unordered | Shots tell a basic story | Shots build tension/emotion purposefully | Shots create a complete emotional arc (setup → action → impact) |

---

## Extended Activity

**Conservation Public Service Announcement:** Create a 15-second animated PSA about dolphin conservation at Kisite-Mpunguti. Use at least 4 shot types. End with a close-up of the conservation message: "Keep 100m away — let Pomboo play in peace."

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-made storyboard template with 3 boxes labeled (wide, medium, close-up) | Use Blender: add a Camera object, animate its position with keyframes, use Track To constraint |
| Use pre-drawn ocean backdrops in Scratch | Add parallax with 3 layers (foreground coral, midground water, background sky) moving at different speeds |
| Focus on shot planning only (skip animation) | Apply the 180-degree rule in a two-character conversation scene |

---

## Teacher Reflection

- [ ] Did learners understand how shot types change the emotional feel?
- [ ] Could they apply the rule of thirds in their compositions?
- [ ] Was the dolphin example engaging? Did they connect camera choices to storytelling?
- [ ] Would a physical "camera frame" prop (cardboard cutout) help next time?