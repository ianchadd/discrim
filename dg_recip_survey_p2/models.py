from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django import forms



class Constants(BaseConstants):
    name_in_url = 'dg_recip_survey_p2'
    players_per_group = None #pairs are made ex-post
    guess_template = 'dg_recip_survey_p2/guess_template.html'
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def participant_vars_dump(self, page):
        for field in page.form_fields:
            if type(getattr(self, field)) != type(None):
                self.participant.vars[field +'_'+str(self.round_number)] = getattr(self, field)

    #inferred demographic variables
    inferred_gender = models.StringField(
        label = '',
        choices = ['Male','Female','Trans/Non-Binary/Other'],
        )
    inferred_age = models.StringField(
        label = '',
        choices = ['Under 18','18 - 24','25 - 34', '35 - 44','45 - 54', '55 - 64','65 or Older'],
        )
    inferred_orientation = models.StringField(
        label = '',
        choices = ['Heterosexual or Straight', 'Non-heterosexual or Non-straight'],
        )
    inferred_politics = models.IntegerField(
        label = '',
        choices =
        [
        [5, 'Very Conservative'],
        [4, 'Conservative'],
        [3, 'Equally Liberal and Conservative'],
        [2, 'Liberal'],
        [1, 'Very Liberal'],
        ]
        )

    inferred_ally = models.StringField(
        label = '',
        choices = ['Yes', 'No'],
        )

    #confidence variables
    gender_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    age_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    orientation_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    ally_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    politics_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )

    #explanation variables
    give_explain = models.LongStringField(
        label = '')
    samedifferent_explain = models.LongStringField(
        label = '')

    #own id explanation variables
    id_explain = models.LongStringField(
        label = '')
    icon_explain = models.LongStringField(
        label = '')

    def id_explain_error_message(self,value):
        if len(value)<5:
            return 'Your response to this question must be at least 5 characters long.'

    def icon_explain_error_message(self,value):
        if len(value)<5:
            return 'Your response to this question must be at least 5 characters long.'

    #open ended response
    thoughts = models.LongStringField(
        label ='First of all, what do you think of the study today?')

    #average guesses
    average_guess = models.IntegerField(
        min=0,
        max=100
        )
