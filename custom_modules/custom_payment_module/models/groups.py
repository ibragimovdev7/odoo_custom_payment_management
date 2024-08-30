from odoo import models, fields

class Group(models.Model):
    _name = 'education.group'
    _description = 'Groups'

    name = fields.Char('Group Name', required=True)
    course_id = fields.Many2one('education.course', string='Course', required=True)
    teacher_id = fields.Many2one('education.teacher', string='Teacher', required=True)
    student_ids = fields.Many2many('education.student', string='Students')
    payment_ids = fields.One2many('education.payment', 'group_id', string='Payments')
 