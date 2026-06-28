#!/usr/bin/env python3
"""
Animation Assistant — Student Progress Tracker, Achievement System & Report Generator

Records student progress against Raspberry Pi Foundation computing taxonomy
and Kenya CBC Computer Science curriculum standards.

Usage:
    python progress_tracker.py add_student --name "John" --age 13 --grade 8
    python progress_tracker.py record --student-id S001 --module 03 --level ME --notes "Great walk cycle"
    python progress_tracker.py badges --student-id S001
    python progress_tracker.py report --student-id S001 --output report.html
    python progress_tracker.py class-report --output class_report.html
    python progress_tracker.py list-students
"""

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════
# STANDARDS DATA (RPF + Kenya CBC)
# ═══════════════════════════════════════════════════════════════════

# RPF 11-strand taxonomy mapping to our modules
RPF_STRANDS = {
    "effective_use_of_tools": {
        "name": "Effective Use of Tools",
        "modules": [2, 14, 18, 22, 26, 39],
    },
    "safety_and_security": {
        "name": "Safety and Security",
        "modules": [15, 37],
    },
    "design_and_development": {
        "name": "Design and Development",
        "modules": [16, 30, 40, 46],
    },
    "impact_of_technology": {
        "name": "Impact of Technology",
        "modules": [17, 47],
    },
    "computing_systems": {
        "name": "Computing Systems",
        "modules": [7, 18, 26],
    },
    "networks": {
        "name": "Networks",
        "modules": [37],
    },
    "creating_media": {
        "name": "Creating Media",
        "modules": list(range(1, 49)),  # All modules
    },
    "algorithms": {
        "name": "Algorithms and Data Structures",
        "modules": [5, 35, 45],
    },
    "programming": {
        "name": "Programming",
        "modules": [5, 26, 45],
    },
    "data_and_information": {
        "name": "Data and Information",
        "modules": [11, 18, 46],
    },
    "artificial_intelligence": {
        "name": "Artificial Intelligence",
        "modules": [47],
    },
}

# RPF Digital Making 5 strands
RPF_DM_STRANDS = {
    "design": {"name": "Design", "modules": [16, 19, 30, 40]},
    "programming": {"name": "Programming", "modules": [5, 26, 45]},
    "physical_computing": {"name": "Physical Computing", "modules": [26]},
    "manufacture": {"name": "Manufacture", "modules": [22, 34, 44]},
    "community_sharing": {"name": "Community and Sharing", "modules": [12, 25, 37, 38]},
}

# Kenya CBC 7 Core Competencies
CBC_CORE_COMPETENCIES = {
    "communication_collaboration": {
        "name": "Communication and Collaboration",
        "modules": [25, 37, 42],
    },
    "critical_thinking": {
        "name": "Critical Thinking and Problem Solving",
        "modules": [7, 29, 35, 46],
    },
    "creativity_imagination": {
        "name": "Creativity and Imagination",
        "modules": list(range(1, 49)),
    },
    "citizenship": {
        "name": "Citizenship",
        "modules": [15, 37, 47],
    },
    "digital_literacy": {
        "name": "Digital Literacy",
        "modules": [2, 5, 18, 26, 45],
    },
    "learning_to_learn": {
        "name": "Learning to Learn",
        "modules": [8, 9, 10, 11],
    },
    "self_efficacy": {
        "name": "Self-Efficacy",
        "modules": [6, 11, 12, 38],
    },
}

# Kenya CBC Assessment Rubric Levels
CBC_LEVELS = {
    "BE": {"name": "Below Expectations", "score": 1, "description": "Limited understanding, needs significant help"},
    "AE": {"name": "Approaching Expectations", "score": 2, "description": "Understands some concepts, needs guidance"},
    "ME": {"name": "Meeting Expectations", "score": 3, "description": "Clear understanding, independent in familiar situations"},
    "EE": {"name": "Exceeding Expectations", "score": 4, "description": "Goes beyond, applies in new contexts, shows creativity"},
}

# Kenya CBC Computer Science Strands (Grades 7-9)
CBC_CS_STRANDS = {
    "foundation_cs": {
        "name": "Foundation of Computer Science",
        "modules": [7, 18, 26],
    },
    "networks": {
        "name": "Computer Networks",
        "modules": [37],
    },
    "software": {
        "name": "Computer Software",
        "modules": [2, 7, 14, 18, 22, 26],
    },
    "programming_intro": {
        "name": "Introduction to Programming",
        "modules": [5, 9, 16, 35, 45, 46],
    },
}

