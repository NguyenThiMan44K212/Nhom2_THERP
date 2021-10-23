# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'School Management Software',
    'sequence': -100,
    'description': """School Management Software""",
    'category': 'Services',
    'website': 'https://www.odoo.school',
    'license': 'LGPL-3',
    'depends': [
        'hr'
    ],
    'data': [
        'views/department.xml',
        'views/lecturer.xml',
        'views/student.xml',
        'views/course.xml',
        'views/school.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}