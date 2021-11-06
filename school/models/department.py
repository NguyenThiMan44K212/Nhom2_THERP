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
    foundation_date = fields.Date(string='Foundation Date', required=True)
    phone = fields.Char(string="Contact Phone", required=True)
    email = fields.Char(string="Contact Email", required=True)
    program = fields.Many2many('school.program', string='Program Name')
    description = fields.Text(string='Description')
    action = fields.Many2many('school.action', string='Action')

    @api.model
    def create(self, vals):
        if vals.get('department_id', ('New')) == ('New'):
            vals['department_id'] = self.env['ir.sequence'].next_by_code('hr.department') or _('New')
        res = super(Department, self).create(vals)
        return res

class Program(models.Model):
    _name = "school.program"
    _description = "Program"

    name_program = fields.Char('Program Name', required=True)
    name_business = fields.Char('Company Name', required=True)
    signed_at = fields.Char('Signed At', required=True)
    signed_on = fields.Datetime('Signed On', required=True)
    content = fields.Text('Content')
