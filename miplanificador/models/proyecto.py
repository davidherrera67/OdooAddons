# -*- coding: utf-8 -*-

from odoo import models, fields


class Proyecto(models.Model):
    _name = 'milibro.proyecto'
    _description = 'Proyectos'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_inicio_estimada = fields.Date(string="Fecha de inicio estimada")
    fecha_fin_estimada = fields.Date(string="Fecha de fin estimada")
    fecha_inicio_real = fields.Date(string="Fecha de inicioreal")
    Fecha_fin_real = fields.Date(string="Fecha de fin real")
