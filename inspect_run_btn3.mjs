import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const needle = "// Render structural architectural improvements";
const idx = html.indexOf(needle);
console.log(html.substring(idx, idx + 2500));
