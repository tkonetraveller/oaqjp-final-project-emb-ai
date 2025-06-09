from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'emotion_detector=emotion_detector:main',
        ],
    },
)