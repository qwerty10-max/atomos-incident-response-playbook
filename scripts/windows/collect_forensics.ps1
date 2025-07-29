# ===========================
# collect_forensics.ps1
# Windows Forensics + Extras
# ===========================

$OutputDir = "C:\IR_Collection_$((Get-Date).ToString('yyyyMMdd_HHmmss'))"
New-Item -Path $OutputDir -ItemType Directory -Force

# System Info
Write-Host "[*] Collecting system info..."
systeminfo > "$OutputDir\systeminfo.txt"
hostname > "$OutputDir\hostname.txt"
Get-WmiObject Win32_OperatingSystem | Select-Object * > "$OutputDir\os_details.txt"

# Running Processes
tasklist /v > "$OutputDir\processes.txt"
Get-Process | Sort-Object CPU -Descending | Select-Object -First 50 | Out-File "$OutputDir\top_processes.txt"

# Network Connections
netstat -ano > "$OutputDir\netstat.txt"

# Scheduled Tasks & Services
schtasks /query /fo LIST /v > "$OutputDir\scheduled_tasks.txt"
Get-Service | Where-Object {$_.Status -eq "Running"} | Out-File "$OutputDir\running_services.txt"

# Startup Programs
Get-CimInstance -ClassName Win32_StartupCommand | Select-Object Name, Command, Location | Out-File "$OutputDir\startup_items.txt"

# User Sessions & Groups
quser > "$OutputDir\user_sessions.txt"
query user > "$OutputDir\query_user.txt"
net user > "$OutputDir\local_users.txt"
net localgroup > "$OutputDir\local_groups.txt"

# USB History
Get-WinEvent -LogName Microsoft-Windows-DriverFrameworks-UserMode/Operational | 
    Where-Object {$_.Id -eq 2003} | 
    Select-Object -First 50 |
    Out-File "$OutputDir\usb_history.txt"

# Hash Critical Files
Get-FileHash C:\Windows\System32\* -Algorithm SHA256 | Out-File "$OutputDir\file_hashes.txt"

# ==========================
# BROWSER HISTORY COLLECTION
# ==========================

Write-Host "[*] Attempting to dump browser history..."
$UserProfile = [Environment]::GetFolderPath("UserProfile")

# Chrome
$ChromeHistory = "$UserProfile\AppData\Local\Google\Chrome\User Data\Default\History"
if (Test-Path $ChromeHistory) {
    Copy-Item $ChromeHistory "$OutputDir\chrome_history.db"
}

# Edge
$EdgeHistory = "$UserProfile\AppData\Local\Microsoft\Edge\User Data\Default\History"
if (Test-Path $EdgeHistory) {
    Copy-Item $EdgeHistory "$OutputDir\edge_history.db"
}

# Firefox
$FirefoxProfiles = Get-ChildItem "$UserProfile\AppData\Roaming\Mozilla\Firefox\Profiles" -Directory
foreach ($profile in $FirefoxProfiles) {
    $places = "$($profile.FullName)\places.sqlite"
    if (Test-Path $places) {
        Copy-Item $places "$OutputDir\firefox_history_$($profile.Name).sqlite"
    }
}

# ==========================
# EVENT LOG EXPORT
# ==========================

Write-Host "[*] Exporting Event Logs..."
wevtutil epl Security "$OutputDir\Security.evtx"
wevtutil epl System "$OutputDir\System.evtx"
wevtutil epl Application "$OutputDir\Application.evtx"

# ==========================
# REGISTRY KEY COLLECTION
# ==========================

Write-Host "[*] Dumping registry keys (AutoRuns, RunOnce)..."

reg export "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" "$OutputDir\HKLM_Run.reg" /y
reg export "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" "$OutputDir\HKCU_Run.reg" /y
reg export "HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce" "$OutputDir\HKLM_RunOnce.reg" /y
reg export "HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce" "$OutputDir\HKCU_RunOnce.reg" /y

# ==========================
# MEMORY DUMP (MANUAL STEP)
# ==========================

Write-Host "[*] Skipping memory dump (requires admin + external tools)."
Write-Host "[!] Please run DumpIt.exe or Magnet RAM Capture manually and save to: $OutputDir"

# ==========================
# ZIP RESULTS
# ==========================

$ZipFile = "$env:USERPROFILE\Desktop\IR_Collection.zip"
Compress-Archive -Path $OutputDir\* -DestinationPath $ZipFile
Write-Host "[✓] Collection complete. Zip saved at: $ZipFile"
