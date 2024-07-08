from odoo import models, fields, api
from datetime import date

class Biodata(models.Model):
    _name = 'biodata'
    _description = 'Biodata'

    name = fields.Char(string="Nama")
    full_name = fields.Char(string="Nama Lengkap")
    birth_date = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(string="Umur", compute='_compute_age', store=True)
    children = fields.Integer(string="Anak")
    photo = fields.Binary(string="Foto")
    gender = fields.Selection([('male', 'Laki-Laki'), ('female', 'Perempuan')], string="Jenis Kelamin")
    
    # Pendidikan fields as boolean
    education_sd = fields.Boolean(string="SD")
    education_smp = fields.Boolean(string="SMP")
    education_sltp = fields.Boolean(string="SLTP")
    education_sma = fields.Boolean(string="SMA")
    education_smk = fields.Boolean(string="SMK")
    education_smu = fields.Boolean(string="SMU")
    education_slta = fields.Boolean(string="SLTA")
    education_kuliah = fields.Boolean(string="Kuliah")

    # Custom fields for relationships
    custom_many2one_id = fields.Many2one('res.partner', string="Custom Many2one")
    custom_one2many_ids = fields.One2many('res.partner', 'parent_id', string="Custom One2many")
    custom_many2many_ids = fields.Many2many('res.partner', string="Custom Many2many")
    custom_one2many_count = fields.Integer(string="One2many Count", compute='_count_one2many_items')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = date.today().year - record.birth_date.year
            else:
                record.age = 0

    @api.depends('custom_one2many_ids')
    def _count_one2many_items(self):
        for record in self:
            record.custom_one2many_count = len(record.custom_one2many_ids)
    
    def action_calculate_age(self):
        for record in self:
            record._compute_age()
