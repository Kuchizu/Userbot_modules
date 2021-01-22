from .. import loader
import asyncio
from collections import deque


def register(cb):
    cb(ProjectsMod())

class ProjectsMod(loader.Module):
    strings = {'name': 'Nudes'}

    async def nudescmd(self, message):
        s = """\u2060⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠    ♥️♥️♥️♥️♥️                     \n ♥️♥️♥️♥️♥️♥️                   \n♥️♥️            ♥️♥️                   \n  ♥️♥️                                      \n       ♥️♥️                                 \n           ♥️♥️                             \n               ♥️♥️                         \n                   ♥️♥️                     \n                      ♥️♥️                  \n ♥️♥️             ♥️♥️                \n  ♥️♥️♥️♥️♥️♥️                  \n     ♥️♥️♥️♥️♥️end nudes!"""
        u = "♥"
        for i in ["❤️","🧡","💛","💚","💜","💙","❤️"]:
            s = s.replace(u, i)
            await message.edit(s)
            u = i
            await asyncio.sleep(1)
