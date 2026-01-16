# TINYI LANGUAGE MODEL

I am building a specialized Document Intelligence system for ancient/inscription-based symbols.
The project works on symbol images stored as files (not embedded in CSV).

Each symbol has multiple visual variants.
Images are normalized and referenced by path only.

## I maintain:

• sign_inventory.csv → one row per image with image path, sign_id, variant_id, normalization info
• sign_map.csv (or JSON) → maps sign_id to canonical meaning/label and groups variants

The goal is not OCR but symbol understanding:
classification of signs, handling variants, and mapping them to canonical meanings.

The pipeline is:
dataset → inventory CSV → mapping file → model training (CNN / hybrid) → inference using references.

This is a Document Intelligence project focused on symbolic documents, not text-heavy PDFs.
