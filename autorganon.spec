# -*- mode: python ; coding: utf-8 -*-

onefile = True
block_cipher = None

from PyInstaller.config import CONF
CONF['distpath'] = r"./dist"

a = Analysis(
    ['main.py'],
    pathex=[
      "./",
      ],
    binaries=[],

    datas=[
    ],

    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pyinstaller", ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    exclude_binaries=False,
    name='autorganon',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,

    runtime_tmpdir=None,
)
if not onefile:
	coll = COLLECT(
      exe,
      a.binaries,
      a.zipfiles,
      a.datas,
      strip=False,
      upx=True,
      upx_exclude=[],
	    name='autorganon',
	)
