# system-monitor
"A real-time system monitoring dashboard in PowerShell showing CPU, RAM, HDD, and SSD usage with charts."

# PowerShell System Monitor

A real-time system monitoring dashboard written in **PowerShell**.  
It shows CPU, RAM, HDD, and SSD usage in live updating charts.

## 🚀 Features
- Updates every 5 seconds
- Keeps last 5 minutes of data
- Windows Forms charts for visualization
- Monitors CPU, Memory, HDD, SSD

## 🛠 Requirements
- Windows 10/11
- PowerShell 5.1 or newer
- .NET Framework (already included in Windows)

## ▶️ Usage
```powershell
git clone https://github.com/Blurrycucumber/powershell-system-monitor.git
cd powershell-system-monitor
powershell -ExecutionPolicy Bypass -File .\system_monitor.ps1

