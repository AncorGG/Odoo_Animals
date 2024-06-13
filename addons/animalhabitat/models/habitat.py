# -*- coding: utf-8 -*-

from odoo import models, fields, api


class habitat(models.Model):
    _name = 'animalhabitat.habitat'
    _description = 'animalhabitat.habitat'

    name = fields.Char()
    climate = fields.Char()
    humidity = fields.Float(string="Humidity (%)", default=0.0)
    ubication = fields.Char()
    animal = fields.One2many('animalhabitat.animal', 'habitat', string='animal')