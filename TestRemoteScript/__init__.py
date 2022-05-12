from __future__ import absolute_import, print_function, unicode_literals
import Live
from .Test import Test

def create_instance(c_instance):
    u""" Creates and returns the Test script """
    return Test(c_instance)

