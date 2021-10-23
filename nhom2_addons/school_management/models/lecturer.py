from odoo import api, fields, models


class Lecturer(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"
    _description = "Lecturer"

#     name = fields.Char(string="Lecturer Name", related='resource_id.name', store=True, readonly=False, tracking=True)
#     lecturer_id = fields.Char(string="Lecturer Code", required=True)
#     birthday = fields.Date('Date of Birth', groups="hr.group_hr_user", tracking=True)
#     gender = fields.Selection([
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other')
#     ], groups="hr.group_hr_user", tracking=True)
#     ident_id = fields.Integer(string='Identification No', required=True)
#     ident_date = fields.Date(string='Identification Issuance Date', required=True)
#     ident_place = fields.Char(string='Identification Issuance Place', required=True)
#     phone = fields.Char(related='address_home_id.phone', related_sudo=False, readonly=False, string="Phone",
#                         groups="hr.group_hr_user")
#     religion = fields.Char(string="Religion", required=True)
#     nation = fields.Char(string="Nation", required=True)
#     email = fields.Char(related='address_home_id.email', string="Email", groups="hr.group_hr_user")
#     bank_account_id = fields.Many2one(
#         'res.partner.bank', 'Bank Account Number',
#         domain="[('partner_id', '=', address_home_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
#         groups="hr.group_hr_user",
#         tracking=True,
#         help='Employee bank salary account')
#     place_of_birth = fields.Char('Place of Birth', groups="hr.group_hr_user", tracking=True)
#     permanent_address = fields.Many2one('res.partner', 'Permanent Address', groups="hr.group_hr_user", tracking=True)
#     temporary_residence_address = fields.Char(string="Temporary Residence Address", required=True)
#     marital = fields.Selection([
#         ('single', 'Single'),
#         ('married', 'Married'),
#         ('cohabitant', 'Legal Cohabitant'),
#         ('widower', 'Widower'),
#         ('divorced', 'Divorced')
#     ], string='Marital Status', groups="hr.group_hr_user", default='single', tracking=True)
#     spouse_complete_name = fields.Char(string="Spouse Complete Name", groups="hr.group_hr_user", tracking=True)
#     spouse_birthdate = fields.Date(string="Spouse Birthdate", groups="hr.group_hr_user", tracking=True)
#     children = fields.Integer(string='Number of Children', groups="hr.group_hr_user", tracking=True)
#     additional_note = fields.Text(string='Additional Note', groups="hr.group_hr_user", tracking=True)
#     image = fields.Binary('Image')
#     family_status = fields.Selection([
#         ('poor_households', 'Poor Households'),
#         ('near_poor_households', 'Near-poor Households'),
#         ('family_difficult', 'Family Difficult'),
#         ('orphan', 'Orphan'),
#         ('ethnic_minority', 'Ethnic Minority')
#     ], string='Family Status', default='single')
#
#     _sql_constraints = [
#         ('lecturer_id_unique', 'unique (lecturer_id)', 'Lecturer code has existed!!')
#     ]
#
#
# class LecturersInfor(models.Model):
#     _inherit = "res.users"
#
#     def get_teacher(self):
#         return self.env['school.lecturer'].search([('Account', '=', self.id)], limit=1)