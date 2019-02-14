from odoo import models, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def unlink(self):
        affected_orderpoints = self.env['stock.warehouse.orderpoint'].search([('product_id', 'in', self.mapped('product_id').ids)])
        affected_orderpoints.write({'force_reprocess': True})
        return super(StockMove, self).unlink()
