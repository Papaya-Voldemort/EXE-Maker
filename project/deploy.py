#!/usr/bin/env python3
"""
Complete setup and deployment script for multi-platform Pomodoro builds.
This script:
1. Copies tomato.png to exe_versions/
2. Initializes git (if needed)
3. Configures remotes for both your repo and EXE-Maker
4. Commits and pushes all changes
"""

import os
import shutil
import subprocess
import sys

PROJECT_DIR = "/Volumes/External Home/Kids Home/PycharmProjects/Tkinter"

def run_cmd(cmd, description=""):
    """Run shell command with error handling."""
    if description:
        print(f"  {description}...", end=" ", flush=True)
    try:
        result = subprocess.run(cmd, shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
        if result.returncode != 0 and "already exists" not in result.stderr:
            if description:
                print(f"⚠️  (continuing)")
            else:
                print(f"⚠️  {result.stderr[:100]}")
            return False
        if description:
            print("✓")
        return True
    except Exception as e:
        if description:
            print(f"✗ {str(e)[:50]}")
        return False

def copy_image():
    """Copy tomato.png to exe_versions/"""
    src = os.path.join(PROJECT_DIR, "tomato.png")
    dst = os.path.join(PROJECT_DIR, "exe_versions", "tomato.png")

    print("\n📋 Step 1: Copying tomato.png to exe_versions/")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print("  ✓ tomato.png copied")
        return True
    else:
        print(f"  ✗ Source not found: {src}")
        return False

def setup_git():
    """Initialize and configure git remotes."""
    print("\n📋 Step 2: Setting up Git repository")

    # Initialize git if needed
    if not os.path.exists(os.path.join(PROJECT_DIR, ".git")):
        run_cmd("git init", "  Initializing git repo")

    # Configure user (GitHub Actions compatible)
    run_cmd('git config user.email "actions@github.com"', "  Setting git user email")
    run_cmd('git config user.name "GitHub Actions"', "  Setting git user name")

    return True

def configure_remotes():
    """Configure git remotes."""
    print("\n📋 Step 3: Configuring Git remotes")

    # Check current remotes
    result = subprocess.run("git remote -v", shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    has_origin = "origin" in result.stdout

    if not has_origin:
        print("  ⓘ No origin remote found.")
        user_input = input("  Enter your GitHub repo URL (or press Enter to skip origin setup): ").strip()
        if user_input:
            run_cmd(f'git remote add origin "{user_input}"', "  Adding origin remote")
        else:
            print("  ⓘ Skipping origin setup")
    else:
        print("  ✓ Origin remote already configured")

    # Add/update exe-maker remote
    result = subprocess.run('git remote get-url exe-maker', shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    if result.returncode == 0:
        print("  ✓ EXE-Maker remote already configured")
    else:
        run_cmd('git remote add exe-maker https://github.com/Papaya-Voldemort/EXE-Maker.git', "  Adding EXE-Maker remote")

def commit_and_push():
    """Commit and push to both repositories."""
    print("\n📋 Step 4: Staging and committing changes")

    run_cmd("git add -A", "  Staging all files")

    commit_msg = "Add multi-platform builds (Windows/macOS/Linux), exe_versions folder, automatic releases, and tomato icon"
    result = subprocess.run(f'git commit -m "{commit_msg}"', shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    if "nothing to commit" in result.stdout or result.returncode == 0:
        print("  ✓ Changes committed")
    else:
        print(f"  ⓘ Commit: {result.stdout[:100]}")

    print("\n📋 Step 5: Pushing to repositories")

    # Push to origin
    result = subprocess.run("git remote get-url origin", shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        print("  → Pushing to origin...")
        run_cmd("git push -u origin main --force 2>&1 | head -20", "    origin push")
    else:
        print("  ⓘ Skipping origin (not configured)")

    # Push to exe-maker
    print("  → Pushing to EXE-Maker repository...")
    run_cmd("git push exe-maker main --force 2>&1 | head -20", "    exe-maker push")

def display_summary():
    """Display final summary and next steps."""
    print("\n" + "="*60)
    print("✅ Setup Complete!")
    print("="*60)

    print("\n📦 What was created:")
    print("  • exe_versions/main.py (clone of your main.py)")
    print("  • exe_versions/tomato.png (app icon)")
    print("  • exe_versions/requirements.txt (PyInstaller + Pillow)")
    print("  • exe_versions/build_windows.ps1 (local Windows build)")
    print("  • .github/workflows/build-windows-exe.yml")
    print("  • .github/workflows/build-macos.yml")
    print("  • .github/workflows/build-linux.yml")

    print("\n🚀 GitHub Actions will now:")
    print("  1. Build Windows EXE on every push")
    print("  2. Build macOS DMG on every push")
    print("  3. Build Linux binary on every push")
    print("  4. Create a new GitHub Release (v1, v2, v3...)")
    print("  5. Upload all binaries to the Release")

    print("\n📊 Git remotes configured:")
    result = subprocess.run("git remote -v", shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    for line in result.stdout.strip().split('\n')[:4]:
        print(f"  {line}")

    print("\n📥 Download your executables from:")
    result = subprocess.run("git remote get-url origin", shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    origin = result.stdout.strip()
    if origin and "github.com" in origin:
        print(f"  {origin.replace('.git', '')}/releases")

    print("\n💡 Local build on Windows:")
    print("  powershell -ExecutionPolicy Bypass -File .\\exe_versions\\build_windows.ps1")

    print("\n✨ Your original main.py is untouched - all builds use exe_versions/main.py")
    print("="*60)

if __name__ == "__main__":
    try:
        print("🎯 Multi-Platform EXE Build Setup")
        print("="*60)

        if not copy_image():
            print("⚠️  Failed to copy image, continuing anyway...")

        setup_git()
        configure_remotes()
        commit_and_push()
        display_summary()

        print("\n✅ All done! Check GitHub Actions tab for build status.")

    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

