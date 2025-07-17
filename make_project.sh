#!/bin/bash

# Base dir is script's location
BASE="$(cd "$(dirname "$0")" && pwd)"

# Folders to create
dirs=(
  ".github/workflows"
  "src/data"
  "src/features"
  "src/models"
  "src/analysis"
  "data/raw"
  "data/interim"
  "data/processed"
  "data/external"
  "notebooks"
  "models"
  "reports/figures"
)

# Create folders with .gitkeep
for d in "${dirs[@]}"; do
  mkdir -p "$BASE/$d"
  touch "$BASE/$d/.gitkeep"
done

# Create common files
files=(
  ".gitignore" ".env" "README.md" "LICENSE"
  "requirements.txt" "environment.yml"
  "reports/final_report.md"
)

for f in "${files[@]}"; do
  path="$BASE/$f"
  mkdir -p "$(dirname "$path")"
  [[ "${f##*.}" == "md" ]] && echo "# $(basename "$f")" > "$path" || touch "$path"
done

# Python source files to auto-create (empty)
py_files=(
  "src/main.py"
  "src/data/collection.py" "src/data/processing.py"
  "src/features/engineering.py"
  "src/models/train.py" "src/models/predict.py" "src/models/evaluation.py"
  "src/analysis/eda.py"
)


for f in "${py_files[@]}"; do
  touch "$BASE/$f"
done

echo "Project scaffold initialized at: $BASE"

