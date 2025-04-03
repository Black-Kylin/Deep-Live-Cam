from setuptools import setup

APP = ['run.py']
DATA_FILES = [
    ('models', ['models/GFPGANv1.4.pth', 'models/inswapper_128_fp16.onnx']),
    ('locales', ['locales/zh.json']),
    ('modules', ['modules/ui.json'])
]
OPTIONS = {
    'argv_emulation': True,
    'packages': [
        'numpy',
        'cv2',
        'onnx',
        'insightface',
        'psutil',
        'tkinter',
        'customtkinter',
        'PIL',
        'torch',
        'torchvision',
        'onnxruntime',
        'opennsfw2',
        'protobuf',
        'tqdm',
        'gfpgan',
        'tkinterdnd2'
    ],
    'iconfile': 'media/icon.icns',
    'plist': {
        'CFBundleName': 'Deep-Live-Cam',
        'CFBundleDisplayName': 'Deep-Live-Cam',
        'CFBundleVersion': '1.8',
        'CFBundleIdentifier': 'com.hacksider.deeplivecam',
        'NSHighResolutionCapable': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name='Deep-Live-Cam'
)