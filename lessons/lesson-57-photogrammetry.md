# Lesson Plan 57: Photogrammetry & 3D Scanning — Real Objects into Animation

**Module Reference:** Prompt 57 — 57-photogrammetry.md  
**Duration:** 80 min  
**Age Group:** 13-17  
**Animation Tool:** RealityScan (free phone app), Blender (import and animate)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports + Computer Science |
| Sub-strand | 3D Scanning, Photogrammetry & Digital Asset Creation |
| Core Competency | Digital Literacy, Critical Thinking & Problem Solving |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Explain** how photogrammetry works (many photos from all angles → software builds 3D model).
2. **Scan** a real object using a phone app (RealityScan) and export it as a 3D model.
3. **Import** a scanned 3D model into Blender and use it in a simple animation.

## Key Inquiry Question

> What if you could scan a real **seashell from Watamu beach** and turn it into a 3D model that a virtual turtle could hold — how does photogrammetry bridge the physical and digital worlds?

---

## Resources

- Phone with RealityScan app (free, iOS/Android) or Polycam
- Blender (free, for importing and animating scanned models)
- Objects to scan: seashells, stones, toys, shoes, coral fragments (dead only)
- Turntable or rotating surface (optional but helpful)
- Good lighting (even, no harsh shadows)
- Internet connection (for processing scans in cloud)
- Optional: Raspberry Pi (for viewing results, not for scanning)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Sea Turtle holding a scanned seashell — **Kasa** in Swahili  
**Habitat:** Conceptually — connecting real Kenyan coastal objects to digital animation  
**Why this approach?** Kenya's beaches are full of scan-worthy objects: seashells, coral fragments (dead/broken), driftwood, stones. By scanning a real seashell from Watamu and putting it in a 3D animation, learners create a direct bridge between their physical environment and their digital creations. The shell is REAL — it came from THEIR beach. No stock asset can replace that connection.  
**Conservation note:** Only scan dead/broken coral, empty shells, and non-living objects. Never take live coral or shells with living creatures inside. Respect beach collection rules — some protected areas prohibit removing any natural materials.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Hold up a seashell. Ask: *"What if I told you this shell could become a 3D model in 5 minutes — and a virtual turtle could hold it in an animation?"*

Show a before/after: photo of a real object → 3D model rotating in Blender. Explain: *This is photogrammetry — taking lots of photos from every angle and letting software build a 3D model. It's how museums digitize artifacts, how game developers create realistic environments, and how YOU can bring real Kenyan objects into your animations.*

### Step 1: How Photogrammetry Works (15 min)

**The process:**
1. **Take 30-50 photos** of an object from every angle — top, bottom, sides, all around
2. **Software finds matching points** between photos (like your eyes find matching points between left and right eye views)
3. **Computer calculates 3D positions** of all those points
4. **Builds a mesh** (3D shape) from the points
5. **Applies texture** (color) from the photos onto the mesh
6. **Result:** a 3D model you can rotate, scale, and animate

