import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

const btnIdx = html.indexOf('id="runFullBtn"');
console.log('runFullBtn index:', btnIdx);

// Look backwards for the enclosing <section data-panel="...">
const beforeBtn = html.substring(0, btnIdx);
const lastPanelIdx = beforeBtn.lastIndexOf('<section data-panel="');
console.log('Enclosing section:', beforeBtn.substring(lastPanelIdx, lastPanelIdx + 60));
