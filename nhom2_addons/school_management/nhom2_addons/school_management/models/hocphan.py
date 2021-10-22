from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
class course(models.Model):
    _name = "my.course"
    _description = "course model"
    semester = fields.Char('semester :', required=True)
    coursename = fields.Char('course name :', required=True)
    coursecode = fields.Char('course code :', required=True)
    credits = fields.Integer('number of credits :', required=True)
    coursetype  = fields.Selection([
        ('major', 'major'),
        ('normal', 'normal'),
        ('others', 'others')
    ], string='Course Type:', default='major')
    theoretical = fields.Integer('number of theoretical periods :', required=True)
    practice = fields.Integer('number of practice periods :', required=True)
    note = fields.Selection([
        ('learnnew', 'learn new'),
        ('learnimprovement', 'learn improvement'),
        ('learnagain', 'learn again')
    ], string='Note:', default='learn new')
    total = fields.Integer('total:', required=True)
    starttime =fields.Date('start time:', required=False)
    endtime = fields.Date('end time:', required=False)
    schedule = fields.Char('schedule:', required=True)
    room = fields.Char('room:', required=True)
    examday = fields.Date('exam day:', required=False)