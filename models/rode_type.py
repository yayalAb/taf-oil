from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class rode_Type(models.Model):
    _name = "rode.type"
    _description = "rode Type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    name = fields.Char(string="Name", required=True)
    rate = fields.Float(string="Rate", required=True)



