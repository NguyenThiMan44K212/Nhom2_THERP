from odoo import fields, models, _, api

class Class(models.Model):
    _name = "school.class"
    _description = "Class"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char('Class Name', required=True)
    class_ID = fields.Char(string='LO', required=True, copy=False, readonly=True,
                           default=lambda seft: _('New'))
    teacher_homeroom = fields.Many2one('hr.employee', 'Homeroom Teacher Name', required=True)
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
    ], string='Status', default='doing')
    note = fields.Text('Description')
    start_date = fields.Date('Start Date', required=False)
    end_date = fields.Date('End Date')
    action = fields.Many2many('school.action', string='Action')
    student_list = fields.One2many(comodel_name='school.student', inverse_name='lop', string='Student List')
    major_id = fields.Many2one(comodel_name='school.major', string="Belonging Major", select=True, copy=False)

    @api.model
    def create(self, vals):
        if vals.get('class_ID', ('New')) == ('New'):
            vals['class_ID'] = self.env['ir.sequence'].next_by_code('school.class') or _('New')
        res = super(Class, self).create(vals)
        return res

class Action(models.Model):
    _name = "school.action"
    _description = "Action"

    name_action = fields.Char('Action Name', required=True)
    location = fields.Char('Location', required=True)
    time = fields.Datetime('Time', required=True)
    content = fields.Text('Content')






