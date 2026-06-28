# Lesson Plan 22: Compositing & Rendering — Making It Look Finished

**Module Reference:** Prompt 22 — 22-compositing-rendering.md  
**Duration:** 70 min  
**Age Group:** 12-17  
**Animation Tool:** Krita (compositing) / Blender (rendering)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports / Computer Science |
| Sub-strand | Digital Animation — Compositing, Layering & Output |
| Core Competency | Creativity & Imagination, Digital Literacy, Communication & Collaboration |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Explain what compositing is and identify at least 3 layers (background, midground, character, effects) in a finished animation.
2. Apply compositing techniques — layering for depth, shadows, and color correction — to an animation featuring a whale shark, and render it to a shareable video file.
3. Value the craft of finishing and presenting work professionally, and understand how visual storytelling can raise awareness about marine conservation.

## Key Inquiry Question

> How do we take a rough animation of **Papa Shinga the Whale Shark** gliding through the ocean and make it look like a finished, cinematic scene — then export it as a video we can share?

---

## Resources

- **Krita** (free, downloadable) for compositing and rendering — or **Blender** (free) for 3D compositing and rendering
- Projector or shared screen for demonstration
- Reference footage of whale sharks in Kenya's Indian Ocean (search "whale shark Watamu")
- Pre-made layered Krita file (`.kra`) with: ocean background layer, whale shark character layer, small fish foreground layer (or learners use their own animation from a previous lesson)
- *Optional:* Raspberry Pi with Krita or Blender for low-resource settings
- Headphones (if adding sound/music to the final render)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Whale Shark — *Papa Shinga* (Swahili)  
**Habitat:** Open ocean waters near Watamu and Diani, Kenya's Indian Ocean coast. Whale sharks visit Kenya's waters seasonally (October–February) to feed on plankton.  
**Why this animal?** The whale shark is the **largest fish in the ocean** — up to 12 meters long. This massive scale makes it perfect for teaching **layering for depth**: the whale shark appears huge in the midground, tiny reef fish dart in the foreground, and the open ocean stretches into a blurred background. The whale shark's gentle, slow drifting motion also benefits from **atmosphere effects** (blue water tint, light rays from the surface, floating particles) that transform a flat animation into an underwater scene.  
**Conservation note:** The whale shark is classified as **Endangered** by the IUCN. Major threats include boat strikes (tourism boats getting too close) and fishing. The Kenya Wildlife Service (KWS) runs a **tagging program** to track whale shark movements and has established tourism guidelines to prevent harassment. **Class discussion:** A finished, polished animation of a whale shark can be shared online to raise awareness — compositing and rendering are the skills that make conservation messages look professional enough for people to share.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Show two versions of the same whale shark animation:

1. **Version A (unfinished):** A flat, single-layer animation of a whale shark shape moving across a white background. Looks like a rough sketch.
2. **Version B (finished):** The same whale shark gliding through layered blue ocean, with light rays from above, tiny fish in the foreground, a vignette darkening the edges, and a slight blue tint.

Ask learners: **"What's the difference? Same animation, same character — so what changed?"**

Guide them to notice:
- **Layers** (background ocean, midground whale shark, foreground fish)
- **Color** (blue underwater tint)
- **Light** (light rays from the surface)
- **Depth** (foreground fish are sharper, background is softer)
- **Vignette** (corners are slightly darker)

Introduce the concept: **Compositing is putting all the pieces together like a sandwich. Each layer is separate. Professional animation ALWAYS composites — nothing is "one drawing."** Then: **Rendering is turning your project into a video file you can share.**

**The Compositing Sandwich:**

```
TOP LAYER:    Color correction, vignette, film grain
EFFECTS:      Light rays, dust particles, bubbles
CHARACTER:    Papa Shinga the whale shark (animated)
MIDGROUND:    Distant coral, water haze
BACKGROUND:   Deep blue ocean, light from surface
```

---

### Step 1: Concept Introduction — Compositing Layers & Effects (15 min)

Teach compositing concepts using the whale shark scene as the example.

**Concept 1: Layering for Depth**

| Layer | Detail Level | Color Saturation | Blur |
|-------|-------------|-------------------|------|
| Background (deep ocean) | Low detail, muted blue | Low | Slightly blurred |
| Midground (whale shark) | Medium detail | Normal | Sharp |
| Foreground (small fish) | High detail, most saturated | High | Sharpest |

**Concept 2: Shadows & Light**
- **Drop shadow:** A soft shadow beneath the whale shark on the ocean floor — grounds the character
- **Rim light:** A bright edge on the whale shark's back (light coming from the surface above) — separates it from the blue background
- **Light rays:** Vertical beams of light filtering down from the ocean surface

**Concept 3: Effects (Simple Versions)**
- **Particles/bubbles:** Small white dots floating upward — adds life to the underwater scene
- **Atmosphere/fog:** A semi-transparent blue layer between the viewer and the background — thickens with distance, creates underwater depth
- **Vignette:** Darken the corners of the frame — draws the eye to the whale shark in the center

