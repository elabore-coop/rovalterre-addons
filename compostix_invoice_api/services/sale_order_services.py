import logging
from odoo.addons.base_rest import restapi
from odoo.addons.component.core import Component
from odoo.addons.base_rest_datamodel.restapi import Datamodel


_logger = logging.getLogger(__name__)

class SaleOrderService(Component):
    _inherit = "base.rest.service"
    _name = "sale.order.service"
    _usage = "so"
    _collection = "compostix.private.services"
    _description = """
        Sale Order Services
        Access to the sale order services is only allowed to authenticated users.
        If you are not authenticated go to <a href='/web/login'>Login</a>
    """
    @restapi.method(
        [(["/create"], "POST")],
        input_param=Datamodel("sale.order.param"),
    )
    def create(self, params):
        # Sale order creation
        values = {
            "partner_id": self.env["res.partner"].browse(params.partner_id).id,
        }
        values = self.env["sale.order"].play_onchanges(values, ["partner_id"])
        order = self.env["sale.order"].create(values)

        # Sale order lines creation
        so_line = self.env["sale.order.line"]
        for line in params.sale_order_lines:
            values = {
                "order_id": order.id,
                "product_id": self.env["product.product"].browse(line.product_id).id,
                "name": line.description,
                "price_unit": line.price_unit,
                "product_uom_qty": line.quantity,
                "discount": line.discount,
            }
            values = so_line.play_onchanges(values, ["product_id","quantity", "price_unit", "discount"])
            so_line.create(values)
        order.action_confirm()
        return {
            "response": "POST called with success, sale order %s created" % order.name,
            "order_name": order.name,
            "order_id": order.id
        }