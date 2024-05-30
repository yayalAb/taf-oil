from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class product_Type(models.Model):
    _name = "product.type"
    _description = "product type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")



