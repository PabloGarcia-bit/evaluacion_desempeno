{
    'name': 'Evaluación de Desempeño ElectroWord',
    'version': '1.0',
    'summary': 'Módulo personalizado para gestionar evaluaciones de empleados',
    'category': 'Human Resources',
    'author': 'Tu Nombre',
    'depends': ['base', 'hr'],  # Es vital que esté 'hr' para usar los empleados
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/evaluacion_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}