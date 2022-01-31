# -*- coding: utf-8 -*-
{
    'name': "Mi Libro",

    'summary': """
        Descripción corta de mi priner modlo enb Odoo""",

    'description': """
        
    """,

    'sequence': 0,
    'application': True,

    'author': "David Herrera Costa",
    'website': "http://www.ieschirinos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sin categoria',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/libro.xml',
        'views/autor.xml',
        'views/editorial.xml',
        'views/categoria.xml',
        'views/cdu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
