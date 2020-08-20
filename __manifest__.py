{
    'name':
    'comm Management Application',
    'description':
    'เก็บเอกสาร ของ กรมสือสารทหารอากาศ',
    'author':
    'sumlee-y',
    'depends': ['base', 'website'],
    'data': [
        'security/comm_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/doc_view.xml',
        'views/doc_list_template.xml',
        'views/doc_type.xml',
        'views/doc_procurement.xml',
    ],
    'application':
    True,
    'installable':
    True,
}
