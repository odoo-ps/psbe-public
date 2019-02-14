from odoo import models, fields


class Orderpoint(models.Model):
    """ Defines Minimum stock rules. """
    _inherit = "stock.warehouse.orderpoint"

    process_date = fields.Datetime()
    force_reprocess = fields.Boolean(default=False)
