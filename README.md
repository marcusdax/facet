# FACET · Four-Sided Property Intelligence & Architectural Engine

> **Every property has four sides: Sight · Worth · Work · Story**  
> Engineered by **ODASI Technologies Inc.** · Trust records by the **AUCTUM** engine · Styled with **Marcus Dax's Fiduciary-OS Machined-Metal Architecture** (`[planned: S-03]`).

---

## Overview

**FACET** is a next-generation real estate visual systems and financial intelligence platform that unifies high-fidelity architectural renovation inpainting, municipal zoning and cadastral GIS lot intelligence, automated building code compliance review, 12-factor hedonic valuation modeling, institutional underwriting, and itemized quantity takeoff.

Inspired by and styled directly with Marcus Dax's **Fiduciary OS** circuit-board and machined-metal visual system from [`marcusdax/Kimi_Agent_Fiduciary-OS-Business-Blueprint`](https://github.com/marcusdax/Kimi_Agent_Fiduciary-OS-Business-Blueprint), FACET combines industrial-grade metallic card sheens, chrome-edge beveled borders, etched copper trace backgrounds, and multi-weight typography.

---

## The Four Sides

### 1. Sight (Visual Loupe & Cadastral GIS)
- **1:1 Exact House Inpainting:** Transformations preserve 100% of the actual home's camera perspective, landscaping, tree canopy, and sky while applying 5 distinct architectural finishes:
  - *Two-Tone Modern Nordic* (Charcoal & Warm Alabaster)
  - *Warm Natural Cedar Accents* (Tongue-and-groove horizontal siding)
  - *Dark Nordic Minimalist* (Iron Ore & matte black casements)
  - *Modern Coastal Farmhouse* (Crisp white board-and-batten)
  - *Pacific Northwest Slate* (Deep slate blue & natural timber)
- **The Loupe Hotspot Inspector (`FastSAM` & `Inpaint-Anything`):** Interactive hotspot overlays for selective material inspection (Windows, Cedar Siding, Standing Seam Metal Roof, Anodized Aluminum Garage Door).
- **OpenAddresses Cadastral GIS Engine:** Automated parcel lot diagramming, legal bounds visualization, SF-3 single-family zoning limits, and maximum building footprint ratio analysis.

### 2. Worth (Appraisal & Institutional Underwriting)
- **12-Factor Automated Valuation Model (`rlowrance/re-avm`):** Hedonic regression scoring curb appeal lift, energy envelope efficiency, and local micro-comps with P10/P50/P90 confidence intervals.
- **Institutional Underwriting (`Rental-Property-Deal-Analyzer`):** Real-time Debt vs. Cash toggle evaluating **1.34x DSCR**, **21.4% 5-Year Levered IRR**, annual Net Operating Income (NOI), and loan amortization schedules.

### 3. Work (Code Compliance & Quantity Takeoff)
- **CrossBeam AI Plan Review Engine (`mikeOnBreeze/cc-crossbeam`):** Automated residential building code conformance matrix checking:
  - **IRC R612:** Window impact rating & fall protection compliance
  - **IRC R602.10:** Wall bracing & continuous weather-resistant barrier (ASTM D226)
  - **IRC R905.10:** Standing seam metal roofing concealed fastener clips & ice barrier
  - **NEC 210.8:** GFCI exterior branch circuit requirements
- **Quantity Takeoff (`datadrivenconstruction/QuantityTakeoff-Python`):** Itemized Bill of Materials (BoM) with unit costs, labor allocation, and standard 10% scrap/waste allowance.

### 4. Story (Executive Dossier & Proposal Generation)
- **Institutional PDF & Markdown Report:** Instant export of comprehensive investor and client dossiers.
- **Multi-Channel Marketing Copy:** Tailored client outreach emails and short-form social/reels walkthrough scripts.
- **Speech Synthesis Audio:** In-browser narration for executive walkthroughs.

---

## Design System & Aesthetic Tokens

Grounded in the **Fiduciary OS** static machined-metal and etched circuit-board specification:
- **Board Ground (`--fos-board`):** `#12161b`
- **Etched Copper Trace Grid (`--fos-board-etch`):** `rgba(200, 135, 74, 0.11)` on a `32px × 32px` grid
- **Machined Chrome Edge (`--chrome-edge`):** `linear-gradient(125deg, #465361 0%, #bbc6d0 15%, #455260 29%, #71808e 48%, #d5dee6 52%, #3d4a58 69%, #8593a1 100%)`
- **Metallic Card Fill (`--card-fill`):** `linear-gradient(145deg, #20242e, #161922 48%, #11141a)`
- **Typography:**
  - **Space Grotesk 700:** Wordmark & Display Headings
  - **Inter 400 / 600:** User Interface & Controls
  - **JetBrains Mono 400 / 500:** Financial Underwriting, Code References & Telemetry

---

## Quickstart

```bash
# 1. Clone repository
git clone https://github.com/marcusdax/facet.git
cd facet

# 2. Launch micro-gateway server
npm start
# Server listens at http://localhost:3111/
```

Open `http://localhost:3111/` in your browser.

---

## License

MIT © 2026 Marcus Dax · Engineered by ODASI Technologies Inc.
