# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteBlogTools(http.Controller):
#     @http.route('/website_blog_tools/website_blog_tools/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_blog_tools/website_blog_tools/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_blog_tools.listing', {
#             'root': '/website_blog_tools/website_blog_tools',
#             'objects': http.request.env['website_blog_tools.website_blog_tools'].search([]),
#         })

#     @http.route('/website_blog_tools/website_blog_tools/objects/<model("website_blog_tools.website_blog_tools"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_blog_tools.object', {
#             'object': obj
#         })
