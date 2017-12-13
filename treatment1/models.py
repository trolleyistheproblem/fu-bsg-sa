# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>

doc = """
This is a eight-period public goods game with 5 players. Assignment to groups is
random.

"""

class Constants(BaseConstants):
    name_in_url = 'pavan1'
    players_per_group = 3
    num_rounds = 12

    #"""Amount allocated to each player"""
    endowment = c(10)
    efficiency_factor = 3
    threshold = c(4)
    typical_response = "Yes"
    atypical_response = "No"
    max_contribution = c(5)
    question_correct = c(12)
    player_4_contribution = c(3)
    player_5_potential_earnings = c(0)
    player_4_potential_earnings = c(0)

class Subsession(BaseSubsession):
	pass
	
class Group(BaseGroup):
	
	computer_submission = models.CurrencyField()
	
	player_5_earnings = models.CurrencyField()
	
	player_5_acceptance = models.CharField()
	
	player_4_earnings = models.CurrencyField()
	
	player_4_acceptance = models.CharField()
	
	total_contribution = models.CurrencyField()
	
	individual_share = models.CurrencyField()
	
	lowest_contribution = models.CurrencyField()
	
	should_display_warning3 = False
	
	should_display_warning4 = True
	
	should_display_warning5 = True
	
	should_display_warning6 = True
	
	should_display_warning7 = True
	
	should_display_warning8 = True
	
	should_display_warning9 = True
	
	should_display_warning10 = True
	
	should_display_warning11 = True
	
	should_display_warning12 = True
	
	count3 = 1
	
	count4 = 1
	
	count5 = 1
	
	count6 = 1
	
	count7 = 1
	
	count8 = 1
	
	count9 = 1
	
	count10 = 1
	
	count11 = 1
	
	count12 = 1

	
	def find_lowest_contribution(self):
		self.lowest_contribution = Constants.endowment
		gen = (p for p in self.get_players())
		for p in gen:
			if p.contribution <= self.lowest_contribution:
				self.lowest_contribution = p.contribution
	
	def should_display_warning3(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count3 = self.count3 + 1
		if self.count3 >= 2:
			self.should_display_warning3 = False
		else:
			self.should_display_warning3 = False
		return self.should_display_warning3	
	
	def should_display_warning4(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count4 = self.count4 + 1
		if self.count4 >= 2:
			self.should_display_warning4 = True
		else:
			self.should_display_warning4 = True
		return self.should_display_warning4	
	
	def should_display_warning5(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count5 = self.count5 + 1
		if self.count5 >= 2:
			self.should_display_warning5 = True
		else:
			self.should_display_warning5 = True
		return self.should_display_warning5	
		
	def should_display_warning6(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count6 = self.count6 + 1
		if self.count6 >= 2:
			self.should_display_warning6 = True
		else:
			self.should_display_warning6 = True
		return self.should_display_warning6	
		
	def should_display_warning7(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count7 = self.count7 + 1
		if self.count7 >= 2:
			self.should_display_warning7 = True
		else:
			self.should_display_warning7 = True
		return self.should_display_warning7	
	
	def should_display_warning8(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count8 = self.count8 + 1
		if self.count8 >= 2:
			self.should_display_warning8 = True
		else:
			self.should_display_warning8 = True
		return self.should_display_warning8	
		
	def should_display_warning9(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count9 = self.count9 + 1
		if self.count9 >= 2:
			self.should_display_warning9 = True
		else:
			self.should_display_warning9 = True
		return self.should_display_warning9		
		
	def should_display_warning10(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count10 = self.count10 + 1
		if self.count10 >= 2:
			self.should_display_warning10 = True
		else:
			self.should_display_warning10 = True
		return self.should_display_warning10
		
	def should_display_warning11(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count11 = self.count11 + 1
		if self.count11 >= 2:
			self.should_display_warning11 = True
		else:
			self.should_display_warning11 = True
		return self.should_display_warning11
		
	def should_display_warning12(self):
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count12 = self.count12 + 1
		if self.count12 >= 2:
			self.should_display_warning12 = True
		else:
			self.should_display_warning12 = True
		return self.should_display_warning12										
	
	def set_payoffs2(self):
		self.total_contribution = sum([p.contribution for p in self.get_players()]) + Constants.max_contribution + Constants.player_4_contribution
		self.individual_share = self.total_contribution * Constants.efficiency_factor / (Constants.players_per_group + 2)
		self.computer_submission = Constants.max_contribution
		gen1 = (p for p in self.get_players() if p.accept_payment() == True)
		gen2 = (p for p in self.get_players() if p.accept_payment() == False)
		for p in gen1:
			p.payoff = Constants.endowment - p.contribution + self.individual_share
			p.acceptance = Constants.typical_response   	
		for p in gen2:
			p.payoff = (Constants.endowment - p.contribution)
			p.acceptance = Constants.atypical_response
		gen = (p for p in self.get_players() if Constants.player_4_contribution < Constants.threshold)
		for p in gen:
			self.count9 = self.count9 + 1
		if self.count9 >= 2 and self.subsession.round_number > 3:
			self.player_5_earnings = Constants.player_5_potential_earnings
			self.player_5_acceptance = Constants.atypical_response
			self.player_4_earnings = self.individual_share + 7
		else:
			self.player_5_earnings = self.individual_share
			self.player_4_earnings = self.individual_share +7 
			self.player_5_acceptance = Constants.typical_response
	
	def set_payoffs1(self):
		self.total_contribution = sum([p.contribution for p in self.get_players()]) + Constants.max_contribution + Constants.player_4_contribution
		self.individual_share = self.total_contribution * Constants.efficiency_factor / (Constants.players_per_group + 2)
		self.computer_submission = Constants.max_contribution
		self.player_5_earnings = self.individual_share
		self.player_4_earnings = self.individual_share +7
		for p in self.get_players():
			p.payoff = Constants.endowment - p.contribution + self.individual_share							

class Player(BasePlayer):

    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    
    enter_emotion = models.CharField(blank=True)
    
    acceptance = models.CharField()

    accept = models.CharField(
    choices=['Yes', 'No'])
    
    gender = models.CharField(
    choices=['Male', 'Female', 'Other'])
    
    age = models.PositiveIntegerField()
    
    income = models.PositiveIntegerField()
    
    why = models.CharField()
    
    irritation = models.CharField(widget=widgets.RadioSelectHorizontal(),
    choices=['0', '1', '2', '3', '4', '5'])
    
    guilt = models.CharField(widget=widgets.RadioSelectHorizontal(),
    choices=['0', '1', '2', '3', '4', '5'])
    
    confusion = models.CharField(widget=widgets.RadioSelectHorizontal(),
    choices=['0', '1', '2', '3', '4', '5'])
    
    admiration = models.CharField(widget=widgets.RadioSelectHorizontal(),
    choices=['0', '1', '2', '3', '4', '5'])
    
    empathy = models.CharField(widget=widgets.RadioSelectHorizontal(),
    choices=['0', '1', '2', '3', '4', '5'])
    
    general_feeling = models.CharField(widget=widgets.RadioSelectHorizontal(),
    choices=['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
    
    education = models.CharField(
    choices=['Some Primary','Completed Primary','Some Secondary', 'Completed Secondary', 'Some University', 'Completed University', 'Masters', 'Doctorate'])
    
    occupation = models.CharField()
    
    feedback = models.CharField(blank=True)
    
    question1 = models.CurrencyField()
    
    question2 = models.CurrencyField()
    
    question3 = models.CurrencyField()
    
    cumulative_total = models.CurrencyField()
    
    question1_truth = False
    
    question2_truth = False
    
    question3_truth = False

    def question_correct1(self):
        self.question1_truth = (self.question1 != Constants.question_correct)
        return self.question1_truth
        
    def question_correct2(self):
        self.question2_truth = (self.question2 != Constants.question_correct)
        return self.question2_truth
        
    def question_correct3(self):
        if (self.question3 != Constants.question_correct):
        	self.question3_truth = False
        else:
        	self.question3_truth = True
        return self.question3_truth
    
    def accept_payment(self):
    	return self.accept == Constants.typical_response
    
    def cumulative_payoff(self):
    	self.cumulative_total = sum([p.payoff for p in self.in_all_rounds()])
    	return self.cumulative_total