{
    'name': 'Taf Oil',
    'version': '1.0',
    'summary': 'Taf Oil summary',
    'sequence': 1,
    'description': """
        Taf Oil Description.
    """,
    'author': 'Ashewa',
    'depends': ['base','mail','hr'],
     'data': [
        'security/ir.model.access.csv',
         'views/rode_type_view.xml',
         'views/source_destination.xml',
         'views/transport_summery.xml',
         'views/menu.xml'
     ],
    'assets': {
        'web._assets_primary_variables': [
        ],
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'auto_install': False,

}
           

        
