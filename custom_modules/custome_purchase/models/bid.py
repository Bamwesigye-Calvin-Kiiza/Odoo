from odoo import models, fields

class RFQBid(models.Model):
    _name = 'rfq.bid'
    _description = 'Bid for RFQ'

    bid_amount = fields.Float('Bid Amount')
    purchase_order_id = fields.Many2one('purchase.order', string='RFQ')
    vendor_id = fields.Many2one('res.partner', string='Vendor')
