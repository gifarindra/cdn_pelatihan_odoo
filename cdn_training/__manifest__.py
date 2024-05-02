# -*- coding: utf-8 -*-
{
    'name': "Training Odoo16",

    'summary': """
        Membuat modul training Odoo16""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cendana2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail',],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/sequence_data.xml',
        'wizards/training_wizard.xml',
        'views/templates.xml',
        'views/menu_training.xml',
        'views/training_session.xml',
        'views/training_course.xml',
        'views/instruktur.xml',
        'views/provinsi.xml',
        'views/kota.xml',
        'views/kecamatan.xml',
        'views/desa.xml',
        'views/peserta.xml',
        'views/jabatan.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
