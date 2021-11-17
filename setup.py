import setuptools
import shutil
import os


# path = os.path.dirname(os.path.abspath(__file__))
# shutil.copyfile(f"{path}/dmm.py", f"{path}/dmm/dmm.py")

setuptools.setup(
    name="ParallelScriptingTools",
    version="0.1",
    author="Ryosuke Kojima",
    author_email="kojima.ryosuke.8e@kyoto-u.ac.jp",
    description="ParallelScriptingTools",
    long_description="ParallelScriptingTools",
    long_description_content_type="text/markdown",
    url="https://github.com/kojima-r/ParallelScriptingTools",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "parallel-gpu= src.parallel_gpu:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
