# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Nganh(models.Model):
    _name = 'Nganh.schoolmanage'
    _description = 'Nganh.schoolmanage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char("Tên Nganh", required=True)
    code = fields.Char("Mã Nganh", required=True)
    siso_SV = fields.Integer("sỉ số SV")
    siso_GV = fields.Integer("sỉ số GV")
    ten_khoa = fields.Char("Tên Khoa", required=True)
    ma_khoa = fields.Char("Mã khoa", required=True)
    sdt = fields.Integer("Số điện thoại")
    gmail = fields.Char("Gmail", required=True)
    ten_lop = fields.Char("Tên Lớp", required=True)
    ma_lop = fields.Char("Mã Lớp", required=True)