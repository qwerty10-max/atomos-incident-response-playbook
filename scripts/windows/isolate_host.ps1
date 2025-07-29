# ===============================
# isolate_host.ps1 (Enhanced)
# Host Isolation + Slack Alert + SIEM Upload + Auto-run snippet
# ===============================

# === CONFIG ===
$IRServer = "192.168.1.100"              # Your IR jump box IP
$AllowedPorts = @(22, 443)                # Allowed ports for IR access
$SlackWebhookUrl = "https://hooks.slack.com/services/XXX/YYY/ZZZ"  # Your Slack Incoming Webhook URL
$SIEMEndpoint = "https://siem.example.com/api/upload"              # Your SIEM HTTP endpoint
$SessionLog = "$env:SystemDrive\IR_Session_Info.txt"

Write-Host "[*] Running host isolation script..." -ForegroundColor Yellow

# === Step 1: Firewall block rules ===
New-NetFirewallRule -DisplayName "Block All Inbound" -Direction Inbound -Action Block -Enabled True -Profile Any -ErrorAction SilentlyContinue
New-NetFirewallRule -DisplayName "Block All Outbound" -Direction Outbound -Action Block -Enabled True -Profile Any -ErrorAction SilentlyContinue

foreach ($port in $AllowedPorts) {
    New-NetFirewallRule -DisplayName "Allow Outbound to IR Server Port $port" `
        -Direction Outbound `
        -Action Allow `
        -RemoteAddress $IRServer `
        -Protocol TCP `
        -LocalPort Any `
        -RemotePort $port `
        -Profile Any -ErrorAction SilentlyContinue

    New-NetFirewallRule -DisplayName "Allow Inbound from IR Server Port $port" `
        -Direction Inbound `
        -Action Allow `
        -RemoteAddress $IRServer `
        -Protocol TCP `
        -LocalPort $port `
        -RemotePort Any `
        -Profile Any -ErrorAction SilentlyContinue
}

# === Step 2: Log session info ===
Write-Host "[*] Logging session info..."
query user > $SessionLog
whoami /all >> $SessionLog
ipconfig /all >> $SessionLog

# === Step 3: Send Slack Alert ===
function Send-SlackAlert {
    param([string]$Message)

    $payload = @{
        text = $Message
    } | ConvertTo-Json

    try {
        Invoke-RestMethod -Uri $SlackWebhookUrl -Method Post -Body $payload -ContentType 'application/json'
        Write-Host "[✓] Slack alert sent."
    }
    catch {
        Write-Warning "Failed to send Slack alert: $_"
    }
}

# === Step 4: Upload log to SIEM ===
function Upload-LogToSIEM {
    param([string]$FilePath)

    if (Test-Path $FilePath) {
        try {
            $bytes = [System.IO.File]::ReadAllBytes($FilePath)
            $base64 = [System.Convert]::ToBase64String($bytes)

            $body = @{
                filename = [System.IO.Path]::GetFileName($FilePath)
                filedata = $base64
                hostname = $env:COMPUTERNAME
                timestamp = (Get-Date).ToString("o")
            } | ConvertTo-Json

            Invoke-RestMethod -Uri $SIEMEndpoint -Method Post -Body $body -ContentType "application/json"
            Write-Host "[✓] Log uploaded to SIEM."
        }
        catch {
            Write-Warning "Failed to upload log: $_"
        }
    }
    else {
        Write-Warning "Log file not found: $FilePath"
    }
}

# === Step 5: Auto-run setup snippet ===
function Setup-AutoRun {
    Write-Host "[*] Creating Scheduled Task to auto-run isolation script..."

    $Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File `"$PSCommandPath`" -WindowStyle Hidden"
    $Trigger = New-ScheduledTaskTrigger -AtStartup
    $Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

    try {
        Register-ScheduledTask -TaskName "IsolateHostOnBoot" -Action $Action -Trigger $Trigger -Principal $Principal -Force
        Write-Host "[✓] Scheduled Task created."
    }
    catch {
        Write-Warning "Failed to create scheduled task: $_"
    }
}

# === EXECUTION ===
Send-SlackAlert "Host isolation completed on $env:COMPUTERNAME at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss'). Allowed IR server: $IRServer"

Upload-LogToSIEM -FilePath $SessionLog

# Uncomment below to setup auto-run (only run once)
# Setup-AutoRun

Write-Host "[✓] Host isolation process finished."
