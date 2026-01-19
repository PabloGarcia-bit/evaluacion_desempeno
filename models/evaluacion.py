from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación de Desempeño de Empleados'

    name = fields.Char(string='Título de Evaluación', required=True)
    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True, default=lambda self: self.env.user.employee_id)
    fecha_evaluacion = fields.Date(string='Fecha de Evaluación', default=fields.Date.context_today)
    puntuacion = fields.Integer(string='Puntuación (1-10)', help="Puntuación del 1 al 10")
    comentarios = fields.Text(string='Comentarios del Evaluador')
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string='Estado', default='pendiente', group_expand='_read_group_stage_ids')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return ['pendiente', 'proceso', 'finalizado']