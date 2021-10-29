from odoo import fields, models

class Class(models.Model):
    _name = "school.class"
    _description = "Ology_Class model"

    name = fields.Char('Class Name', required=True)
    teacher_homeroom = fields.Char('Homeroom Teacher Name', required=True)
    phone_teacher = fields.Char('Homeroom Teacher Phone')
    email_teacher = fields.Char('Homeroom Teacher Email')
    class_monitor = fields.Char('Class Monitor Name', required=True)
    phone_class_monitor = fields.Char('Class Monitor Phone')
    email_class_monitor = fields.Char('Class Monitor Email')
    vice_monitor = fields.Char('Vice Monitor Name', required=True)
    phone_vice_monitor = fields.Char('Vice Monitor Phone')
    email_vice_monitor = fields.Char('Vice Monitor Email')
    secretary = fields.Char('Secretary Name', required=True)
    phone_secretary = fields.Char('Secretary Phone')
    email_secretary = fields.Char('Secretary Email')
    total = fields.Integer('Number Of Students', required=True)
    school_year = fields.Char('School Year', required=True)
    course = fields.Char('Course', required=True)
    status = fields.Selection([
        ('doing', 'Doing'),
        ('done', 'Done'),
    ], string='Status', default='Doing')
    note = fields.Text('Description')
    start_date = fields.Date('Start Date', required=False)
    end_date = fields.Date('End Date')
    action = fields.Char('Action', required=True)