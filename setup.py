from os.path import join, dirname, abspath
from setuptools import find_packages, setup, Extension


def read_file(file_name):
    here = abspath(dirname(__file__))
    with open(join(here, file_name), encoding='utf-8') as f:
        return f.read()


h_files = [
    "pyorient_native/orientc_reader.h",
    "pyorient_native/orientc_writer.h",
    "pyorient_native/orientc.h",
    "pyorient_native/helpers.h",
    "pyorient_native/parse_exception.h",
    "pyorient_native/listener.h",
    "pyorient_native/encoder.h",
    "pyorient_native/pendian.h"
]
pyorient_native = Extension(
    "pyorient_native",
    sources=[
        "pyorient_native/orientc_reader.cpp",
        "pyorient_native/orientc_writer.cpp",
        "pyorient_native/helpers.cpp",
        "pyorient_native/parse_exception.cpp",
        "pyorient_native/listener.cpp",
        "pyorient_native/encoder.cpp",
        "pyorient_native/pyorient_native.cpp"],
    depends=h_files,
    library_dirs=[],
    include_dirs=["./pyorient_native"],
    language="c++",
    libraries=["stdc++"]
)

setup(
    name="pyorient_native",
    version="1.2.4",
    description="OrientDB Binary Serialization package for python",
    long_description=read_file('README.md'),
    author="Nikul Ukani",
    author_email="nhu2001@columbia.edu",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: C++'
    ],
    ext_modules=[pyorient_native],
    packages=find_packages(
        exclude=[
            'build',
            'docs',
            'tests'
        ]
    ),
    extras_require={
        'test': [
            'pytest',
            'pytest-cython'
        ],
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    zip_safe=False,
    url="https://github.com/nikulukani/pyorient_native",
    download_url="https://github.com/nikulukani/pyorient_native/"
                 "archive/1.2.3.tar.gz"
)
