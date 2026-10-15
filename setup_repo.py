import os

FILES = {
    ".gitignore": r'''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
.venv/
env/

# Datasets and large model weights
data/
*.csv
models/*.pth
models/*.onnx
!models/.gitkeep

# Local setup script & IDE files
setup_repo.py
.vscode/
.idea/
.DS_Store
Thumbs.db
''',

    "requirements.txt": r'''torch>=2.1.0
torchvision>=0.16.0
timm>=0.9.12
opencv-python-headless>=4.8.0
numpy>=1.24.0
pandas>=2.0.0
Pillow>=10.0.0
scikit-learn>=1.3.0
streamlit>=1.32.0
onnx>=1.15.0
onnxruntime>=1.17.0
matplotlib>=3.8.0
''',

    ".streamlit/config.toml": r'''[theme]
primaryColor = "#0EA5E9"
backgroundColor = "#0F172A"
secondaryBackgroundColor = "#1E293B"
textColor = "#F8FAFC"
font = "sans serif"

[server]
maxUploadSize = 50
headless = true
''',

    "models/.gitkeep": r'''''',

    "README.md": r'''# 👁️ RetinoScan Edge
**Explainable Edge-AI for Early Diabetic Retinopathy Triaging, Lesion Localization, and Rural Clinical Workflow Optimization.**

Built for **Challenge 01: AI/ML in Healthcare** (*AI for better healthcare outcomes*).

## 🎯 Alignment with Hackathon Checkpoints
1. **Early Disease-Risk Prediction:** Combines deep retinal feature logits with systemic patient biomarkers (HbA1c, diabetes duration, blood pressure) to forecast 6-month vision-loss progression risk.
2. **Medical Image Analysis & Decision Support:** Uses **Ben Graham Illumination Normalization**, **Green-Channel CLAHE**, and **Grad-CAM** activation heatmaps so doctors visually verify microaneurysms and exudates rather than trusting a black-box score.
3. **Patient Monitoring & Preventive Care:** Tracks multi-visit retinal severity drifts over time and generates personalized bilingual (English & Hindi) glycemic/lifestyle preventive regimens.
4. **Healthcare Accessibility & Workflow Optimization:** Compresses `EfficientNet-B0` via **ONNX Dynamic INT8 Quantization** (~75% smaller footprint, <25ms CPU latency) for offline rural clinics and exports interoperable **HL7 FHIR JSON** triage records.

## 🚀 Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
