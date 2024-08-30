from odoo import models, fields

class Teacher(models.Model):
    _name = 'education.teacher'
    _description = 'Teachers'

    name = fields.Char('Teacher Name', required=True)
    subject = fields.Char('Subject')
    course_ids = fields.Many2many('education.course', string='Courses')
    group_ids = fields.One2many('education.group', 'teacher_id', string='Groups')
