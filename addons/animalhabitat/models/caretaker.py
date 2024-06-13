# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class caretaker(models.Model):
    _name = 'animalhabitat.caretaker'
    _description = 'animalhabitat.caretaker'
    
    name = fields.Char()
    surname = fields.Char()
    birthday = fields.Date()
    description = fields.Char()

