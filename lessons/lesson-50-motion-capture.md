# Lesson Plan 50: Motion Capture & Mocap — Real Performance to Digital Animation

**Module Reference:** Prompt 50 — 50-motion-capture.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Phone camera + Rokoko Vision (free AI mocap) or DeepMotion, Blender (cleanup)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports + Computer Science |
| Sub-strand | Motion Capture Technology & Digital Performance |
| Core Competency | Digital Literacy, Critical Thinking & Problem Solving |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Explain** how motion capture works (track joints → build skeleton → apply to character).
2. **Use** a free AI mocap tool (Rokoko Vision or DeepMotion) to turn a video of their own movement into animation data.
3. **Clean up** mocap data by fixing foot sliding, adding exaggeration, and adjusting timing.

## Key Inquiry Question

> What if you could record yourself swimming like a **sea turtle (Kasa)** and the computer turned your motion into animation — how would you make it feel like a turtle and not a human?

---

## Resources

- Phone with camera (for recording movement)
- Internet access for Rokoko Vision (com.rokoko.com/vision — free, browser-based) or DeepMotion (deepmotion.com — free tier)
- Blender (free, for cleanup and applying mocap to a character) — optional for advanced
- Open space for recording movement
- Reference video of sea turtles swimming at Watamu
- Optional: Raspberry Pi for viewing results (not for processing mocap)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Green Sea Turtle (*Chelonia mydas*) — **Kasa** in Swahili  
**Habitat:** Seagrass beds in Watamu Marine National Park, Diani-Chale Marine Reserve.  
**Why this animal?** Turtles "fly" through water with graceful, sweeping flipper motions. For mocap, learners record themselves doing turtle-like swimming motions (standing and sweeping arms in large arcs). The AI tracks their joints and creates a skeleton. Then they modify the skeleton to feel like a turtle — slower, heavier, more graceful. This teaches the key mocap lesson: *mocap gives you 90% of the motion, you add the last 10% of the character.*  
**Conservation note:** Green sea turtles are Endangered. They eat plastic bags mistaking them for jellyfish. KWS and Local Ocean Trust protect nesting sites at Watamu.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show a short clip of a video game character running. Ask: *"How do game characters move so realistically? Someone animated every frame by hand?"*

Answer: *No — they used motion capture. A real person moved, cameras tracked their joints, and the computer turned it into animation data. The person IS the character. Today we'll do it with a phone and free AI tools.*

Show a video of a sea turtle swimming. Ask: *"Could we capture a HUMAN doing this motion and turn it into turtle animation? Let's find out."*

### Step 1: How Mocap Works (15 min)

**The 3-step process:**
1. **Track the joints:** AI identifies your body parts (head, shoulders, elbows, hips, knees, ankles) in each video frame
2. **Build a skeleton:** The computer connects the joints into a stick figure that follows your motion
3. **Apply to a character:** The skeleton drives a 3D character — when you raise your arm, the character raises its arm

**Free AI mocap tools:**
- **Rokoko Vision** (rokoko.com/vision) — free, browser-based, upload video → get BVH animation data
- **DeepMotion** (deepmotion.com) — free tier, upload video → get 3D animation
- **Blender** — import the mocap data, apply to a character, clean up

**The 90/10 Rule:**
Mocap gives you 90% of the motion. You add the last 10%:
- Fix foot sliding (feet should plant, not slide)
- Add exaggeration (push poses 15% past reality)
- Adjust timing (mocap can feel too fast or too slow)
- Add character (a turtle moves differently from a human, even with the same skeleton)

### Step 2: Recording & Processing Mocap (25 min)

**Step 1: Record the movement**
1. Find an open space (classroom cleared, or outdoors)
2. Stand far enough from the camera that the whole body is visible
3. Record a 5-second video of "turtle swimming" motion:
   - Stand with arms spread wide (like flippers)
   - Sweep both arms down in a big arc (like a power stroke)
   - Bring arms back up (recovery)
   - Repeat 3 times

