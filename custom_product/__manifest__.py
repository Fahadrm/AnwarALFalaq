{
    'name' : 'Custom Product',
    'version' : '1.1',
    'summary': 'Customer Relationship',
    'sequence': 1,
    'description': "This Is A Customer Relationship Software",
    'category': 'crm',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['base', 'product', 'stock', 'purchase'],
    'data': [

        'security/ir.model.access.csv',
        # 'data/crm_sequence_data.xml',
        
        'views/product_view.xml',
        'views/sec_uom_view.xml',
        'views/uom_uom_view.xml',
        'views/stock_received_view.xml',
       


    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
