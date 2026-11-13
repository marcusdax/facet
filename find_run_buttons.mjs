import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const regex = /id="([^"]*run[^"]*)"/gi;
let m;
while ((m = regex.exec(html)) !== null) {
  console.log('Button ID:', m[1]);
}

const btnMatches = [...html.matchAll(/Run Complete Multimodal Analysis/gi)];
console.log('Button text occurrences:', btnMatches.length);
btnMatches.forEach(b => {
  console.log('Context around button:', html.substring(Math.max(0, b.index - 100), Math.min(html.length, b.index + 200)));
});
