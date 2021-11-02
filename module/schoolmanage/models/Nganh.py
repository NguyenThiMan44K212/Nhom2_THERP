# -*- coding: utf-8 -*-

from odoo import models, fields, api


class specialized(models.Model):
    _name = 'specialized.schoolmanage'
    _description = 'specialized.schoolmanage'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    specialized_name = fields.Char("specialized_name", required=True)
    specialized_code = fields.Char("specialized_code", required=True)
    quantity_SV = fields.Integer("quantity_SV")
    quantity_GV = fields.Integer("quantity_GV")
    Department_name = fields.Char("Department_name", required=True)
    Department_code = fields.Char("Department_code", required=True)
    phone = fields.Integer("phone")
    gmail = fields.Char("Gmail", required=True)
    class_name = fields.Char("class_name", required=True)
    class_code = fields.Char("class_code", required=True)