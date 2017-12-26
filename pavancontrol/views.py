# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

class Question1(Page):
	def is_displayed(self):
		return self.subsession.round_number == 1
		
	form_model = models.Player
	form_fields = ['question1']
	
	timeout_submission = {'question1': c(Constants.question_correct)}
	
class Question2(Page):
	def is_displayed(self):
		return self.player.question1 != Constants.question_correct and self.subsession.round_number == 1
		
	form_model = models.Player
	form_fields = ['question2']
	
	timeout_submission = {'question2': c(Constants.question_correct)}
	
class Question3(Page):
	def is_displayed(self):
		return (self.player.question2 != Constants.question_correct and self.subsession.round_number == 1 and self.player.question1 != Constants.question_correct)
		
	form_model = models.Player
	form_fields = ['question3']
	
	timeout_submission = {'question3': c(Constants.question_correct)}
	
class Feedback1(Page):

	def is_displayed(self):
		return self.subsession.round_number == 1 and self.player.question1 == Constants.question_correct
		
class Feedback2(Page):

	def is_displayed(self):
		return self.subsession.round_number == 1 and self.player.question2 == Constants.question_correct
		
class Feedback3(Page):

	def is_displayed(self):
		return (self.subsession.round_number == 1 and self.player.question1 != Constants.question_correct and self.player.question2 != Constants.question_correct and self.player.question3 == Constants.question_correct)
		
class Feedback4(Page):

	def is_displayed(self):
		return (self.subsession.round_number == 1 and self.player.question1 != Constants.question_correct and self.player.question2 != Constants.question_correct and self.player.question3 != Constants.question_correct)
		
class TrialRoundResultsWaitPage(WaitPage):

    def is_displayed(self):
    	return self.subsession.round_number == 1
    	
    body_text = "Waiting for other players. The experiment will begin shortly."	

class Introduction(Page):

	def is_displayed(self):
		return self.subsession.round_number == 1

class Contribute1(Page):

	def is_displayed(self):
		return True
	
	def vars_for_template(self):
		return {
			'round_number': self.subsession.round_number
		}
	
	form_model = models.Player
	form_fields = ['contribution']
	timeout_submission = {'contribution': c(Constants.endowment/2)}
    
class FirstResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs1()
        self.group.find_lowest_contribution()
        
    body_text = "Waiting for other players"


class PrivateResults(Page):
	def is_displayed(self):
		return True

class Results_Round_1(Page):
	def is_displayed(self):
		return True
		
	form_model = models.Player
	form_fields = ['accept', 'feedback']
	
	timeout_submission = {'accept': "yes"}
	timeout_submission = {'feedback': ""}
	
	def vars_for_template(self):
	
		return {
            'individual_earnings': self.player.payoff - Constants.endowment + self.player.contribution,
            'player_5_earning': self.group.player_5_earnings,
            'player_4_earning': self.group.player_4_earnings,
            'round_number': self.subsession.round_number
        }
                                        
class SecondResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs2()
        
    body_text = "Waiting for other players"
    
class SecondResults(Page):

	def vars_for_template(self):
	
		return{
			'player_5_earning': self.group.player_5_earnings,
			'player_4_earning': self.group.player_4_earnings,
			'accept_payment_response': self.player.acceptance,
			'player_5_response': self.group.player_5_acceptance,
			'player_4_response': self.group.player_4_acceptance,
			'round_number': self.subsession.round_number,
		}
     
class Player_5_Feedback_Round_3(Page):

	def is_displayed(self):
		return self.group.should_display_warning3() and self.subsession.round_number == 3
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}
		
class Player_5_Feedback_Round_4(Page):

	def is_displayed(self):
		return self.group.should_display_warning4() and self.subsession.round_number == 4
		
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}
		
class Player_5_Feedback_Round_5(Page):

	def is_displayed(self):
		return self.group.should_display_warning5() and self.subsession.round_number == 5
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}

class Player_5_Feedback_Round_6(Page):

	def is_displayed(self):
		return self.group.should_display_warning6() and self.subsession.round_number == 6
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}

class Player_5_Feedback_Round_7(Page):

	def is_displayed(self):
		return self.group.should_display_warning7() and self.subsession.round_number == 7
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}
		
class Player_5_Feedback_Round_8(Page):

	def is_displayed(self):
		return self.group.should_display_warning8() and self.subsession.round_number == 8
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}

class Player_5_Feedback_Round_9(Page):

	def is_displayed(self):
		return self.group.should_display_warning9() and self.subsession.round_number == 9
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}
class Player_5_Feedback_Round_10(Page):

	def is_displayed(self):
		return self.group.should_display_warning10() and self.subsession.round_number == 10
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}
		
class Player_5_Feedback_Round_11(Page):

	def is_displayed(self):
		return self.group.should_display_warning11() and self.subsession.round_number == 11
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}		
		
class Player_5_Feedback_Round_12(Page):

	def is_displayed(self):
		return self.group.should_display_warning12() and self.subsession.round_number == 12
	
	def vars_for_template(self):
		return {
			'amount': self.group.lowest_contribution
		}	
		
class Exit_Survey(Page):

	def is_displayed(self):
		return self.subsession.round_number == 12
	
	form_model = models.Player
	form_fields = ['gender', 'age', 'education', 'income', 'occupation', 'why']
		
class Additional_Questions(Page):

	def is_displayed(self):
		return self.subsession.round_number == 12
	
	form_model = models.Player
	form_fields = ['irritation', 'empathy', 'general_feeling', 'admiration', 'confusion', 'guilt', 'enter_emotion']

class AdditionalQuestionsWaitPage(WaitPage):

    def is_displayed(self):
    	return self.subsession.round_number == 12
    	
    body_text = "Based on the observed behavior of the players in the previous rounds, the experimenter has additional questions to ask this group."	

class Receipt(Page):

	def is_displayed(self):
		return self.subsession.round_number == 12
	
	def vars_for_template(self):
		return {
			'Receipt': self.player.cumulative_payoff,
		}				
page_sequence = [Introduction,
			Question1,
			Question2,
			Question3,
			Feedback1,
			Feedback2,
			Feedback3,
			Feedback4,
			TrialRoundResultsWaitPage,
            Contribute1,
            FirstResultsWaitPage,
			PrivateResults,
            Results_Round_1,
            SecondResultsWaitPage,
            SecondResults,
            Exit_Survey,
            AdditionalQuestionsWaitPage,
            Additional_Questions,
            Receipt]
