{
    'name': 'Custom Purchase Module',
    'version': '1.0.0',
    'depends': ['purchase'],  # Ensure you include the default Purchase app
    'summary': 'Extends Purchase App with custom RFQ to Vendor relation',
    'data': [
        'security/ir.model.access.csv',
        'views/rfq_views.xml',
        'views/bid_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': -100,
}
