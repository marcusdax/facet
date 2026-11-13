import fs from 'fs';

const targets = [
  'C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\facet.html',
  'C:\\Users\\test 123\\.gemini\\antigravity\\scratch\\facet\\index.html',
  'C:\\Users\\test 123\\.gemini\\antigravity\\brain\\89988694-c086-4aed-895f-e958b4cd5c24\\facet.html',
  'C:\\Users\\test 123\\.gemini\\antigravity\\brain\\89988694-c086-4aed-895f-e958b4cd5c24\\propertyinsight_pro.html'
];

targets.forEach(t => {
  let html = fs.readFileSync(t, 'utf8');
  const oldBlock = `  // ---------- PIPELINE TRACKER & EXECUTION ----------
  const STEPS = ['Insight', 'Inpainting', 'Scope', 'Estimates', 'Permits', 'Safety', 'Upsell', 'Outreach'];
  function renderTracker(stepStates = {}) {
    $('pipelineTracker').innerHTML = STEPS.map(s => {
      const status = stepStates[s] || 'idle';
      const icon = { idle: '○', running: '◐', done: '●', error: '✕' }[status];
      const color = { idle: 'text-[var(--muted-foreground,#94a3b8)] border-[#3a434c]', running: 'text-indigo-400 border-indigo-500 bg-indigo-500/10', done: 'text-emerald-400 border-emerald-500 bg-emerald-500/10', error: 'text-red-400 border-red-500' }[status];
      return \`<li class="p-1.5 rounded border text-center font-medium \${color}">\${icon} \${s}</li>\`;
    }).join('');
  }
  renderTracker();\n\n`;

  if (html.includes(oldBlock)) {
    html = html.replace(oldBlock, '');
    fs.writeFileSync(t, html, 'utf8');
    console.log('Removed duplicate STEPS block in:', t);
  }
});
