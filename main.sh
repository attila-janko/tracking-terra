#!/bin/bash

# Navigate to your project directory
cd /Users/atesz/Documents/tracking-terra/

# Activate your virtual environment if you have one
# source /path/to/your/venv/bin/activate

# Run your Python script
/opt/homebrew/bin/python3 /Users/atesz/Documents/tracking-terra/Scraper.py

# Check for a .gitignore file and create it if it doesn't exist
if [ ! -f .gitignore ]; then
    touch .gitignore
fi

# Ensure .DS_Store is in .gitignore
if ! grep -q ".DS_Store" .gitignore; then
    echo ".DS_Store" >> .gitignore
fi

# Add .gitignore changes to staging
git add .gitignore

# Stage any other changes, including the updated index.html
git add index.html

# Commit changes with a check to ensure there's something to commit
if ! git diff --cached --exit-code > /dev/null; then
    git commit -m "Update sold tickets count and ignore .DS_Store"
else
    echo "No changes to commit."
fi



GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_cronjob -o IdentitiesOnly=yes" git push origin main --force

