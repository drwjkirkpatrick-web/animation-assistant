# Lesson Plan 21: Rigging Deep Dive — From Drawing to Puppet

**Module Reference:** Prompt 21 — 21-rigging-deep-dive.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Scratch (Level 1) / Blender (Level 2-3)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Computer Science |
| Sub-strand | Digital Animation — Character Rigging & Puppet Construction |
| Core Competency | Creativity & Imagination, Digital Literacy, Critical Thinking |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain what a rig is and why rigging saves time compared to frame-by-frame drawing for character animation.
2. Build a simple pivot rig (Level 1) or bone rig (Level 2) for a sea turtle character using Scratch or Blender.
3. Appreciate the value of investing time in setup to enable efficient, consistent animation — and connect this to conservation patience (protecting turtles takes long-term commitment).

## Key Inquiry Question

> How do we build a digital puppet of **Kasa the Green Sea Turtle** so we can pose her swimming without redrawing every frame?

---

## Resources

- **Scratch** (free, browser-based) for Level 1 pivot rigging — or **Blender** (free, downloadable) for Level 2-3 bone rigging
- Projector or shared screen for demonstration
- Reference images/videos of a green sea turtle swimming (search "green sea turtle swimming slow motion")
- Printed sea turtle body-part template (head, shell, 4 flippers as separate outlines) — for planning on paper first
- *Optional:* Raspberry Pi with Blender installed for low-resource settings
- Graph paper and pencils for sketching the rig plan before building digitally

---

## Local Context: Kenyan Ocean Animal

**Animal:** Green Sea Turtle — *Kasa* (Swahili)  
**Habitat:** Seagrass beds in Watamu Marine National Park and Diani Reef, Kenya's Indian Ocean coast (*Bahari ya Hindi*)  
**Why this animal?** A sea turtle has a clear, simple body structure — a shell (body), a head, and four flippers — that maps perfectly onto a basic rig. Each flipper has an obvious pivot point (where it joins the shell), making it the ideal first character for learning how bones and pivots work. The turtle's graceful swimming also demonstrates why rigging is useful: you pose the flippers in a few key positions and let the software create smooth swimming motion.  
**Conservation note:** The green sea turtle is classified as **Endangered** by the IUCN. Major threats include plastic pollution (turtles mistake plastic bags for jellyfish) and accidental bycatch in fishing nets. The Kenya Wildlife Service (KWS) protects nesting sites at Watamu Marine National Park — local conservation groups like Local Ocean Conservation patrol beaches at night during nesting season to protect eggs from poachers. **Class discussion:** Just as rigging takes upfront investment before you see results, turtle conservation requires patience and long-term commitment before populations recover.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show a 30-second slow-motion video of a green sea turtle swimming through coral at Watamu Marine National Park. Ask learners:

- "How many times would we have to redraw the turtle to animate 5 seconds of swimming at 12 frames per second?" *(Answer: 60 drawings!)*
- "What if we could draw the turtle ONCE and just move her flippers?"

Introduce the concept: **A rig is a digital skeleton with controls. You build it once, then pose it forever — like a marionette puppet.** Connect to the Swahili name *Kasa* and explain that today they'll build *Kasa* as a digital puppet.

**Quick concept check:** Show the "When to Rig vs. Draw" comparison:

| Situation | Approach |
|-----------|----------|
| 5-second bouncing ball | Frame-by-frame (shape changes) |
| 30-second turtle swimming scene | **Rig!** (same character, lots of poses) |
| Full short film with Kasa | **Rig!** (saves massive time) |

---

### Step 1: Concept Introduction — What Is a Rig? (15 min)

Teach the core rigging concepts using Kasa the Green Sea Turtle as the example.

**Key terms (write on board):**
- **Pivot point:** The spot a body part rotates around (like a door hinge). For Kasa's flipper, the pivot is where the flipper meets the shell.
- **Bone:** A connected segment in a skeleton. Moving a parent bone moves all child bones.
- **Parenting:** Connecting parts so moving the shell also moves the head and flippers attached to it.
- **Pivot rig (Level 1):** Separate body parts, each with its own rotation point. Simplest rig.
- **Bone rig (Level 2):** A connected skeleton — hip → spine → head, with limb bones branching out.

**Show the rig plan on the board:**

```
Kasa's Rig Plan (Level 1 — Pivot Rig):

        [Head]
          |
    [Shell/Body] ── pivot center
       / | | \
  [FL] [FR] [RL] [RR]
   front-left, front-right, rear-left, rear-right flippers

Each flipper pivots where it meets the shell.
The head pivots at the neck.
```

**Code Block — Scratch Pivot Rig (Level 1, Ages 12-14):**

In Scratch, each body part is a separate sprite. You set the **costume center** (pivot point) for each sprite, then use `turn` blocks to pose them.