**Concept 4: Color Correction**
- **Blue tint:** Add a slight blue color over everything → instantly feels underwater
- **Brightness/Contrast:** Slightly lower brightness, raise contrast → more cinematic
- **Saturation:** Slightly lower saturation for deep ocean, keep the whale shark's spots vibrant

**Code Block — Krita Compositing Steps (Layer-by-Layer):**

```text
=== COMPOSITING PAPA SHINGA IN KRITA ===

STEP 1: Set up your layers (bottom to top)
─────────────────────────────────────────
Layer 1 (BOTTOM):   "Background Ocean" — fill with deep blue gradient
                    (dark blue at bottom → lighter blue at top)
Layer 2:            "Light Rays" — white vertical lines, 20% opacity,
                    use Soft Light blend mode
Layer 3:            "Whale Shark" — your animated character
                    (import your animation frames or draw directly)
Layer 4:            "Foreground Fish" — small fish silhouettes,
                    sharp and dark in the bottom corners
Layer 5:            "Bubbles/Particles" — small white dots,
                    40% opacity, scattered across the frame
Layer 6:            "Atmosphere" — semi-transparent blue fill,
                    15% opacity, between viewer and background
Layer 7 (TOP):      "Vignette + Color Correction" — darkened corners
                    (radial gradient, black edges → transparent center)

STEP 2: Add the vignette
───────────────────────
1. Create a new layer at the top
2. Select the Gradient tool (G)
3. Choose Radial gradient: transparent center → black edges
4. Drag from center to corner
5. Set layer opacity to 30%
6. Set blend mode to "Multiply"
→ Instant cinematic look! The corners darken, eye goes to center.

STEP 3: Add rim light to the whale shark
─────────────────────────────────────────
1. Create a layer ABOVE the whale shark layer
2. Set blend mode to "Screen" or "Linear Dodge"
3. Pick a light blue-white color
4. Paint a thin bright line along the whale shark's back
   (where light from the surface would hit)
5. Set opacity to 50%
→ The whale shark now separates from the blue background.

STEP 4: Add bubbles (particle effect)
──────────────────────────────────────
1. Create a layer above the atmosphere layer
2. Pick a small round brush, white color, 40% opacity
3. Dots small circles scattered around the whale shark
4. For animation: make bubbles drift upward over frames
   (frame 1: bubble at y=200, frame 12: bubble at y=100)
```

---

### Step 2: Guided Practice — Composite the Whale Shark Scene Together (15 min)

Walk through building the composited scene step by step. Learners follow along in Krita.

1. **Open Krita.** Create a new document: 1280×720 pixels, 12 FPS (or 24 for smoother animation).

