# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'version': '1.0',
    'author': '',
    'maintainer': '',
    'website': '',
    'sequence': -100,

    'description': """ School Management Softwar""",

    'depends': ['base',"mail" ,"portal"],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/datastudent.xml',
        "views/student_view.xml"
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
