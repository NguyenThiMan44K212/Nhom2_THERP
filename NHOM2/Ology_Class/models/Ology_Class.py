from odoo import _, api, fields, models
class Ology(models.Model):
    _name = "my.ology"
    _description = "Ology_Class model"

    name = fields.Char(string='ID', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    Ology = fields.Char('Ology :', required=True)
    Target = fields.Char('Target :', required=True)
    training_system = fields.Selection([
        ('fulltime', 'full time'),
        ('parttime', 'part time'),
        ('Postgraduate', 'Postgraduate'),
    ], string='status:', default='full time')

    Class_name = fields.Char('Class name :', required=True)
    teacherHroom = fields.Integer('Homeroom teacher name :', required=True)
    SDTteacher = fields.Char('Homeroom teacher phone :', required=True)
    Emailteacher = fields.Char('homeroom teacher Email  :', required=True)

    Class_monitor = fields.Integer('Class monitor name :', required=True)
    SDTClass_monitor = fields.Char('Class monitor phone :', required=True)
    EmailClass_monitor = fields.Char('Class monitor Email  :', required=True)
    total = fields.Integer('total :', required=True)
    status = fields.Selection([
        ('doing', 'doing'),
        ('done', 'done'),
    ], string='status:', default='doing')
    note = fields.Char('Note :', required=True)
    starttime =fields.Date('start time:', required=False)
    endtime = fields.Date('end time:', required=False)
    action = fields.Char('action :', required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('my.ology') or _('New')
        res = super(Ology, self).create(vals)
        return res
