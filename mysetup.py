#!/usr/bin/python
#coding=GBK
from distutils.core import setup
import py2exe
myjob='xj_test.py'
setup(windows=[{"script": myjob}])

#python mysetup.py py2exe --dist-dir "d:\xj_test"