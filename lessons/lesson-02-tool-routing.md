# Lesson Plan 2: Tool Routing — Choosing the Right Animation Software

**Module Reference:** Prompt 2 — 02-tool-routing.md  
**Duration:** 75 min  
**Age Group:** 12-16  
**Animation Tool:** Multiple — Scratch, Stop Motion Studio, Krita, Blender (demonstration); Python for decision-tree coding  

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Computer Science |
| Sub-strand | Algorithms & Decision-Making |
| Core Competency | Critical Thinking & Problem Solving, Digital Literacy |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:

1. **Explain** how a decision tree works and why matching the right tool to the right person matters in animation (and in problem-solving generally).
2. **Build** a working tool-recommendation program in Python (or a flowchart in Scratch) that takes a student's age, experience, and interests and outputs the best animation tool for them.
3. **Value** the principle of starting simple and progressing step by step — just as Pweza the Octopus uses different arms for different tasks.

## Key Inquiry Question

> Pweza the Octopus has **eight arms** for eight different jobs. How do we build a
> program that picks the **right animation tool** for each student — the way Pweza
> picks the right arm?

---

## Resources

- Computers with Python 3 installed (or Replit.com / Trinket.io for browser-based Python)
- Scratch (alternative for learners who prefer visual coding)
- Printed "Tool Cards" — one card per tool (Scratch, Stop Motion Studio, Pencil2D, Krita, Synfig Studio, OpenToonz, Blender) with age range, difficulty, and what it's best for
- Projector for live demo of each tool (2-min tour of each)
- Reference image of an octopus (Pweza) for the metaphor
- Optional: Raspberry Pi with Python 3 for low-resource settings

---

## Local Context: Kenyan Ocean Animal

**Animal:** Octopus (*Octopus cyanea*) — **Pweza** in Swahili  
**Habitat:** Coral reefs of Watamu Marine National Park, Mombasa Marine National
Park, and Diani-Chale Marine Reserve. The day octopus lives in crevices and
holes on the reef, coming out to hunt crabs and shrimp.  
**Why this animal?** An octopus has **eight arms**, each capable of a different
task — touching, gripping, tasting, swimming, jetting away. This is a perfect
metaphor for **tool routing**: the animation assistant has many tools (Scratch,
Krita, Blender…) and must choose the right one for each student's needs, just as
Pweza chooses the right arm for each job. Octopuses are also famous problem-solvers
(opening jars, navigating mazes) — which connects to the algorithmic thinking this
lesson teaches.  
**Conservation note:** Octopuses are not currently endangered, but they face
pressure from reef destruction, overfishing, and coral bleaching. KWS protects
their reef habitat within marine parks. Octopuses are highly intelligent — some
scientists argue they are the smartest invertebrates — which makes protecting
their habitat even more important. Learners can reflect on how an animal this
clever deserves a healthy reef.

---

## Lesson Development

### Introduction (8 min)

**Hook:** Show a short video or photo of an octopus using different arms for
different tasks — gripping a rock, reaching into a crack, jetting away from a
predator. Ask learners:

- *"How many arms does Pweza have? Does she use all of them the same way?"*
- *"What would happen if Pweza tried to use her jet-propulsion arm to carefully
  pick up an egg?"*

Explain: **Pweza has the right arm for the right job.** In animation, we have
many software tools — but if a 10-year-old tries to learn Blender before they've
tried Scratch, it's like using a jet arm to pick up an egg. Today we'll build a
program that matches the right tool to the right person.

### Step 1: Concept Introduction — Decision Trees & the Tool Library (15 min)

**Teach the concept:** A **decision tree** is a set of yes/no questions that lead
to a recommendation. It's how the animation assistant decides which tool to
recommend.

Show the full tool decision tree on the board (from the prompt module):

```
Age 10-12, no experience:
  → Scratch (likes coding) OR Stop Motion Studio (likes crafts/LEGO)

Age 10-12, some Scratch experience:
  → Pencil2D

Age 12-14, likes drawing:
  → Krita

Age 12-14, doesn't want to draw every frame:
  → Synfig Studio

Age 14-17, serious about animation:
  → OpenToonz (2D) OR Blender (3D)

Age 14-17, wants 3D specifically:
  → Blender
```

Give a 2-minute tour of each tool (show the interface on the projector):
- **Scratch:** Block-based, colourful, drag-and-drop — for young beginners
- **Stop Motion Studio:** Phone/tablet app, frame-by-frame with a camera — for
  kids who like physical making
- **Pencil2D:** Simple drawing timeline — the bridge from Scratch to "real" animation
- **Krita:** Professional drawing tools + animation timeline — for artists
- **Synfig Studio:** Tweening-focused, you set key poses and the software fills
  in between — for kids who don't want to draw every frame
