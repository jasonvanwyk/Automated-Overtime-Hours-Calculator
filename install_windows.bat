@echo off
echo ===== Automated Overtime Hours Calculator - Windows Installer =====
echo.
echo This script will install the Automated Overtime Hours Calculator on your Windows system.
echo.
echo Developed by Precept Systems (Pty) Ltd
echo Contact: 083 288 9052 | info@precept.co.za | www.precept.co.za
echo.
echo Prerequisites:
echo  - Python 3.11 or higher must be installed
echo  - pip must be installed
echo.
echo Press any key to continue with installation or CTRL+C to cancel...
pause > nul

echo.
echo Step 1: Installing required packages...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error installing required packages. Please make sure Python and pip are installed correctly.
    pause
    exit /b 1
)

echo.
echo Step 2: Creating executable...
pip install pyinstaller
if %ERRORLEVEL% NEQ 0 (
    echo Error installing PyInstaller. Please check your internet connection.
    pause
    exit /b 1
)

pyinstaller automated_overtime_calculator.spec
if %ERRORLEVEL% NEQ 0 (
    echo Error creating executable. Please contact support.
    pause
    exit /b 1
)

echo.
echo Step 3: Creating desktop shortcut...
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\Automated Overtime Calculator.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%CD%\dist\Automated Overtime Calculator.exe" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%CD%\dist" >> CreateShortcut.vbs
echo oLink.Description = "Automated Overtime Hours Calculator" >> CreateShortcut.vbs
echo oLink.IconLocation = "%CD%\icon.ico" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript //nologo CreateShortcut.vbs
del CreateShortcut.vbs

echo.
echo Installation complete!
echo The Automated Overtime Calculator has been installed and a shortcut has been created on your desktop.
echo.
echo Press any key to exit...
pause > nul
