// PropertyInsight Pro - Local Micro-Gateway & Static Asset Server
// Runs locally to serve dashboard, assets, and proxy Gemini API calls.
// Zero external npm dependencies.

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PORT = process.env.PORT || 3111;

const BRAIN_DIR = 'C:\\Users\\test 123\\.gemini\\antigravity\\brain\\89988694-c086-4aed-895f-e958b4cd5c24';

const IMAGES = {
  before: path.join(BRAIN_DIR, 'house_base_hd.png'),
  'two-tone': path.join(BRAIN_DIR, 'exact_house_after_two-tone.jpg'),
  cedar: path.join(BRAIN_DIR, 'exact_house_after_cedar.jpg'),
  nordic: path.join(BRAIN_DIR, 'exact_house_after_nordic.jpg'),
  farmhouse: path.join(BRAIN_DIR, 'exact_house_after_farmhouse.jpg'),
  slate: path.join(BRAIN_DIR, 'exact_house_after_slate.jpg')
};

let configKey = '';
try {
  const cfgPath = path.join(__dirname, 'config.json');
  if (fs.existsSync(cfgPath)) {
    const raw = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
    configKey = raw.apiKey || '';
  }
} catch (e) {
  // ignore
}

function resolveKey(req) {
  return (
    req.headers['x-goog-api-key'] ||
    req.headers['x-api-key'] ||
    process.env.GEMINI_API_KEY ||
    configKey ||
    ''
  );
}

function sendCors(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, x-goog-api-key, x-api-key');
}

const server = http.createServer(async (req, res) => {
  sendCors(res);

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const url = new URL(req.url, `http://localhost:${PORT}`);

  // Health check
  if (url.pathname === '/api/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'online',
      version: '3.7.0',
      timestamp: new Date().toISOString(),
      hasKeyConfigured: Boolean(process.env.GEMINI_API_KEY || configKey),
      imagesAvailable: Object.keys(IMAGES).filter(k => fs.existsSync(IMAGES[k]))
    }));
    return;
  }

  // Image serving endpoints
  if (url.pathname.startsWith('/api/images/')) {
    const key = url.pathname.replace('/api/images/', '').toLowerCase();
    const filePath = IMAGES[key];
    if (filePath && fs.existsSync(filePath)) {
      const isPng = filePath.endsWith('.png');
      res.writeHead(200, {
        'Content-Type': isPng ? 'image/png' : 'image/jpeg',
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      });
      res.end(fs.readFileSync(filePath));
      return;
    }
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: `Image not found for key: ${key}` }));
    return;
  }

  // Gemini Proxy
  if (url.pathname.startsWith('/api/gemini/')) {
    const model = url.searchParams.get('model') || 'gemini-3.8-flash';
    const effectiveKey = resolveKey(req);

    if (!effectiveKey) {
      res.writeHead(401, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        error: { message: 'No Gemini API key provided. Supply x-api-key header or set GEMINI_API_KEY.' }
      }));
      return;
    }

    let bodyData = '';
    req.on('data', chunk => { bodyData += chunk; });
    req.on('end', async () => {
      try {
        const targetUrl = `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent?key=${effectiveKey}`;
        const targetRes = await fetch(targetUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: bodyData || '{}'
        });

        const data = await targetRes.json().catch(() => ({}));
        res.writeHead(targetRes.status, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(data));
      } catch (err) {
        res.writeHead(502, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: { message: `Gateway fetch failed: ${err.message}` } }));
      }
    });
    return;
  }

  // Assets bundle serving
  if (url.pathname === '/architectural_assets.js') {
    const jsPath = path.join(BRAIN_DIR, 'architectural_assets.js');
    if (fs.existsSync(jsPath)) {
      res.writeHead(200, { 'Content-Type': 'application/javascript; charset=utf-8' });
      res.end(fs.readFileSync(jsPath));
      return;
    }
  }

  // QR Code serving
  if (url.pathname === '/qr' || url.pathname === '/phone_qr_code.png') {
    const qrPath = path.join(BRAIN_DIR, 'phone_qr_code.png');
    if (fs.existsSync(qrPath)) {
      res.writeHead(200, { 'Content-Type': 'image/png' });
      res.end(fs.readFileSync(qrPath));
      return;
    }
  }

  // Dashboard serving
  if (url.pathname === '/' || url.pathname === '/index.html' || url.pathname === '/facet' || url.pathname === '/facet.html') {
    const htmlPath = path.join(BRAIN_DIR, 'facet.html');
    if (fs.existsSync(htmlPath)) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(fs.readFileSync(htmlPath));
      return;
    }
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: { message: 'Not found' } }));
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`[FACET Gateway · The Loupe] Running on http://localhost:${PORT} and http://0.0.0.0:${PORT}`);
  console.log(`[FACET Gateway · The Loupe] Local Network: http://192.168.1.182:${PORT}`);
  console.log(`[FACET Gateway · The Loupe] Health check: http://localhost:${PORT}/api/health`);
});
