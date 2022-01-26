#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
        name='RLA',
        version=0.3,
        description=(
            'RL assistant'
        ),
        author='Xiong-Hui Chen',
        author_email='chenxh@lamda.nju.edu.cn',
        maintainer='Xiong-Hui Chen',
        packages=[package for package in find_packages()
                        if package.startswith("RLA")],
        platforms=["all"],
        install_requires=[
            "pyyaml<=5.3.1",
            # "argparse<=1.4.0",
            "dill<=0.3.4",
            "seaborn"
        ]
    )
