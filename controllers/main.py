from odoo import http


class docs(http.Controller):
    @http.route('/comm/doc', auth='user',website=True)
    def list(self, **kwargs):
        doc = http.request.env['comm.doc']
        docs = doc.search([])
        return http.request.render('comm_doc.doc_list_template',
                                   {'docs': docs})
