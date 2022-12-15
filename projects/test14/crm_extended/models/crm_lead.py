from odoo import fields, models   #


class CrmLead(models.Model):   #definimos la clase 
    _inherit = 'crm.lead'      ##ereda de crem.lead
    needed_quality = fields.Char()  #el campo que queremos agregar se llama needed_queality


    ##debemos cargar este nuevo modulo a la lista __init__py
    
