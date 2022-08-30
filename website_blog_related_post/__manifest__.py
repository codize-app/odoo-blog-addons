# -*- coding: utf-8 -*-
{
    'name': "Website Blog Related Post",

    'summary': """
        Website Blog Related Post""",

    'description': """
        Website Blog Related Post
    """,

    'author': "Codize",
    'website': "https://www.codize.ar",

    'category': 'Website',
    'version': '0.1',

    'depends': ['base', 'website_blog'],

    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/website_blog_related_post/static/src/js/related_post.js',
            '/website_blog_related_post/static/src/css/style.css'
        ],
    },
    'demo': [
    ],
}
