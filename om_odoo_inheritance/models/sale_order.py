from odoo import models, fields, api



class SaleOrder(models.Model): #omodi snippet untuk model inheritance
    _inherit = 'sale.order'    #tanpa _name hanya _inherit dengan nama model yang diinherit

    confirmed_user_id = fields.Many2one(comodel_name='res.users', string='Confirmed Users') #penambahan field baru pada model sale.order dari model res.users, perubahandpt dilihat di techn -> models -> fields -> misc
    
    def action_confirm(self):
        super(SaleOrder,self).action_confirm() #untuk mewariskan function, menggunakan super, super(ClassNamePewaris, self(tergantungargumen function)).nama_function()
        print('yippie!') #statement akan dieksekusi karena function telah diinherit menggunakan super, posisi super menentukan function mana yang akan dieksekusi tlbh dahulu
        self.confirmed_user_id = self.env.user.id # mengambil value dari user.id yang saat ini login dan menjadikannya value dari confirmed_user_id