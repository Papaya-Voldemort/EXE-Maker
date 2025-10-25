<#
PowerShell helper to build a Windows .exe with PyInstaller.
Run this on a Windows machine with Python installed (3.8+).
Usage (from repo root):
  powershell -ExecutionPolicy Bypass -File .\exe_versions\build_windows.ps1
#>
param(
    [string]$MainScript = ".\exe_versions\main.py",
    [string]$Requirements = ".\exe_versions\requirements.txt",
    [string]$IconSource = ".\exe_versions\tomato.png"
)

Write-Host "Creating virtual environment .venv..."
python -m venv .venv
Write-Host "Activating virtual environment..."
. .venv\Scripts\Activate.ps1

Write-Host "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r $Requirements

Write-Host "Converting PNG to ICO for Windows icon..."
python -c @"
from PIL import Image
try:
    img = Image.open('$IconSource')
    img = img.convert('RGBA')
    img.save('exe_versions\icon.ico')
    print('Icon created: exe_versions\icon.ico')
except Exception as e:
    print(f'Warning: Could not create icon: {e}')
"@

Write-Host "Running PyInstaller..."
# Include the PNG and use icon for Windows. On Windows the separator is ';'
pyinstaller --onefile --windowed --add-data "exe_versions\tomato.png;." --icon=exe_versions\icon.ico $MainScript

if ($LASTEXITCODE -ne 0) {
    Write-Error "PyInstaller failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}

Write-Host "Build complete. The exe will be in the 'dist' folder."
Write-Host "Artifact path: .\dist\main.exe"

