#!/bin/bash
# Setup script to configure git remotes and prepare for push

# Add the EXE-Maker repo as a second remote
git remote add exe-maker https://github.com/Papaya-Voldemort/EXE-Maker.git 2>/dev/null || git remote set-url --add origin https://github.com/Papaya-Voldemort/EXE-Maker.git

echo "Git remotes configured. Current remotes:"
git remote -v

echo ""
echo "Ready to push! Run:"
echo "  git add ."
echo "  git commit -m 'Add multi-platform builds, exe_versions folder, and automatic releases'"
echo "  git push origin main"
echo "  git push exe-maker main"

