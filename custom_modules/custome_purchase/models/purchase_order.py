from odoo import models, fields, api

# models/purchase_order.py
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    selected_bid_id = fields.Many2one('rfq.bid', string='Winning Bid')
    vendor_id = fields.Many2one('res.partner', string='Assigned Vendor(s)', compute='_compute_vendor', store=True)

    @api.depends('selected_bid_id')
    def _compute_vendor(self):
        for order in self:
            order.vendor_id = order.selected_bid_id.vendor_id