- **OpenToonz:** Professional 2D studio software (used by Studio Ghibli!) — for
  serious 2D animators
- **Blender:** Full 3D suite + Grease Pencil 2D — for 3D and serious teens

Now show how this decision tree becomes **Python code**:

```python
def recommend_tool(age, experience, interests):
    """
    Pweza's Tool Router — picks the right animation tool for a student.
    Like an octopus choosing the right arm for the job!

    age: number (10-17)
    experience: "none" | "some" | "intermediate" | "advanced"
    interests: list of strings like ["drawing", "coding", "3d", "lego/clay"]
    """

    # Branch 1: Young beginners (10-12)
    if age <= 12 and experience == "none":
        if "coding" in interests or "storytelling" in interests:
            tool = "Scratch"
            project = "bouncing ball sprite"
            principle = "timing"
        elif "lego/clay" in interests:
            tool = "Stop Motion Studio"
            project = "LEGO walk cycle"
            principle = "timing"
        else:
            tool = "Scratch"
            project = "bouncing ball sprite"
            principle = "timing"

    # Branch 2: Young with some experience (10-12, knows Scratch)
    elif age <= 12 and experience in ("some", "intermediate"):
        tool = "Pencil2D"
        project = "bouncing ball with squash & stretch"
        principle = "squash-and-stretch"

    # Branch 3: Middle group who likes drawing (12-14)
    elif age <= 14 and "drawing" in interests:
        tool = "Krita"
        project = "bouncing ball with squash & stretch"
        principle = "squash-and-stretch"

    # Branch 4: Middle group who doesn't want to draw every frame
    elif age <= 14:
        tool = "Synfig Studio"
        project = "tweened shape morph"
        principle = "slow-in-and-slow-out"

    # Branch 5: Older teens who want 3D (14-17)
    elif age >= 14 and "3d" in interests:
        tool = "Blender"
        project = "keyframed cube bounce"
        principle = "timing"

    # Branch 6: Older teens, serious 2D path (14-17)
    elif age >= 14:
        tool = "OpenToonz"
        project = "character head turn"
        principle = "anticipation"

    # Fallback
    else:
        tool = "Scratch"
        project = "bouncing ball sprite"
        principle = "timing"

    # Return the result like the prompt module's output format
    print(f"Recommended tool: {tool}")
    print(f"Why: Best match for age {age}, experience '{experience}'.")
    print(f"Alternative: Try Pencil2D if {tool} feels too advanced.")
    print(f"First project: {project}")
    print(f"Animation principle focus: {principle}")
    return tool, project, principle


# --- TEST IT: Pweza helps three different students ---

print("=" * 50)
print("Student 1: 10-year-old who loves coding")
print("=" * 50)
recommend_tool(age=10, experience="none", interests=["coding", "storytelling"])

print()
print("=" * 50)
print("Student 2: 13-year-old artist")
print("=" * 50)
recommend_tool(age=13, experience="none", interests=["drawing"])

print()
print("=" * 50)
print("Student 3: 15-year-old who wants 3D")
print("=" * 50)
recommend_tool(age=15, experience="some", interests=["3d", "coding"])
```

**Teaching point:** Walk through how the `if/elif` branches mirror the decision
tree. Each branch is like one of Pweza's arms — a different path for a different
situation. The `return` statement packages the recommendation just like the
animation assistant's output format.

### Step 2: Guided Practice — Run and Modify the Router (15 min)

Learners follow along step by step.

1. **Open Python** → Use IDLE, Thonny, or go to Trinket.io / Replit.com for
   browser-based Python (no installation needed).
2. **Type (or paste) the code** from Step 1 into the editor.
3. **Run it** → Click Run. You should see three student recommendations printed.
4. **Verify:** Student 1 should get Scratch, Student 2 should get Krita, Student
   3 should get Blender. Does it match?
5. **Add a new student:** Add a fourth test call at the bottom:

```python
print()
print("=" * 50)
print("Student 4: 11-year-old who loves LEGO")
print("=" * 50)
recommend_tool(age=11, experience="none", interests=["lego/clay"])
```

6. **Run again** → Student 4 should get Stop Motion Studio.
7. **Modify a branch:** What if a 12-year-old has "some" experience and likes
   drawing? Trace the code: `age <= 12` is True, but `experience == "none"` is
   False, so it falls through to the `elif age <= 12 and experience in (...)`
   branch → Pencil2D. Is that the right choice? Discuss as a class.

**Check:** Can every learner explain what each `if/elif` branch does? Can they
trace one student profile through the code and predict the output?

### Step 3: Independent Practice — Extend Pweza's Router (20 min)

Learners extend the decision tree with new features.

**Challenge choices (pick at least one):**

**Option A: Add platform checking**
Add a `platform` parameter ("windows", "mac", "linux", "chromebook", "ipad").
If the platform is "chromebook", only recommend web-based tools (Scratch web
edition). Print a warning if a desktop-only tool would have been recommended.

