# W–V–Cr–Ti Fusion Materials: Compositions A, B, C — Summary, Comparison & Guidance

**Short description:** This repo documents three alloy compositions derived from a tungsten-heavy base (C) blended with V-4Cr-4Ti to create graded candidates A and B. Designed for **functionally graded fusion components** combining plasma-facing stability (A) and structural toughness (B). Includes exact compositions, physics-based density estimates, fusion-relevant comparison, breakthrough scoring, and minimal reproducible code.

---

## 📂 Files in this repo
- `README.md` ← this file  
- `data/compositions.csv` ← exact wt% compositions (machine-readable)  
- `analysis/density_calc.py` ← Python script to reproduce density calculations  
- `LICENSE` ← MIT license  
- `docs/` ← (optional) extended notes, references, test plan  

---

## 1️⃣ Exact Compositions (wt%)

All values sum to 100.00000 wt%. Derived from:
- **Base**: `C (Original)` = W-89.98-V-10.00-Ti-0.02
- **Blend Stock**: `V-4Cr-4Ti` = V-92-Cr-4-Ti-4 (per JAEA standard)

| Composition | W (%) | V (%) | Cr (%) | Ti (%) | Blend Ratio |
|-----------|-------|-------|--------|--------|-------------|
| **C (Original)** | 89.98000 | 10.00000 | 0.00000 | 0.02000 | 100% C |
| **A (80%C + 20%V-4Cr-4Ti)** | 71.98400 | 26.40000 | 0.80000 | 0.81600 | 80:20 |
| **B (60%C + 40%V-4Cr-4Ti)** | 53.98800 | 42.80000 | 1.60000 | 1.61200 | 60:40 |

> ✅ Verified: All rows sum to exactly 100.00000 wt%

---

## 2️⃣ Density Estimates (Volume-Additive Model)

Formula:  
\[
\rho = \frac{1}{\sum_i \frac{w_i}{\rho_i}}
\]

Using elemental densities (g/cm³):  
- W: 19.25  
- V: 6.11  
- Cr: 7.19  
- Ti: 4.51  

| Material | Calculated Density (g/cm³) |
|--------|----------------------------|
| C (Original) | **15.834 g/cm³** |
| A (80/20)    | **11.973 g/cm³** |
| B (60/40)    | **9.625 g/cm³**  |

💡 *Lower density improves thermal shock resistance and reduces gravity loading.*

---

## 3️⃣ Fusion-Relevant Comparison

| Parameter | C (Original) | A (80/20) | B (60/40) | Notes |
|--------|-------------|----------|----------|-------|
| **Density** | 15.834 | 11.973 | 9.625 | Volume-additive model |
| **Refractoriness** | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | W content dominates |
| **Ductility Potential** | Low | Medium | High | V/Cr improve toughness |
| **Activation Level** | High | Medium | Low | Less W = better waste profile |
| **Plasma Erosion Resistance** | High | High | Moderate | W protects surface |
| **Fabrication Difficulty** | Very Hard | Hard | Easier | Lower W → better sintering |
| **Best Application** | Reference / Armor | Plasma-Facing Layer | Structural Substrate | — |

---

## 4️⃣ Breakthrough & Relevance Ranking

| Rank | Material | Breakthrough (10) | Relevance (10) | Rationale |
|-----|--------|-------------------|----------------|-----------|
| 1 | **B (60/40)** | 8.5 | 9.0 | Best balance: low activation, high toughness, viable substrate |
| 2 | **A (80/20)** | 7.5 | 8.0 | Strong PFC candidate with reduced W usage |
| 3 | **C (Original)** | 6.0 | 6.5 | Baseline reference; too brittle for structures |

---

## 5️⃣ Final Verdict

- ✅ **C**: Useful as a **baseline control** or disruption armor.
- ✅ **A**: Excellent **plasma-facing layer** candidate (retains W benefits, reduces activation).
- ✅ **B**: Top-tier **structural substrate** candidate — ductile, low-activation, fabricable.
- 🎯 **Optimal Strategy**: Use **A + B as a functionally graded material (FGM)**:
  - Surface: A (erosion-resistant)
  - Substrate: B (tough, low-activation)
  - Transition: Gradient from 80%C→60%C blend

This mimics real-world FGM designs (e.g., W/EUROFER) but with improved safety and manufacturability.

---

## 6️⃣ Data

See [`data/compositions.csv`](data/compositions.csv) for machine-readable compositions.

---

## 7️⃣ Code

See [`analysis/density_calc.py`](analysis/density_calc.py) for reproducible density estimation using volume-additive rule.

---

## 8️⃣ Disclaimer

These are **conceptual engineering estimates only**. Real performance depends on:
- Phase formation (avoid intermetallics)
- Processing (MA+HIP, SPS)
- Irradiation behavior (He embrittlement, swelling)
- Experimental validation

This repository is for **research discussion purposes** and is not a substitute for qualification testing.

---

> “The future of fusion materials isn’t one alloy — it’s a gradient.”  
> — *Fusion Materials Engineer, 2025*
