# exe_versions

This folder holds everything needed to build native executables for Windows, macOS, and Linux without modifying your original project.

## Folder Structure

- `main.py` – Clone of the main Pomodoro app (local changes here, not in root)
- `tomato.png` – App icon (used for all platforms and as Windows icon)
- `icon.ico` – Generated Windows icon (auto-created during build)
- `requirements.txt` – Python dependencies (PyInstaller, Pillow)
- `build_windows.ps1` – PowerShell build script for local Windows builds

## What's New

✨ **Multi-Platform Builds**: Windows EXE, macOS DMG, and Linux binary
🎯 **Tomato Icon**: Used as the app icon across all platforms
🚀 **Automatic Releases**: GitHub Actions creates versioned releases automatically
📦 **Isolated Builds**: All builds use `exe_versions/main.py` and `exe_versions/tomato.png`

## GitHub Actions Workflows

Three workflows automatically build on every push to `main`:

1. **build-windows-exe.yml** → Produces `Pomodoro-vX.exe` + uploads to release
2. **build-macos.yml** → Produces `Pomodoro-vX.dmg` + uploads to release
3. **build-linux.yml** → Produces `Pomodoro-vX-linux.tar.gz` + uploads to release

Each workflow uses `github.run_number` as the version, so releases auto-increment.

## How to Build Locally on Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\exe_versions\build_windows.ps1
```

Output: `.\dist\main.exe`

The script will:
- Create a `.venv`
- Install PyInstaller and Pillow
- Convert `tomato.png` → `icon.ico`
- Build with PyInstaller (includes PNG + icon)

## How to Build on GitHub (Recommended)

1. **Ensure your repo is initialized:**
   ```bash
   cd /path/to/your/repo
   git init
   git add .
   git commit -m "Initial commit with multi-platform builds"
   ```

2. **Add your GitHub repo as origin:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   ```

3. **Push to GitHub:**
   ```bash
   git push -u origin main
   ```

4. **GitHub Actions will automatically:**
   - Build Windows, macOS, and Linux versions
   - Create a new release (v1, v2, v3, etc.)
   - Attach the binaries to the release

5. **Download from:** https://github.com/YOUR_USERNAME/YOUR_REPO/releases

## How to Push to Multiple Repos

If you want to push to both your main repo and `EXE-Maker`:

```bash
# Add EXE-Maker as a second remote
git remote add exe-maker https://github.com/Papaya-Voldemort/EXE-Maker.git

# Push to both
git push origin main
git push exe-maker main
```

Or use the included setup script:
```bash
chmod +x setup_remotes.sh
./setup_remotes.sh
```

## Notes

- **Original `main.py` untouched:** Your root `main.py` stays unchanged. All exe builds use `exe_versions/main.py`.
- **Icon on all platforms:** The `tomato.png` is used as the app icon for Windows (.ico), macOS, and Linux.
- **Automatic versioning:** Each successful build increments the version (v1, v2, v3...) automatically.
- **No manual version updates needed:** GitHub Actions handles versioning via `github.run_number`.

## Troubleshooting

**Windows build fails locally?**
- Ensure Python 3.8+ is installed and in PATH
- Run PowerShell as Administrator
- Delete `.venv` and try again

**macOS build creates DMG but I can't open it?**
- The DMG is valid; try double-clicking and dragging the app to Applications

**Linux binary won't run?**
- Extract the tar.gz: `tar -xzf Pomodoro-*.tar.gz`
- Make it executable: `chmod +x main`
- Run: `./main`