**What you can scan (and what you CAN'T):**

| Good for Scanning | Bad for Scanning |
|-------------------|-----------------|
| Seashells (solid, textured) | Shiny/reflective objects (mirrors, metal) |
| Stones and rocks | Transparent objects (glass, clear plastic) |
| Driftwood | Very thin/flat objects (paper, leaves) |
| Toys (action figures) | Moving objects (animals, people) |
| Shoes | Objects with no texture (plain white ball) |
| Coral fragments (dead) | Live coral (don't remove from reef!) |

**Free tools:**
- **RealityScan** (Epic Games, free) — easiest, phone-based, cloud processing
- **Polycam** (free tier) — similar to RealityScan
- **Meshroom** (open source, PC) — runs locally, no cloud needed

### Step 2: Scanning a Seashell (25 min)

**Step-by-step with RealityScan:**

1. **Place the object** on a surface with good, even lighting
   - Outdoor overcast day = best (soft, even light)
   - Indoor with multiple lamps = OK
   - Direct sunlight = bad (harsh shadows confuse the software)

2. **Open RealityScan** and start a new capture

3. **Walk around the object** taking photos:
   - Start at eye level, walk all the way around (15-20 photos)
   - Move higher, walk around again (10-15 photos)
   - Move lower, walk around again (5-10 photos)
   - Total: 30-50 photos from EVERY angle

4. **Review the capture** — the app shows coverage. If areas are missing, add more photos.

5. **Process** — tap "Create Model." The app uploads to cloud and processes (1-3 minutes).

6. **Export** — save as OBJ or USDZ file

**Tips for better scans:**
- Keep the object still — don't move it between photos
- Overlap photos by 60-70% (each photo should cover most of what the previous one did)
- Get close enough that the object fills most of the frame
- Include some background (helps the software calculate positions)

```python
# For Meshroom (open-source alternative on PC/Raspberry Pi)
# After taking photos with any camera:

import subprocess
import os

# Meshroom command-line processing
photos_dir = "/home/walker/scans/seashell_photos"
output_dir = "/home/walker/scans/seashell_output"

# Run Meshroom pipeline
cmd = f"meshroom_batch --input {photos_dir} --output {output_dir}"
print(f"Running: {cmd}")
# subprocess.run(cmd, shell=True)  # Uncomment to actually run
print("This will take 10-30 minutes depending on photo count and hardware")
```

### Step 3: Import into Blender & Animate (20 min)

**Import the scanned seashell:**
1. Open Blender → File → Import → Wavefront OBJ
2. Select your exported seashell file
3. The shell appears in the 3D viewport with real textures

**Simple animation — turtle finds a shell:**
1. Import or create a simple turtle shape (can be a basic model)
2. Animate the turtle moving toward the shell
3. Animate the shell being picked up (parent the shell to the turtle's flipper)
4. Add a camera and render

```python
# Blender Python script (run in Blender's Scripting tab)
# This imports a scanned OBJ and creates a simple pick-up animation

import bpy
import os

# Import the scanned seashell
bpy.ops.import_scene.obj(filepath="/path/to/seashell.obj")

# The imported shell is now selected
shell = bpy.context.active_object
shell.name = "Seashell_From_Watamu"
shell.scale = (0.5, 0.5, 0.5)  # Scale down if too large
shell.location = (3, 0, 0)  # Place it to the right

# Create a simple turtle (cube placeholder — replace with real model)
bpy.ops.mesh.primitive_cube_add(size=1, location=(-3, 0, 0))
turtle = bpy.context.active_object
turtle.name = "Kasa_Turtle"

# Animate turtle moving toward shell (frames 1-48)
turtle.location = (-3, 0, 0)
turtle.keyframe_insert(data_path="location", frame=1)

turtle.location = (2, 0, 0)  # Move close to shell
turtle.keyframe_insert(data_path="location", frame=48)

# Shell gets "picked up" at frame 60
shell.location = (2, 0, 0)
shell.keyframe_insert(data_path="location", frame=48)

shell.location = (2, 0, 1.5)  # Shell lifts up
shell.keyframe_insert(data_path="location", frame=60)

print("Animation created! Press Spacebar to play in Blender.")
```

### Step 4: Sharing & Feedback (10 min)

Learners show their scanned objects in Blender. Discuss:
- *"What was the hardest part of scanning?"*
- *"Does the 3D model look like the real object? What's different?"*
- *"How could you use this in a bigger animation project?"*

**Conservation tie-in:** *"You scanned a real shell from Kenya's coast. That shell is now digital — it'll last forever, even if the real one breaks. Museums use photogrammetry to preserve artifacts. What Kenyan ocean object would you want to preserve digitally for future generations?"*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Scanning Process | Could not complete a scan | Completed scan but model is incomplete | Full scan with good coverage and detail | Full scan + optimized + cleaned up mesh |
| Understanding | Cannot explain photogrammetry | Explains "taking photos" but not the 3D part | Explains photo→matching points→3D mesh pipeline | Explains pipeline + knows what objects scan well/poorly + why |
| Blender Integration | Could not import model | Imported but can't animate | Imported + animated in a simple scene | Imported + animated + lit + rendered a finished shot |

---

## Extended Activity

**Kenyan Coastal Object Library:** Start a class project to scan 10 objects from Kenya's coast — different shells, stones, coral fragments, driftwood pieces. Build a shared library of 3D assets that the whole class can use in their animations. This is how professional studios build asset libraries. Each object is tagged with where it was found: "Seashell — Watamu Beach — scanned March 2026."

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Use RealityScan (easiest — automated) | Use Meshroom (open source, more control over parameters) |
| Teacher scans one object for the class to share | Clean up the mesh in Blender: remove artifacts, fix holes, optimize polygons |
| Focus on the scanning (skip Blender import) | Rig the scanned object: add bones, make it movable, animate it dancing |
| Scan simple objects (round stones) | Scan complex objects (coral with many branches) and try photogrammetry challenges |

---

## Teacher Reflection

- [ ] Did learners understand how photogrammetry works?
- [ ] Was RealityScan accessible (phone compatibility, internet for processing)?
- [ ] Could they import the model into Blender successfully?
- [ ] Did the connection between real Kenyan objects and digital animation resonate?
- [ ] Would a class trip to scan objects at a beach be feasible?