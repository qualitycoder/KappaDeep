#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""Skyline - Philips Hue integration for KappaDeep."""

from integrations.color import Color
from integrations.group import Group
from extensions.hue import Hue
from config import config

from twitchio.ext import commands

@commands.cog()
class Skyline:
    """Skyline base class."""

    stream_room = Group('Bedroom',
                        lights=[
                            'Roo side table',
                            'Lunar side table',
                            'Desk Portrait Left',
                            'Desk Portrait Right'
                        ])

    def __init__(self, bot):
        """Init."""
        self.bot = bot
        self.skyline = Hue(config.BRIDGE_IP)
        self.skyline.start()

    @commands.command(name='lights')
    async def light_command(self, ctx):
        """Set lights to a given color."""
        color = Color()
        self.bot.loop.create_task(self.skyline.set_color(stream_room.lights,
                                                         skyline.colors['red']))
