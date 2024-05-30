from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class sourceDestination(models.Model):
    _name = "source.destination"
    _description = "Source Destination"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    name = fields.Char(string="Name", compute='_compute_name')
    source = fields.Char(string="Source", required=True)
    destination = fields.Char(string="Destination", required=True)
    paved = fields.Many2one('rode.type', string='Paved', tracking=True)
    paved_km = fields.Float(string="Paved KM")
    gravel = fields.Many2one('rode.type', string='Gravel', tracking=True)
    gravel_km = fields.Float(string="Gravel KM")

    @api.depends('source', 'destination')
    def _compute_name(self):
        for record in self:
            if record.source and record.destination:
                record.name = record.source + " - " + record.destination
            else:
                record.name = ""