**Step 2: Process with Rokoko Vision**
1. Go to rokoko.com/vision (free, browser-based)
2. Upload your video
3. Wait for AI to process (1-2 minutes)
4. Download the BVH file (motion data)

```scratch
// While we can't run mocap in Scratch, we can simulate the concept:
// 1. Record video of yourself doing a motion
// 2. Use the video as a backdrop
// 3. Animate a sprite to follow your key joint positions

// Create a "skeleton" sprite with separate body parts:
// Head, torso, left arm, right arm, left leg, right leg
// Each part follows the corresponding body part in the video

when [green flag] clicked
switch backdrop to [mocap-video-frame-1]
// Position sprite body parts to match video frame 1
go to x: (0) y: (50)    ← Head
// ... position each body part
wait (0.1) seconds
switch backdrop to [mocap-video-frame-2]
// Reposition body parts to match frame 2
// ... repeat for key frames
```

**Step 3: Clean up (in Blender or by hand)**
Common mocap problems and fixes:
- **Foot sliding:** Feet appear to slide on the ground instead of planting. Fix: lock the foot position when it should be planted.
- **Jittery data:** Small random movements from AI noise. Fix: smooth the animation curves.
- **T-pose at start:** Many mocap files start with the character in a T-pose. Fix: delete the first few frames.

### Step 3: Making It Feel Like a Turtle (20 min)

**Challenge:** Take the human mocap data and transform it into turtle animation.

**What to change:**
1. **Timing:** Slow it down by 50% — turtles are slower than humans
2. **Weight:** Add more frames at the bottom of each stroke — turtles are heavy
3. **Exaggeration:** Push the arm arcs wider — turtle flippers sweep bigger than human arms
4. **Character:** If using Blender, replace the human skeleton with a turtle model
5. **Environment:** Add underwater feel — particles, light rays, bubble effects

**Ethics note:** Mocap performers are ACTORS. When you record someone's movement, that's their performance. In professional animation, mocap performers get acting credit (like Andy Serkis for Gollum). Always credit the person who performed the motion in your animation.

### Step 4: Sharing & Feedback (10 min)

Show the original human video alongside the cleaned-up animation. Discuss:
- *"What did mocap give you for free?"*
- *"What did you have to add to make it feel like a turtle?"*
- *"Was the 90/10 rule accurate — was it 90% done and 10% cleanup?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Mocap Understanding | Cannot explain how mocap works | Explains concept but not the 3 steps | Explains track→skeleton→apply pipeline | Explains pipeline + 90/10 rule + cleanup needs |
| Tool Usage | Could not process video | Processed video but couldn't get data | Successfully processed and downloaded mocap data | Processed + imported into Blender/Scratch + applied to character |
| Character Transformation | Left raw mocap as-is | Changed speed but nothing else | Adjusted timing + weight + exaggeration | Full transformation: timing + weight + exaggeration + character model + environment |

---

## Extended Activity

**Ocean Performance Mocap:** Record three different ocean animal movements (turtle swim, dolphin jump, octopus crawl). Process all three with mocap. Create a short animation that transitions between the three characters — same skeleton, different timing and exaggeration for each animal. Add a conservation message: "Every animal moves differently — every animal matters."

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Use Rokoko Vision (easiest — upload and go) | Use Blender: import BVH mocap, apply to rigged character, use NLA editor to blend clips |
| Focus on understanding the concept (skip processing) | Clean up foot sliding with IK constraints; add jitter smoothing |
| Teacher processes one demo video for the class | Record full-body mocap with multiple actions; create a character animation reel |
| Discuss the ethics but don't require credits | Add full credits: "Motion performed by [name]. Character design by [name]." |

---

## Teacher Reflection

- [ ] Did learners understand how AI mocap works?
- [ ] Was Rokoko Vision accessible (internet speed, browser compatibility)?
- [ ] Could they see the difference between raw mocap and cleaned-up animation?
- [ ] Did the ethics discussion land — do they understand mocap performers are actors?