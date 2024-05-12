from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class OdooPlayground(models.Model):
    _name = 'odoo.playground'
    _description = 'Odoo Playground'

    DEFAULT_ENV_VARIABLES = '''#Available Variables:
    #   -self: Current Object
    #   -self.env: Odoo environment on which the action has been triggered
    #   -self.env.user: Return to the current user (as an instance)
    #   -self.env.is_system: Return whether the current user has group "Settings", or is in SuperUser Mode
    #   -self.env.is_admin: Return whether the current user has group "Access Rights", or is in Superuser Mode
    #   -self.env.is_superuser: Return whether the environment is in superuser mode
    #   -self.env.company:  Return the current company (as an instance)
    #   -self.env.companies: Return a recordset of the enabled companies by the user
    #   -self.env.lang: Return the current language code \n\n\n\n'''
    
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