from odoo import api, models, fields

class HostpitalPatients(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patients'

    # create fields of the database table for the module
    name = fields.Char(string='Name')
    DOB = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    ref = fields.Char(string='Reference')
    image = fields.Image(string='Image')
    father_name = fields.Char(string='Father Name')
    mother_name = fields.Char(string='Mother Name')
    marital_status = fields.Selection([('single','Single'),('married','Married'), ('divorced','Divorced')], string='Marital Status')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
    active = fields.Boolean(string='Active',default=True)

