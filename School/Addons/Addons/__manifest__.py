# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'version': '1.0',
    'author': '',
    'maintainer': '',
    'website': '',

    'description': """ School Management Softwar""",

    'depends': ['base',"mail" ,"portal"],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        "views/student_view.xml"
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
