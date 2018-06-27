"""
ASGI config for bot project.

Used for WebSockets
"""

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot.settings")
channel_layer = channels.asgi.get_channel_layer()
