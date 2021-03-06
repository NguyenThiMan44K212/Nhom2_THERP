# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School',
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
        'data/data.xml',
        'views/department.xml',
        'views/ology.xml',
        'views/classroom.xml',
        'views/major.xml',
        'views/student.xml',
        'views/lecturer.xml',
        'views/school.xml',
        'reports/report_student.xml',
        'reports/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}