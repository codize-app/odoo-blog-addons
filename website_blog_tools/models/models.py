# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class website_blog_tools(models.Model):
#     _name = 'website_blog_tools.website_blog_tools'
#     _description = 'website_blog_tools.website_blog_tools'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
