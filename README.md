<table width="100%">
  <tr>
    <td align="center" min-width="150">
      <img src="docs/images/rice-shower.png" alt="Status" width="150" height="150" />
    </td>
    <td align="left">
      <pre>
 █████▄  ▄▄  ▄▄▄▄ ▄▄▄▄▄   ▄█████ ▄▄ ▄▄  ▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄ ▄▄▄▄    In early development!
 ██▄▄██▄ ██ ██▀▀▀ ██▄▄    ▀▀▀▄▄▄ ██▄██ ██▀██ ██ ▄ ██ ██▄▄  ██▄█▄   ---------------------
 ██   ██ ██ ▀████ ██▄▄▄   █████▀ ██ ██ ▀███▀  ▀█▀█▀  ██▄▄▄ ██ ██   version 0.0.18
<strong> DISCORD BOT made with Discord.py                                                     🥕</tr>
</table>

Rice Shower Bot is your all-in-one Discord companion, 
featuring Uma Musume-inspired mini-games where you can train and race your horses, 
along with tools to manage and moderate your server, and fun commands to keep everyone entertained. 
Fast, reliable, and ready to make your server lively!

![Discord.py](https://img.shields.io/badge/Discord.py-2.4-5865F2?style=flat-square&logo=discord&logoColor=white)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white)](#)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Early%20Development-yellow)

## Description
A modular and scalable Discord bot framework built with Python and discord.py.
Designed for easy extension with commands and events, centralized logging, and a clean project structure.
Currently in early development; some package structure and features may change as the project evolves.


![What's New Banner](docs/images/whats-new_banner.png)

## Discord Bot Features

| Category | Description |
|----------|-------------|
| **General Commands** | Provides simple utility commands for everyday server tasks, fun interactions, and informational queries. Designed to be easy-to-use for both developers and users. Includes UI/UX components for an interactive experience, like buttons, menus, and embedded responses. |
| **Moderation Commands** | Core moderation features that are actively being developed and improved, including member management, permission checks, and automated enforcement tools. Comes with UI/UX components to streamline interactions, confirmations, and status displays. |

## Source Code Features

| Feature | Description |
|---------|-------------|
| **Dynamic Autoloader** | Automatically discovers and loads commands, events, and modules from your project folders. Adding new features is as simple as creating a file—no need to touch core bot code. Ideal for modular development and fast iteration. |
| **Centralized Logging** | Important bot actions—like startup events, module loads, and command execution—appear in the console for immediate visibility. Full activity logs, including Discord internal logs, are saved to a file for detailed debugging, monitoring, and auditing. |
| **Configurable Settings** | Easily adjust command prefixes, intents, tokens, and logging behavior through the config folder. Supports multiple environments, so you can switch settings with minimal changes. |
| **Reusable Utilities** | Comes with helper modules for logging, autoloading, permissions tracking, message sending, and other common tasks. These utilities make building new features or integrating external APIs faster and cleaner. |
| **Persistent User Data** | Stores user-related information in **SQLite**, enabling commands and events to read/write persistent data efficiently, without requiring an external database server. |
