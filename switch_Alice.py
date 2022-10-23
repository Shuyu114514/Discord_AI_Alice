import numpy as np
import discord
import os

# temporary abandoned file

switch_Alice = True


async def Alice_is_working():
    global switch_Alice
    if switch_Alice:
        return True
    else:
        return False


async def Alice_turn_on():
    global switch_Alice
    switch_Alice = True


async def Alice_turn_off():
    global switch_Alice
    switch_Alice = False
