from odoo import models, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.multi
    def unlink(self):
        affected_orderpoints = self.env['stock.warehouse.orderpoint'].search([('product_id', 'in', self.mapped('product_id').ids)])
        affected_orderpoints.write({'force_reprocess': True})
        return super(StockQuant, self).unlink()
