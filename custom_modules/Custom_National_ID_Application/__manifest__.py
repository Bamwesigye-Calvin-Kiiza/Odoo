{
    'name': 'National ID Application',
    'version': '1.0.0',
    'summary': 'Module for National ID Application and Approval Workflow',
    'sequence': -100,
    'author': 'Bamwesigye Calvin Kiiza',
    'category': 'Custom ID ',
    'description': """
        This module allows users to apply for national IDs online. 
        The application is processed in two stages of approval.
    """,
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/national_id_application_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}
