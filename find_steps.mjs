import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const matches = [...html.matchAll(/const STEPS/g)];
console.log('STEPS occurrences:', matches.length);
matches.forEach(m => console.log('at', m.index, html.substring(m.index - 30, m.index + 80).replace(/\n/g, ' ')));
