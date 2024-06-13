# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class animal(models.Model):
    _name = 'animalhabitat.animal'
    _description = 'animalhabitat.animal'

    name = fields.Char()
    age = fields.Integer(compute='_compute_age', store=True)
    birthday = fields.Date()
    species = fields.Char()
    onExtinction = fields.Boolean(string='onExtinction')
    description = fields.Char()
    habitat = fields.Many2one('animalhabitat.habitat', string='Habitat')

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                birth_date = record.birthday
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

