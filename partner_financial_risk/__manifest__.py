# -*- coding: utf-8 -*-
{
    'name': 'Partner financial risk',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'crm'],
    'data': [
        'data/ir_configparameter_data.xml',
        'views/crm_lead_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,    
}