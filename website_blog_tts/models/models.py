# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import pyttsx3
import base64
import re
import os

engine = pyttsx3.init();
engine.setProperty('voice', 'spanish')
engine.setProperty("rate", 220)

regex = re.compile(r'<[^>]+>')

class BlogPost(models.Model):
    _inherit = 'blog.post'

    def remove_tts(self):
        self.content_tts = False

    def generate_tts(self):
        self.remove_tts()
        content = regex.sub('', self.content)
        engine.save_to_file(content[:6500], '/tmp/speech.mp3')
        engine.runAndWait()
        file = open('/tmp/speech.mp3', 'rb')
        data = file.read()
        os.unlink('/tmp/speech.mp3')
        encoded = base64.b64encode(data)
        self.content_tts = encoded

    content_tts = fields.Binary('TTS')
