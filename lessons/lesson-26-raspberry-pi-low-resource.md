# Lesson Plan 26: Raspberry Pi & Low-Resource Animation — You Don't Need a Fancy Computer

**Module Reference:** Prompt 26 — 26-raspberry-pi-low-resource.md  
**Duration:** 80 min  
**Age Group:** 12-14  
**Animation Tool:** Python + Pygame on Raspberry Pi (also works on any Linux computer or Chromebook with Python)

---

## CBE Strand Mapping

| CBE Field | Value |
|-----------|-------|
| Strand | Computer Science |
| Sub-strand | Programming & Digital Media Creation |
| Core Competency | Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Identify at least two animation tools that run on a Raspberry Pi or low-resource computer and explain what each is good for.
2. Write and run a Python (Pygame) program that animates a jellyfish character pulsing and drifting across the screen, demonstrating squash & stretch.
3. Explain how limited hardware (slower CPU, less RAM) affects animation work and describe at least two strategies to work effectively within those limits.

## Key Inquiry Question

> A jellyfish (*Pweza*'s cousin) pulses its bell to move through the water —
> squashing and stretching with every beat. How can we make a Raspberry Pi
> do the same thing with just 30 lines of Python code?

---

## Resources

- Raspberry Pi 3, 4, or 5 (with Raspberry Pi OS desktop) OR any computer with Python 3 and Pygame installed
- Monitor, keyboard, and mouse for each Pi/station
- MicroSD card (16GB+) with Raspberry Pi OS
- Reference photos or video of a jellyfish pulsing (search "jellyfish swimming slow motion" on YouTube)
- Optional: Pi Camera Module + push button + breadboard + jumper wires (for the stop-motion extension)
- Printed copy of the Python code starter (for learners who need paper reference)
- Internet connection (for installing Pygame if not pre-installed)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Jellyfish (Swahili: *Ng'ombe wa Bahari* is sometimes used informally, but most Kenyan coastal communities simply call them *medusa* or *jellyfish* — no single common Swahili name is widely used)  
**Habitat:** Found throughout Kenya's Indian Ocean waters — visible in Mombasa Marine National Park, Watamu Marine National Park, and along the coast seasonally. Moon jellyfish and box jellyfish drift through the reef areas.  
**Why this animal?** The jellyfish is the PERFECT low-resource animation character. Its body is a simple dome (bell) that you can draw with one Python circle. Its movement — pulsing the bell to propel itself — is a natural squash & stretch cycle. You don't need complex artwork, a powerful GPU, or 3D rendering. A jellyfish animation teaches the most important animation principle (squash & stretch) with the LEAST computing power. It's the ultimate "you don't need a fancy computer" animal.  
**Conservation note:** Jellyfish populations are actually increasing in some areas due to ocean warming and overfishing of their predators (turtles and tuna). While jellyfish themselves are not endangered, their population boom is a warning sign of reef ecosystem imbalance. When sea turtle (*kasa*) populations drop — from plastic pollution and bycatch — jellyfish numbers rise because turtles are one of their main predators. Protecting turtles protects the balance of the whole reef.

---

## Lesson Development

### Introduction (10 min)

Start with a question: *"Raise your hand if you think you need an expensive
gaming computer to make animations."* Most learners will raise their hands.

Now show them a 30-second video of a jellyfish pulsing through the water
in slow motion. Ask:
- *"What shape is the jellyfish's body?"* (A dome / half-circle)
- *"What happens when it moves?"* (The bell squashes down, then stretches
  back up — that's the pulse)
- *"How many colors do we need to draw this?"* (Just one or two!)

Tell learners: **Today, we're going to animate this jellyfish pulsing and
drifting across the screen using a Raspberry Pi and about 30 lines of
Python code. No gaming PC required.**

Explain the philosophy from the module: *"You CAN animate on what you have.
A Raspberry Pi costs about the same as a textbook. It's not fast, but it
WORKS. Slower rendering means more thinking time between renders."*

### Step 1: Concept Introduction — Animation on Raspberry Pi (15 min)

Briefly introduce what runs on a Raspberry Pi and what doesn't:

| Tool | Runs on Pi? | Good For |
|------|-------------|----------|
| Scratch | ✅ Yes (pre-installed) | Block-based animation, ages 10-13 |
| Python + Pygame | ✅ Yes (pre-installed) | Code-based animation, sprite sheets, ages 13-17 |
| Stop Motion (Pi Camera + Python) | ✅ Yes | Physical stop motion with a push button |
| Pencil2D | ✅ Yes (Pi 4/5) | Hand-drawn 2D animation |
| Blender | ❌ No (too heavy) | Needs a dedicated GPU |
| OpenToonz | ❌ No (x86 only) | Professional 2D, no ARM build |

Then introduce the animation principle of the day: **Squash & Stretch.**

- When the jellyfish pulses, the bell **squashes** (gets shorter and wider)
- When it recovers, the bell **stretches** (gets taller and narrower)
- The volume stays the same — it's just the SHAPE that changes
- This is the #1 principle that makes animation feel alive

Show the class this diagram on the board:

```
  REST        SQUASH       STRETCH      REST
   ⌒           ___          ⌒⌒          ⌒
  /   \        |   |        | |         /   \
 |     |  →    |___|   →    | |   →    |     |
  \___/         ‾‾‾         | |         \___/
                            ‾‾‾
  Normal      Compressed    Elongated   Normal
  (wide)      (short+wide)  (tall+narrow) (wide)
```

Now show the Python code that does this. Walk through it line by line:

```python
# Jellyfish Pulse Animation — Raspberry Pi + Pygame
# Demonstrates: squash & stretch, drift movement, frame-based animation
# Runs on: Raspberry Pi 3, 4, or 5 (or any computer with Python + Pygame)

import pygame
import math

pygame.init()

# Screen setup — keep it small for Pi performance
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pweza the Jellyfish — Squash & Stretch")
clock = pygame.time.Clock()

# Colors (ocean theme)
OCEAN_BLUE = (10, 50, 100)
JELLY_PINK = (255, 180, 200)
JELLY_DARK = (200, 120, 160)

# Jellyfish properties
jelly_x = 100       # starting position (left side)
jelly_y = 240
base_width = 80     # rest size
base_height = 60
pulse_speed = 0.08  # how fast it pulses (radians per frame)
drift_speed = 1     # how fast it drifts right

frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- ANIMATION LOGIC ---
    frame += 1

    # Squash & stretch: use a sine wave to cycle between squash and stretch
    # sin oscillates between -1 and 1, so we use it to scale the bell
    pulse = math.sin(frame * pulse_speed)  # -1.0 to 1.0

    # When pulse > 0: STRETCH (tall and narrow)
    # When pulse < 0: SQUASH (short and wide)
    # Volume stays roughly constant: width * height ≈ base_width * base_height
    current_width = base_width - (pulse * 15)   # narrower when stretching
    current_height = base_height + (pulse * 15)  # taller when stretching

    # Drift: jellyfish slowly moves right, with a gentle vertical bob
    jelly_x += drift_speed
    jelly_y += math.sin(frame * 0.03) * 0.5  # gentle up-down bob

    # Wrap around when it reaches the right edge
    if jelly_x > 700:
        jelly_x = -60

    # --- DRAW ---
    screen.fill(OCEAN_BLUE)

    # Draw the jellyfish bell (an ellipse that changes shape = squash & stretch)
    bell_rect = pygame.Rect(0, 0, int(current_width), int(current_height))
    bell_rect.center = (int(jelly_x), int(jelly_y))
    pygame.draw.ellipse(screen, JELLY_PINK, bell_rect)

    # Draw tentacles (simple lines that trail below the bell)
    for i in range(5):
        tentacle_x = jelly_x - 30 + (i * 15)
        tentacle_sway = math.sin(frame * 0.05 + i) * 5  # gentle sway
        pygame.draw.line(
            screen, JELLY_DARK,
            (tentacle_x, jelly_y + current_height // 2),
            (tentacle_x + tentacle_sway, jelly_y + current_height // 2 + 40),
            2
        )

    pygame.display.flip()
    clock.tick(30)  # 30 FPS — smooth enough, not too heavy for Pi

pygame.quit()
```

Key things to point out:
- The `pulse` variable uses `math.sin()` to oscillate — this creates the
  natural squash/stretch cycle without manually keyframing
- `current_width` and `current_height` change in opposite directions so
  the VOLUME stays constant (this is the squash & stretch rule)
- `clock.tick(30)` runs at 30 FPS — fast enough to look smooth, slow
  enough that the Pi doesn't overheat
- The screen is only 640×480 — small resolution means better performance

### Step 2: Guided Practice — Run It Together (15 min)

Have every learner (or pair) open a terminal on their Raspberry Pi and
type along with you:

**Step 1: Check that Pygame is installed**
```bash
python3 -c "import pygame; print('Pygame version:', pygame.version.ver)"
```
If it prints a version number, you're ready. If you get an error, install it:
```bash
sudo apt update
sudo apt install python3-pygame
```

**Step 2: Create the file**
```bash
mkdir ~/animation
nano ~/animation/jellyfish.py
```
(Or use the Mu editor / Thonny if available — easier for beginners than nano.)

**Step 3: Paste the code from Step 1 into the file and save it.**

**Step 4: Run it!**
```bash
cd ~/animation
python3 jellyfish.py
```

Walk around the room as animations start appearing on screens. Common
issues and fixes:
- **Black screen / no window:** Make sure you're running from the desktop,
  not over SSH without X11 forwarding. Raspberry Pi OS desktop is required.
- **Jellyfish is too fast:** Change `pulse_speed = 0.08` to `0.04`
- **Jellyfish is too slow:** Change `pulse_speed = 0.08` to `0.15`
- **Colors look wrong:** Check that the RGB values are correct (0-255 range)

Ask learners to observe: *"When does the jellyfish look squashed? When
does it look stretched? Does the overall size (volume) change?"*

### Step 3: Independent Practice — Make It Yours (20 min)

Challenge learners to modify the jellyfish animation in at least TWO of
these ways:

**Option A — Change the animal (beginner):**
Change the colors and shape to make a different ocean animal:
- Green Sea Turtle (*Kasa*): change the ellipse to a flatter oval, make
  it green `(50, 150, 80)`, remove tentacles, add flipper rectangles
- Clownfish: make the ellipse orange `(255, 130, 0)`, add white stripes
  (draw small white rectangles on top), make it dart instead of drift

**Option B — Add a second character (intermediate):**
Add a second jellyfish (or a different animal) that drifts in from the
right side. Use different colors and a different pulse speed so they
don't move in sync.

```python
# Add a second jellyfish — add these variables near the top:
jelly2_x = 600
jelly2_y = 300
jelly2_color = (180, 220, 255)  # light blue jellyfish

# Add this inside the while loop, after drawing the first jellyfish:
jelly2_x -= 0.5  # drifts LEFT (opposite direction)
if jelly2_x < -60:
    jelly2_x = 700

pulse2 = math.sin(frame * 0.06)  # different pulse speed = out of sync
bell2_rect = pygame.Rect(0, 0,
    int(base_width - pulse2 * 15),
    int(base_height + pulse2 * 15))
bell2_rect.center = (int(jelly2_x), int(jelly2_y))
pygame.draw.ellipse(screen, jelly2_color, bell2_rect)
```

**Option C — Add interactive control (advanced):**
Make the jellyfish respond to keyboard input:
- UP/DOWN arrows move it vertically
- LEFT/RIGHT arrows change drift speed
- SPACE bar makes it do a big pulse (squash hard, then stretch far)

```python
# Add this inside the event loop:
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        pulse_speed = 0.3  # big fast pulse!
    if event.key == pygame.K_UP:
        jelly_y -= 20
    if event.key == pygame.K_DOWN:
        jelly_y += 20
```

Remind learners: **Save often! Raspberry Pi can crash under heavy load.**
Press `Ctrl+S` in the editor every few minutes.

### Step 4: Sharing & Performance Notes (10 min)

Have learners (or pairs) show their animation on the projector or to a
neighboring pair. Discuss:

- *"What did you change? How does it look different from the original?"*
- *"Did the Pi handle it smoothly, or did it slow down when you added a
  second character?"*

Share the **Pi-Specific Tips** from the module:

| Tip | Why It Matters |
|-----|----------------|
| Add a heatsink or fan | Pi gets hot during rendering; overheating causes crashes |
| Render to USB drive, not SD card | SD cards wear out from repeated writes |
| Use the official Pi power supply | Underpower = random crashes |
| Save often | Pi can crash under load; don't lose your work |
| Keep resolution small (640×480) | Smaller screen = faster rendering |

Tell learners: *"This Pi is not fast. But it WORKS. Every animation you
just made was created on a $35 computer. That's the point — you don't need
expensive hardware to start. You need curiosity and patience."*

**Upgrade path:** If learners outgrow the Pi, the next step is any used
laptop with 8GB RAM — that can run Blender for 3D animation. But for 2D
code-based animation, the Pi is perfect.

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Code execution | Code does not run; errors not resolved | Code runs but jellyfish does not move or pulse | Code runs; jellyfish pulses with visible squash & stretch and drifts across screen | Code runs smoothly; squash & stretch is clearly visible and volume stays constant; movement feels organic |
| Understanding squash & stretch | Cannot explain what squash & stretch means | Describes squash & stretch but cannot identify it in their own code | Explains how the sine wave creates squash & stretch and why volume must stay constant | Explains the principle AND can modify the code to change the squash/stretch amount and speed intentionally |
| Low-resource awareness | Does not know what tools run on Pi | Lists 1 tool that runs on Pi | Lists 2+ tools that run on Pi and 1+ that does not; explains why Blender won't run | Explains Pi performance tradeoffs (resolution, FPS, cooling) and can recommend tools for different Pi models (3 vs 4 vs 5) |

---

## Extended Activity

**Homework / Follow-up: Push-Button Stop Motion Studio**

If the school has Pi Camera Modules and push buttons, learners can build
a physical stop-motion station following the Raspberry Pi Foundation's
official "Push Button Stop Motion" project:

1. Connect a Pi Camera Module and a push button to the GPIO pins
2. Install the software:
   ```bash
   sudo apt install python3-picamzero
   ```
3. Write a Python script that captures a photo every time the button is
   pressed
4. Animate a clay or LEGO crab (*Kaa*) moving across a sand surface
   (mchanga) — crabs are found on Kenyan beaches and are great stop-motion
   subjects
5. Assemble the frames into a video:
   ```bash
   ffmpeg -r 10 -i frames/frame%03d.jpg -qscale 2 crab_animation.mp4
   ```

This connects to the next lesson (Kid-Friendly FAQ) where learners will
learn to answer common animation questions — including "What computer do
I need?" and "Can I animate on a Raspberry Pi?"

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide the full code pre-printed on paper so they can type it in without worrying about writing it from scratch. Pair them with a more experienced learner. Focus on getting the code to RUN and observing the squash & stretch, rather than modifying it. | Challenge them to add a background (draw a reef at the bottom of the screen using rectangles and polygons), add color gradient to the ocean (dark blue at bottom, lighter at top), or implement frame-rate-independent animation using `clock.get_time()` instead of a fixed frame counter. Extra challenge: add a school of small fish (samaki) that the jellyfish drifts past. |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes? Could they run the code and see squash & stretch?
- [ ] Was the jellyfish a good example for squash & stretch on a Pi?
- [ ] Did the Raspberry Pi hardware perform adequately, or were there too many crashes/lag?
- [ ] Was the Python code at the right level, or did learners struggle with the syntax?
- [ ] What would I change next time?