# Lesson Plan 55: Stop Motion with Nature & Found Objects — Animating the Real World

**Module Reference:** Prompt 55 — 55-nature-found-objects.md  
**Duration:** 80 min  
**Age Group:** 10-17  
**Animation Tool:** Stop Motion Studio (phone app, free), Raspberry Pi + camera (alternative)

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Creative Arts & Sports |
| Sub-strand | Stop Motion Animation — Nature & Found Object Animation |
| Core Competency | Creativity & Imagination, Digital Literacy, Environmental Awareness |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. **Collect** natural materials responsibly from Kenya's coastal environment (leaves, stones, twigs, shells, sand) following respect-nature rules.
2. **Create** characters from found objects (stone + twig = person, shell = body, leaves = wings) and animate them using Stop Motion Studio.
3. **Tell** a short environmental story through nature stop motion, connecting animation to conservation.

## Key Inquiry Question

> Can a **seashell from Watamu beach** become a swimming turtle, and can stones and twigs tell a story about protecting Kenya's ocean?

---

## Resources

- Phone with Stop Motion Studio app (free, iOS/Android)
- Phone stand or tripod (for stable overhead capture)
- Natural materials: fallen leaves, stones, twigs, seashells, sand, flowers (collected responsibly)
- Found objects: keys, coins, buttons, bottle caps (with permission)
- Flat surface (tray, table, or ground outdoors)
- Optional: Raspberry Pi + Pi Camera + Python stop motion script for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Sea Turtle (created from found objects) — **Kasa** in Swahili  
**Habitat:** conceptually — Kenya's beaches and marine parks  
**Why this approach?** Kenya's coastline is rich with natural materials perfect for stop motion: seashells from Watamu, driftwood from Diani, coral fragments (dead/broken only — never live coral), sand, and coastal plants. Building a turtle from a smooth beach stone (shell) and four small twigs (flippers) connects learners directly to their environment. The animation isn't ABOUT the ocean — it's MADE FROM the ocean's gifts.  
**Conservation note:** Collect responsibly — take only fallen/dead materials, never pull living plants or take live coral. Return natural materials to where you found them when done. Don't litter a beach with animation props. This lesson IS about environmental respect.

---

## Lesson Development

### Introduction (10 min)

**Hook:** Hold up a smooth beach stone and four small twigs. Ask: *"What animal could this become?"*

Arrange them: stone flat on the table, twigs sticking out as flippers, a small pebble as the head. *"It's a sea turtle. And with a phone camera, we can make it swim."*

Show a short clip of Ainslie Henderson's nature puppet stop motion (or similar found-object animation). Explain: *The world is your toy box. Every object can become a character. Today we animate the real world — using materials from Kenya's coast.*

### Step 1: Collect with Respect (10 min)

**Rules for collecting (teach these FIRST):**
- Take fallen leaves and twigs, not living ones
- Never pull up wildflowers by the root — snip the stem if needed
- Leave enough for wildlife — don't strip a bush bare
- Avoid rare or protected species — when in doubt, leave it
- Only take dead/broken coral, NEVER live coral
- Return natural materials to where you found them when done
- Don't litter a beach with your animation props

**Material collection (outdoor or pre-collected):**
| Material | What It Becomes | Source |
|----------|----------------|--------|
| Smooth beach stone | Turtle shell / whale body | Watamu/Diani beach |
| Small twigs | Flippers, legs, arms | Ground (fallen only) |
| Seashells | Bodies, shields, hats | Beach |
| Sand | Ground/ocean floor | Beach |
 Fallen leaves | Wings, fins, seaweed | Ground |
| Driftwood | Backgrounds, reefs | Beach |

**Found objects from home (with permission):**
Keys, coins, buttons, bottle caps, paper clips, string, fabric scraps

### Step 2: Building Characters & Basic Animation (20 min)

**Build Kasa the Turtle:**
1. Place a smooth stone flat on the surface (shell)
2. Position four small twigs at the corners (flippers)
3. Add a tiny pebble at the front (head)
4. Add a leaf behind (trailing seaweed or tail)

**Animate Kasa swimming — 10 frames:**

