# AI System for Undeciphered Scripts  

## Overview
This project aims to build an AI-assisted framework for the analysis of **undeciphered writing systems**, with the **Indus Script** as the primary case study.  
The focus is on **data engineering, corpus construction, and statistical language modeling**, rather than premature semantic interpretation.

The system is designed to be **modular and extensible**, allowing future integration of computer vision models and large language models once a clean symbolic corpus is established.

---

## Objectives
- Construct a **clean, machine-readable corpus** of undeciphered script inscriptions  
- Normalize and index **glyph images** consistently  
- Lay groundwork for future **vision-based and multimodal AI models**

---

## Project Scope
### Current Phase (Phase 1: Data & Symbolic Modeling)
- Glyph image normalization
- Sign inventory construction
- Inscription-level JSON corpus creation
- Statistical sequence modeling (n-gram, HMM)

### Future Phases
- CNN / ViT-based glyph embeddings
- Multimodal alignment (image + symbol + position)
- Transformer-based sequence modeling
- Cross-script generalization to other undeciphered scripts

---

## Dataset Sources
- **Glyph images**: indusscript.in  
- **Inscription metadata and sign sequences**: Public Firestore backend used by indusscript.in  

---

---

## Data Representation

### 1. Sign Inventory (`sign_inventory.csv`)
A minimal mapping between sign IDs and glyph images.

```csv
sign_id,image_file,normalized_image_file
1,sign_001.png,normalized_images/sign_001.png
```

## Inscription JSON Schema
```bash
{
  "inscription_id": "M-2420",
  "line_id": 2,
  "site": null,
  "object_type": null,
  "material": null,
  "direction": "RTL",
  "sign_sequence": [1, 167, 7],
  "positions": ["INIT", "MED", "TERM"]
}
```
