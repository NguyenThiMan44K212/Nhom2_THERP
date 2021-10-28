# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Ology_Class Management',
    'version': '1.0',
    'summary': 'Ology_Class Management Software',
    'sequence': -100,
    'description': """Ology_Class Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.school',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'view/views.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}