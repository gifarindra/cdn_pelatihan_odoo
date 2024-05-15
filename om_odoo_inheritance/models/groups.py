from odoo import models, fields, api, _



class ResGroups(models.Model):
    _inherit = 'res.groups'

    def get_application_groups(self, domain): #menginherit fungsi yang memunculkan user groups
        group_id = self.env.ref('project.group_project_task_dependencies').id #akses id dengan env.ref
        wave_picking_id = self.env.ref('stock.group_stock_picking_wave').id
        return super(ResGroups, self).get_application_groups(domain + [('id', 'not in', (group_id,wave_picking_id))]) #pemunculan user groups yang tidak dalam domain variabel tsb
        #nama id bisa dicari di metadata groups