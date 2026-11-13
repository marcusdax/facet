import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const needle = "$('runFullBtn')";
const idx = html.indexOf(needle);
console.log('Index of runFullBtn in script:', idx);

if (idx !== -1) {
  console.log(html.substring(idx - 50, idx + 2500));
}
