# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'Department.schoolmanage'
    _description = 'Department.schoolmanage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char("Tên khoa", required=True)
    code = fields.Char("Mã khoa", required=True)
    Dean_name = fields.Char("Tên trưởng Khoa", required=True)
    sdt = fields.Integer("Số điện thoại")
    gmail = fields.Char("Gmail", required=True)
    specialized_name = fields.Char("Tên Ngành", required=True)
    specialized_code = fields.Char("Mã Ngành", required=True)

