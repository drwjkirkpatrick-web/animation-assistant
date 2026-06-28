# Lesson Plan 18: Workflow & File Management — Good Digital Habits

**Module Reference:** Prompt 18 — 18-workflow-file-management.md  
**Duration:** 75 min  
**Age Group:** 12-17  
**Animation Tool:** Krita (primary) — steps adaptable to Scratch / Blender / Pencil2D  

---

## CBC Strand Mapping

| CBC Field | Value |
|-----------|-------|
| Strand | Computer Science / Creative Arts & Sports |
| Sub-strand | Digital Literacy — File Management & Project Workflow |
| Core Competency | Digital Literacy, Critical Thinking & Problem Solving |
| Assessment Rubric Level | BE / AE / ME / EE |

---

## Learning Outcomes

By the end of this lesson, the learner should be able to:
1. Create a correctly named, well-structured project folder for an animation project using the `[Project]_[Version]_[Date].[ext]` naming pattern.
2. Save versioned copies (v01, v02...) at project milestones and export a finished animation with correct fps/resolution settings.
3. Value file-management habits as professional practice that protects creative work from loss.

## Key Inquiry Question

> A whale shark animation took you 3 hours — then your laptop crashed and you can't find the file. What habit would have saved your work, and how do professionals make sure this never happens?

---

## Resources

- Laptop or Raspberry Pi with Krita (or Scratch/Blender/Pencil2D)
- USB stick OR cloud account (Google Drive) for the backup demo
- Printed "Pre-Flight Checklist" (one per learner) — see Step 1
- Projector to demo folder creation and the "lost file" scenario
- Reference image of a whale shark (Papa Shinga)

---

## Local Context: Kenyan Ocean Animal

**Animal:** Whale Shark — *Papa Shinga*  
**Habitat:** Open ocean off Watamu and Diani-Chale Marine Reserve, visiting the Kenyan coast October–February.  
**Why this animal?** The whale shark is the largest fish in the ocean — animating it is a BIG project with many frames, layers, and reference files. Big projects are exactly where messy file management causes tears. It's the perfect case study: you *need* folders for reference, project, exports, and notes.  
**Conservation note:** Whale sharks are **Endangered** (IUCN). Main threats: boat strikes and fishing. KWS runs a tagging program and tourism guidelines so boats keep a safe distance. We save our files carefully — and we protect the gentle giant we're animating.

---

## Lesson Development

### Introduction (8 min)

**The "heartbreak" hook.** Tell a true-style story: *"A student spent a whole weekend animating a whale shark. On Monday the file was gone — saved as 'untitled.kra' somewhere they couldn't find. They cried. Today we make sure that never happens to you."* Ask who has ever lost a file. Most hands go up. Say: *"Professionals have a system. Today you learn it."*

### Step 1: Concept Introduction — Naming, Folders & the Pre-Flight Checklist (15 min)

Teach the three core habits (age 12-17 level). Put the **Pre-Flight Checklist** on the board:

```text
PRE-FLIGHT CHECKLIST (do BEFORE you start animating)
[ ] Created a project folder with the right name
[ ] Set the correct resolution (1280x720 or 1920x1080)
[ ] Set the correct frame rate (12 or 24 fps)
[ ] Saved the project file immediately (with a good name!)
[ ] Know exactly where exports will go
```

**Naming pattern** (the single most important rule):

```text
[ProjectName]_[Version]_[Date].[ext]

GOOD:  WhaleShark_v01_2026-06-28.kra
       WhaleShark_v02_2026-07-05.kra
       WhaleShark_final_2026-07-12.mp4

BAD:   animation1.kra
       final_final_v3.mp4
       whale thing.kra        ← spaces = trouble

RULES:
- No spaces (use _ or -)
- Version numbers ALWAYS (v01, v02, v03...)
- Date as YYYY-MM-DD (sorts alphabetically = chronological)
- Never write "final" until it's truly done
```

**Folder structure** (the version to teach this age group):

```text
MyAnimations/
├── WhaleShark/
│   ├── reference/        ← whale shark photos, video clips
│   ├── project/          ← the .kra project file(s)
│   ├── exports/          ← exported MP4s / GIFs / PNGs
│   │   ├── v01/
│   │   ├── v02/
│   │   └── final/
│   └── notes/            ← ideas, feedback, storyboard sketches
└── _Archive/             ← old projects (don't delete, archive)
```

> **The golden rule:** *Never overwrite your only copy.* Finished the keyframes? Save as **v02** before you start inbetweening. Mess up? Go back to v01.

### Step 2: Guided Practice — Set Up the Whale Shark Project Together (18 min)

Walk through every step as a class; learners follow on their own machines.

