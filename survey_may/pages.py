from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Overview(Page):
	pass

class Survey0(Page):
	form_model = 'player'
	form_fields = [ 'birth_year',
					'sex',
					'gi_m',
					'gi_f',
					'gi_tm',
					'gi_tf',
					'gi_gq',
					'gi_nb',
					'gi_o',
					'gi_other',
					'sexuality',
					'sexuality_other']

	def error_message(self,values):
		if values["gi_o"] and not values["gi_other"]:
			return "If you select 'other' you must state your identity in the field below."
		if not (values["gi_m"] or values["gi_f"] or values["gi_tm"] or values["gi_tf"] or values["gi_gq"] or values["gi_nb"] or values["gi_o"]):
			return "You must select at least one gender identity."
		if values["sexuality"]==3 and not values["sexuality_other"]:
			return "If you select 'other' you must state your sexuality in the field below."

class Survey1(Page):
	template_name = "survey_may/SurveyPage.html"
	form_model = 'player'
	form_fields = ["risk", "gamble"]

class Survey2(Page):
	template_name = "survey_may/SurveyPage.html"
	form_model = 'player'
	form_fields = ["descrim"]

class Survey3(Page):
	def is_displayed(self):
		return self.player.sexuality != 0
	form_model = 'player'
	form_fields = ["so_importance","so_hiding","so_family","so_friends","so_prof"]

page_sequence = [Overview, Survey0, Survey1, Survey2, Survey3]
