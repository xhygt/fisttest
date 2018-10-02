#!/usr/bin/python
# -*- coding: utf-8 -*-
_global_dict={}
def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):

    _global_dict[name] = value

def get_value(name, defValue=None):
    # global _global_dict
    try:
        return _global_dict[name]
    except KeyError:
        return defValue