#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/22 1:31

def chapter(name, chapter=-1):
    print("\n\n")
    if chapter == -1:
        print("===== <Chapter: %s> =====" % name)
    else:
        print("===== <Chapter %d: %s> =====" % (chapter, name))
