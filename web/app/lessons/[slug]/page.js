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

export default function LessonPage({ params }) {
  const lessons = getAllLessons();
  const filename = lessons[params.slug];

  let html = '<p>Lesson not found.</p>';
  let prev = null;
  let next = null;

  if (filename) {
    const raw = fs.readFileSync(path.join(lessonsDir, filename), 'utf8');
    html = marked.parse(raw, { mangle: false, headerIds: false });

    const nums = Object.keys(lessons).sort((a, b) => Number(a) - Number(b));
    const idx = nums.indexOf(params.slug);
    if (idx > 0) prev = nums[idx - 1];
    if (idx < nums.length - 1) next = nums[idx + 1];
  }

  return (
    <div className="lesson-page">
      <nav className="lesson-nav">
        <a href="/" className="lesson-back">← Back to Home</a>
      </nav>
      <article
        className="lesson-content"
        dangerouslySetInnerHTML={{ __html: html }}
      />
      <div className="lesson-nav-bottom">
        {prev && <a href={`/lessons/${prev}`} className="btn btn-secondary">← Lesson {prev}</a>}
        <a href="/" className="btn btn-secondary">Home</a>
        {next && <a href={`/lessons/${next}`} className="btn btn-secondary">Lesson {next} →</a>}
      </div>
    </div>
  );
}