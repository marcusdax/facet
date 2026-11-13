import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const nIdx = html.indexOf('id="noticeBanner"');
console.log(html.substring(nIdx - 80, nIdx + 500));
