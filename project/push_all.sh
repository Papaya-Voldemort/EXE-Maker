#!/bin/bash
# Complete setup and push script for multi-platform EXE builds

set -e

PROJECT_DIR="/Volumes/External Home/Kids Home/PycharmProjects/Tkinter"
cd "$PROJECT_DIR"

echo "🚀 Starting setup and push to GitHub..."
echo ""

# Step 1: Copy tomato.png to exe_versions
echo "📋 Step 1: Copying tomato.png to exe_versions/"
cp tomato.png exe_versions/tomato.png
echo "✓ tomato.png copied"
echo ""

# Step 2: Initialize git if needed and configure remotes
echo "📋 Step 2: Configuring Git remotes..."
if [ ! -d .git ]; then
    git init
    echo "✓ Git repository initialized"
fi

# Set origin if not already set
if ! git remote get-url origin > /dev/null 2>&1; then
    read -p "Enter your GitHub repo URL (e.g., https://github.com/username/repo.git): " origin_url
    git remote add origin "$origin_url"
    echo "✓ Origin remote added"
fi

# Add exe-maker as additional remote for pushing
if ! git remote get-url exe-maker > /dev/null 2>&1; then
    git remote add exe-maker https://github.com/Papaya-Voldemort/EXE-Maker.git
    echo "✓ EXE-Maker remote added"
else
    git remote set-url exe-maker https://github.com/Papaya-Voldemort/EXE-Maker.git
    echo "✓ EXE-Maker remote updated"
fi
echo ""

# Step 3: Add all files
echo "📋 Step 3: Staging files..."
git add -A
echo "✓ Files staged"
echo ""

# Step 4: Create commit
echo "📋 Step 4: Creating commit..."
git commit -m "Add multi-platform builds (Windows, macOS, Linux), exe_versions folder with isolated main.py, automatic releases with version bumping, and tomato.png as app icon" || echo "ℹ️  No changes to commit"
echo ""

# Step 5: Push to both repos
echo "📋 Step 5: Pushing to GitHub..."
echo "   → Pushing to origin (main repo)..."
git push -u origin main 2>&1 || echo "ℹ️  Already up to date or push skipped"
echo ""

echo "   → Pushing to exe-maker repo..."
git push exe-maker main 2>&1 || echo "ℹ️  EXE-Maker push skipped or already up to date"
echo ""

# Step 6: Display status
echo "✅ Setup complete!"
echo ""
echo "📊 Git remotes:"
git remote -v
echo ""

echo "🎉 Next steps:"
echo "   1. GitHub Actions will automatically build on every push:"
echo "      • Windows EXE (build-windows-exe.yml)"
echo "      • macOS DMG (build-macos.yml)"
echo "      • Linux binary (build-linux.yml)"
echo ""
echo "   2. Check releases at:"
origin=$(git remote get-url origin)
repo_name=$(echo "$origin" | sed 's/.*\///' | sed 's/\.git$//')
repo_user=$(echo "$origin" | sed 's/.*github.com\///' | sed 's/\/.*//')
echo "      https://github.com/$repo_user/$repo_name/releases"
echo ""
echo "   3. Each successful build creates a new versioned release (v1, v2, v3...)"
echo "   4. Download binaries from the Releases page"

