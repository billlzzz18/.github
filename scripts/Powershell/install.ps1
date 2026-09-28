[CmdletBinding()]
param (
    [string]$Repo = $env:REPO,
    [string]$BinName = $env:BIN_NAME,
    [string]$InstallDir = "$env:LOCALAPPDATA\Programs\bin"
)

$ErrorActionPreference = 'Stop'

if (-not $Repo) { $Repo = "your-org/icon-engine" }
if (-not $BinName) { $BinName = "icon-cli" }

$Arch = if ([System.Environment]::Is64BitOperatingSystem) { "x86_64" } else { "i686" }
$Target = "$Arch-pc-windows-msvc"

Write-Host "🚀 Installing $BinName for $Target from $Repo..." -ForegroundColor Cyan

# ดึง Release ล่าสุดจาก GitHub
$ApiUrl = "https://api.github.com/repos/$Repo/releases/latest"
try {
    $Release = Invoke-RestMethod -Uri $ApiUrl -Headers @{ "User-Agent" = "PowerShell" }
    $LatestTag = $Release.tag_name
} catch {
    Write-Error "❌ Failed to fetch latest release from GitHub API: $_"
    exit 1
}

$DownloadUrl = "https://github.com/$Repo/releases/download/$LatestTag/$BinName-$Target.zip"
$TempZip = [System.IO.Path]::GetTempFileName() + ".zip"
$TempExtract = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), [System.IO.Path]::GetRandomFileName())

Write-Host "📦 Downloading $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $TempZip

Write-Host "📂 Extracting binary..." -ForegroundColor Yellow
Expand-Archive -Path $TempZip -DestinationPath $TempExtract -Force

if (-not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null
}

$SourceExe = Join-Path $TempExtract "$BinName.exe"
$DestExe = Join-Path $InstallDir "$BinName.exe"
Move-Item -Path $SourceExe -Destination $DestExe -Force

# ล้างไฟล์ชั่วคราว
Remove-Item $TempZip -Force
Remove-Item $TempExtract -Recurse -Force

# เพิ่มโฟลเดอร์เข้า User PATH หากยังไม่มี
$UserPath = [System.Environment]::GetEnvironmentVariable("Path", "User")
if ($UserPath -notlike "*$InstallDir*") {
    [System.Environment]::SetEnvironmentVariable("Path", "$UserPath;$InstallDir", "User")
    Write-Host "⚙️ Added $InstallDir to User PATH." -ForegroundColor Green
}

Write-Host "✅ Successfully installed $BinName ($LatestTag) to $DestExe" -ForegroundColor Green
