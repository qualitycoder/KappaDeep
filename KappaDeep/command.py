#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Command():
    def __init__(self, name, **kwargs):
        self.name = name
        self.response = kwargs.get('response')

# r00
