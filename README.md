# MacChecker

MacChecker, is a free open-source Mac Info checker! 
You can use it, to test out used MacBooks before buying!
Built on Python. Here, you can check system detailed information, 
using only one app! CPU, GPU, Battery Cycles! And also export data!

![2024-06-09 19 29 35](https://github.com/AelasarHD/MacChecker/assets/84845779/2c742d47-84da-44c4-ba9c-b2b1091fba74)





## Installation

### Option 1 — Download the prebuilt app

1. Download the latest `MacChecker.app` archive from [Releases](https://github.com/AelasarHD/MacChecker/releases).
2. Unzip it and open `MacChecker.app`.
3. macOS Gatekeeper will block it the first time (unsigned app). Open it once, click `Cancel` on the warning, then right-click (or `Ctrl`+click) the app, choose `Open`, and confirm `Open` again.
4. For a better experience, move `MacChecker.app` into `Applications`.

![2024-06-09 19 29 35](https://github.com/AelasarHD/MacChecker/assets/84845779/2c742d47-84da-44c4-ba9c-b2b1091fba74)

### Option 2 — Run from source

```bash
git clone https://github.com/AelasarHD/MacChecker.git
cd MacChecker
pip install -r requirements.txt
python mac_checker.py
```

### Option 3 — Build your own standalone .app

```bash
pip install -r requirements.txt
pip install py2app
python setup.py py2app
```

The built app will appear in the `dist/` folder.


## Supported

- Both: **Intel** and **Apple Silicon** CPUs
- All **MacBook Pro** (2006-2021)
- All **MacBook Air** (2009-2024)
- From macOS Sierra (10.12), up to macOS Sonoma (14+)

## IMPORTANT

- **More Macs will be added in the future.** Also, I'm planning to add iMac, Mac Mini support! 

