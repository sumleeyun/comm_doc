from odoo import api, fields, models
from odoo.exceptions import Warning
from io import BytesIO
import base64


class procurement(models.Model):
    _name = 'comm.procurement'
    _description = 'procurement'

    name = fields.Char('ชื่อสัญญา', required=True)
    number_type = fields.Many2one('comm.doc_type',string="ประเภท")
    procu_number = fields.Char('เลขที่สัญญา')
    codetype = fields.Selection([('ซ', 'ซ'), ('จ', 'จ')],'ประเภทรหัส')
    procu_code = fields.Integer('รหัส')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date(string="ลงวันที่")
    #upload_file = fields.Binary(string='แนบไฟล์', attachment=True)
    #file_name = fields.Char(string="ชื่อไฟล์ ")
    upload_file = fields.Many2many(comodel_name="ir.attachment", relation="m2m_ir_attachment_relation",
                                  column1="m2m_id", column2="attachment_id", string="แนบไฟล์",)

    chairman_id = fields.Many2many('res.partner',
                                   'chairman_partner',
                                   'procurement_id',
                                   'part_chairman_id',
                                   string="คณะกรรมการจัดซื้อ-จัดจ้าง")
    secretary_id = fields.Many2many('res.partner',
                                    'secretary_partner',
                                    'procurement_id',
                                    'part_secret_id',
                                    string="คณะกรรมการตรวจรับ-พัสดุ")
    description = fields.Html('Description')
