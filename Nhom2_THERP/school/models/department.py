import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Department(models.Model):
    _inherit = "hr.department"
    _description = "Department"

    department_id = fields.Char(string='KH', required=True, copy=False, readonly=True,
                              default=lambda seft: _('New'))
    ology_list = fields.Many2many('school.ology', string='Ology List', required=True)
    dean = fields.Many2many('hr.employee', string='Leader', required=True)
    foundation_date = fields.Date('Foundation date', required=True)
    phone = fields.Char("Contact Phone", required=True)
    email = fields.Char("Contact Email", required=True)

class Action(models.Model):
    _name = "school.action"
    _description = "Action model"

    name_action = fields.Many2one('hr.department', string='Action name')
    location = fields.Char('Location')
    time = fields.Date('Time')

    @api.model
    def create(self, vals):
        if vals.get('department_id', ('New')) == ('New'):
            vals['department_id'] = self.env['ir.sequence'].next_by_code('hr.department') or _('New')
        res = super(Department, self).create(vals)
        return res
