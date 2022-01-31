# -*- coding: utf-8 -*-

from odoo import models, fields ,api


class Editorial(models.Model):
    _name = 'milibro.editorial'
    _description = 'Descripción del modelo editorial'

    name = fields.Char(string="Nombre",required=True)
    direccion = fields.Char(string="Direccion")
    poblacion = fields.Char(string="Poblacion")

    #campo calculado
    cantidad_libros = fields.Integer(compute="_num_libros")
    # one2many
    libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="editorial_id", required=False)

    @api.depends("libro_ids")
    def _num_libros(self):
        for libros in self:
            libros.cantidad_libros = len(libros.libro_ids)

