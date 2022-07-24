# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlogPost(models.Model):
    _inherit = 'blog.post'

    def _compute_readtime(self):
        for post in self:
            time = int(len(post.content.split()) / 200)
            if time == 0:
                time = 1
            post.readtime = time

    readtime = fields.Integer('Tiempo de Lectura', readonly=True, compute=_compute_readtime)
