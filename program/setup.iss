[Setup]
AppName=My Python Application
AppVersion=1.0.0
DefaultDirName={autopf}\MyPythonApp
DefaultGroupName=My Python Application
UninstallDisplayIcon={app}\main.exe
Compression=lzma2
SolidCompression=yes
OutputDir=.\Outputs
OutputBaseFilename=MyPythonApp_Setup

[Files]
Source: "..\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\src\*"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\My Python Application"; Filename: "{app}\main.exe"
Name: "{autodesktop}\My Python Application"; Filename: "{app}\My Python Application"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,My Python Application}"; Flags: nowait postinstall skipifsilent