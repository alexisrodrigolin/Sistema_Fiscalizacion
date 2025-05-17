# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['PayPoint.py'],
    pathex=[],
    binaries=[],
    datas=[('pay.ico', '.')],
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
    name='front',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['pay.ico'],
    version='paypoint.version',
)
