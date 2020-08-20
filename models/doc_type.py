from odoo import api, fields, models
from odoo.exceptions import Warning
from io import BytesIO
import base64


class doc_type(models.Model):
    _name = 'comm.doc_type'
    _description = 'doc type'
    doc_type_id = fields.Integer("ID")
    name = fields.Char('ประเภทของเอกสาร', required=True)
    active = fields.Boolean('Active?', default=True)
