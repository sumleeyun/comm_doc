from odoo import api, fields, models
from odoo.exceptions import Warning
from io import BytesIO
import base64


class doc(models.Model):
    _name = 'comm.doc'
    _description = 'doc'

    name = fields.Char('เรื่อง', required=True)
    doc_number = fields.Char('คำสั่ง สอ.ทอ.(ฉ)/พ.ค.')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date(string='ลงวันที่')
    upload_file = fields.Binary(string='แนบไฟล์', attachment=True)
    file_name = fields.Char(string="ชื่อไฟล์ ")
    chairman_id = fields.Many2one('res.partner',
                                  string='ประธาน/ผู้ได้รับการแต่งตั้ง')
    secretary_id = fields.Many2one('res.partner',
                                   string='เลขานุการ/ผู้ได้รับแต่งตั้ง')
    description = fields.Html('Description')
    doc_type_id = fields.Many2one('comm.doc_type', string='ประเภทของเอกสาร')

    
    def open_comm_doc(self, val1, val2):

        form_id = self.env.ref('comm_doc.view_form_doc').id
        tree_id = self.env.ref('comm_doc.view_tree_doc').id

        return {
            'type': 'ir.actions.act_window',
            'name': val2,
            'view_type': 'form',
            'view_mode': 'tree,form',
            'views': [(tree_id, 'tree'), (form_id, 'form')],
            'domain': [('doc_type_id', '=', val1)],
            'context': {
                'doc_type_id': val1
            },
            'res_model': 'comm.doc',
        }
#test demod