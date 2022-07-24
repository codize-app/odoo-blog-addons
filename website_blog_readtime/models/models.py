# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
regex = re.compile(r'<[^>]+>')

class BlogPost(models.Model):
    _inherit = 'blog.post'

    def _compute_readtime(self):
        for post in self:
            content = regex.sub('', post.content)
            time = int(len(content.split()) / 200)
            if time == 0:
                time = 1
            post.readtime = time

    readtime = fields.Integer('Tiempo de Lectura', readonly=True, compute=_compute_readtime)
