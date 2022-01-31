# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Autor(models.Model):
    _name = 'milibro.autor'
    _description = 'Descripción del modelo autor'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)

    # campo calculado
    cantidad_libros_escritos = fields.Integer(compute="_num_libros_escritos")
    name = fields.Char(compute="_cambiar_nombre",store=True)

    # Relaciones

    # one2many
    libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="autor_id", required=False)

    @api.depends("libro_ids")
    def _num_libros_escritos(self):
        for libro in self:
            libro.cantidad_libros_escritos = len(libro.libro_ids)


    @api.depends("nombre","apellidos")
    def _cambiar_nombre(self):
        for persona in self:
            if persona.nombre != None and persona.apellidos !=None:
                persona.name = str(persona.apellidos) + "," + str(persona.nombre)
            else:
                persona.name = ""