# Module names for display
MODULE_NAMES = {
    1: "System Persona", 2: "Tool Routing", 3: "Project Guide", 4: "Principle Explainer",
    5: "Code-First Animation", 6: "Critique & Feedback", 7: "Troubleshooting", 8: "Curriculum Planner",
    9: "Daily Challenge", 10: "Reference Library", 11: "Progress Tracker", 12: "Showcase & Exhibition",
    13: "Animation Glossary", 14: "Tool Comparison", 15: "Parent & Teacher Guide", 16: "Story & Storyboard",
    17: "Animation History", 18: "Workflow & File Management", 19: "Color Theory & Design",
    20: "Sound & Audio Design", 21: "Rigging Deep Dive", 22: "Compositing & Rendering",
    23: "Portfolio & Career", 24: "Animation Styles", 25: "Collaboration & Team",
    26: "Raspberry Pi & Low-Resource", 27: "Kid-Friendly FAQ", 28: "Acting for Animation",
    29: "Animation Physics", 30: "Character Design", 31: "Camera & Cinematography",
    32: "Advanced Body Mechanics", 33: "Facial Animation", 34: "Special Effects",
    35: "Timing Charts & Spacing", 36: "Accessibility & Adaptive", 37: "Community & Etiquette",
    38: "Contests & Festivals", 39: "Animation Editing", 40: "Background Design",
    41: "Anatomy & Figure Drawing", 42: "Voice Acting", 43: "Music Sync",
    44: "Mixed Media & Experimental", 45: "Game Animation & Sprites", 46: "Production Management",
    47: "AI Ethics", 48: "Pacing & Rhythm",
}

# Achievement/Badge definitions
ACHIEVEMENTS = [
    # ── RPF Creator Level (Beginning) ──
    {"id": "first_frame", "name": "First Frame", "emoji": "🎬", "description": "Complete your first animation in any tool",
     "condition": lambda s: s.completed_count() >= 1, "tier": "creator"},
    {"id": "tool_explorer", "name": "Tool Explorer", "emoji": "🔧", "description": "Try 2 different animation tools",
     "condition": lambda s: len(s.tools_used()) >= 2, "tier": "creator"},
    {"id": "first_export", "name": "First Export", "emoji": "📤", "description": "Successfully export an animation as video or GIF",
     "condition": lambda s: s.has_module(22) and s.module_level(22) in ["ME", "EE"], "tier": "creator"},

    # ── RPF Builder Level (Fundamentals) ──
    {"id": "squash_master", "name": "Squash Master", "emoji": "⚽", "description": "Ball visibly squashes on impact",
     "condition": lambda s: s.has_module(4) and s.module_level(4) in ["ME", "EE"], "tier": "builder"},
    {"id": "arc_archer", "name": "Arc Archer", "emoji": "🏹", "description": "Ball follows a curved arc path",
     "condition": lambda s: s.has_module(29) and s.module_level(29) in ["ME", "EE"], "tier": "builder"},
    {"id": "timing_keeper", "name": "Timing Keeper", "emoji": "⏱️", "description": "Animation shows slow in/out (easing)",
     "condition": lambda s: s.has_module(35) and s.module_level(35) in ["ME", "EE"], "tier": "builder"},
    {"id": "weight_lifter", "name": "Weight Lifter", "emoji": "🏋️", "description": "Animation shows believable weight",
     "condition": lambda s: s.has_module(29) and s.module_level(29) == "EE", "tier": "builder"},

    # ── RPF Developer Level (Body Mechanics) ──
    {"id": "walk_warrior", "name": "Walk Cycle Warrior", "emoji": "🚶", "description": "Character walks without sliding feet",
     "condition": lambda s: s.has_module(3) and s.module_level(3) == "ME" or (s.has_module(32) and s.module_level(32) in ["ME", "EE"]),
     "tier": "developer"},
    {"id": "anticipation_ace", "name": "Anticipation Ace", "emoji": "🎯", "description": "Character winds up before jumping",
     "condition": lambda s: s.has_module(32) and s.module_level(32) in ["ME", "EE"], "tier": "developer"},
    {"id": "follow_phenom", "name": "Follow-Through Phenom", "emoji": "💨", "description": "Arms/hair/cloth trails after body stops",
     "condition": lambda s: s.has_module(32) and s.module_level(32) == "EE", "tier": "developer"},

    # ── RPF Developer Level (Performance) ──
    {"id": "mood_master", "name": "Mood Master", "emoji": "🎭", "description": "Same walk animated happy AND sad",
     "condition": lambda s: s.has_module(28) and s.module_level(28) in ["ME", "EE"], "tier": "developer"},
    {"id": "lip_sync_starter", "name": "Lip Sync Starter", "emoji": "👄", "description": "Mouth shapes match audio",
     "condition": lambda s: s.has_module(33) and s.module_level(33) in ["ME", "EE"], "tier": "developer"},
    {"id": "voice_actor", "name": "Voice Actor", "emoji": "🎙️", "description": "Recorded dialogue for a character",
     "condition": lambda s: s.has_module(42) and s.module_level(42) in ["ME", "EE"], "tier": "developer"},

    # ── RPF Maker Level (Storytelling) ──
    {"id": "storyboard_sketcher", "name": "Storyboard Sketcher", "emoji": "📋", "description": "Completed a storyboard with 6+ panels",
     "condition": lambda s: s.has_module(16) and s.module_level(16) in ["ME", "EE"], "tier": "maker"},
    {"id": "scene_setter", "name": "Scene Setter", "emoji": "🌅", "description": "Clear staging in every shot",
     "condition": lambda s: s.has_module(40) and s.module_level(40) in ["ME", "EE"], "tier": "maker"},
    {"id": "cut_master", "name": "Cut Master", "emoji": "✂️", "description": "2+ shots edited together with purposeful timing",
     "condition": lambda s: s.has_module(39) and s.module_level(39) in ["ME", "EE"], "tier": "maker"},
    {"id": "short_film_finisher", "name": "Short Film Finisher", "emoji": "🏆", "description": "Completed a 15-60 second animated short",
     "condition": lambda s: s.has_module(46) and s.module_level(46) in ["ME", "EE"], "tier": "maker"},

    # ── RPF Maker Level (Advanced) ──
    {"id": "rigging_rookie", "name": "Rigging Rookie", "emoji": "🦴", "description": "Built and animated a simple rig",
     "condition": lambda s: s.has_module(21) and s.module_level(21) in ["ME", "EE"], "tier": "maker"},
    {"id": "effect_animator", "name": "Effect Animator", "emoji": "🔥", "description": "Animated fire, water, smoke, or particles",
     "condition": lambda s: s.has_module(34) and s.module_level(34) in ["ME", "EE"], "tier": "maker"},
    {"id": "sound_designer", "name": "Sound Designer", "emoji": "🔊", "description": "Added SFX, music, and ambient audio",
     "condition": lambda s: s.has_module(20) and s.module_level(20) in ["ME", "EE"], "tier": "maker"},
    {"id": "game_animator", "name": "Game Animator", "emoji": "🎮", "description": "Created game-ready animation loops",
     "condition": lambda s: s.has_module(45) and s.module_level(45) in ["ME", "EE"], "tier": "maker"},

    # ── RPF Maker Level (Mastery) ──
    {"id": "style_specialist", "name": "Style Specialist", "emoji": "🎨", "description": "Identifiable personal style across 3+ works",
     "condition": lambda s: s.has_module(24) and s.module_level(24) == "EE", "tier": "maker"},
    {"id": "mentor_badge", "name": "Mentor Badge", "emoji": "🧑‍🏫", "description": "Helped another student with their animation",
     "condition": lambda s: s.has_module(25) and s.module_level(25) in ["ME", "EE"], "tier": "maker"},
    {"id": "contest_competitor", "name": "Contest Competitor", "emoji": "🥇", "description": "Entered an animation contest or festival",
     "condition": lambda s: s.has_module(38) and s.module_level(38) in ["ME", "EE"], "tier": "maker"},
    {"id": "pi_pioneer", "name": "Pi Pioneer", "emoji": "🥧", "description": "Animated on a Raspberry Pi or low-resource device",
     "condition": lambda s: s.has_module(26) and s.module_level(26) in ["ME", "EE"], "tier": "maker"},
    {"id": "physics_master", "name": "Physics Master", "emoji": "📐", "description": "Applied the Odd Rule and physics principles",
     "condition": lambda s: s.has_module(29) and s.module_level(29) == "EE", "tier": "maker"},

    # ── Kenya CBC Competency Badges ──
    {"id": "digital_citizen", "name": "Digital Citizen", "emoji": "🛡️", "description": "Demonstrated online safety and ethical behavior",
     "condition": lambda s: s.has_module(37) and s.module_level(37) in ["ME", "EE"], "tier": "cbc"},
    {"id": "creative_thinker", "name": "Creative Thinker", "emoji": "💡", "description": "Created original animation from own idea",
     "condition": lambda s: s.has_module(16) and s.module_level(16) == "EE", "tier": "cbc"},
    {"id": "problem_solver", "name": "Problem Solver", "emoji": "🧩", "description": "Independently debugged animation issues",
     "condition": lambda s: s.has_module(7) and s.module_level(7) in ["ME", "EE"], "tier": "cbc"},
    {"id": "collaborator", "name": "Collaborator", "emoji": "🤝", "description": "Worked on a team animation project",
     "condition": lambda s: s.has_module(25) and s.module_level(25) in ["ME", "EE"], "tier": "cbc"},
    {"id": "code_creator", "name": "Code Creator", "emoji": "💻", "description": "Programmed animation using Scratch or Python",
     "condition": lambda s: s.has_module(5) and s.module_level(5) in ["ME", "EE"], "tier": "cbc"},
    {"id": "ai_ethicist", "name": "AI Ethicist", "emoji": "🤖", "description": "Understood and applied AI ethics principles",
     "condition": lambda s: s.has_module(47) and s.module_level(47) in ["ME", "EE"], "tier": "cbc"},
]

