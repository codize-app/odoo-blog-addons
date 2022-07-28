# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import re
regex = re.compile(r'<[^>]+>')

class WebsiteBlog(http.Controller):

    #@http.route(['/blog/render_pop_posts'], type='json', auth='public', website=True)
    #def render_latest_posts(self, template, domain, limit=None, order='visits desc'):
    #    posts = request.env['blog.post'].search(domain, limit=limit, order=order)
    #    return request.env.ref(template).render({'posts': posts})

    @http.route(['/blog/render_related_posts'], type='json', auth='public', website=True)
    def render_related_posts(self, id, limit=None):
        post = request.env['blog.post'].search([('id', '=', id)])
        posts = []
        if post.tag_ids:
            posts_odoo = request.env['blog.post'].search([('website_published', '=', True),('id', '!=', id),('tag_ids', 'in', post.tag_ids[0].id)], limit=limit)
        else:
            posts_odoo = request.env['blog.post'].search([('website_published', '=', True),('id', '!=', id)], limit=limit)
        for p in posts_odoo:
            content = regex.sub('', p.content)
            posts.append({'name': p.name, 'id': p.id, 'blog_id': p.blog_id.id, 'teaser': content[:80]+'...'})
        return {'posts': posts}
