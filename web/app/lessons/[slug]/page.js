import { marked } from 'marked';
import fs from 'fs';
import path from 'path';

// ═══ Build a slug → filename map at build time ═══
const lessonsDir = path.join(process.cwd(), 'lessons-content');

function getAllLessons() {
  if (!fs.existsSync(lessonsDir)) return {};
  const map = {};
  for (const f of fs.readdirSync(lessonsDir)) {
    if (!f.startsWith('lesson-') || !f.endsWith('.md')) continue;
    const num = f.match(/^lesson-(\d+)/);
    if (num) {
      map[num[1]] = f;
    }
  }
  return map;
}

// Pre-render all 58 lesson pages at build time
export async function generateStaticParams() {
  const lessons = getAllLessons();
  return Object.keys(lessons).map((n) => ({ slug: n }));
}

export async function generateMetadata({ params }) {
  const lessons = getAllLessons();
  const filename = lessons[params.slug];
  if (!filename) return { title: 'Lesson Not Found — Animation Assistant' };
  const raw = fs.readFileSync(path.join(lessonsDir, filename), 'utf8');
  const titleMatch = raw.match(/^#\s+(.+)$/m);
  return {
    title: titleMatch ? `${titleMatch[1]} — Animation Assistant` : `Lesson ${params.slug} — Animation Assistant`,
  };
}

// ═══ Bubbles component (same as home page) ═══
function Bubbles() {
  const bubbles = Array.from({ length: 12 }, (_, i) => ({
    left: `${(i * 7.5 + 3) % 100}%`,
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

export default function LessonPage({ params }) {
  const lessons = getAllLessons();
  const filename = lessons[params.slug];

  let html = '<p>Lesson not found.</p>';
  let prev = null;
  let next = null;
  let lessonTitle = `Lesson ${params.slug}`;

  if (filename) {
    const raw = fs.readFileSync(path.join(lessonsDir, filename), 'utf8');
    html = marked.parse(raw, { mangle: false, headerIds: false });

    const titleMatch = raw.match(/^#\s+(.+)$/m);
    if (titleMatch) lessonTitle = titleMatch[1];

    const nums = Object.keys(lessons).sort((a, b) => Number(a) - Number(b));
    const idx = nums.indexOf(params.slug);
    if (idx > 0) prev = nums[idx - 1];
    if (idx < nums.length - 1) next = nums[idx + 1];
  }

  return (
    <>
      {/* Nav */}
      <nav>
        <div className="nav-inner">
          <a href="/" className="nav-brand"><span className="wave">🌊</span>Animation Assistant</a>
          <div className="nav-links">
            <a href="/#modules">All Modules</a>
            <a href="/#animals">Ocean Animals</a>
            <a href="/#start">Quick Start</a>
            <a href="https://github.com/drwjkirkpatrick-web/animation-assistant" target="_blank" rel="noopener">GitHub ↗</a>
          </div>
        </div>
      </nav>

      {/* Wave header */}
      <header className="lesson-hero">
        <Bubbles />
        <div className="wave-bg">
          <svg viewBox="0 0 2880 200" preserveAspectRatio="none" style={{ height: '200px' }}>
            <path fill="rgba(79,195,209,0.08)" d="M0,100 Q360,40 720,100 T1440,100 T2160,100 T2880,100 V200 H0 Z" />
            <path fill="rgba(79,195,209,0.05)" d="M0,130 Q360,70 720,130 T1440,130 T2160,130 T2880,130 V200 H0 Z" />
          </svg>
        </div>
        <div className="lesson-hero-content">
          <div className="lesson-hero-emoji">🌊</div>
          <h1>{lessonTitle}</h1>
          <div className="lesson-hero-nav">
            {prev && <a href={`/lessons/${prev}`} className="btn btn-secondary">← Lesson {prev}</a>}
            <a href="/#modules" className="btn btn-secondary">All Modules</a>
            {next && <a href={`/lessons/${next}`} className="btn btn-secondary">Lesson {next} →</a>}
          </div>
        </div>
      </header>

      {/* Lesson content */}
      <section className="section-dark lesson-section">
        <div className="container lesson-container">
          <article
            className="lesson-content"
            dangerouslySetInnerHTML={{ __html: html }}
          />
        </div>
      </section>

      {/* Bottom navigation */}
      <section className="section-light lesson-bottom-nav">
        <div className="container">
          <div className="lesson-nav-bottom">
            {prev && <a href={`/lessons/${prev}`} className="btn btn-secondary">← Lesson {prev}</a>}
            <a href="/" className="btn btn-primary">Back to Home</a>
            {next && <a href={`/lessons/${next}`} className="btn btn-secondary">Lesson {next} →</a>}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <p className="footer-text">
          Teaching kids to animate with Kenya's ocean. From Watamu to Lamu — every animal is a character waiting to be animated.
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