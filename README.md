# SmartSorter

An automated, background file organization system built with Python. It monitors folders in real-time and uses a keyword-based semantic analysis (AI) to sort files into intelligent categories before falling back to default extension-based sorting.

## 🚀 Features
- **Real-time Monitoring:** Continuously tracks folder events using OS file system signals via `watchdog`.
- **Hybrid Intelligent Sorting:** Extracts semantic keywords from file names, matches them to an AI concept map, and dynamically generates directory paths.
- **Robust Fallback:** If no semantic keyword is matched, falls back to sorting by physical file extensions.

---

## 🏗️ AI Semantic Map Architecture

The system evaluates raw file names by stripping extension formats and splitting strings into clean sub-tokens to search matches within `AI_KEYWORD_MAP`:

* **`Finance_And_Work`:** Documents containing keywords like `bill`, `contract`, `report`, `salary`, `work`.
* **`Education`:** Files with titles including `homework`, `learning`, `university`, `school`, `course`.
* **`Entertainment_And_Gaming`:** Media containing terms like `game`, `play`, `steam`, `screenshot`, `wallpaper`.
* **`Personal_And_Media`:** Private archives containing `photo`, `family`, `music`, `travel`.

---

## 🛠️ Infrastructure & Deployment Guide

To run this background worker inside your local environment:

```bash
# 1. Spin up a clean virtual environment
pip install watchdog

# 2. Configure the target path inside the source file
target_folder = r"C:\Your\Target\Directory"

# 3. Fire up the background service
python main.py
```
