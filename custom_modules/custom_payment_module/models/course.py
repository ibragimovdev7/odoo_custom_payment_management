from odoo import models, fields

class Course(models.Model):
    _name = 'custom.course'
    _description = 'Course Information'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")
    teacher_ids = fields.Many2many('custom.teacher', string="Teachers")
