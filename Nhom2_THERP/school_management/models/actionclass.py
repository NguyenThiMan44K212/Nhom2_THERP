from odoo import fields, models, _, api

class Action(models.Model):
    _name = "school.action"
    _description = "Action model"

    ID = fields.Char(string='ID', required=True, copy=False, readonly=True,
                               default=lambda seft: _('New'))

    name_action = fields.Char(string='Action name')
    location = fields.Char('Location')
    time = fields.Date('Time')

    @api.model
    def create(self, vals):
        if vals.get('ID', ('New')) == ('New'):
            vals['ID'] = self.env['ir.sequence'].next_by_code('school.action') or _('New')
        res = super(Action, self).create(vals)
        return res