```text
STEP-BY-STEP: Set up the WhaleShark project (Krita)

1. Create the folder structure:
   MyAnimations / WhaleShark / {reference, project, exports, notes}

2. Save 1-2 whale shark reference images into reference/

3. Open Krita:
   File → New
   Set:  Width 1280, Height 720,  Resolution 72 dpi,  FPS 12
   (12 fps = cartoon style; 24 = smoother but more drawing)

4. Save IMMEDIATELY:
   File → Save As → project/WhaleShark_v01_2026-06-28.kra

5. Draw a simple whale shark silhouette on frame 1
   (big body, wide mouth, spots). Just a placeholder is fine.

6. Set the export location NOW (don't wait):
   We will export to: exports/v01/

7. Open the Pre-Flight Checklist — tick all 5 boxes out loud.
```

**The backup demo:** copy the `WhaleShark` folder to a USB stick. Say *"Two copies of everything important. Drives die."* For schools with no USB: email the export to yourself as a backup.

### Step 3: Independent Practice — Animate + Version Like a Pro (20 min)

Challenge: *"Animate the whale shark drifting slowly across the screen (8–12 frames). Save a new version at every milestone. End with a correct export."*

Give them the milestone/version plan:

```text
VERSION PLAN (follow this exactly):

v01 = keyframes only (start pose, mid pose, end pose)
      → Save As: WhaleShark_v01_[date].kra  (DONE in Step 2)

v02 = add inbetweens (smooth the drift)
      → Save As: WhaleShark_v02_[date].kra

v03 = add spots/texture details
      → Save As: WhaleShark_v03_[date].kra

EXPORT v03:
   Krita:  File → Render Animation
   Format: MP4 (or PNG sequence if MP4 unavailable)
   FPS: 12,  Resolution: 1280x720
   Save to: exports/v03/WhaleShark_v03_[date].mp4

BACKUP: copy exports/v03/*.mp4 to USB or cloud
```

Remind them: a whale shark moves SLOWLY because it's huge — that's the timing/spacing principle from earlier lessons. Few, evenly spaced frames = slow heavy drift. Mess up the inbetweening? Re-open v01, try again. **That's why versions exist.**

### Step 4: Sharing & Feedback (10 min)

Learners open their `exports/` folder and play their MP4 for a partner. Partner checks the **file-management scorecard** (not the art — the habits):

```text
PARTNER CHECK:
[ ] Folder structure correct (reference/project/exports/notes)?
[ ] File names follow the pattern (no spaces, has version + date)?
[ ] At least 2 versioned .kra files exist (v01, v02...)?
[ ] Export is in the exports folder with the right name?
[ ] A backup exists (USB or cloud or emailed)?
```

Celebrate clean folders as much as good animation — *professionals do this.*

---

## Assessment

| Criteria | BE (Below Expectation) | AE (Approaching) | ME (Meets) | EE (Exceeds) |
|----------|------------------------|-------------------|------------|--------------|
| Folder structure | No folders; file dumped on desktop | Some folders but missing subfolders or misnamed | Correct 4-folder structure (reference/project/exports/notes) + _Archive understood | Full structure + explains why each subfolder exists + uses _Archive for old work |
| File naming & versioning | "animation1.kra" or has spaces; single overwritten copy | Named but no version number or no date | Correct `[Project]_v##_YYYY-MM-DD.kra` with 2+ versions saved | 3+ versions saved at real milestones; never overwrote only copy; can explain the rule |
| Export & backup | No export or wrong settings | Exported but wrong fps/resolution or wrong location | Exported MP4 at 12fps/1280x720 into exports/ folder | Correct export + backup to USB/cloud + can teach the export steps to a peer |

---

## Extended Activity

**Homework — "Audit your old projects":** Look at your existing animation files on your computer/phone. Apply the 5-step cleanup plan: (1) make a `MyAnimations/_Archive/` folder, (2) move old/finished projects there, (3) rename any file with spaces or "final_final", (4) add a date to files that have none, (5) back up your best export to USB or cloud. Bring a screenshot of your cleaned-up folder next class. This protects your whale shark project — and every future one. Connects to conservation: KWS *tags* whale sharks to track and protect them — you *tag* (name) your files to track and protect your work.

---

## Differentiation

| For learners who need more support | For advanced learners |
|-------------------------------------|----------------------|
| Use the simplified structure (`working/` + `done/` only); provide a pre-filled folder template they copy; reduce to 1 version + 1 export | Require full folder structure + a written backup strategy; have them use Blender with the Output Properties path set explicitly; challenge: automate versioning with a small script or naming macro |

---

## Teacher Reflection

- [ ] Did learners achieve the outcomes?
- [ ] Was the whale shark project big enough to show why file management matters?
- [ ] Did every learner leave with a correctly named, backed-up project?
- [ ] What would I change next time?