# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'Department.schoolmanage'
    _description = 'Department.schoolmanage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    Department_name = fields.Char("Department_name", required=True)
    Department_code = fields.Char("Department_code", required=True)
    Dean_name = fields.Char("Dean_name", required=True)
    phone = fields.Integer("phone")
    gmail = fields.Char("Gmail", required=True)
    address = fields.Char("address", required=True)
    specialized_name = fields.Char("specialized_name", required=True)
    specialized_code = fields.Char("specialized_code", required=True)

