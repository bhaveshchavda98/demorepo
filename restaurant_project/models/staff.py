from odoo import api, fields, models

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = 'This model will store data of our staff'

    name = fields.Char(string="Name", size=50 )
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