# RPF progression tiers
RPF_TIERS = {
    "creator": {"name": "Creator", "order": 1, "emoji": "🐣"},
    "builder": {"name": "Builder", "order": 2, "emoji": "🏗️"},
    "developer": {"name": "Developer", "order": 3, "emoji": "⚙️"},
    "maker": {"name": "Maker", "order": 4, "emoji": "🏆"},
    "cbc": {"name": "CBC Competency", "order": 5, "emoji": "🇰🇪"},
}


# ═══════════════════════════════════════════════════════════════════
# DATABASE
# ═══════════════════════════════════════════════════════════════════

DB_PATH = Path(__file__).parent / "progress.db"


def get_db():
    """Get database connection, creating tables if needed."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade INTEGER,
            school TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            module_id INTEGER NOT NULL,
            cbc_level TEXT NOT NULL,
            notes TEXT,
            recorded_at TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS badges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            badge_id TEXT NOT NULL,
            awarded_at TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            UNIQUE(student_id, badge_id)
        )
    """)
    conn.commit()
    return conn


# ═══════════════════════════════════════════════════════════════════
# STUDENT CLASS
# ═══════════════════════════════════════════════════════════════════

class Student:
    """Represents a student with their progress records."""

    def __init__(self, row):
        self.student_id = row["student_id"]
        self.name = row["name"]
        self.age = row["age"]
        self.grade = row["grade"]
        self.school = row["school"]
        self.created_at = row["created_at"]

    @classmethod
    def get(cls, conn, student_id):
        row = conn.execute("SELECT * FROM students WHERE student_id = ?", (student_id,)).fetchone()
        if not row:
            print(f"Student {student_id} not found.")
            sys.exit(1)
        return cls(row)

    def _records(self, conn):
        return conn.execute(
            "SELECT * FROM progress WHERE student_id = ? ORDER BY recorded_at", (self.student_id,)
        ).fetchall()

    def completed_modules(self, conn):
        """Set of module IDs completed at ME or EE level."""
        records = self._records(conn)
        # Get the highest level per module
        best = {}
        for r in records:
            mid = r["module_id"]
            level = r["cbc_level"]
            if mid not in best or CBC_LEVELS[level]["score"] > CBC_LEVELS[best[mid]]["score"]:
                best[mid] = level
        return {mid: lvl for mid, lvl in best.items() if lvl in ["ME", "EE"]}

    def completed_count(self, conn=None):
        if conn is None:
            conn = get_db()
        return len(self.completed_modules(conn))

    def has_module(self, module_id, conn=None):
        if conn is None:
            conn = get_db()
        return module_id in self.completed_modules(conn)

    def module_level(self, module_id, conn=None):
        if conn is None:
            conn = get_db()
        records = self._records(conn)
        best = None
        for r in records:
            if r["module_id"] == module_id:
                if best is None or CBC_LEVELS[r["cbc_level"]]["score"] > CBC_LEVELS[best]["score"]:
                    best = r["cbc_level"]
        return best

    def all_module_levels(self, conn=None):
        """Dict of module_id -> highest level achieved."""
        if conn is None:
            conn = get_db()
        records = self._records(conn)
        best = {}
        for r in records:
            mid = r["module_id"]
            lvl = r["cbc_level"]
            if mid not in best or CBC_LEVELS[lvl]["score"] > CBC_LEVELS[best[mid]]["score"]:
                best[mid] = lvl
        return best

    def tools_used(self, conn=None):
        """Inferred tools from modules completed."""
        if conn is None:
            conn = get_db()
        # Module -> tool mapping
        tool_modules = {
            2: ["scratch", "stop-motion-studio", "pencil2d", "krita", "synfig", "opentoonz", "blender"],
            5: ["scratch", "python"],
            14: ["scratch", "stop-motion-studio", "pencil2d", "krita", "synfig", "opentoonz", "blender"],
            26: ["raspberry-pi", "scratch", "pygame", "stopmotion"],
            45: ["scratch", "pygame", "godot", "unity"],
        }
        tools = set()
        completed = self.completed_modules(conn)
        for mid in completed:
            if mid in tool_modules:
                tools.update(tool_modules[mid])
        return tools

    def earned_badges(self, conn=None):
        """List of achievement IDs earned."""
        if conn is None:
            conn = get_db()
        earned = []
        for ach in ACHIEVEMENTS:
            try:
                if ach["condition"](self):
                    earned.append(ach)
            except TypeError:
                # condition needs conn
                if ach["condition"](self):
                    earned.append(ach)
        return earned

    def rpf_tier(self, conn=None):
        """Current RPF progression tier based on badges."""
        if conn is None:
            conn = get_db()
        earned = self.earned_badges(conn)
        tiers_earned = {ach["tier"] for ach in earned}
        # Highest tier achieved
        best = "creator"
        for tier_id, tier in RPF_TIERS.items():
            if tier_id in tiers_earned and tier["order"] > RPF_TIERS[best]["order"]:
                best = tier_id
        return best

    def cbc_strand_progress(self, conn=None):
        """Progress per Kenya CBC CS strand."""
        if conn is None:
            conn = get_db()
        levels = self.all_module_levels(conn)
        result = {}
        for strand_id, strand in CBC_CS_STRANDS.items():
            strand_mods = strand["modules"]
            completed = [m for m in strand_mods if m in levels and levels[m] in ["ME", "EE"]]
            total = len(strand_mods)
            pct = len(completed) / total * 100 if total > 0 else 0
            result[strand_id] = {
                "name": strand["name"],
                "completed": len(completed),
                "total": total,
                "percentage": round(pct, 1),
                "modules": [{"id": m, "name": MODULE_NAMES.get(m, f"Module {m}"),
                             "level": levels.get(m, "—")} for m in strand_mods],
            }
        return result

    def rpf_strand_progress(self, conn=None):
        """Progress per RPF 11-strand taxonomy."""
        if conn is None:
            conn = get_db()
        levels = self.all_module_levels(conn)
        result = {}
        for strand_id, strand in RPF_STRANDS.items():
            strand_mods = strand["modules"]
            completed = [m for m in strand_mods if m in levels and levels[m] in ["ME", "EE"]]
            total = len(strand_mods)
            pct = len(completed) / total * 100 if total > 0 else 0
            result[strand_id] = {
                "name": strand["name"],
                "completed": len(completed),
                "total": total,
                "percentage": round(pct, 1),
            }
        return result

    def cbc_competency_progress(self, conn=None):
        """Progress per Kenya CBC 7 core competencies."""
        if conn is None:
            conn = get_db()
        levels = self.all_module_levels(conn)
        result = {}
        for comp_id, comp in CBC_CORE_COMPETENCIES.items():
            comp_mods = comp["modules"]
            completed = [m for m in comp_mods if m in levels and levels[m] in ["ME", "EE"]]
            total = len(comp_mods)
            pct = len(completed) / total * 100 if total > 0 else 0
            result[comp_id] = {
                "name": comp["name"],
                "completed": len(completed),
                "total": total,
                "percentage": round(pct, 1),
            }
        return result


