# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteBlogTts(http.Controller):
#     @http.route('/website_blog_tts/website_blog_tts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_blog_tts/website_blog_tts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_blog_tts.listing', {
#             'root': '/website_blog_tts/website_blog_tts',
#             'objects': http.request.env['website_blog_tts.website_blog_tts'].search([]),
#         })

#     @http.route('/website_blog_tts/website_blog_tts/objects/<model("website_blog_tts.website_blog_tts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_blog_tts.object', {
#             'object': obj
#         })
