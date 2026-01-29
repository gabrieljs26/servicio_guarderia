# -*- coding: utf-8 -*-
{
    'name': "Servicio de Guardería",

    'summary': "Gestión de servicio de guardería para empleados",

    'description': """
        Módulo para gestionar el servicio de guardería.
        Hereda de Empleados (monitor) y Eventos (calendario).
    """,

    'author': "Gabriel",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

