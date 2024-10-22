{
    'name': "Real Estate Advertisement",
    'version': '1.0',
    'category': 'Housing',
    'author': "Bamwesigye Calvin",
    'sequence': -100,
    'description': """
    Housing advertisements module
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate.xml',
        'views/sale.xml'
    ],
    'depends':['sale'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
