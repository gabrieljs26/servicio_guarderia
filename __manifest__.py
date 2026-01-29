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


    'category': 'Human Resources',
    'version': '0.1',

  
    'depends': ['base', 'hr', 'calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
  
}

