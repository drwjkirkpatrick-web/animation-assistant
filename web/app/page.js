import './globals.css';

// ═══ Data ═══

const marineBigFive = [
  { emoji: '🐢', name: 'Green Sea Turtle', swahili: 'Kasa', principle: 'Weight shift, heavy vs light, quadruped locomotion' },
  { emoji: '🐬', name: 'Bottlenose Dolphin', swahili: 'Pomboo', principle: 'Arcs, anticipation, breaching (jump physics)' },
  { emoji: '🦈', name: 'Whale Shark', swahili: 'Papa Shinga', principle: 'Scale through timing, massive weight, slow momentum' },
  { emoji: '🐙', name: 'Octopus', swahili: 'Pweza', principle: 'Secondary motion (8 tentacles = complex trailing)' },
  { emoji: '🪼', name: 'Jellyfish', swahili: '—', principle: 'Squash & stretch (pulsing bell), secondary motion (tentacle delay)' },
];

const moduleGroups = [
  {
    title: 'Core Assistant',
    range: '01–08',
    modules: [
      { n: '01', e: '🐬', t: 'System Persona & Character Voice' },
      { n: '02', e: '🐢', t: 'Tool Routing — Right Software' },
      { n: '03', e: '🐙', t: 'Step-by-Step Project Guide' },
      { n: '04', e: '🪼', t: 'Principle Explainer — 12 Principles' },
      { n: '05', e: '🐠', t: 'Code-First Animation (Scratch/Python)' },
      { n: '06', e: '🦈', t: 'Critique & Feedback' },
      { n: '07', e: '🐢', t: 'Troubleshooting' },
      { n: '08', e: '🐬', t: 'Curriculum Planner' },
    ],
  },
  {
    title: 'Extended Modules',
    range: '09–18',
    modules: [
      { n: '09', e: '🦀', t: 'Daily Challenge Generator' },
      { n: '10', e: '🐬', t: 'Reference Library Guide' },
      { n: '11', e: '🐠', t: 'Progress Tracker & Badges' },
      { n: '12', e: '🐢', t: 'Showcase & Exhibition' },
      { n: '13', e: '🐙', t: 'Animation Glossary' },
      { n: '14', e: '🦈', t: 'Tool Comparison Helper' },
      { n: '15', e: '🐬', t: 'Parent & Teacher Guide' },
      { n: '16', e: '🐢', t: 'Story & Storyboard Builder' },
      { n: '17', e: '🪼', t: 'Animation History & Inspiration' },
      { n: '18', e: '🐠', t: 'Workflow & File Management' },
    ],
  },
  {
    title: 'Gap-Fill Pass 1',
    range: '19–28',
    modules: [
      { n: '19', e: '🐠', t: 'Color Theory & Visual Design' },
      { n: '20', e: '🐬', t: 'Sound & Audio Design' },
      { n: '21', e: '🐙', t: 'Rigging Deep Dive' },
      { n: '22', e: '🪼', t: 'Compositing & Rendering' },
      { n: '23', e: '🐢', t: 'Portfolio & Career Path' },
      { n: '24', e: '🐠', t: 'Animation Styles & Techniques' },
      { n: '25', e: '🐬', t: 'Collaboration & Team Animation' },
      { n: '26', e: '🐠', t: 'Raspberry Pi & Low-Resource' },
      { n: '27', e: '🦀', t: 'Kid-Friendly FAQ' },
      { n: '28', e: '🐙', t: 'Acting for Animation' },
    ],
  },
  {
    title: 'Gap-Fill Pass 2',
    range: '29–38',
    modules: [
      { n: '29', e: '🦈', t: 'Animation Physics & Weight' },
      { n: '30', e: '🐢', t: 'Character Design & Shape Language' },
      { n: '31', e: '🐬', t: 'Camera & Cinematography' },
      { n: '32', e: '🐢', t: 'Advanced Body Mechanics' },
      { n: '33', e: '🐙', t: 'Facial Animation & Expressions' },
      { n: '34', e: '🪼', t: 'Special Effects Animation' },
      { n: '35', e: '🐠', t: 'Timing Charts & Spacing' },
      { n: '36', e: '🐢', t: 'Accessibility & Adaptive Animation' },
      { n: '37', e: '🐬', t: 'Community & Online Etiquette' },
      { n: '38', e: '🐠', t: 'Contests, Festivals & Challenges' },
    ],
  },
  {
    title: 'Gap-Fill Pass 3',
    range: '39–48',
    modules: [
      { n: '39', e: '🐙', t: 'Animation Editing & Post-Production' },
      { n: '40', e: '🪸', t: 'Background & Environment Design' },
      { n: '41', e: '🐢', t: 'Anatomy & Figure Drawing' },
      { n: '42', e: '🐙', t: 'Voice Acting & Dialogue Recording' },
      { n: '43', e: '🐬', t: 'Music Synchronization & Beat Sync' },
      { n: '44', e: '🪸', t: 'Mixed Media & Experimental Techniques' },
      { n: '45', e: '🐠', t: 'Game Animation & Sprite Sheets' },
      { n: '46', e: '🦈', t: 'Production & Project Management' },
      { n: '47', e: '🐙', t: 'AI Ethics & Animation Tools' },
      { n: '48', e: '🐬', t: 'Pacing & Rhythm' },
    ],
  },
  {
    title: 'Real-World Motion & Realism',
    range: '49–58',
    modules: [
      { n: '49', e: '🐬', t: 'Rotoscoping & Video Reference' },
      { n: '50', e: '🐢', t: 'Motion Capture & Mocap' },
      { n: '51', e: '🐢', t: 'Balance, Weight Shift & Ground Contact' },
      { n: '52', e: '🦈', t: 'Exaggeration vs Realism' },
      { n: '53', e: '🪼', t: 'Cloth, Hair & Secondary Motion' },
      { n: '54', e: '🐙', t: 'Micro-Expressions & Subtle Performance' },
      { n: '55', e: '🐢', t: 'Stop Motion with Nature & Found Objects' },
      { n: '56', e: '🐬', t: 'Observational Sketching & Movement Studies' },
      { n: '57', e: '🐚', t: 'Photogrammetry & 3D Scanning' },
      { n: '58', e: '🐟', t: 'Light, Shadow & Ambient Occlusion' },
    ],
  },
];

