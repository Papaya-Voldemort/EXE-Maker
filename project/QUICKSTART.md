# 🚀 Quick Start Guide - Multi-Platform EXE Build Setup

## What I've Set Up For You

✅ **exe_versions folder** - Isolated from your original project
  - `main.py` - Clone of your app (build uses this, not root main.py)
  - `tomato.png` - App icon for all platforms
  - `requirements.txt` - PyInstaller + Pillow
  - `build_windows.ps1` - Local Windows build script
  - `README.md` - Detailed build instructions

✅ **GitHub Actions Workflows** - Automatic builds on every push
  - `build-windows-exe.yml` → Creates Windows EXE + releases it
  - `build-macos.yml` → Creates macOS DMG + releases it
  - `build-linux.yml` → Creates Linux binary + releases it

✅ **Automatic Release Management**
  - Each successful build creates a new GitHub Release
  - Version auto-increments (v1, v2, v3...)
  - All binaries attached to release

✅ **Original Files Untouched**
  - Your root `main.py` stays as-is
  - Your root `tomato.png` stays as-is
  - All builds use isolated exe_versions folder

## One-Command Deployment

Run this to copy tomato.png, initialize git, configure remotes, and push to both repos:

```bash
python3 /Volumes/External\ Home/Kids\ Home/PycharmProjects/Tkinter/deploy.py
```

Or from your project directory:
```bash
cd /Volumes/External\ Home/Kids\ Home/PycharmProjects/Tkinter
python3 deploy.py
```

This will:
1. ✅ Copy tomato.png to exe_versions/
2. ✅ Initialize git (if needed)
3. ✅ Configure both GitHub remotes (your repo + EXE-Maker)
4. ✅ Stage and commit all changes
5. ✅ Push to both repositories
6. ✅ Display download links for your releases

## What Happens Next

Once pushed to GitHub:
- 🔨 Windows workflow builds → `Pomodoro-v1.exe`
- 🍎 macOS workflow builds → `Pomodoro-v1.dmg`
- 🐧 Linux workflow builds → `Pomodoro-v1-linux.tar.gz`
- 📦 All uploaded to GitHub Releases automatically

## Download Your Builds

After push, visit:
`https://github.com/YOUR_USERNAME/YOUR_REPO/releases`

Each release will have:
- ✅ Windows EXE
- ✅ macOS DMG
- ✅ Linux binary
- ✅ Release notes (auto-generated)

## Local Build on Windows

If you have a Windows machine:

```powershell
powershell -ExecutionPolicy Bypass -File .\exe_versions\build_windows.ps1
```

Output: `.\dist\main.exe`

## File Structure

```
YourProject/
├── main.py (UNTOUCHED - original)
├── tomato.png (UNTOUCHED - original)
├── exe_versions/
│   ├── main.py (USED FOR BUILDS - cloned)
│   ├── tomato.png (USED FOR BUILDS - copied)
│   ├── requirements.txt
│   ├── build_windows.ps1
│   └── README.md
├── .github/workflows/
│   ├── build-windows-exe.yml
│   ├── build-macos.yml
│   └── build-linux.yml
└── deploy.py (THIS SETUP SCRIPT)
```

## Troubleshooting

**deploy.py asks for GitHub URL?**
- Provide: `https://github.com/YOUR_USERNAME/YOUR_REPO.git`
- Or press Enter to skip (EXE-Maker will still get pushed)

**Build fails on GitHub Actions?**
- Check the Actions tab for detailed logs
- Most common: icon conversion or path issues (already fixed)

**macOS DMG won't open?**
- It's valid - just drag the app to Applications folder

**Linux binary won't run?**
- Extract: `tar -xzf Pomodoro-*.tar.gz`
- Make executable: `chmod +x main`
- Run: `./main`

## Summary

You now have:
- 📦 **3 platform builds** (Win/Mac/Linux)
- 🤖 **Fully automated** via GitHub Actions
- 🎯 **Isolated builds** (your originals stay clean)
- 🚀 **Auto-releasing** (versions increment automatically)
- 🎨 **Branded icon** (tomato.png on all platforms)

**Next step:** Run `python3 deploy.py` and you're done! 🎉

