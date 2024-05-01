# -*- coding: utf-8 -*-
{
    'name': "(Training) Odoo Mates ERP Hospital", #module name shown in the odoo 

    'summary': """
        Hospital Management System
        (Odoo Mates Odoo15 ERP Youtube Tutorial)""", #ringkasan module

    'description': """
        Hospital Management System
        (Presentasi ERP Hospital dengan Odoomates Youtube Tutorial) 
    """,#deskripsi umum

    'author': "Cendana2000", #developer info
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '16.0.1',

    # any module necessary for this one to work correctly (module(s) dependance of this current module)
    'depends': ['base','mail',],    

    # always loaded
    'data': [
        #'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_hospital.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ], #needed xmls
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True, #if the installable has false value, the module couldnt be installed
    'license': 'LGPL-3', #licensing rights
    'auto_install': False, #automatically install the module into the database
    #'sequence': -100, to make the module appear on the first sequence of the loaded modules, lower sequence number get appeared first
    #'application: True' to make the module main domain to be an application and can be searched with the apps filter
}

#module can be created manually by making a folder inside a folder that has been included within .conf file in the addons_path
#then one can make the __init__.py and __manifest__.py manually with a text editor and copy a manifest/init sample from other modules
#the other folders such as, models, views, can also be created manually

#another way to make module is with scaffold from the command line 
#C:\Odoo\Odoo16\server\pyodoo16 odoo-bin scaffold (module_name) (C:\Odoo\Odoo16\server\addons) <- module save location 