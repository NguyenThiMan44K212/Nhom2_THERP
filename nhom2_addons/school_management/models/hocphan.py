from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
class Term(models.Model):
    _name = "my.term"
    _description = "Term model"
    kyhoc = fields.Char('Ky hoc:', required=True)
    tenhp = fields.Char('Ten HP:', required=True)
    mahp = fields.Char('Ma HP:', required=True)
    sotc = fields.Integer('So tin chi:', required=True)
    loaihp = fields.Selection([
        ('chuyennganh', 'Chuyen nganh'),
        ('binhthuong', 'Binh thuong'),
        ('khac', 'Khac')
    ], string='Loai HP:', default='Chuyen nganh')
    sotlt = fields.Integer('So lop ly thuyet:', required=True)
    sotth = fields.Integer('So lop thuc hanh:', required=True)
    ghichu = fields.Selection([
        ('moi', 'Hoc moi'),
        ('lai', 'Hoc lai'),
        ('caithien', 'Cai thien')
    ], string='Ghi chu:', default='Hoc moi')
    tgbd =fields.Date('Thoi gian bat dau:', required=False)
    tgkt = fields.Date('Thoi gian ket thuc:', required=False)
    lich = fields.Char('Lich hoc:', required=True)
    phong = fields.Char('Phong:', required=True)
    ngaythi = fields.Date('Ngay thi:', required=False)