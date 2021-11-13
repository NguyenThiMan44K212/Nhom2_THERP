from odoo import _, fields, models, api


class Student(models.Model):
    _name = 'school.student'
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    first_name = fields.Char('First Name', size=128, translate=True)
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128, required=True)
    name = fields.Char('Name')
    student_id = fields.Char("SV", required=True, copy=False, readonly=True,
                             default=lambda seft: _('New'))
    sdt = fields.Char("Phone")
    email = fields.Char("Email")
    ngay_sinh = fields.Date("Date Of Birth")
    dia_chi_thuong_tru = fields.Char("Permanent Address", required=True)
    dia_chi_tam_tru = fields.Char("Temporary Address")
    cmnd = fields.Char("Identification No", required=True)
    ident_date = fields.Date(string='Identification Date')
    ident_place = fields.Char(string='Identification Place')
    gioi_tinh = fields.Selection([
        ('one', 'Male'),
        ('two', 'Female'),
        ('three', 'Other')], required=True, default="one", string="Gender")
    lop = fields.Many2one(comodel_name='school.class', string="Class", select=True, copy=False)
    nganh_hoc = fields.Many2many('school.ology', string="Ology")
    chuyen_nganh = fields.Many2many('school.major', string="Major")
    khoa = fields.Many2one('hr.department', 'Department', required=True)
    ten_giao = fields.Many2one('hr.employee', 'Homeroom Teacher Name', required=True)
    bang_cap = fields.Char("Diploma")
    sinh_nam = fields.Selection([
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6')
    ], required=True, default="one", string="Year Students")
    stk = fields.Char("Bank Account")
    nam_nhap = fields.Date("Date Start", required=True)
    nam_ra = fields.Date("Date Graduate")
    status = fields.Selection([
        ('one', 'Studying'),
        ('two', 'Graduated'),
        ('three', 'Reserve')], required=True, default="one", string="Status")
    he_dt = fields.Selection([
        ('one', 'Formal'),
        ('two', 'Unofficial'),
        ('three', 'High Quality'),
        ('four', 'Postgraduate'),
    ], string='Training System', default='one', required=True)
    so_tc = fields.Integer("Number Of Credits")
    notes = fields.Text(string="Description")
    xe = fields.Boolean("Parking Card?")
    ktx = fields.Boolean("Dorm?")
    anh = fields.Binary('Image')
    quoc_gia = fields.Many2one('res.country', string='Country')
    family = fields.Many2many('school.family', string='Information Family')
    dan_toc = fields.Many2one('school.nation', string='Nation')
    ton_giao = fields.Many2one('school.religion', string='Religion')
    clb = fields.Boolean(string='Join The Club?')

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        if not self.middle_name:
            self.name = str(self.first_name) + " " + str(
                self.last_name)
        else:
            self.name = str(self.first_name) + " " + str(
                self.middle_name) + " " + str(self.last_name)

    @api.model
    def create(self, vals):
        if vals.get('student_id', ('New')) == ('New'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('school.student') or _('New')
        res = super(Student, self).create(vals)
        return res

class Relationship(models.Model):
    _name = 'school.relationship'
    _description = "Relationship"

    name = fields.Char("Relationship")

class Family(models.Model):
    _name = 'school.family'
    _description = "Family"

    name = fields.Char('Parent Name', required=True)
    quan_he = fields.Many2one('school.relationship', string="Relationship", required=True)
    dia_chi = fields.Char("Address")
    lien_he = fields.Char("Phone Number")
    student = fields.Many2many('school.student', string='Student(s)', required=True)

    _sql_constraints = [(
        'unique_parent',
        'unique(name)',
        'Can not create parent multiple times!'
    )]

class Nation(models.Model):
    _name = 'school.nation'
    _description = "Nation"

    name = fields.Char(string='Nation', required=True)

class Religion(models.Model):
    _name = 'school.religion'
    _description = "Religion"

    name = fields.Char(string="Religion", required=True)