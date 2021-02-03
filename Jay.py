from .. import loader
import asyncio
import random
from collections import deque


def register(cb):
    cb(ProjectsMod())

class ProjectsMod(loader.Module):
    strings = {'name': 'GAI'}

    async def gaicmd(self, message):
        await message.edit('🏳️‍🌈 Я гей на: ' + str(random.randint(-1,111)) + '% 🏳️‍🌈')
