import fs from 'fs';

const html = fs.readFileSync('C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html', 'utf8');

// Check navigation tab order
const navSlice = html.substring(html.indexOf('<nav'), html.indexOf('</nav>'));
const tabMatches = [...navSlice.matchAll(/data-tab="([^"]+)"/g)].map(m => m[1]);
console.log('Tab Order in Nav:', tabMatches);

const firstTabIsInput = tabMatches[0] === 'input' && tabMatches[1] === 'overview';
console.log('Is Tab 1 Input and Tab 2 Overview?', firstTabIsInput);

// Check panel visibility in static HTML
const inputPanelMatch = html.match(/<section data-panel="input" class="([^"]*)"/);
const overviewPanelMatch = html.match(/<section data-panel="overview" class="([^"]*)"/);

console.log('Input Panel classes:', inputPanelMatch?.[1]);
console.log('Overview Panel classes:', overviewPanelMatch?.[1]);

const inputVisible = !inputPanelMatch?.[1].includes('hidden');
const overviewHidden = overviewPanelMatch?.[1].includes('hidden');

console.log('Input panel visible by default?', inputVisible);
console.log('Overview panel hidden by default?', overviewHidden);

// Check hero run button
console.log('Has heroRunBtn?', html.includes('id="heroRunBtn"'));
console.log('Has auto tab switch in executeMultimodalAnalysis?', html.includes("setTab('overview')"));
console.log('Has smooth scroll to comparisonBox?', html.includes("comp.scrollIntoView({ behavior: 'smooth', block: 'center' })"));

const allGood = firstTabIsInput && inputVisible && overviewHidden && html.includes('id="heroRunBtn"');
console.log('FLOW REARCHITECTURE STATUS:', allGood ? 'PASSED 100%' : 'FAIL');
process.exit(allGood ? 0 : 1);
