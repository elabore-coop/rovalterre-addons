from odoo.addons.base_rest.controllers import main


class CompostixPrivateApiController(main.RestController):
    _root_path = "/compostix_api/private/"
    _collection_name = "compostix.private.services"
    _default_auth = "api_key"
