from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class OdooPlayground(models.Model):
    _name = 'odoo.playground'
    _description = 'Odoo Playground'

    DEFAULT_ENV_VARIABLES = ''''''
    
    #self merupakan sebuah objek recordset yang mana kita bisa akses field2 hingga value dari field2 tsb dengan pernyataan self.
    
    
    model_id = fields.Many2one(comodel_name='ir.model', string='Model')
    code = fields.Text(string='Code', default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string='Result')
    
    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code.strip(), {'self':model})
        except Exception as e:
            self.result = str(e)