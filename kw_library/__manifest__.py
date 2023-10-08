{
    'name': 'Library',
    'summary': '',
    'license': 'LGPL-3',
    'author': 'My Company',
    'website': 'https://www.yourcompany.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'external_dependencies': {'python': [], },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/book.xml',
        'views/author.xml',
        'views/category/xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ]
}
