# -*- coding: utf-8 -*-

from odoo import models, fields

class ServicioGuarderia(models.Model):
    _name = 'servicio.guarderia'
    _description = 'Servicio de Guardería'
    _inherits = {
        'hr.employee': 'employee_id',
        'calendar.event': 'event_id',
    }

    # Relación con employee (Monitor)
    employee_id = fields.Many2one(
        'hr.employee', 
        required=True, 
        ondelete='cascade', 
        auto_join=True, 
        index=True,
        string='Monitor (Empleado)'
    )

    # Relación con event (Horario/Evento)
    event_id = fields.Many2one(
        'calendar.event', 
        required=True, 
        ondelete='cascade', 
        auto_join=True, 
        index=True,
        string='Evento de Calendario'
    )

    # Campos propios del servicio
    descripcion = fields.Text(string="Descripción del Servicio")
    
    rango_edad = fields.Selection([
        ('0-2', '0 - 2 años'),
        ('3-5', '3 - 5 años'),
        ('6-8', '6 - 8 años'),
        ('9-11', '9 - 11 años')
    ], string="Rango de Edad")