const badgeTiers = [
  { icon: '🌱', name: 'Creator', count: '3 badges', desc: 'First animation, tool exploration, first export' },
  { icon: '🔧', name: 'Builder', count: '4 badges', desc: 'Squash, arcs, timing, weight' },
  { icon: '🎨', name: 'Developer', count: '6 badges', desc: 'Walk cycle, anticipation, follow-through, mood, lip sync, voice' },
  { icon: '🏆', name: 'Maker', count: '11 badges', desc: 'Storyboard, rigging, effects, sound, game animation, contests, Pi pioneer, physics master, mentor, style, short film' },
  { icon: '🇰🇪', name: 'CBE Competency', count: '6 badges', desc: 'Digital citizen, creative thinker, problem solver, collaborator, code creator, AI ethicist' },
];

const designPrinciples = [
  { n: 1, t: 'Age-calibrated everything', d: 'Tone, vocabulary, tools, critique depth' },
  { n: 2, t: 'The 12 Principles are the backbone', d: 'Every module ties to them' },
  { n: 3, t: 'Project-based learning', d: 'Kids learn by making (ball → walk cycle → short film)' },
  { n: 4, t: 'Process over product', d: 'Celebrate effort, not just polished results' },
  { n: 5, t: 'Never dismiss a kid\'s ambition', d: 'Redirect to age-appropriate starting points' },
  { n: 6, t: 'Hardware equity', d: 'Pi, Chromebook, and phone kids can animate too' },
  { n: 7, t: 'Acting > drawing', d: 'Performance is the #1 animator skill' },
  { n: 8, t: 'Animation is for everyone', d: 'Adaptive tools for all needs' },
  { n: 9, t: 'Physics makes it believable', d: 'Weight, momentum, the Odd Rule' },
  { n: 10, t: 'Done > perfect', d: 'Finishing matters more than perfecting' },
  { n: 11, t: 'AI is a tool, not a replacement', d: 'Learn fundamentals first' },
  { n: 12, t: 'Local is powerful', d: 'Kenya\'s ocean animals make animation relevant' },
];

const mpaTable = [
  { park: 'Watamu Marine National Park', county: 'Kilifi', species: 'Turtles, whale sharks, coral', lessons: '29, 30, 49, 51, 55, 57' },
  { park: 'Kisite-Mpunguti Marine Reserve', county: 'Kwale', species: 'Dolphins, sea turtles', lessons: '01, 31, 43, 49, 56' },
  { park: 'Malindi Marine National Park', county: 'Kilifi', species: 'Coral fish, sea turtles', lessons: '44' },
  { park: 'Mombasa Marine National Park', county: 'Mombasa', species: 'Coral reef, diverse fish', lessons: '44, 53' },
  { park: 'Diani-Chale Marine Reserve', county: 'Kwale', species: 'Whale sharks, dolphins', lessons: '51, 58' },
  { park: 'Lamu Archipelago', county: 'Lamu', species: 'Dugongs, turtles, mangroves', lessons: 'Reference' },
];