```python
def recommend_tool(age, experience, interests, platform="any"):
    # ... existing code ...
    # After choosing the tool, check platform:
    desktop_only = ["Pencil2D", "Krita", "Synfig Studio", "OpenToonz", "Blender"]
    if platform == "chromebook" and tool in desktop_only:
        print(f"NOTE: {tool} doesn't run on Chromebook. Use Scratch web edition instead!")
        tool = "Scratch (web)"
    # ... return ...
```

**Option B: Add a "difficulty score"**
Print a difficulty rating (1-5 stars) for the recommended tool:
- Scratch: ⭐ (1 star)
- Stop Motion Studio: ⭐⭐ (2 stars)
- Pencil2D: ⭐⭐ (2 stars)
- Krita: ⭐⭐⭐ (3 stars)
- Synfig Studio: ⭐⭐⭐ (3 stars)
- OpenToonz: ⭐⭐⭐⭐ (4 stars)
- Blender: ⭐⭐⭐⭐⭐ (5 stars)

**Option C: Build it in Scratch instead**
For learners who prefer visual coding, build the decision tree as a Scratch
project using `ask` blocks and `if/else` blocks:

```scratch
when [green flag] clicked
ask [How old are you?] and wait
set [age] to (answer)
ask [Have you used Scratch before? (yes/no)] and wait
set [used_scratch] to (answer)
if <(age) < (13)> then
    if <(used_scratch) = [yes]> then
        say [Try Pencil2D! It is the next step after Scratch.] for (4) seconds
    else
        say [Start with Scratch! It is perfect for you.] for (4) seconds
    end
else
    ask [Do you like drawing? (yes/no)] and wait
    if <(answer) = [yes]> then
        say [Try Krita! Great drawing tools plus animation.] for (4) seconds
    else
        say [Try Synfig Studio! It tweens for you.] for (4) seconds
    end
end
```

### Step 4: Sharing & Feedback (10 min)

Learners demonstrate their tool router. Each presenter runs their program with a
classmate's real profile (age, experience, interests) and shows the
recommendation.

**Critique questions:**
1. *"Did the router pick a tool that actually makes sense for that person?"*
2. *"Can you trace the code and explain WHY it picked that tool?"*
3. *"Is there a case where the router gives a bad recommendation? How would you
   fix it?"*

Celebrate learners who added creative features (platform checking, difficulty
scores, error handling).

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Decision tree understanding | Cannot explain how the if/elif branches lead to different recommendations | Can explain the concept but cannot trace a specific profile through the code | Can trace any student profile through the code and correctly predict the output | Can explain the decision tree, trace profiles, and identify cases where the logic could be improved |
| Code implementation | Code does not run or has syntax errors that prevent execution | Code runs but gives wrong recommendations for some test cases | Code runs correctly for all provided test cases and matches the decision tree | Code runs correctly AND includes at least one extension (platform check, difficulty score, error handling) |
| Tool knowledge | Cannot name more than 2 animation tools or their appropriate age groups | Names 3-4 tools but confuses which age group they suit | Names all 7 tools and correctly matches each to its appropriate age group and use case | Names all tools, explains trade-offs between them, and can justify why one tool is better than another for a specific student |

---

## Extended Activity

**Homework: Pweza's Reef Survey**

Pweza needs to recommend the right hiding spot for each reef animal. Build a
second decision tree program (`recommend_shelter`) that takes an animal's size
and swimming speed and recommends a reef shelter:

- Small + fast → coral branch crevice (like clownfish in an anemone)
- Small + slow → under a rock (like a crab)
- Large + fast → open water near drop-off (like a dolphin)
- Large + slow → seagrass bed (like a green sea turtle)

This practises the same `if/elif` logic with a conservation-themed scenario. It
connects to the next lesson (Project Guide) where learners will follow
step-by-step instructions to build their first animation.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Provide the full Python code from Step 1; task is to run it and test with 3 profiles, not write new code | Add input validation: check that age is between 10-17, print an error message if not |
| Use the Scratch visual coding option (Option C) instead of Python — block-based logic is easier to trace | Add a database (dictionary) of tool details and have the program print a full "Tool Card" with features, download link, and tutorial suggestion |
| Work in pairs — one reads the decision tree, one types the code | Convert the decision tree into a recursive function that can handle nested conditions (e.g., "if 12-14 AND likes drawing AND has a drawing tablet → Krita; if no tablet → Pencil2D") |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the octopus (Pweza) metaphor effective for explaining decision trees?
- [ ] Did the Python code work in the classroom setup, or did I need to troubleshoot installations?
- [ ] Were the tool demos too rushed? Should I spend more time on each tool next time?
- [ ] What would I change next time?