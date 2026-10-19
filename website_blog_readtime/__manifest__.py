# -*- coding: utf-8 -*-
{
    'name': "Website Blog ReadTime",

    'summary': """
        Readtime for Odoo Blog""",

    'description': """
        Add ReadTime in minutes to Odoo Blog
    """,

    'author': "Codize",
    'website': "https://www.codize.ar",

    'category': 'Website',
    'version': '19.0.1.0.0',
    'license': 'AGPL-3',

    'depends': ['base', 'website', 'website_blog'],

    'data': [
        'views/views.xml',
    ],

    'demo': [
    ],
}