2. **Build the background:** Create the bottom layer. Use the Gradient tool to fill with a vertical gradient: dark blue (#0a3d5c) at the bottom → medium blue (#1a6b8a) at the top. This is the open ocean at Diani.

3. **Add light rays:** New layer above background. Use a soft white brush to paint 3-4 diagonal lines from the top of the frame going down. Set opacity to 20%, blend mode: Soft Light. These are sun beams filtering through the ocean surface.

4. **Place the whale shark:** Import the whale shark animation (or draw a simple whale shark silhouette — wide body, flat head, white spots). Position it in the center, slightly below middle. This is the **midground**.

5. **Add foreground fish:** New layer above the whale shark. Draw 2-3 small, dark fish silhouettes in the bottom corners. They should be **sharper and darker** than the whale shark — they're closer to the camera. This creates instant depth.

6. **Add the vignette:** Top layer. Radial gradient, transparent center → dark edges. Opacity 30%, blend mode: Multiply. **Ask: "See how the eye now goes straight to the whale shark?"**

7. **Quick polish — blue tint:** Create a final adjustment layer. Fill with blue (#1a5c8a). Opacity 15%, blend mode: Overlay. The whole scene now feels underwater.

**Check:** Does the scene have depth? Can learners identify each layer and why it's there?

---

### Step 3: Independent Practice — Polish & Render (20 min)

Learners complete their composited scene and render it to a video file.

**Challenge:** Add at least 3 compositing elements to your whale shark animation, then render it as an MP4.

**Rendering in Krita:**

```text
=== RENDERING IN KRITA ===

PRE-RENDER CHECKLIST:
[ ] Output path set (you KNOW where the file is going)
[ ] Resolution: 1280x720 (720p minimum for sharing)
[ ] FPS: 12 (cartoon) or 24 (smooth) — match your animation
[ ] Audio included (if you added sound)
[ ] File format: MP4 (for sharing)

STEPS:
1. File → Render Animation
2. In the Render dialog:
   - Output: choose your folder (e.g., /home/student/whale-shark-animation/)
   - Format: MP4 (H.264)
   - FPS: 12
   - Resolution: 1280 x 720
   - Check "Include audio" if you have a sound layer
3. Click "Render"
4. Wait for the progress bar to finish
5. Navigate to your output folder — find the .mp4 file
6. Double-click to play it in your video player!

TROUBLESHOOTING:
- If MP4 fails: export as PNG sequence instead, then use
  a video editor or FFmpeg to combine:
  ffmpeg -framerate 12 -i frame_%04d.png -c:v libx264
    -pix_fmt yuv420p whale-shark.mp4
- If the file is too big: reduce resolution to 854x480 (480p)
- If you can't find the file: check the output path you set!
```

**Rendering in Blender (for 3D users):**

```python
# === BLENDER RENDER SETTINGS ===
# 1. Open Output Properties (printer icon on right panel)
# 2. Set output path FIRST:
#    //home/student/whale-shark-render/whale_shark.mp4
# 3. Set format:

import bpy

# Output settings
bpy.context.scene.render.filepath = "/home/student/whale-shark-render/whale_shark.mp4"
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'

# Resolution & FPS
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.fps = 24

# 4. Render: Ctrl+F12 (or Render → Render Animation)
# 5. Check the output path — Blender saves to /tmp by default!
#    ALWAYS verify where your file is going.

bpy.ops.render.render(animation=True)
```

**Success check:** Each learner has a composited whale shark animation rendered as an MP4 (or GIF for short loops) that they can play and share.

---

### Step 4: Sharing & Feedback (10 min)

Learners play their rendered videos for the class or in small groups.

**Critique framework:**
- **I notice…** ("I notice the light rays make it feel really underwater")
- **I wonder…** ("I wonder if the vignette could be darker?")
- **What if…** ("What if you added bubbles rising from the whale shark?")

**Class discussion:**
- "Which compositing effect made the biggest difference? Was it the vignette, the rim light, or the depth layering?"
- "How would you share this animation to raise awareness about whale shark conservation? YouTube? School presentation? Social media?"
- "What format did you render in and why?" *(MP4 for sharing, GIF for short loops, PNG sequence for importing to other software)*

**File format cheat sheet (display on board):**

| Format | Use For | Pros | Cons |
|--------|---------|------|------|
| MP4 (H.264) | Sharing anywhere | Universal, good quality, small file | Can't edit layers |
| GIF | Short loops, social media | Loops, no player needed | Limited colors, big files |
| PNG Sequence | Importing to other software | Highest quality, lossless | Many files, need to assemble |

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Compositing — Layering | All elements on one layer; no depth or separation between background, character, and foreground | Some elements separated into layers but depth is flat; foreground and background look the same sharpness | Clear layer separation: background is muted/blurred, midground (whale shark) is sharp, foreground adds depth | Layering creates strong depth; additionally uses atmosphere, blur gradient, and scale contrast between whale shark and foreground fish |
| Effects & Polish | No effects added; scene looks flat and unfinished | 1 effect added (e.g., vignette OR rim light) but scene still looks rough | 3+ effects added (vignette, rim light, particles/bubbles, color tint); scene looks finished and cinematic | Effects are layered thoughtfully and support the mood; color correction enhances the underwater feeling; overall look is professional |
| Rendering & Export | Did not render or cannot find the output file | Rendered but wrong format, wrong resolution, or file is unplayable | Successfully rendered to MP4 at 720p+ with correct FPS; file is playable and shareable | Rendered at 1080p with audio; understands format trade-offs (MP4 vs GIF vs PNG); can troubleshoot render issues |

---

## Extended Activity

**Homework/Project: Conservation Awareness Render**

Render your whale shark animation with a **title card** at the beginning: "Papa Shinga — The Gentle Giant of Watamu" and an **end card** with a conservation fact: "Whale sharks are endangered. Boat strikes and fishing are their biggest threats. Support KWS tagging programs."

Share the rendered video with your family or on social media. Count how many people watch it — you're using animation skills for conservation awareness!

**Connect to next lesson:** Save your rendered video — it will be a key piece in your animation portfolio (Lesson 23: Portfolio & Career Path).

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide a pre-made Krita file with layers already set up — learners only need to adjust opacity and blend modes to see the effect. Focus on just 2 effects: vignette + color tint. Render as GIF (simpler than MP4). | Use Blender's Compositor node system to build a node-based compositing tree. Add a glare node for the light rays, a lens distortion node, and a color balance node. Render at 1080p with ambient underwater sound. Experiment with depth of field (background blur). |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the Papa Shinga the Whale Shark example engaging? Did the scale of the animal help teach depth and layering?
- [ ] Did learners successfully render their animations, or did rendering cause confusion (file paths, formats)?
- [ ] Was the Krita compositing workflow clear, or should I provide a pre-made layered file next time?
- [ ] What would I change next time? (Consider: more time on rendering, pre-made assets for struggling learners, or a dedicated rendering troubleshooting session)
- [ ] Did the conservation connection — using finished animation to raise awareness — resonate with learners?