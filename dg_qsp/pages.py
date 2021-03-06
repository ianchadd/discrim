from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        task_2 = self.round_number == 1
        task_3 = not task_2
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            task_2 = task_2,
            task_3 = task_3,
            #my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            #my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(pvars),
            task = task,
            part = part
        )


class Offer(Page):
    form_model = 'player'
    form_fields = ['gave']
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        task_2 = self.round_number == 1
        task_3 = not task_2
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            task_2 = task_2,
            task_3 = task_3,
            #my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            #my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(pvars),
            task = task,
            part = part
        )

    def before_next_page(self):
        self.player.set_payoffs()
        self.player.participant_vars_dump(self)
        self.participant.vars['task'] += 1
'''
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )
'''

class Results(Page):
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'        
        return dict(
            #my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            #my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(self.participant.vars)
        )



page_sequence = [Introduction,
                 Offer,
                 #ResultsWaitPage,
                 #Results
                 ]