```scratch
// === KASA RIG IN SCRATCH ===
// Step 1: Create 6 sprites — Shell, Head, Front-Left Flipper,
//          Front-Right Flipper, Rear-Left Flipper, Rear-Right Flipper
// Step 2: For EACH sprite, set the costume center to the pivot point:
//   - Shell: center of shell
//   - Head: bottom of neck (where it joins shell)
//   - Each flipper: the end closest to the shell

// Step 3: Position all sprites to assemble Kasa:

// [Shell sprite] — the body, stays in center
when green flag clicked
go to x: 0 y: 0
point in direction 90

// [Head sprite] — positioned above the shell
when green flag clicked
go to x: 0 y: 45
point in direction 90

// [Front-Left Flipper] — pivot at shell edge
when green flag clicked
go to x: -25 y: 5
point in direction 120

// --- SWIMMING ANIMATION ---
// Animate the front-left flipper sweeping (paddling motion):

when [swim] button clicked
repeat 10
  turn left 5 degrees   // flipper sweeps forward
  wait 0.05 seconds
end
repeat 10
  turn right 5 degrees  // flipper sweeps back
  wait 0.05 seconds
end

// Repeat this pattern for all 4 flippers, offsetting
// the timing so front and rear flippers alternate
// (just like a real turtle swims!)
```

**For Blender users (Level 2-3, Ages 15-17) — Bone Rig Steps:**

```python
# === KASA BONE RIG IN BLENDER ===
# Step-by-step in the Blender viewport (no scripting needed,
# but here's the Python equivalent for reference):

import bpy

# 1. In Edit Mode, create bones for Kasa's skeleton:
#    Hip (center of shell) → Spine → Neck → Head
#    Hip → Front-Left-Flipper → Flipper-Tip
#    Hip → Front-Right-Flipper → Flipper-Tip
#    Hip → Rear-Left-Flipper → Flipper-Tip
#    Hip → Rear-Right-Flipper → Flipper-Tip

# 2. Add an Armature (Shift+A → Armature → Single Bone)
# 3. Extrude bones (E key in Edit Mode) to build the skeleton
# 4. Parent the turtle mesh to the armature with automatic weights:
#    Select mesh, then Shift-select armature, Ctrl+P → With Automatic Weights

# 5. Test the rig — pose the front-left flipper:
bpy.ops.object.mode_set(mode='POSE')
armature = bpy.context.active_object

# Select the front-left flipper bone and rotate it
bone = armature.pose.bones["Front-Left-Flipper"]
bone.rotation_euler = (0, 0, 0.5)  # rotate 0.5 radians ≈ 28 degrees

# 6. KEY POINT: The flipper should rotate from the shoulder
#    (where it meets the shell), NOT from the tip.
#    If it rotates from the wrong point, check:
#    - Bone roll direction
#    - Weight painting (select mesh, Weight Paint mode)
```

**The 3 most important bones for Kasa:**
1. **Hip/Shell center** — center of gravity, everything connects here
2. **Neck** — controls head direction (where Kasa looks = where she swims)
3. **Front flipper bones** — these do the swimming animation, the main action

---

### Step 2: Guided Practice — Build Kasa's Rig Together (15 min)

Walk through building the rig step by step. Learners follow along.

**For Scratch (Level 1):**

1. **Draw the parts:** Open Scratch. Create 6 new sprites. For each, draw one part of Kasa:
   - Shell (oval body with shell pattern)
   - Head (smaller oval with eyes)
   - 4 flippers (paddle shapes, slightly curved)
   
2. **Set pivot points:** For each sprite, go to the Costumes tab → click "Set Costume Center" → drag the crosshair to where the part connects to the shell. **This is the most important step!** If the pivot is wrong, the flipper will rotate from its tip instead of its base.

3. **Assemble Kasa:** Use `go to x: __ y: __` blocks to position all parts together. The shell is the base; flippers go at the corners; the head goes on top.

4. **Test one flipper:** Add the `turn` block code from Step 1 to the front-left flipper. Click it. Does the flipper paddle from its base? If it spins from the center or the tip, fix the costume center.

**For Blender (Level 2):**

1. Import or model a simple turtle shape (can be basic — a shell sphere + head + 4 flipper cylinders).
2. Add Armature, build bones from the shell center outward.
3. Parent with automatic weights (Ctrl+P → With Automatic Weights).
4. Pose the front-left flipper bone in Pose Mode — does the mesh follow?

**Common rigging mistake (tell learners now):**
> "Pivot in the wrong place: the flipper rotates from the tip instead of the shoulder. Fix: move the pivot point / costume center to where the flipper meets the shell."

---

### Step 3: Independent Practice — Animate Kasa Swimming (20 min)

Learners build their own version and animate a simple swimming cycle.

**Challenge:** Make Kasa swim across the screen by alternating her flipper movements.

**Scratch starter code:**

