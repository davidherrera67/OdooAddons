# -*- coding: utf-8 -*-

from odoo import fields, api, models
from odoo.exceptions import ValidationError


class Libro(models.Model):
    _name = 'milibro.libro'
    _description = 'Descripción del modelo libro'
    # CONSTRAINT PARA QUE SEA UNICO EL ISBN
    _sql_constraints = [('isbn_unico', 'unique(isbn)', 'El isbn debe ser unico')]

    name = fields.Char(string="Titulo", required=True, help=("Escribe tu nombre"))
    descripcion = fields.Text(string="Resumen", help=("Escribe la descripcion"))
    isbn = fields.Char(string="ISBN", required=True)

    # YA NO SE CREAN LOS CAMPOS autor y nombre ASÍ , SINO QUE SE CREAN COMO MANY2ONE ABAJO.
    # autor = fields.Char(string="Autor",help=("Escribe el autor"))
    # editorial = fields.Char(string="Editorial",help=("Escribe la editorial"))

    # Relaciones:

    # many2one
    autor_id = fields.Many2one(comodel_name="milibro.autor", string="Autor",
                               required=True)  # lleva required a true porque no va a tener 0 autores el libro entonces le obligas a poner el autor si o si con requerido a true.
    editorial_id = fields.Many2one(comodel_name="milibro.editorial", string="Editorial", required=True)
    # ENUNCIADO: Crea un campo de relación en la clase Libro, de forma, que un Libro tenga un CDU y modifica la vista form de Libros para incluir dicho campo.
    cdu_id = fields.Many2one(comodel_name="milibro.cdu", string="CDU", required=True)

    # many2many
    categoria_ids = fields.Many2many(comodel_name="milibro.categoria", string="Categorías")

    # campo calculado con interfaz @onChange
    num_paginas = fields.Integer(
        string="Num. paginas")  # aqui no se le dice nada del compute...se le dice luego en el onchange o en el constraints)
    num_paginas = fields.Integer(string="Num. paginas")
    tejuelo = fields.Char(string="tejuelo")

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:

    @api.onchange("num_paginas")
    def _comprobarNumPaginasOnChange(self):
        res = {}
        if self.num_paginas < 0:
            res['warning'] = {'title': ('Advertencia'),
                              'message': ('El numero de paginas no puede ser menor a 0 (ONCHANGE Methodology.)')
                              }
        return res

    @api.constrains("num_paginas")
    def _validar_num_paginas_constrains(self):
        for registro in self:
            if registro.num_paginas <= 0:
                raise ValidationError("El numero de paginas ha de ser mayor o igual a 0 (CONSTRAINS)")

    @api.depends("name", "autor_id", "cdu_id")
    def _calcular_tejuelo(self):
        for r in self:
            if r.name and r.autor_id and r.apellidos:
                r.tejuelo = str(r.cdu_id) + "-" + str(r.name)[0:3].upper() + "-" + str(r.autor_id)[0:3].lower()
            else:
                r.tejuelo = ""

