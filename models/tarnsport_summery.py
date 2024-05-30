from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class transportSummery(models.Model):
    _name = "transport.summery"
    _description = "Transport Summery"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'inv_no'
    inv_no = fields.Char(string="Invoice No", required=True)
    fdc_no = fields.Char(string="FDC#", required=True)
    loadin_date = fields.Datetime(string="Loading Date", required=True)
    src_dst = fields.Many2one('source.destination', string='Source - Destination', tracking=True)
    type_or_product = fields.Selection([
        ('ago', 'AGO'),
        ('mgr', 'MGR'),
    ], string='Product Type', default='ago', required=True, tracking=True)
    gravel_km = fields.Float(string="Paved Km", compute="_compute_rate")
    gravel_rate = fields.Float(string="Paved Rate", compute="_compute_rate")
    paved_km = fields.Float(string="Gravel Km", compute="_compute_rate")
    paved_rate = fields.Float(string="Gravel Rate", compute="_compute_rate")
    cost_ltr = fields.Float(string="Cost/ltr", compute='_compute_cost_ltr')
    qty_at_20 = fields.Float(string="QTY at 20")
    gross_amount = fields.Float(string="Gross Amount", compute='_compute_gross_amount')
    lebu_birr = fields.Float(string="Debit Note")
    loss = fields.Float(string="Loss(Birr)")
    nat_pay = fields.Float(string="Nat Pay", compute='_compute_net_pay')
    source = fields.Char(string="Source", compute='_compute_src_dest')
    destination = fields.Char(string="Destination", compute='_compute_src_dest')

    @api.depends('src_dst')
    def _compute_rate(self):
        for record in self:
            if record.src_dst:
                record.gravel_km = record.src_dst.gravel_km
                record.gravel_rate = record.src_dst.gravel.rate
                record.paved_km = record.src_dst.paved_km
                record.paved_rate = record.src_dst.paved.rate
            else:
                record.gravel_km = 0
                record.gravel_rate = 0
                record.paved_km = 0
                record.paved_rate = 0

    @api.depends('gravel_km', 'gravel_rate', 'paved_km', 'paved_rate')
    def _compute_cost_ltr(self):
        for record in self:
            if record.src_dst:
                record.cost_ltr = ((record.gravel_km * record.gravel_rate) + (
                            record.paved_km * record.paved_rate)) / 100
            else:
                record.cost_ltr = 0

    @api.depends('cost_ltr', 'qty_at_20')
    def _compute_gross_amount(self):
        for record in self:
            if record.cost_ltr and record.qty_at_20:
                record.gross_amount = record.cost_ltr * record.qty_at_20
            else:
                record.gross_amount = 0

    @api.depends('gross_amount', 'lebu_birr', 'loss')
    def _compute_net_pay(self):
        for record in self:
            if record.gross_amount:
                record.nat_pay = (record.gross_amount - (record.lebu_birr + record.loss))
            else:
                record.nat_pay = 0

    @api.depends('src_dst')
    def _compute_src_dest(self):
        for record in self:
            if record.src_dst:
                record.source = record.src_dst.source
                record.destination = record.src_dst.destination
            else:
                record.source = ""
                record.destination = ""


