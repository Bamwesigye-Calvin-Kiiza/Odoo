from odoo import api, fields, models

class RealEstateModel(models.Model):
    _name = 'estate.model'
    _description = 'RealEstateModel'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price',required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms =fields.Integer(string='Rooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garages = fields.Boolean(string='Garages')
    garden = fields.Boolean(string='Garden')
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')],string='Garden Orientation')
    owner_id = fields.Many2one('res.partner', string='Owner')
