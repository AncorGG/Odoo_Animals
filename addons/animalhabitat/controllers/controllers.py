# -*- coding: utf-8 -*-
# from odoo import http


# class Animalhabitat(http.Controller):
#     @http.route('/animalhabitat/animalhabitat', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/animalhabitat/animalhabitat/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('animalhabitat.listing', {
#             'root': '/animalhabitat/animalhabitat',
#             'objects': http.request.env['animalhabitat.animalhabitat'].search([]),
#         })

#     @http.route('/animalhabitat/animalhabitat/objects/<model("animalhabitat.animalhabitat"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('animalhabitat.object', {
#             'object': obj
#         })

