"""
py2app build script for MacChecker.

Build the standalone macOS .app bundle (must be run on macOS):

    pip install -r requirements.txt
    pip install py2app
    python setup.py py2app

The finished app will be placed in the `dist/` folder.
"""
from setuptools import setup

APP = ['mac_checker.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'MyIcon.icns',
    'packages': ['PyQt5', 'psutil'],
    'plist': {
        'CFBundleName': 'MacChecker',
        'CFBundleDisplayName': 'MacChecker',
        'CFBundleIdentifier': 'org.pythonmac.unspecified.MacChecker',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
        'NSHumanReadableCopyright': 'Copyright not specified',
    },
}

setup(
    app=APP,
    name='MacChecker',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
