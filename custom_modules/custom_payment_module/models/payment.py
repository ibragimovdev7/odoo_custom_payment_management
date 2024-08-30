from odoo import models, fields

class Payment(models.Model):
    _name = 'education.payment'
    _description = 'Payments'

    student_id = fields.Many2one('education.student', string='Student', required=True)
    group_id = fields.Many2one('education.group', string='Group', required=True)
    amount = fields.Float('Amount', required=True)
    date = fields.Date('Payment Date', default=fields.Date.today)
    description = fields.Text('Description')
    receipt = fields.Binary('Payment Receipt')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid')
    ], string='Status', default='pending')
