import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const navStart = html.indexOf('<nav');
const navEnd = html.indexOf('</nav>');
console.log(html.substring(navStart, navEnd + 6));