# ═══════════════════════════════════════════════════════════════════
# CLI COMMANDS
# ═══════════════════════════════════════════════════════════════════

def cmd_add_student(args):
    conn = get_db()
    # Generate student ID
    count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    sid = f"S{count + 1:03d}"
    now = datetime.now().isoformat()
    conn.execute(
        "INSERT INTO students (student_id, name, age, grade, school, created_at) VALUES (?, ?, ?, ?, ?, ?)",
        (sid, args.name, args.age, args.grade, args.school, now),
    )
    conn.commit()
    print(f"✅ Student added: {sid} — {args.name}, age {args.age}, grade {args.grade}")


def cmd_list_students(args):
    conn = get_db()
    rows = conn.execute("SELECT * FROM students ORDER BY student_id").fetchall()
    if not rows:
        print("No students registered yet.")
        return
    print(f"{'ID':<8} {'Name':<20} {'Age':<5} {'Grade':<7} {'School':<20} {'Modules':<8} {'Badges':<7}")
    print("─" * 80)
    for row in rows:
        student = Student(row)
        mods = student.completed_count(conn)
        badges = len(student.earned_badges(conn))
        print(f"{student.student_id:<8} {student.name:<20} {student.age:<5} {student.grade or '—':<7} {student.school or '—':<20} {mods:<8} {badges:<7}")


