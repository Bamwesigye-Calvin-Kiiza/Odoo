
{
    'name': 'Purchase Request',
    'version': '1.0.0',
    'category': 'Purchases',
    'summary': 'Module for employees to send purchase requests to the Procurement department.',
    'depends': ['base','purchase'],

    'data': [
        'security/ir.model.access.csv',
        'views/purchase_request_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': -100,
}
