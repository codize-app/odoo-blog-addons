# -*- coding: utf-8 -*-
{
    'name': "Website Blog TTS",

    'summary': """
        Website Blog TTS""",

    'description': """
        Website Blog TTS
    """,

    'author': "Codize",
    'website': "https://www.codize.ar",

    'category': 'Website',
    'version': '0.1',
    'license': 'AGPL-3',

    'depends': ['base', 'website', 'website_blog'],
    'external_dependencies': {
        'python': ['pyttsx3']
    },

    'data': [
        'views/views.xml',
    ],
    'demo': [
    ],
}
