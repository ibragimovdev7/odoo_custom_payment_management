from odoo import models, fields

class Student(models.Model):
    _name = 'education.student'
    _description = 'Students'

    name = fields.Char('Student Name', required=True)
    age = fields.Integer('Age')
    email = fields.Char('Email')
    group_ids = fields.Many2many('education.group', string='Groups')
    payment_ids = fields.One2many('education.payment', 'student_id', string='Payments')
