import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const panels = [...html.matchAll(/<section data-panel="([^"]+)"([^>]*)/gi)];
panels.forEach(p => console.log('Panel:', p[1], 'attrs:', p[2]));

const tabs = [...html.matchAll(/data-tab="([^"]+)"([^>]*)/gi)];
tabs.forEach(t => console.log('Tab:', t[1], 'attrs:', t[2]));