def cmd_record(args):
    conn = get_db()
    student = Student.get(conn, args.student_id)
    level = args.level.upper()
    if level not in CBC_LEVELS:
        print(f"Invalid level '{args.level}'. Use: BE, AE, ME, or EE")
        sys.exit(1)
    now = datetime.now().isoformat()
    conn.execute(
        "INSERT INTO progress (student_id, module_id, cbc_level, notes, recorded_at) VALUES (?, ?, ?, ?, ?)",
        (student.student_id, args.module, level, args.notes or "", now),
    )
    conn.commit()
    mod_name = MODULE_NAMES.get(args.module, f"Module {args.module}")
    print(f"✅ Recorded: {student.name} — Module {args.module} ({mod_name}) — Level: {CBC_LEVELS[level]['name']}")
    if args.notes:
        print(f"   Notes: {args.notes}")

    # Check for new badges
    earned = student.earned_badges(conn)
    # Check which are already in DB
    previously = conn.execute(
        "SELECT badge_id FROM badges WHERE student_id = ?", (student.student_id,)
    ).fetchall()
    prev_ids = {r["badge_id"] for r in previously}
    new_badges = [b for b in earned if b["id"] not in prev_ids]
    for badge in new_badges:
        conn.execute(
            "INSERT OR IGNORE INTO badges (student_id, badge_id, awarded_at) VALUES (?, ?, ?)",
            (student.student_id, badge["id"], now),
        )
        print(f"🏅 NEW BADGE: {badge['emoji']} {badge['name']} — {badge['description']}")
    conn.commit()


def cmd_badges(args):
    conn = get_db()
    student = Student.get(conn, args.student_id)
    earned = student.earned_badges(conn)
    tier = student.rpf_tier(conn)
    print(f"\n{'='*60}")
    print(f"  {student.name} — Achievements & Badges")
    print(f"  RPF Tier: {RPF_TIERS[tier]['emoji']} {RPF_TIERS[tier]['name']}")
    print(f"{'='*60}")

    # Group by tier
    for tier_id, tier_info in sorted(RPF_TIERS.items(), key=lambda x: x[1]["order"]):
        tier_badges = [b for b in earned if b["tier"] == tier_id]
        if not tier_badges and tier_id != "cbc":
            continue
        print(f"\n{tier_info['emoji']} {tier_info['name']} ({len(tier_badges)} badges)")
        print("─" * 40)
        if not tier_badges:
            print("  (none yet — keep learning!)")
        for badge in tier_badges:
            print(f"  {badge['emoji']} {badge['name']}")
            print(f"     {badge['description']}")

    # Show locked badges (not yet earned)
    earned_ids = {b["id"] for b in earned}
    locked = [b for b in ACHIEVEMENTS if b["id"] not in earned_ids]
    if locked:
        print(f"\n{'─'*40}")
        print(f"🔒 Locked ({len(locked)} remaining)")
        for badge in locked[:5]:  # Show next 5
            print(f"  {badge['emoji']} {badge['name']} — {badge['description']}")
        if len(locked) > 5:
            print(f"  ... and {len(locked) - 5} more")


