from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
from odoo.addons.datamodel.fields import NestedModel


class SaleOrderLineParam(Datamodel):
    _name = "sale.order.line.param"

    product_id = fields.Integer(required=True, allow_none=True)
    description = fields.String(required=False)
    price_unit = fields.Float(required=True)
    quantity = fields.Float(required=True)
    discount = fields.Float(required=False)

class SaleOrderParam(Datamodel):
    _name = "sale.order.param"

    partner_id = fields.Integer(required=True, allow_none=True)
    sale_order_lines = fields.List(NestedModel("sale.order.line.param"))
    