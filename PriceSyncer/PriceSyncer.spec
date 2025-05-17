# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['PriceSyncer.py'],
    pathex=[],
    binaries=[],
    datas=[('price.ico', '.')],
    hiddenimports=['mysql.connector.plugins.mysql_native_password'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PriceSyncer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['price.ico'],
    version='PriceSyncer.version'
)
