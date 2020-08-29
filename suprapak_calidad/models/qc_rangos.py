# -*- coding: utf-8 -*-
# Copyright 2010 NaN Projectes de Programari Lliure, S.L.
# Copyright 2014 Serv. Tec. Avanzados - Pedro M. Baeza
# Copyright 2014 Oihane Crucelaegui - AvanzOSC
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _

class qcRangoAncho(models.Model):
    """
    Tolerancia en ancho
    """
    _name = 'qc.rango.ancho'
    _description = 'Rango Ancho'

    rango_min = fields.Float(string='Rango Minimo', default=0.00)
    rango_max = fields.Float(string='Rango Maximo', default=0.00)
    tolerancia_min = fields.Float(string='Tolerancia Minima', default=0.00)
    tolerancia_max = fields.Float(string='Tolerancia Maxima', default=0.00)


class qcRangoCorte(models.Model):
    _name = 'qc.rango.corte'
    _description = 'Rango Corte'

    rango_min = fields.Float(string='Rango Minimo', default=0.00)
    rango_max = fields.Float(string='Rango Maximo', default=0.00)
    tolerancia_min_cor = fields.Float(string='Tolerancia Cortado Minima', default=0.00)
    tolerancia_max_cor = fields.Float(string='Tolerancia Cortado Maxima', default=0.00)
    tolerancia_min_sel = fields.Float(string='Tolerancia Sellado Minima', default=0.00)
    tolerancia_max_sel = fields.Float(string='Tolerancia Sellado Maxima', default=0.00)

class qcRangoEncogimiento(models.Model):
    _name = 'qc.rango.encogimiento'
    _description = 'Rango Encogimiento'

    sheet_film = fields.Char(string='Pelicula')
    sheet_composite = fields.Char(string='Composicion')
    longitudinal = fields.Char(string='Longitudinal')
    trasnversal = fields.Char(string='Trasnversal')

class qcRangoGrafilado(models.Model):
    _name = 'qc.rango.grafilado'
    _description = 'Rango Grafilado'

    rango_min = fields.Float(string='Rango Minimo', default=0.00)
    rango_max = fields.Float(string='Rango Maximo', default=0.00)
    tolerancia_min = fields.Float(string='Tolerancia Minima', default=0.00)
    tolerancia_max = fields.Float(string='Tolerancia Maxima', default=0.00)

class qcRangoCalibre(models.Model):
    _name = 'qc.rango.calibre'
    _description = 'Rango Calibre'

    sheet_caliber = fields.Float(string='Calibre', default=0.00)
    tolerancia_min = fields.Float(string='Tolerancia Minima', default=0.00)
    tolerancia_max = fields.Float(string='Tolerancia Maxima', default=0.00)

class qcRangoMuestra(models.Model):
    _name = 'qc.rango.muestra'
    _description = 'Rango Muestra'

    tolerancia_min = fields.Float(string='Tolerancia Minima', default=0.00)
    tolerancia_max = fields.Float(string='Tolerancia Maxima', default=0.00)
    nivel1 = fields.Float(string='NIVEL 1', default=0.00)
    nivel2 = fields.Float(string='NIVEL 2', default=0.00)
    nivel3 = fields.Float(string='NIVEL 3', default=0.00)

