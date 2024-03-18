#!/bin/bash

# Navigate to your project directory
cd /Users/atesz/Documents/tracking-terra/

# Activate your virtual environment if you have one
# source /path/to/your/venv/bin/activate

# Run your Python script
/opt/homebrew/bin/python3 /Users/atesz/Documents/tracking-terra/Scraper.py

# Add changes to git
git add index.html

# Commit changes
git commit -m "Update sold tickets count"

# Push changes to GitHub
git push origin tracking-terra
