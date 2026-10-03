import manifest from '../data/manifest.json';

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

export const homes = (manifest.homes || {}) as Record<string, { title: string; bodyClass: string; css: string; chrome: string; dir?: string }>;
export const posts = (manifest.posts || []) as Array<{ slug: string; title: string; excerpt: string; cover: string; date: string; site: string; categories: string[]; format: string; bodyClass: string }>;
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
  return {
    title: p.title || slug,
    description: p.excerpt || '',
    bodyClass: p.bodyClass || DEFAULT_BODY_CLASS,
    css: 'single',
    js: 'single',
    dir: 'ltr',
    main: pick(POST, slug + '.html'),
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
