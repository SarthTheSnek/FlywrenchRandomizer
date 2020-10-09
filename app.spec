# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src\\app.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 ('src\\Icon.ico', '.'),
                 ('src\\logic\\', 'logic\\')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          onefile=True,
          onedir=True,
          name='Flywrench Randomizer',
          debug=all,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False, icon='src\\Icon.ico')