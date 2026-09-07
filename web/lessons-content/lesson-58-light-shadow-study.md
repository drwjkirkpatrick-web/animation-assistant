# Lesson Plan 58: Light, Shadow & Ambient Occlusion — Making Things Feel Solid

**Module Reference:** Prompt 58 — 58-light-shadow-study.md  
**Duration:** 80 min  
**Age Group:** 12-17  
**Animation Tool:** Paper & pencils (observation), Krita (painting light/shadow), Blender (3D lighting)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports + Integrated Science |
| Sub-strand | Light, Shadow & Optics in Animation |
| Core Competency | Creativity & Imagination, Critical Thinking & Problem Solving |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Observe** real-world lighting and identify 5 components: highlight, terminator, core shadow, reflected light, and cast shadow.
2. **Explain** that shadows are NOT black — they have color (cool blue from sky, warm from reflected ground light).
3. **Apply** ambient occlusion (dark crevices where light can't reach) and 3-point lighting to an animation scene featuring a Kenyan ocean animal.

## Key Inquiry Question

> Why does a **manta ray** silhouetted against the ocean surface light look so dramatic — and how do real-world light and shadow make our animated characters feel solid and three-dimensional?

---

## Resources

- Paper and pencils (for outdoor observation)
- A white ball or egg (for light observation exercise)
- Krita (for painting light and shadow on 2D animation)
- Blender (for 3-point lighting setup, advanced)
- Reference photos/video of manta rays from below (silhouette against surface light)
- Optional: flashlight or lamp (for indoor lighting demo)
- Optional: Raspberry Pi with Krita for digital painting

---

## Local Context: Kenyan Ocean Animal

**Animal:** Manta Ray (*Mobula birostris*) — occasionally spotted in Kenya's waters  
**Habitat:** Open ocean along Kenya's coast, sometimes seen at Diani-Chale Marine Reserve.  
**Why this animal?** Manta rays seen from below are dramatic silhouettes against the bright ocean surface — a perfect example of light creating form. The dark ray against the light water is pure contrast. But look closer: the ray's underside isn't pure black — it has reflected light from the water below. The water isn't pure white — it has color gradients from depth. This one image teaches all 5 light components at once.  
**Conservation note:** Manta rays are Vulnerable. They are slow-breeding and threatened by fishing and habitat degradation. KWS monitors manta ray sightings as part of marine biodiversity tracking.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Take a white ball (or egg) outside on a sunny day. Put it on white paper. Ask learners to sit and LOOK for 2 full minutes.

Ask: *"How many different shades of light and dark can you see on this white ball?"*

Learners will notice:
- The brightest spot (highlight — where the sun hits directly)
- The shadow side (but it's NOT black — it has color!)
- The shadow on the paper (cast shadow — but it's not black either!)
- The dark crescent where the ball meets the paper (contact shadow / ambient occlusion)

Explain: *Realism isn't just about movement. It's about how light wraps around objects, how shadows have COLOR, and how dark crevices make things feel three-dimensional. Today we study light — and use a manta ray to understand it.*

### Step 1: The 6 Principles of Light & Shadow (15 min)

**1. Observe Real-World Light**
- Light WRAPS around objects — it doesn't stop at a hard edge
- There's a gradient from light to dark called the TERMINATOR
- Shadows are NOT black — they have color (cool blue from sky, warm from ground)

**2. The 5 Components of Light on Any Object:**

```
         ☀ SUN
          |
    ┌─────┴─────┐
    |  HIGHLIGHT |  ← Brightest spot (sun hits directly)
    |───────────|
    | TERMINATOR |  ← Where light transitions to shadow
    |───────────|
    | CORE SHADOW|  ← Darkest part of the shadow side
    |───────────|
    | REFLECTED  |  ← Light bounced back from ground/sky
    |   LIGHT    |     (shadows are NEVER as dark as you think)
    └─────┬─────┘
          |
    ===CAST SHADOW=== ← Shadow on the ground (has color, not black)
    ==CONTACT/AO==    ← Darkest where object meets ground
```

**3. Shadows Have COLOR**
- Outdoor shadow = cool blue/purple (lit by blue sky, not sun)
- Indoor shadow = warm (lit by reflected light from walls/floor)
- Underwater shadow = deep teal (light filtered through water)

**4. Ambient Occlusion (AO)**
- Crevices, corners, and areas where objects meet are DARKER
- Light can't reach into tight spaces → they're naturally darker
- This is what makes objects feel "grounded" and "solid"
- The contact shadow where a foot meets the ground is AO
- The dark crack between two rocks is AO

**5. 3-Point Lighting (for animation scenes)**

| Light | Position | Purpose |
|-------|----------|---------|
| Key light | Front-left, 45° up | Main light — defines shape |
| Fill light | Front-right, softer | Fills shadows (less harsh) |
| Rim/back light | Behind, above | Separates character from background |

**6. Underwater Lighting (for ocean scenes)**
- Light comes from ABOVE (surface)
- Light rays filter through water (god rays / caustics)
- Color shifts: warm near surface, cool/blue at depth
- Particles in water scatter light (haze/fog effect)

### Step 2: Painting Light on a Sea Turtle (20 min)

**In Krita, paint light and shadow on a sea turtle:**

1. Draw a simple sea turtle shape (flat color base)
2. Determine light direction: from above (sun through ocean surface)
3. Add HIGHLIGHT on the top of the shell (brightest)
4. Add TERMINATOR on the sides (gradient from light to shadow)
5. Add CORE SHADOW on the underside (darkest part of the turtle)
6. Add REFLECTED LIGHT on the bottom edges (light bouncing off the ocean floor)
7. Add CONTACT SHADOW under the turtle on the seafloor
8. Add AMBIENT OCCLUSION where flippers meet the shell (dark crevices)

```
Color guide for underwater scene:
- Highlight:     pale yellow-green (#C4D8B0) — sun through water
- Mid tone:      sea green (#5B8A72) — turtle's base color
- Core shadow:   dark teal (#1A4A4A) — NOT black, blue-green
- Reflected:     lighter teal (#4A8A8A) — light from below
- Cast shadow:   dark blue-green (#2A5A5A) — on the seafloor
- AO (crevices): very dark teal (#0A2A2A) — where flippers meet shell
```

```scratch
// In Scratch, simulate light/shadow with costume changes:
// Costume 1: Flat color (no shading) — looks fake
// Costume 2: With highlight and shadow — looks 3D

when [green flag] clicked
switch costume to [turtle-flat]
say [This is flat color — no light or shadow] for (3) seconds
switch costume to [turtle-shaded]
say [Now with highlight, shadow, and AO — feels solid!] for (3) seconds
```

### Step 3: Manta Ray Silhouette Scene (20 min)

**Challenge:** Create a scene with a manta ray silhouetted against the ocean surface light.

**In Krita (2D):**
1. Background: gradient from deep blue (bottom) to bright blue-white (top = surface)
2. Manta ray: dark silhouette (but NOT pure black — use dark teal #0A3A3A)
3. Add reflected light on the ray's edges (light from the water below)
4. Add god rays: light beams coming from the surface (semi-transparent yellow-white)
5. Add particles: small dots floating in the water (light scattering)

**In Blender (3D, advanced):**
```python
# Blender Python: Set up underwater 3-point lighting for a manta ray scene

import bpy

# Key light (sun from above = ocean surface)
bpy.ops.object.light_add(type='SUN', location=(0, 0, 10))
key_light = bpy.context.active_object
key_light.name = "Surface_Light"
key_light.data.energy = 3.0
key_light.data.color = (0.9, 0.95, 0.8)  # Slightly green-blue (water filter)

# Fill light (from below = reflected from seafloor)
bpy.ops.object.light_add(type='AREA', location=(0, 0, -5))
fill_light = bpy.context.active_object
fill_light.name = "Reflected_Light"
fill_light.data.energy = 50
fill_light.data.color = (0.3, 0.5, 0.6)  # Cool teal
fill_light.data.size = 5

# Rim light (from behind = separation from background)
bpy.ops.object.light_add(type='SPOT', location=(0, -5, 3))
rim_light = bpy.context.active_object
rim_light.name = "Rim_Light"
rim_light.data.energy = 200
rim_light.data.color = (0.8, 0.9, 1.0)  # Pale blue

# Set world background to underwater gradient
world = bpy.context.scene.world
world.use_nodes = True
bg = world.node_tree.nodes["Background"]
bg.inputs[0].default_value = (0.05, 0.15, 0.25, 1.0)  # Deep ocean blue
bg.inputs[1].default_value = 1.0

print("Underwater 3-point lighting set up! Add your manta ray model and render.")
```

### Step 4: Sharing & Feedback (10 min)

Show the flat (no lighting) vs shaded (with lighting) versions side by side. Discuss:
- *"Which one feels more three-dimensional? Why?"*
- *"Can you see the 5 light components?"*
- *"Are the shadows black or colored? What color are they?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Light Observation | Cannot identify light components | Identifies 2-3 components | Identifies all 5 components in real observation | Identifies 5 + explains color of shadows + AO concept |
| Shading Application | Flat color only (no shading) | Some shading but shadows are black | All 5 components with colored shadows | 5 components + AO + reflected light + underwater color shift |
| Scene Quality | No sense of depth or lighting | Basic lighting but flat | Clear 3D feel with proper light direction | Dramatic scene with god rays, particles, and mood lighting |

---

## Extended Activity

**Underwater Conservation Scene:** Create a full underwater scene featuring a sea turtle swimming through a Kenyan coral reef. Apply all 6 light principles: surface light from above, god rays filtering through water, colored shadows on the reef, ambient occlusion in coral crevices, reflected light from the sandy bottom, and particles scattering light. Add a plastic bag drifting in the light as a conservation element — its unnatural whiteness contrasts with the reef's natural colors.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Use 3 light components only (highlight, shadow, cast shadow) | Use Blender: full 3-point lighting + AO shader + caustics |
| Work on paper with pencil (grayscale only) | Paint in Krita with full color: warm highlights, cool shadows |
| Focus on the outdoor observation exercise | Study Marco Bucci's painting tutorials (online) for advanced light theory |
| Provide pre-drawn turtle outline to shade | Create a time-of-day lighting study: same scene at noon, sunset, and night |

---

## Teacher Reflection

- [ ] Did learners understand that shadows are NOT black?
- [ ] Could they identify the 5 light components in the outdoor observation?
- [ ] Was the manta ray silhouette an effective example of dramatic lighting?
- [ ] Did the underwater lighting context connect to their experience of Kenya's ocean?
- [ ] Would more time on outdoor observation (before screen work) improve results?