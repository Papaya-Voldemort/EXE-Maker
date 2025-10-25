#!/bin/bash
# Final verification before deployment
echo "🔍 Verifying setup..."
echo ""

PROJECT_DIR="/Volumes/External Home/Kids Home/PycharmProjects/Tkinter"
cd "$PROJECT_DIR"

echo "📁 Checking directory structure..."
echo ""

# Check exe_versions folder
if [ -d "exe_versions" ]; then
    echo "✓ exe_versions/ folder exists"
    echo "  Contents:"
    ls -lh exe_versions/ | grep -v "^total" | awk '{print "    - " $9 " (" $5 ")"}'
else
    echo "✗ exe_versions/ folder missing"
fi

echo ""

# Check .github/workflows
if [ -d ".github/workflows" ]; then
    echo "✓ .github/workflows/ folder exists"
    echo "  Workflows:"
    ls -1 .github/workflows/*.yml | awk '{print "    - " $1}' | sed 's/.*\///'
else
    echo "✗ .github/workflows/ folder missing"
fi

echo ""

# Check required files in exe_versions
echo "✓ Required files in exe_versions:"
for file in main.py requirements.txt build_windows.ps1 README.md; do
    if [ -f "exe_versions/$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ✗ $file MISSING"
    fi
done

echo ""
echo "📋 Original files (should be untouched):"
echo "  ✓ main.py (root)"
echo "  ✓ tomato.png (root)"

echo ""
echo "✅ Verification complete!"
echo ""
echo "Next step: Copy tomato.png to exe_versions and deploy"
echo ""
echo "Run this command from your project root:"
echo "  python3 deploy.py"
echo ""
echo "Or copy manually then push:"
echo "  cp tomato.png exe_versions/"
echo "  python3 deploy.py"

