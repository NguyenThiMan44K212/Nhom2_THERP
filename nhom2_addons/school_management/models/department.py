from odoo import fields, models

class Department(models.Model):
    _name = 'school.department'
    _description = "Department"
    _rec_name = 'ten_khoa'

    ten_khoa = fields.Char("Department's Name")
    ma_khoa = fields.Char(string="Department ID", required=True)
    so_nam_toi_thieu_tot_nghiep = fields.Integer('Minimum Year Graduation Number')

    _sql_constraints = [
        ('ma_khoa_unique', 'unique (ma_khoa)', 'Department has existed!!')
    ]

class Majors(models.Model):
    _name = 'school.major'
    _description = "Major"
    _rec_name = 'ten_nganh'

    ten_nganh = fields.Char(string="Majors's Name")
    ma_nganh = fields.Char(string="Majors ID", required=True)
    ma_khoa = fields.Many2one('school.majors', string="Department ID", required=True)

    _sql_constraints = [
        ('ma_nganh_unique', 'unique (ma_nganh)', 'Majors has existed!!')
    ]

class Class(models.Model):
    _name = 'school.class'
    _description = "Class"
    _rec_name = 'ten_lop'

    ten_lop = fields.Char(string="Class's Name")
    ma_lop = fields.Char(string="Class ID", required=True)
    ma_khoa = fields.Many2one('school.class', string="Department ID", required=True)

    _sql_constraints = [
        ('ma_lop_unique', 'unique (ma_lop)', 'Class has existed!!')
    ]




