# Steam Shared Library Unblocker

The purpose of this project is to allow players to continue playing their shared library games even when the friends they are sharing from are playing games from their library. It achieves this by blocking the network connections to Steam, causing it to operate in offline mode without needing to close off all internet connections.

⚠️ **NOTE:** This workaround will not allow the use of Steam services like multiplayer in most games that rely on Steam services for multiplayer.

## Directory Structure

The repository is organized as follows:

- `Windows`: This Folder contains scripts for Windows systems, using the `netsh` command to manipulate Windows Firewall rules.
- `Linux`: This Folder contains scripts for Linux systems, using the `iptables` command to manage network traffic.
- `Systray_Application`: This Folder contains a system tray application for controlling the blocking/unblocking scripts in a more user-friendly manner.

## Systray Application

The system tray application provides a graphical interface for users to block/unblock network connections to Steam. The application runs in the system tray and provides menu options to block/unblock connections or exit the application.

A ready-to-use executable of the systray application for Windows systems is available in the [Releases](https://github.com/2Shad/SteamLibraryUnblocker/releases) section of the project repository. Download the .exe file and run it on your machine.

### Usage

1. Run the Systray_Application.exe.
2. Right-click the system tray icon to open the menu.
3. Select 'Block' to block Steam network traffic.
4. Select 'Unblock' to unblock Steam network traffic.
5. To close the application, select 'Exit'.

## Windows Scripts

The Windows scripts are named `block_steam_traffic.bat` and `unblock_steam_traffic.bat`. They work with the Advanced Firewall feature built into modern versions of Windows. They add or remove firewall rules which block all incoming and outgoing traffic for the Steam program for all IP addresses except for a specified range.

### Usage

1. Run the script as an administrator.
2. To block Steam network traffic, run `block_steam_traffic.bat`.
3. To unblock Steam network traffic, run `unblock_steam_traffic.bat`.

## Linux Scripts

The Linux scripts are named `block_steam_traffic.sh` and `unblock_steam_traffic.sh`. They use `iptables` to add or remove rules that block all incoming and outgoing traffic for the Steam program for all IP addresses except for a specified range.

**NOTE:** The ports used in the scripts (27036:27037) are commonly used by the Steam client for In-Home Streaming, but you should replace them with the actual ports used by your Steam application.

### Usage

1. Run the script with root privileges.
2. To block Steam network traffic, run `block_steam_traffic.sh`.
3. To unblock Steam network traffic, run `unblock_steam_traffic.sh`.

**IMPORTANT:** These `iptables` commands apply only to the current session. If you reboot the system, these changes will be lost. To make them permanent, you may need to use a tool like `iptables-persistent` or manually save and restore the rules at startup.
