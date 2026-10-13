import manifest from '../data/manifest.json';
import { getCollection } from 'astro:content';
import { marked } from 'marked';

const CHROME = import.meta.glob('../generated/chrome/*.html', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;
const HOME = import.meta.glob('../generated/home/*.html', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;
const POST = import.meta.glob('../generated/posts/*.html', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;
const CAT = import.meta.glob('../generated/cat/*.html', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;
const TAG = import.meta.glob('../generated/tag/*.html', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;
const PAGE = import.meta.glob('../generated/page/*.html', { query: '?raw', import: 'default', eager: true }) as Record<string, string>;

const pick = (map: Record<string, string>, file: string) => {
  const k = Object.keys(map).find((x) => x.endsWith('/' + file));
  return k ? map[k] : '';
};

const SITE_DESC = 'CoinAI News';
const DEFAULT_BODY_CLASS = 'post-template-default single single-post single-format-standard wp-embed-responsive theme-atlas s-front site-skin site-light box-solid wheading-simple sticky-header-active reading-indicator-bottom sticky-sidebar elementor-default elementor-kit-6';

type Chrome = { header: string; footer: string; tail: string };
const chrome = (key: string): Chrome => ({
  header: pick(CHROME, key + '.header.html'),
  footer: pick(CHROME, key + '.footer.html'),
  tail: pick(CHROME, key + '.tail.html'),
});

// --- Purani posts (manifest.json se) ---
const oldPosts = (manifest.posts || []) as Array<{
  slug: string;
  title: string;
  excerpt: string;
  cover: string;
  date: string;
  site: string;
  categories: string[];
  format: string;
  bodyClass: string;
}>;

// --- Nayi posts (src/content/blog/ se) ---
let newPosts: any[] = [];
try {
  const collection = await getCollection('blog');
  console.log('COLLECTION COUNT:', collection.length);
  const newPostsRaw = await Promise.all(
    collection
      .filter((p: any) => p.data.draft !== true)
      .map(async (p: any) => {
        const cleanId = (p.id || '').replace(/\.(md|mdx)$/i, '').split('/').pop();
        const slug = p.data.slug || cleanId;
        const htmlBody = await marked.parse(p.body || '');
        return {
          slug,
          title: p.data.title || slug,
          excerpt: p.data.description || '',
          cover: p.data.image || '',
          date: p.data.pubDate
            ? new Date(p.data.pubDate).toISOString().split('T')[0]
            : '2026-01-01',
          site: 'CoinAINews',
          categories: [p.data.category || 'Market News'],
          format: 'standard',
          bodyClass: 'single-post',
          _isNew: true,
          _body: htmlBody,
          _data: p.data,
        };
      })
  );
  newPosts = newPostsRaw.filter((p: any) => p.slug);
} catch (e) {
  console.warn('Blog collection not available:', e);
}

// --- Dono ko merge karo ---
export const posts = [...oldPosts, ...newPosts].sort((a, b) => {
  const da = new Date(a.date).getTime();
  const db = new Date(b.date).getTime();
  return db - da;
});

console.log('NEWPOSTS COUNT:', newPosts.length);
console.log('POSTS COUNT:', posts.length);

export const homes = (manifest.homes || {}) as Record<string, { title: string; bodyClass: string; css: string; chrome: string; dir?: string }>;
export const categories = (manifest.categories || {}) as Record<string, { title: string; bodyClass: string }>;
export const tags = (manifest.tags || {}) as Record<string, { title: string; bodyClass: string }>;
export const pages = (manifest.pages || {}) as Record<string, { title: string; bodyClass: string }>;

export type Doc = { title: string; description: string; bodyClass: string; css: string; js: string; dir: string; main: string } & Chrome;

export function homeDoc(variant: string): Doc {
  const m = homes[variant] ?? homes.default;
  if (!m) {
    return { title: 'CoinAI News', description: SITE_DESC, bodyClass: 'home', css: 'home-default', js: 'home-default', dir: 'ltr', main: '', ...chrome('default') };
  }
  const key = homes[variant] ? variant : 'default';
  return { title: m.title, description: SITE_DESC, bodyClass: m.bodyClass, css: m.css, js: m.css, dir: m.dir || 'ltr', main: pick(HOME, key + '.html'), ...chrome(m.chrome) };
}

export function postDoc(slug: string): Doc {
  const p = posts.find((x) => x.slug === slug);
  if (!p) {
    return { title: 'Not Found', description: '', bodyClass: DEFAULT_BODY_CLASS, css: 'single', js: 'single', dir: 'ltr', main: '', ...chrome('inner') };
  }

  let mainHtml = '';

  if ((p as any)._body && (p as any)._body.length > 0) {
    const data = (p as any)._data || {};
    const body = (p as any)._body;
    mainHtml = `
      <article class="atlas-post" data-slug="${p.slug}">
        <header class="atlas-post__header">
          <h1 class="atlas-post__title">${data.title || p.title}</h1>
          <div class="atlas-post__meta">
            <span class="atlas-post__author">${data.author || 'Coin AI News Team'}</span>
            <time class="atlas-post__date" datetime="${p.date}">${p.date}</time>
          </div>
          <div class="atlas-post__categories">
            <span class="atlas-post__category">${data.category || 'Market News'}</span>
          </div>
        </header>
        <div class="atlas-post__content">
          ${body}
        </div>
      </article>
    `;
  } else {
    mainHtml = pick(POST, slug + '.html');
  }

  return {
    title: p.title || slug,
    description: p.excerpt || '',
    bodyClass: p.bodyClass || DEFAULT_BODY_CLASS,
    css: 'single',
    js: 'single',
    dir: 'ltr',
    main: mainHtml,
    ...chrome('inner')
  };
}

export function catDoc(cat: string): Doc {
  const m = categories[cat];
  return { title: m?.title || cat, description: SITE_DESC, bodyClass: m?.bodyClass || 'archive', css: 'archive', js: 'archive', dir: 'ltr', main: pick(CAT, cat + '.html'), ...chrome('inner') };
}

export function tagDoc(tag: string): Doc {
  const m = tags[tag];
  return { title: m?.title || tag, description: SITE_DESC, bodyClass: m?.bodyClass || 'archive', css: 'archive', js: 'archive', dir: 'ltr', main: pick(TAG, tag + '.html'), ...chrome('inner') };
}

export function pageDoc(name: string, css = 'archive'): Doc {
  const m = pages[name];
  return { title: m?.title || 'Atlas', description: SITE_DESC, bodyClass: m?.bodyClass || '', css, js: css, dir: 'ltr', main: pick(PAGE, name + '.html'), ...chrome('inner') };
}