def cmd_report(args):
    conn = get_db()
    student = Student.get(conn, args.student_id)
    html = generate_report_html(student, conn)
    output = args.output or f"report_{student.student_id}.html"
    Path(output).write_text(html)
    print(f"✅ Report generated: {output}")
    print(f"   Open in browser: file://{Path(output).resolve()}")


def cmd_class_report(args):
    conn = get_db()
    rows = conn.execute("SELECT * FROM students ORDER BY student_id").fetchall()
    if not rows:
        print("No students registered.")
        return
    html = generate_class_report_html([Student(r) for r in rows], conn)
    output = args.output or "class_report.html"
    Path(output).write_text(html)
    print(f"✅ Class report generated: {output}")


# ═══════════════════════════════════════════════════════════════════
# HTML REPORT GENERATION
# ═══════════════════════════════════════════════════════════════════

def _progress_bar(pct, label=""):
    """Generate an HTML progress bar."""
    color = "#22c55e" if pct >= 75 else "#f59e0b" if pct >= 50 else "#ef4444"
    return f"""
    <div class="progress-container">
        <span class="progress-label">{label}</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width:{pct}%; background:{color}"></div>
        </div>
        <span class="progress-pct">{pct}%</span>
    </div>"""


def generate_report_html(student, conn):
    """Generate a printable HTML progress report for a single student."""
    levels = student.all_module_levels(conn)
    badges = student.earned_badges(conn)
    tier = student.rpf_tier(conn)
    cbc_strands = student.cbc_strand_progress(conn)
    rpf_strands = student.rpf_strand_progress(conn)
    competencies = student.cbc_competency_progress(conn)

    # Badges HTML grouped by tier
    badges_html = ""
    for tier_id, tier_info in sorted(RPF_TIERS.items(), key=lambda x: x[1]["order"]):
        tier_badges = [b for b in badges if b["tier"] == tier_id]
        if not tier_badges:
            continue
        badge_items = "".join(
            f'<div class="badge"><span class="badge-emoji">{b["emoji"]}</span>'
            f'<span class="badge-name">{b["name"]}</span>'
            f'<span class="badge-desc">{b["description"]}</span></div>'
            for b in tier_badges
        )
        badges_html += f'<div class="badge-tier"><h3>{tier_info["emoji"]} {tier_info["name"]}</h3><div class="badge-grid">{badge_items}</div></div>'

    # CBC strand progress
    cbc_html = ""
    for sid, s in cbc_strands.items():
        cbc_html += _progress_bar(s["percentage"], s["name"])
        for m in s["modules"]:
            lvl = m["level"]
            lvl_class = f"level-{lvl.lower()}" if lvl != "—" else "level-na"
            cbc_html += f'<div class="module-row"><span>{m["name"]}</span><span class="level-tag {lvl_class}">{lvl}</span></div>'

    # RPF strand progress
    rpf_html = ""
    for sid, s in rpf_strands.items():
        rpf_html += _progress_bar(s["percentage"], s["name"])

    # CBC competency progress
    comp_html = ""
    for cid, c in competencies.items():
        comp_html += _progress_bar(c["percentage"], c["name"])

    # Completed modules summary
    completed = [m for m, l in levels.items() if l in ["ME", "EE"]]
    total_mods = len(MODULE_NAMES)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Animation Progress Report — {student.name}</title>
