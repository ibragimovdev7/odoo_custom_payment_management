{
    'name': 'Custom Payment Module',
    'version': '1.0',
    'category': 'Education',
    'author': 'Abdugani Ibragimov',
    'summary': 'Payment management for educational centers',
    'description': """
        A module for automating payment management in educational centers.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/education_data.xml',
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/group_views.xml',
        'views/payment_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