```python
# For Raspberry Pi stop motion (alternative to phone app)
# Uses Pi Camera to capture frames

from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1280, 720)

frame = 1
print("Stop Motion Studio — Raspberry Pi Edition")
print("Press Enter to capture frame, type 'done' to finish")

while True:
    command = input(f"Frame {frame}: Press Enter to capture or type 'done': ")
    if command == "done":
        break
    camera.capture(f"/home/pi/animation/frame_{frame:03d}.jpg")
    print(f"Captured frame {frame}")
    frame += 1

print(f"Done! Captured {frame-1} frames.")
print("Use ffmpeg to combine: ffmpeg -framerate 12 -i frame_%03d.jpg -s 1280x720 output.mp4")
```

**Animation steps (for phone app):**
1. Open Stop Motion Studio
2. Position phone overhead using stand
3. Frame 1: Take photo of Kasa in starting position
4. Move twigs slightly forward (swim stroke) → Frame 2
5. Move twigs more → Frame 3
6. Move head pebble slightly → Frame 4
7. Continue for 10 frames
8. Play back at 5-8 fps

### Step 3: Environmental Story Animation (25 min)

**Challenge:** Create a 15-second nature stop motion with an environmental message.

**Story options:**
1. **Turtle meets plastic:** Kasa the stone-turtle is swimming (frame by frame). A plastic bottle cap drifts in. Kasa approaches it, mistaking it for food. A fish made of leaves swims in and pushes the cap away. Message: "Plastic doesn't belong in our ocean."
2. **Reef restoration:** Broken coral fragments are scattered. Frame by frame, they arrange themselves into a reef pattern. Leaf-fish appear. The reef comes alive. Message: "We can rebuild what's broken."
3. **Crab cleanup:** A bottle-cap crab is walking on the beach (sand surface). It finds plastic pieces and carries them off-screen one by one. Message: "Even the smallest can make a difference."

**Checklist:**
- [ ] Built character(s) from natural/found materials
- [ ] Animated at least 15 frames
- [ ] Story has a clear beginning, middle, end
- [ ] Environmental message is clear (doesn't need to be preachy)
- [ ] Materials collected responsibly
- [ ] Played back — does it tell the story?

### Step 4: Sharing & Cleanup (15 min)

**Present animations to the class.** Discuss:
- *"What story did your materials tell?"*
- *"What was the hardest part of animating real objects?"*
- *"Did any 'happy accident' happen (wind moved a leaf, stone rolled) that you kept?"*

**Cleanup: CRITICAL**
- Return all natural materials to where they were found
- Compost leaves and twigs
- Return stones and shells to the beach
- Recycle any plastic props used in the animation
- Leave the space cleaner than you found it

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Character Building | Object doesn't read as a character | Somewhat recognizable but unclear | Clear character from found objects | Creative use of 3+ materials; character has personality |
| Animation | Jerky, objects shift between frames | Some smoothness but inconsistent | Smooth movement, objects stay in place between frames | Smooth + varied movement + multiple characters interacting |
| Environmental Story | No story or message | Story exists but unclear | Clear story with environmental message | Story + message + emotional impact + creative use of materials |
| Responsible Collection | Didn't follow collection rules | Followed some rules | Followed all collection rules + cleaned up | Followed rules + cleaned up + taught others about responsible collection |

---

## Extended Activity

**Coastal Field Trip Animation:** If possible, take the class to a Kenyan beach (Watamu, Diani, or Mombasa). Collect materials on-site, set up phone stands on the sand, and animate directly on the beach. The wind, light changes, and waves become part of the animation. This is the Nelson-Atkins approach — filming directly outdoors with nature. The outdoor challenges (wind moving the set, changing light, insects visiting) become creative opportunities, not problems.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide pre-collected materials | Animate a lifecycle: seed growing into plant, caterpillar to butterfly (using leaves) |
| Use 8 frames instead of 15 | Use Raspberry Pi + Python for time-lapse outdoor animation (wind effects, tide changes) |
| Focus on character building (skip story) | Add sound effects and voiceover (record ocean sounds on phone) |
| Work in pairs (one moves, one captures) | Create multi-scene story with different materials for each setting |

---

## Teacher Reflection

- [ ] Did learners collect materials responsibly?
- [ ] Could they build recognizable characters from found objects?
- [ ] Was the environmental message organic to the animation or forced?
- [ ] Did the cleanup happen properly — all materials returned?
- [ ] Would an outdoor session (at a beach) be feasible for next time?