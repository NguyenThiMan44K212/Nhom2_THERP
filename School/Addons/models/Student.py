from odoo import _, api, fields, models

class Student(models.Model):
    _name = 'student'
    _description = "Module Student Management"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char("Name", required=True)
    code = fields.Char("ID", required=True,copy=False, readonly=True,
                       default=lambda seft: _('New'))
    sdt = fields.Integer("Phone Number")
    gmail = fields.Char("Gmail", required=True)
    ngay_sinh = fields.Date("Date of Birth")
    dia_chi_thuong_tru = fields.Char("Permanent address", required=True)
    dia_chi_tam_tru = fields.Char("Shelter address")
    cmnd = fields.Integer("CMND", required=True)
    gioi_tinh = fields.Selection([
        ('one', 'Male'),
        ('two', 'Female'),
        ('three', 'Other')],required=True ,default="one" , string="Gender")
    dan_toc = fields.Char("Nation")
    ton_giao = fields.Char("Religion")
    # many
    # data=fields.Many2one("Tên bảng", string="Ngành học")
    # tạo
    nganh_hoc=fields.Char("Ology")
    chuyen_nganh = fields.Char("Major")
    khoa = fields.Char("Faculty")
    ten_giao=fields.Char("Teacher Name")
# many
    lop=fields.Char("Class Name")
    bang_cap=fields.Char("Didiploma")
    sinh_nam=fields.Char("Year Student")
    nganh_2=fields.Char("Ology 2")
    stk=fields.Char("Dong A account number")
    nam_nhap=fields.Date("Date Start",required=True)
    nam_ra=fields.Date("Date Graduate")
    status = fields.Selection([
        ('one', 'Under graduate'),
        ('two', 'Granduate'),
        ('three', 'Reserve')], required=True, default="one" , string="Status")
    he_dt=fields.Char("Formal_Education")
    so_tc=fields.Char("Credits")
    notes=fields.Char("Description")
    dai_dien = fields.Char("Surrogate")
    dia_chi=fields.Char("Address")
    lien_he=fields.Char("Phone Number")
    xe=fields.Boolean("Parking card?")
    ktx=fields.Boolean("Dorm?")

    @api.model
    def create(self, vals):
        if vals.get('code', ('New')) == ('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('student') or _('New')
        res = super(Student, self).create(vals)
        return res



