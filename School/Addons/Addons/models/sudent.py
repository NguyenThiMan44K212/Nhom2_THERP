from odoo import fields, models

class Sudent(models.Model):
    _name = 'student'
    _description = "Module quan ly sinh vien"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char("Tên sinh viên", required=True)
    code = fields.Char("Mã sinh viên", required=True)
    sdt = fields.Integer("Số điện thoại")
    gmail = fields.Char("Gmail", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    dia_chi_thuong_tru = fields.Char("Địa chỉ thường trú", required=True)
    dia_chi_tam_tru = fields.Char("Đại chỉ tạm trú", required=True)
    cmnd = fields.Integer("Số chứng minh", required=True)
    gioi_tinh = fields.Selection([
        ('one', 'Nam'),
        ('two', 'Nữ'),
        ('three', 'Khác')],required=True ,default="one" , string="Giới tính")
    dan_toc = fields.Char("Dân tộc")
    ton_giao = fields.Char("Tôn giáo")
    # many
    # data=fields.Many2one("Tên bảng", string="Ngành học")
    nganh_hoc=fields.Char("Ngành học")
    chuyen_nganh = fields.Char("Chuyên ngành")
    khoa = fields.Char("Khoa")
    ten_giao=fields.Char("Tên giáo viên")
# many
    lop=fields.Char("Tên lớp")
    bang_cap=fields.Char("Bằng cấp")
    sinh_nam=fields.Char("Sinh viên năm")
    nganh_2=fields.Char("Ngành 2")
    stk=fields.Char("STK ngân hàng Đông Á")
    nam_nhap=fields.Date("Ngày nhập học" , required=True)
    nam_ra=fields.Date("Ngày ra trường" ,required=True)
    status = fields.Selection([
        ('one', 'Đang học'),
        ('two', 'Đã ra trường'),
        ('three', 'Bảo lưu')], required=True, default="one" , string="Trạng thái")
    he_dt=fields.Char("Hệ đào tạo")
    so_tc=fields.Char("Số tín chỉ")
    notes=fields.Char("Mô tả")
    ten_ba=fields.Char("Tên bố")
    nghe_ba=fields.Char("Nghề nghiệp ba")
    ten_ma=fields.Char("Tên mẹ")
    nghe_ma=fields.Char("Nghề nghiệp mẹ")
    dia_chi=fields.Char("Địa chỉ")
    lien_he=fields.Char("Số điện thoại liên hệ")
    xe=fields.Boolean("Có đăng ký thẻ xe")
    ktx=fields.Boolean(" Có ở KTX")




