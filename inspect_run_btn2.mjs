import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const needle = "$('runFullBtn').addEventListener('click'";
const idx = html.indexOf(needle);
console.log(html.substring(idx + 1500, idx + 4000));