<style>
  body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1a1a2e; background: #f8f9fa; }}
  .report {{ max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
  h1 {{ color: #7c3aed; border-bottom: 3px solid #7c3aed; padding-bottom: 10px; }}
  h2 {{ color: #6d28d9; margin-top: 30px; }}
  h3 {{ color: #5b21b6; }}
  .header {{ display: flex; justify-content: space-between; align-items: center; }}
  .student-info {{ background: #f3f4f6; padding: 15px 20px; border-radius: 8px; margin: 20px 0; }}
  .student-info span {{ display: inline-block; margin-right: 25px; font-size: 14px; }}
  .student-info strong {{ color: #4c1d95; }}
  .tier-badge {{ display: inline-block; padding: 8px 16px; border-radius: 20px; font-weight: bold; color: white; }}
  .tier-creator {{ background: #22c55e; }}
  .tier-builder {{ background: #3b82f6; }}
  .tier-developer {{ background: #8b5cf6; }}
  .tier-maker {{ background: #f59e0b; }}
  .tier-cbc {{ background: #ef4444; }}
  .summary-stats {{ display: flex; gap: 15px; margin: 20px 0; }}
  .stat-card {{ flex: 1; background: #f3f4f6; padding: 15px; border-radius: 8px; text-align: center; }}
  .stat-number {{ font-size: 32px; font-weight: bold; color: #7c3aed; }}
  .stat-label {{ font-size: 12px; color: #6b7280; text-transform: uppercase; }}
  .progress-container {{ display: flex; align-items: center; gap: 10px; margin: 8px 0; }}
  .progress-label {{ width: 220px; font-size: 13px; flex-shrink: 0; }}
  .progress-bar {{ flex: 1; height: 20px; background: #e5e7eb; border-radius: 10px; overflow: hidden; }}
  .progress-fill {{ height: 100%; border-radius: 10px; transition: width 0.3s; }}
  .progress-pct {{ width: 50px; font-size: 13px; font-weight: bold; text-align: right; }}
  .module-row {{ display: flex; justify-content: space-between; padding: 4px 0 4px 230px; font-size: 12px; color: #6b7280; }}
  .level-tag {{ padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }}
  .level-be {{ background: #fee2e2; color: #991b1b; }}
  .level-ae {{ background: #fef3c7; color: #92400e; }}
  .level-me {{ background: #d1fae5; color: #065f46; }}
  .level-ee {{ background: #dbeafe; color: #1e40af; }}
  .level-na {{ background: #f3f4f6; color: #9ca3af; }}
  .badge-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }}
  .badge {{ background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px; display: flex; flex-direction: column; gap: 4px; }}
  .badge-emoji {{ font-size: 24px; }}
  .badge-name {{ font-weight: bold; font-size: 14px; color: #4c1d95; }}
  .badge-desc {{ font-size: 11px; color: #6b7280; }}
  .section {{ margin: 25px 0; }}
  .standards-note {{ background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px; margin: 20px 0; font-size: 13px; }}
  .footer {{ margin-top: 40px; padding-top: 15px; border-top: 1px solid #e5e7eb; font-size: 12px; color: #9ca3af; text-align: center; }}
  @media print {{ body {{ margin: 0; background: white; }} .report {{ box-shadow: none; max-width: 100%; padding: 20px; }} }}
</style>
</head>
<body>
<div class="report">
  <div class="header">
    <h1>🎬 Animation Learning Progress Report</h1>
    <div class="tier-badge tier-{tier}">{RPF_TIERS[tier]['emoji']} {RPF_TIERS[tier]['name']}</div>
  </div>

  <div class="student-info">
    <span><strong>Name:</strong> {student.name}</span>
    <span><strong>Age:</strong> {student.age}</span>
    <span><strong>Grade:</strong> {student.grade or '—'}</span>
    <span><strong>School:</strong> {student.school or '—'}</span>
    <span><strong>Student ID:</strong> {student.student_id}</span>
    <span><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d')}</span>
  </div>

  <div class="summary-stats">
    <div class="stat-card"><div class="stat-number">{len(completed)}</div><div class="stat-label">Modules Completed</div></div>
    <div class="stat-card"><div class="stat-number">{len(badges)}</div><div class="stat-label">Badges Earned</div></div>
    <div class="stat-card"><div class="stat-number">{len(student.tools_used(conn))}</div><div class="stat-label">Tools Used</div></div>
    <div class="stat-card"><div class="stat-number">{total_mods}</div><div class="stat-label">Total Modules</div></div>
  </div>

  <div class="standards-note">
    📋 This report maps progress against the <strong>Raspberry Pi Foundation Computing Taxonomy</strong>
    (11 strands) and the <strong>Kenya CBC Computer Science Curriculum</strong> (Grades 7-9, 4 strands).
    Assessment uses the Kenya CBC 4-level rubric: BE (Below), AE (Approaching), ME (Meeting), EE (Exceeding).
  </div>

  <h2>🇰🇪 Kenya CBC Computer Science — Strand Progress</h2>
  <div class="section">
    {cbc_html}
  </div>

  <h2>🥧 Raspberry Pi Foundation — Computing Strands</h2>
  <div class="section">
    {rpf_html}
  </div>

  <h2>🇰🇪 Kenya CBC Core Competencies</h2>
  <div class="section">
    {comp_html}
  </div>

  <h2>🏅 Achievements & Badges</h2>
  <div class="section">
    {badges_html if badges_html else '<p>No badges earned yet. Complete modules at ME or EE level to earn badges!</p>'}
  </div>

  <div class="footer">
    Generated by Animation Assistant Progress Tracker | {datetime.now().strftime('%Y-%m-%d %H:%M')}
    <br>Aligned with RPF Computing Taxonomy & Kenya CBC Computer Science Curriculum (KICD)
  </div>
</div>
</body>
</html>"""


def generate_class_report_html(students, conn):
    """Generate a class-level report showing all students."""

    # Build table rows
    rows_html = ""
    for s in students:
        levels = s.all_module_levels(conn)
        completed = len([m for m, l in levels.items() if l in ["ME", "EE"]])
        badges = len(s.earned_badges(conn))
        tier = s.rpf_tier(conn)
        tier_class = f"tier-{tier}"

        # CBC strand percentages
        cbc = s.cbc_strand_progress(conn)
        prog_pct = sum(v["percentage"] for v in cbc.values()) / len(cbc) if cbc else 0

        rows_html += f"""<tr>
            <td>{s.student_id}</td>
            <td>{s.name}</td>
            <td>{s.age}</td>
            <td>{s.grade or '—'}</td>
            <td><span class="tier-badge-sm {tier_class}">{RPF_TIERS[tier]['emoji']} {RPF_TIERS[tier]['name']}</span></td>
            <td>{completed}/{len(MODULE_NAMES)}</td>
            <td>{badges}</td>
            <td>{prog_pct:.0f}%</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Class Progress Report — Animation Assistant</title>
<style>
  body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1a1a2e; background: #f8f9fa; }}
  .report {{ max-width: 1000px; margin: 0 auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
  h1 {{ color: #7c3aed; border-bottom: 3px solid #7c3aed; padding-bottom: 10px; }}
  h2 {{ color: #6d28d9; }}
  table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
  th {{ background: #7c3aed; color: white; padding: 10px; text-align: left; font-size: 13px; }}
  td {{ padding: 8px 10px; border-bottom: 1px solid #e5e7eb; font-size: 13px; }}
  tr:nth-child(even) {{ background: #f9fafb; }}
  .tier-badge-sm {{ padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; color: white; }}
  .tier-creator {{ background: #22c55e; }}
  .tier-builder {{ background: #3b82f6; }}
  .tier-developer {{ background: #8b5cf6; }}
  .tier-maker {{ background: #f59e0b; }}
  .tier-cbc {{ background: #ef4444; }}
  .stats {{ display: flex; gap: 15px; margin: 20px 0; }}
  .stat-card {{ flex: 1; background: #f3f4f6; padding: 15px; border-radius: 8px; text-align: center; }}
  .stat-number {{ font-size: 28px; font-weight: bold; color: #7c3aed; }}
  .stat-label {{ font-size: 12px; color: #6b7280; text-transform: uppercase; }}
  .standards-note {{ background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px; margin: 20px 0; font-size: 13px; }}
  .footer {{ margin-top: 40px; padding-top: 15px; border-top: 1px solid #e5e7eb; font-size: 12px; color: #9ca3af; text-align: center; }}
  @media print {{ body {{ margin: 0; background: white; }} .report {{ box-shadow: none; max-width: 100%; padding: 20px; }} }}
</style>
</head>
<body>
<div class="report">
  <h1>🎬 Class Animation Progress Report</h1>

  <div class="standards-note">
    📋 Aligned with <strong>Raspberry Pi Foundation Computing Taxonomy</strong> and
    <strong>Kenya CBC Computer Science Curriculum</strong> (KICD, Grades 7-9).
    Assessment uses the Kenya CBC 4-level rubric (BE/AE/ME/EE).
  </div>

  <div class="stats">
    <div class="stat-card"><div class="stat-number">{len(students)}</div><div class="stat-label">Students</div></div>
    <div class="stat-card"><div class="stat-number">{sum(len(s.earned_badges(conn)) for s in students)}</div><div class="stat-label">Total Badges</div></div>
    <div class="stat-card"><div class="stat-number">{sum(len([m for m,l in s.all_module_levels(conn).items() if l in ['ME','EE']]) for s in students)}</div><div class="stat-label">Modules Completed</div></div>
  </div>

  <h2>Student Summary</h2>
  <table>
    <thead>
      <tr><th>ID</th><th>Name</th><th>Age</th><th>Grade</th><th>RPF Tier</th><th>Modules</th><th>Badges</th><th>CBC Progress</th></tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <div class="footer">
    Generated by Animation Assistant Progress Tracker | {datetime.now().strftime('%Y-%m-%d %H:%M')}
    <br>Aligned with RPF Computing Taxonomy & Kenya CBC Computer Science Curriculum (KICD)
  </div>
</div>
</body>
</html>"""


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Animation Assistant — Student Progress Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python progress_tracker.py add_student --name "John" --age 13 --grade 8
  python progress_tracker.py record --student-id S001 --module 3 --level ME --notes "Great walk cycle"
  python progress_tracker.py badges --student-id S001
  python progress_tracker.py report --student-id S001 --output john_report.html
  python progress_tracker.py class-report --output class_report.html
  python progress_tracker.py list-students
        """
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add_student", help="Register a new student")
    p_add.add_argument("--name", required=True, help="Student name")
    p_add.add_argument("--age", type=int, required=True, help="Student age")
    p_add.add_argument("--grade", type=int, help="Grade level (Kenya: 7-9 for JSS)")
    p_add.add_argument("--school", help="School name")
    p_add.set_defaults(func=cmd_add_student)

    p_list = sub.add_parser("list-students", help="List all registered students")
    p_list.set_defaults(func=cmd_list_students)

    p_record = sub.add_parser("record", help="Record module progress for a student")
    p_record.add_argument("--student-id", required=True, help="Student ID (e.g., S001)")
    p_record.add_argument("--module", type=int, required=True, help="Module number (1-48)")
    p_record.add_argument("--level", required=True, choices=["BE", "AE", "ME", "EE"],
                          help="CBC assessment level")
    p_record.add_argument("--notes", help="Optional notes about the assessment")
    p_record.set_defaults(func=cmd_record)

    p_badges = sub.add_parser("badges", help="Show badges and achievements for a student")
    p_badges.add_argument("--student-id", required=True, help="Student ID")
    p_badges.set_defaults(func=cmd_badges)

    p_report = sub.add_parser("report", help="Generate printable HTML progress report")
    p_report.add_argument("--student-id", required=True, help="Student ID")
    p_report.add_argument("--output", help="Output HTML file path")
    p_report.set_defaults(func=cmd_report)

    p_class = sub.add_parser("class-report", help="Generate class-level HTML report")
    p_class.add_argument("--output", help="Output HTML file path")
    p_class.set_defaults(func=cmd_class_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()