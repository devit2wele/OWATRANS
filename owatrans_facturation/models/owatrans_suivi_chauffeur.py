# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models

TYPE_CONTAINER = [
    ("type_20", "20'"),
    ("type_40", "40'"),
]





class SuiviChauffeur(models.Model):
    _name = 'owatrans.suivi.chauffeur'

    @api.depends('vehicule')
    def _compute_contact_chauffeur(self):
    	contact_chauffeur = False
    	for res in self:
    		if res.vehicule and res.vehicule.driver_id:
    			if res.vehicule.driver_id.phone and res.vehicule.driver_id.mobile:
    				contact_chauffeur = res.vehicule.driver_id.phone +' / '+ res.vehicule.driver_id.mobile
    			elif res.vehicule.driver_id.phone:
    				contact_chauffeur = res.vehicule.driver_id.phone
    			elif res.vehicule.driver_id.mobile:
    				contact_chauffeur = res.vehicule.driver_id.mobile
    			else:
    				contact_chauffeur = False
    		self.contact_chauffeur = contact_chauffeur
    
    date = fields.Date(string='Date', default=date.today())
    vehicule = fields.Many2one('fleet.vehicle', string='Matricule', required=True)
    type_container = fields.Selection(TYPE_CONTAINER, string='Pied')
    prenom_nom = fields.Char(string="Prénom/Nom")
    contact_chauffeur = fields.Char(string='Contact Chauffeur', compute='_compute_contact_chauffeur')
    positionnement = fields.Char(string='Positionnement')
    geolocalisation = fields.Char(string='Géolocalisation')
    compagnie = fields.Many2one('res.partner', string='Compagnie')
    oberservations = fields.Char(string='Oberservations')
