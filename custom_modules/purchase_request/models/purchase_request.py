from odoo import models, fields


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    employee_id = fields.Many2one('res.users', string='Employee', default=lambda self: self.env.user)
    product_id = fields.Many2one('purchase.order.line', string='Product', required=True)
    product_description = fields.Text('Product Description', required=False)
    product_quantity = fields.Integer('Quantity', required=True)
    request_description = fields.Text('Request Description', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    def action_confirm(self):
        self.state = 'confirmed'
