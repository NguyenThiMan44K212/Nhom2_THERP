# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Khoa(models.Model):
    _name = 'Khoa.schoolmanage'
    _description = 'Khoa.schoolmanage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char("Tên khoa", required=True)
    code = fields.Char("Mã khoa", required=True)
    siso = fields.Integer("sỉ số SV")
    ten_truongkhoa = fields.Char("Tên trưởng Khoa", required=True)
    sdt = fields.Integer("Số điện thoại")
    gmail = fields.Char("Gmail", required=True)
    ten_Nganh = fields.Char("Tên Ngành", required=True)
    ma_Nganh = fields.Char("Mã Ngành", required=True)

