# -*- mode: python ; coding: utf-8 -*-
import sys
import site
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

block_cipher = None
ROOT = Path(SPECPATH)

# Collect all PyQt6 and Qt6 data
from PyInstaller.utils.hooks import collect_data_files, collect_submodules
hiddenimports = [
    'PyQt6', 'PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets', 'PyQt6.QtSvg',
    'src', 'src.paraphraser', 'src.humanizer', 'src.humanizer_v2',
    'src.text_analyzer', 'src.settings_manager', 'src.model_registry',
    'src.model_downloader', 'src.export_manager', 'src.history_manager',
    'src.diff_viewer', 'src.rag_engine',
    'ui', 'ui.main_window', 'ui.model_selector', 'ui.onboarding_dialog', 'ui.history_dialog',
    'llama_cpp', 'docx', 'fitz', 'pymupdf', 'rank_bm25', 'sqlite3', 'tqdm', 'requests',
    'PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets',
]
datas = [
    (str(ROOT / 'resources'), 'resources'),
    (str(ROOT / 'src'), 'src'),
    (str(ROOT / 'ui'), 'ui'),
]
binaries = []

a = Analysis(
    [str(ROOT / 'main.py')],
    pathex=[str(ROOT)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[str(ROOT / 'pyi_rth_qt_plugins.py')],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LocalWrite',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='LocalWrite',
)

app = BUNDLE(
    coll,
    name='LocalWrite.app',
    icon='resources/icon.icns',
    bundle_identifier='ai.localwrite.desktop',
    info_plist={
        'CFBundleName': 'LocalWrite',
        'CFBundleDisplayName': 'LocalWrite',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleExecutable': 'LocalWrite',
        'CFBundleIdentifier': 'ai.localwrite.desktop',
        'NSHighResolutionCapable': True,
        'NSRequiresAquaSystemAppearance': False,
        'LSMinimumSystemVersion': '11.0',
        'LSApplicationCategoryType': 'public.app-category.productivity',
        'NSPrincipalClass': 'NSApplication',
        'NSHumanReadableCopyright': 'Copyright 2025. MIT License.',
    },
)