// ═══ Bubble component ═══
function Bubbles() {
  const bubbles = Array.from({ length: 15 }, (_, i) => ({
    left: `${(i * 6.5 + 3) % 100}%`,
    size: `${8 + Math.random() * 22}px`,
    duration: `${8 + Math.random() * 10}s`,
    delay: `${Math.random() * 8}s`,
  }));
  return (
    <>
      {bubbles.map((b, i) => (
        <div
          key={i}
          className="bubble"
          style={{
            left: b.left,
            width: b.size,
            height: b.size,
            animationDuration: b.duration,
            animationDelay: b.delay,
          }}
        />
      ))}
    </>
  );
}

// ═══ Page ═══
export default function Home() {
  return (
    <>
      {/* Nav */}
      <nav>
        <div className="nav-inner">
          <div className="nav-brand"><span className="wave">🌊</span>Animation Assistant</div>
          <div className="nav-links">
            <a href="#features">Features</a>
            <a href="#animals">Ocean Animals</a>
            <a href="#modules">58 Modules</a>
            <a href="#badges">Badges</a>
            <a href="#standards">Standards</a>
            <a href="#start">Quick Start</a>
            <a href="https://github.com/drwjkirkpatrick-web/animation-assistant" target="_blank" rel="noopener">GitHub ↗</a>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <header className="hero">
        <Bubbles />
        <div className="wave-bg">
          <svg viewBox="0 0 2880 200" preserveAspectRatio="none" style={{ height: '200px' }}>
            <path fill="rgba(79,195,209,0.08)" d="M0,100 Q360,40 720,100 T1440,100 T2160,100 T2880,100 V200 H0 Z" />
            <path fill="rgba(79,195,209,0.05)" d="M0,130 Q360,70 720,130 T1440,130 T2160,130 T2880,130 V200 H0 Z" />
          </svg>
        </div>
        <div className="hero-content">
          <div className="hero-emoji">🌊</div>
          <h1>Animation Assistant</h1>
          <p className="hero-tagline">
            Teaching kids to animate with Kenya's ocean. Every kid in Mombasa, Kilifi, Kwale, and Lamu
            deserves to tell their stories through animation — using the marine animals swimming right
            outside their doorstep.
          </p>
          <div className="hero-cta">
            <a href="#start" className="btn btn-primary">Quick Start for Teachers</a>
            <a href="#modules" className="btn btn-secondary">Browse 58 Modules</a>
          </div>
          <div className="hero-stats">
            <div className="hero-stat"><div className="num">58</div><div className="label">Prompt Modules</div></div>
            <div className="hero-stat"><div className="num">58</div><div className="label">Lesson Plans</div></div>
            <div className="hero-stat"><div className="num">341</div><div className="label">Test Cases</div></div>
            <div className="hero-stat"><div className="num">30</div><div className="label">Badges</div></div>
            <div className="hero-stat"><div className="num">30+</div><div className="label">Ocean Species</div></div>
          </div>
        </div>
      </header>

      {/* What's Inside */}
      <section id="features" className="section-dark">
        <div className="container">
          <h2 className="section-title">What's Inside</h2>
          <p className="section-subtitle">Five pillars that make this a complete animation education system</p>
          <div className="feature-grid">
            <div className="feature-card">
              <div className="icon">📚</div>
              <h3>58 Prompt Modules</h3>
              <p>Testable system prompts covering everything from the bouncing ball to micro-expressions. Each prompt has a code block and a "What to Test" table with specific inputs and expected behaviors.</p>
            </div>
            <div className="feature-card">
              <div className="icon">📝</div>
              <h3>58 Complete Lesson Plans</h3>
              <p>CBE-aligned, ready-to-teach lesson plans — one for every prompt module. Every lesson uses Kenyan Indian Ocean marine animals as animation characters. A teacher can pick up any lesson plan and teach it directly.</p>
            </div>
            <div className="feature-card">
              <div className="icon">🧪</div>
              <h3>Test Harness</h3>
              <p>341 test cases across all 58 prompts, with CLI for listing, focusing, and non-interactive review.</p>
            </div>
            <div className="feature-card">
              <div className="icon">📊</div>
              <h3>Progress Tracker</h3>
              <p>SQLite-backed student tracker with 30 achievement badges across 5 tiers, printable HTML reports, and standards-aligned progress bars.</p>
            </div>
            <div className="feature-card">
              <div className="icon">🔬</div>
              <h3>Research</h3>
              <p>Animation tools landscape (7 tools for ages 10–17), four-pass gap analysis (42 gaps identified and filled), standards mapping, and Kenya ocean animals reference with 30+ species.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Marine Big Five */}
      <section id="animals" className="section-light">
        <div className="container">
          <h2 className="section-title">Why Kenya's Ocean Animals?</h2>
          <p className="section-subtitle">
            Every lesson plan uses at least one animal from Kenya's Marine Big Five or reef ecosystem as the
            animation subject. This isn't decoration — it's pedagogy.
          </p>
          <div className="animal-grid">
            {marineBigFive.map((a, i) => (
              <div key={i} className="animal-card">
                <div className="emoji">{a.emoji}</div>
                <div className="name">{a.name}</div>
                <div className="swahili">{a.swahili}</div>
                <div className="principle">{a.principle}</div>
              </div>
            ))}
          </div>
          <p style={{ marginTop: '2rem', color: 'var(--text-muted)', fontSize: '0.95rem', textAlign: 'center', maxWidth: '700px', margin: '2rem auto 0' }}>
            Kids in Mombasa animate <strong style={{ color: 'var(--ocean-glow)' }}>Pomboo the Dolphin</strong> leaping at
            Kisite-Mpunguti. Kids in Kilifi animate <strong style={{ color: 'var(--ocean-glow)' }}>Kasa the Turtle</strong> nesting
            at Watamu. The animals are real, the locations are real, the conservation messages are real. Animation becomes a
            way to connect with and protect their own environment.
          </p>
        </div>
      </section>

      {/* 58 Modules */}
      <section id="modules" className="section-dark">
        <div className="container">
          <h2 className="section-title">The 58 Modules at a Glance</h2>
          <p className="section-subtitle">
            From the bouncing ball to photogrammetry — every module tied to the 12 Principles and a Kenyan ocean animal
          </p>
          {moduleGroups.map((group, gi) => (
            <div key={gi} className="module-group">
              <div className="module-group-header">
                <h3>{group.title}</h3>
                <span className="range">{group.range}</span>
              </div>
              <div className="module-grid">
                {group.modules.map((m, mi) => (
                  <div key={mi} className="module-item">
                    <span className="num">{m.n}</span>
                    <span className="emoji">{m.e}</span>
                    <span className="label">{m.t}</span>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Tool Progression */}
      <section className="section-light">
        <div className="container">
          <h2 className="section-title">Animation Tool Progression</h2>
          <p className="section-subtitle">No kid is left out because of hardware</p>
          <div className="tool-progression">
            <pre>{`Beginner (10-12)          Intermediate (12-14)         Advanced (14-17)
─────────────────────────────────────────────────────────────────────
Scratch ${'─'.repeat(5)}► Krita ${'─'.repeat(9)}► OpenToonz
Stop Motion Studio ${'─'.repeat(2)}► Pencil2D ${'─'.repeat(7)}► Blender (3D)
                        Synfig (tweening) ${'─'.repeat(5)}► Blender (Grease Pencil)`}</pre>
          </div>
          <p style={{ marginTop: '1.5rem', color: 'var(--text-muted)', fontSize: '0.92rem', textAlign: 'center' }}>
            Also supports: <strong style={{ color: 'var(--ocean-glow)' }}>Raspberry Pi</strong>, Chromebook, phone/tablet,
            game engines, and adaptive/accessible tools.
          </p>
        </div>
      </section>

      {/* Badges */}
      <section id="badges" className="section-dark">
        <div className="container">
          <h2 className="section-title">Progress Tracker & Achievement System</h2>
          <p className="section-subtitle">
            30 badges across 5 tiers — auto-awarded when a student reaches ME or EE on relevant modules
          </p>
          <div className="badge-grid">
            {badgeTiers.map((t, i) => (
              <div key={i} className="badge-tier">
                <div className="tier-icon">{t.icon}</div>
                <h4>{t.name}</h4>
                <div className="count">{t.count}</div>
                <p>{t.desc}</p>
              </div>
            ))}
          </div>
          <div className="tool-progression" style={{ marginTop: '2rem' }}>
            <pre style={{ fontSize: '0.8rem' }}>{`# Register a student
python tracker/progress_tracker.py add_student --name "Amani" --age 13 --grade 8 --school "Mombasa Primary"

# Record module progress (CBE rubric: BE, AE, ME, EE)
python tracker/progress_tracker.py record --student-id S001 --module 29 --level ME --notes "Great whale shark physics"

# View badges and RPF tier
python tracker/progress_tracker.py badges --student-id S001

# Generate printable HTML report
python tracker/progress_tracker.py report --student-id S001 --output report.html`}</pre>
          </div>
        </div>
      </section>

      {/* Standards */}
      <section id="standards" className="section-light">
        <div className="container">
          <h2 className="section-title">Standards Alignment</h2>
          <p className="section-subtitle">Mapped to two major computing education frameworks</p>
          <div className="standards-grid">
            <div className="standard-card">
              <h3>🥧 Raspberry Pi Foundation</h3>
              <p>11 content strands + 5 Digital Making strands + 4 progression levels (Creator → Builder → Developer → Maker)</p>
            </div>
            <div className="standard-card">
              <h3>🇰🇪 Kenya CBE</h3>
              <p>4 strands (Foundation, Networks, Software, Programming) + 7 core competencies + 4-level rubric (BE/AE/ME/EE)</p>
            </div>
          </div>
        </div>
      </section>

      {/* Marine Protected Areas */}
      <section className="section-dark">
        <div className="container">
          <h2 className="section-title">Kenya's Marine Protected Areas</h2>
          <p className="section-subtitle">Real locations used in real lesson plans</p>
          <div className="tool-progression" style={{ padding: 0, overflow: 'hidden' }}>
            <table className="mpa-table">
              <thead>
                <tr>
                  <th>Park</th>
                  <th>County</th>
                  <th>Key Species</th>
                  <th>Lesson Reference</th>
                </tr>
              </thead>
              <tbody>
                {mpaTable.map((r, i) => (
                  <tr key={i}>
                    <td>{r.park}</td>
                    <td>{r.county}</td>
                    <td>{r.species}</td>
                    <td>{r.lessons}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* Design Principles */}
      <section className="section-light">
        <div className="container">
          <h2 className="section-title">12 Design Principles</h2>
          <p className="section-subtitle">The philosophy behind every module, lesson, and interaction</p>
          <div className="principles-grid">
            {designPrinciples.map((p, i) => (
              <div key={i} className="principle-item">
                <span className="pnum">{p.n}</span>
                <span className="ptext"><strong>{p.t}</strong> — {p.d}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Quick Start */}
      <section id="start" className="section-dark">
        <div className="container">
          <h2 className="section-title">Quick Start for Teachers</h2>
          <p className="section-subtitle">Seven steps from clone to classroom</p>
          <div className="quickstart">
            <ol>
              <li>Read the lesson template: <code>lessons/LESSON-TEMPLATE.md</code></li>
              <li>Pick a lesson: Any <code>lessons/lesson-NN-*.md</code> file — they're numbered by difficulty</li>
              <li>Check the ocean animal reference: <code>research/kenya-ocean-animals.md</code></li>
              <li>Gather resources: Each lesson lists what you need (mostly free tools)</li>
              <li>Teach: Follow the 4-step lesson development structure</li>
              <li>Assess: Use the BE/AE/ME/EE rubric table in each lesson</li>
              <li>Track progress: Use <code>tracker/progress_tracker.py</code> to record and badge</li>
            </ol>
            <p className="start-hint">
              <strong>Recommended starting point for beginners:</strong> Lesson 01 (System Persona) → Lesson 04 (Principles)
              → Lesson 29 (Physics with whale sharks)
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <p className="footer-text">
          This project is part of a growing movement to make animation education accessible to every child,
          regardless of hardware, budget, or geography. From Watamu to Lamu, from Mombasa to Diani — the ocean
          is our classroom, and every animal is a character waiting to be animated.
        </p>
        <div className="footer-links">
          <a href="https://github.com/drwjkirkpatrick-web/animation-assistant" target="_blank" rel="noopener">GitHub Repository ↗</a>
          <a href="https://github.com/drwjkirkpatrick-web/animation-assistant#readme" target="_blank" rel="noopener">README ↗</a>
        </div>
        <p className="license">MIT License — free to use, modify, and share. Built for the kids of Kenya's coast and beyond. 🌊</p>
      </footer>
    </>
  );
}