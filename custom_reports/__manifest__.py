from odoo import models

class SalesReport(models.AbstractModel):
    _name = 'report.custom_reports.sales_report_template'

    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }
