Flywrench Randomizer
====================
[![forthebadge][python-shield]][python-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![GitHub Release][release-shield]][release-url]

## Table of Contents

* [What Is This?](#what-is-this)
    * [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
        * [Windows](#windows)
        * [Mac OS X](#mac-os)
        * [Linux](#linux)
    * [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)

## What Is This?
[![Level Editor SS][level-editor-ss]][flywrench-steam-url]  
This is a level randomizer for Flywrench. Any of the lines that appear inside each of the levels, including the walls?
Yep, those are all randomized. Depending on the type of line, it will randomize the color in a pool and assign it to the
line.

This application will provide a modular randomizer experience by allowing the user to choose what they would like
randomized. This also includes all of the level names.

### Features
The current list of features include:
* Randomizing Obstacles
    * Wall Colors
    * Pinwheel Colors
    * Moving Line Colors
    * Turret Colors
* Level Name Randomizing
* Backup/Restore Level Files
* Setting/Randomizing the Randomizer Seed

## Getting Started
*Currently only Windows support*  
Releases can be found in the releases section of this repository located
[here](https://github.com/SarthTheSnek/FlywrenchRandomizer/releases)  
Just download the .exe and run the program.

You are also able to run this program from source.

### Prerequisites
* python > 3.7
    * (If you are planning on building the exe, you *MUST* use Python 3.8)
* pip

#### Windows
Either download [python 3.8](https://www.python.org/downloads/) or use the Windows Store (Windows 10) to download
Python.

Download [pip](https://pip.pypa.io/en/stable/installing/) and follow the directions to get you started.

Verify both are running in a command line:
```
python3 -v
pip -v
```

#### Mac OS
Installing python & pip utilizes [Homebrew](https://brew.sh).

```bash
brew install python
python3 -v
pip3 -v
```

#### Linux
Install python & pip using your respective package manager.

```bash
# Debian-Based Distros
apt install python3

# CentOS-Based Distros
yum install python3

# Fedora-Based Distros
dnf install python3

# Arch-Based Distros
pacman -S python3
```

### Installation
1. Clone this repo
```bash
git clone https://github.com/SarthTheSnek/FlywrenchRandomizer
```

2. Install module prerequisites
```bash
pip3 install -r requirements.txt
```

3. Run the python app script
```bash
python3 src/app.py
```

## Contributing
Contributing to the project is always welcome and are **greatly appreciated**. This project is open source and will
continue to be that way.

1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/SuperSnakeyFeature`)
3. Commit your Changes (`git commit -m 'I added a cool new thing!'`)
4. Push to the Branch (`git push origin feature/SuperSnakeyFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information

<!-- MARKDOWN LINKS -->
[issues-shield]: https://img.shields.io/github/issues/sarththesnek/flywrenchrandomizer?style=for-the-badge
[issues-url]: https://github.com/sarththesnek/flywrenchrandomizer/issues
[license-shield]: https://img.shields.io/github/license/sarththesnek/flywrenchrandomizer?style=for-the-badge
[license-url]: https://github.com/SarthTheSnek/FlywrenchRandomizer/blob/master/LICENSE
[python-shield]: https://img.shields.io/badge/python-3.8-blue?style=for-the-badge
[python-url]: https://www.python.org/downloads/release/python-380
[release-shield]: https://img.shields.io/github/release/sarththesnek/flywrenchrandomizer?style=for-the-badge
[release-url]: https://github.com/sarththesnek/flywrenchrandomizer/releases
[level-editor-ss]: https://github.com/SarthTheSnek/FlywrenchRandomizer/blob/master/.github/IMAGES/window.png?raw=true
[flywrench-steam-url]: https://store.steampowered.com/app/337350/Flywrench/