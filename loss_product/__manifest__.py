# -*- coding: utf-8 -*-
{
    'name': "loss_product",

    'summary': """
        1.Identify the loss products from list view by color
        2.Loss product detail message for the users in point of sale settings
        3.Identify loss product in pos cart""",

    'description': """
        1.identify the loss products from list view by color
        2.loss product detail message for the users in point of sale settings
        3. identify loss product in pos cart
    """,

    'author': "Loyal It Solutions PVT LTD",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_settings.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'qweb' : ['static/src/xml/pos.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