```scratch
// === KASA SWIMMING CYCLE ===
// On the SHELL sprite (controls overall movement):

when green flag clicked
forever
  // Kasa glides forward — smooth swimming
  glide 1 secs to x: (x position + 50) y: (y position - 10)
  // Slight up-down bob = natural swimming arc
  glide 1 secs to x: (x position + 50) y: (y position + 10)
end

// On each FLIPPER sprite — alternating paddle motion:
// Front-left and rear-right paddle together,
// then front-right and rear-left paddle together.

// [Front-Left Flipper]
when green flag clicked
forever
  repeat 8
    turn left 4 degrees
    wait 0.03 seconds
  end
  repeat 8
    turn right 4 degrees
    wait 0.03 seconds
  end
end

// [Front-Right Flipper] — OFFSET: starts when front-left finishes
when green flag clicked
wait 0.48 seconds   // half a cycle offset
forever
  repeat 8
    turn right 4 degrees   // opposite direction (mirror)
    wait 0.03 seconds
  end
  repeat 8
    turn left 4 degrees
    wait 0.03 seconds
  end
end

// Rear flippers: same pattern, smaller rotation (2 degrees)
// — rear flippers steer, front flippers power the swimming
```

**Blender challenge:** Keyframe the front-left flipper at 3 positions (extended, mid-stroke, folded) across 12 frames. Copy the keyframes to create a loop. Offset the right-side flippers by 6 frames. Play back — does Kasa look like she's swimming?

**Success check:** Kasa moves across the screen with flippers paddling in an alternating rhythm. The motion looks like real swimming, not flailing.

---

### Step 4: Sharing & Feedback (10 min)

Learners present their rigged Kasa to the class or in small groups.

**Critique framework (from Prompt 06):**
- **I notice…** (state what you see — "I notice the flippers alternate left and right")
- **I wonder…** (ask a question — "I wonder if the rear flippers could move less?")
- **What if…** (suggest an idea — "What if Kasa could turn her head to look around?")

**Celebrate:** Every working rig is an achievement — rigging is one of the hardest parts of animation. Applaud learners who got even one flipper working correctly.

**Class discussion questions:**
- "How many drawings would this swimming animation have taken frame-by-frame? How long did the rig take instead?"
- "What would you add to Kasa's rig if you had more time?" *(Answers: facial expression controls, shell squash for impact, IK on front flippers for pushing off coral)*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Rig Construction | Body parts exist but are not connected; pivots are in wrong places; character falls apart when moved | Most parts assembled; some pivots correct; character holds together but looks awkward when posed | All parts assembled with correct pivot points; character poses without breaking apart; rig is functional | Rig is well-organized with correct pivots AND additional features (head turn, flipper detail, clean naming) |
| Animation Using Rig | Flippers do not move or move incorrectly; no swimming motion visible | Some flipper motion but timing is off or all flippers move simultaneously | Flippers alternate in a swimming pattern; Kasa moves across the screen with believable motion | Smooth swimming cycle with alternating flippers, natural body bob, and character personality |
| Understanding Rigging Concepts | Cannot explain what a rig is or when to use one vs. frame-by-frame | Can explain what a rig is but unsure when rigging is the better choice | Clearly explains what a rig is, when to rig vs. draw, and why pivots matter | Explains rigging concepts AND can compare pivot rigs vs. bone rigs, with examples of when each is better |

---

## Extended Activity

**Homework/Project: Rig Pweza the Octopus**

Kasa has 4 flippers — but *Pweza the Octopus* has **8 arms**! Challenge learners to build a rig for an octopus character. Each arm needs 2-3 bone segments (upper arm, lower arm, tip) for realistic curling motion. This is an advanced rigging challenge that connects to the next lesson on secondary motion and overlap.

**Conservation connection:** Research why octopuses are important to Kenya's reef ecosystems. How does overfishing affect octopus populations? What can coastal communities do? Write 3 sentences connecting rigging complexity to biodiversity complexity.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-drawn turtle body part sprites (Scratch) or a pre-modeled turtle mesh (Blender) so they focus only on rigging, not drawing. Start with just 2 flippers (front only) before adding rear flippers. Use the Scratch pivot rig only. | Build a full bone rig in Blender with IK (Inverse Kinematics) on the front flippers — drag the flipper tip and the whole arm follows. Add a shape key for Kasa blinking her eyes. Create a turn-around rig (Kasa can face left, right, and forward). |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Kasa the Green Sea Turtle example engaging? Did learners connect with the local animal?
- [ ] Did the Scratch pivot rig work well for younger learners, or did they struggle with the costume center concept?
- [ ] Was the Blender bone rig too complex for first-time riggers? Should I scaffold more next time?
- [ ] What would I change next time? (Consider: more time on pivot points, pre-made assets for struggling learners, or splitting into two lessons — pivot rigs and bone rigs separately)
- [ ] Did the conservation discussion about turtle protection at Watamu resonate with learners?