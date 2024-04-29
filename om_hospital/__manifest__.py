# -*- coding: utf-8 -*-
{
    'name': "(Training) Odoo Mates ERP Hospital",

    'summary': """
        Odoo Mates Odoo15 ERP Youtube Tutorial""",

    'description': """
        Presentasi ERP Hospital dengan Odoomates Youtube Tutorial
    """,

    'author': "Cendana2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_hospital.xml',
        'views/hospital_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
