# -*- coding: utf-8 -*-

from odoo import models, fields, api


class specialized(models.Model):
    _name = 'specialized.schoolmanage'
    _description = 'specialized.schoolmanage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    specialized_name = fields.Char("specialized_name", required=True)
    specialized_code = fields.Char("specialized_code", required=True)
    quantity_SV = fields.Integer("sỉ số SV")
    quantity_GV = fields.Integer("sỉ số GV")
    Department_name = fields.Char("Tên Khoa", required=True)
    Department_code = fields.Char("Mã khoa", required=True)
    phone = fields.Integer("Số điện thoại")
    gmail = fields.Char("Gmail", required=True)
    class_name = fields.Char("Tên Lớp", required=True)
    class_code = fields.Char("Mã Lớp", required=True)