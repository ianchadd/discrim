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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_may'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #custom field maker functions
    def make_check_field(label):
        return models.BooleanField(
            label=label,
            widget=widgets.CheckboxInput,
            initial=False,
            blank=True
            )
    def make_list_field(label,choiceList):
      return models.IntegerField(
        label=label,
        choices = [[x, y] for x, y in enumerate(choiceList)],
        )
    def make_list_radio(label,choiceList):
      return models.IntegerField(
        label=label,
        choices = [[x, y] for x, y in enumerate(choiceList)],
        widget=widgets.RadioSelect
        )

    birth_year = models.IntegerField(label = "1. What is your year of birth?", min=1900, max=2004)
    sex = make_list_field(  "2. What sex were you assigned at birth, on your original birth certificate?", 
                            ["Male","Female"])
    gi_m = make_check_field("Male")
    gi_f = make_check_field("Female")
    gi_tm = make_check_field("Trans Male / Trans Man")
    gi_tf = make_check_field("Trans Female / Trans Woman")
    gi_gq = make_check_field("Genderqueer / Gender non-conforming")
    gi_nb = make_check_field("Nonbinary")
    gi_o = make_check_field("Other (please state below)")
    gi_other = models.StringField(label = "", blank = True)

    sexuality = make_list_field("4. Which do you consider yourself to be?", 
                                ["Heterosexual or straight","Gay or lesbian","Bisexual","Other (please state below)"])
    sexuality_other = models.StringField(label = "", blank = True)


    risk = make_list_field( "5. How do you see yourself: are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?", 
                                ["0 (Not at all willing to take risks)","1","2","3","4","5","6","7","8","9","10 (Very willing to take risks)"] )
    gamble =make_list_radio("6. We will now ask you a hypothetical question. Below is a list of gambles. Which gamble would you want to play?",
                            [ "Lottery 1: gives you $28 for sure",
                            "Lottery 2: gives you either $36 or $24 with equal chance",
                            "Lottery 3: gives you either $44 or $20 with equal chance",
                            "Lottery 4: gives you either $52 or $16 with equal chance",
                            "Lottery 5: gives you either $60 or $12 with equal chance",
                            "Lottery 6: gives you either $70 or $2 with equal chance"])
    descrim = make_list_radio("7. How much discrimination is there in the United States today against LGBTQ+ individuals?",
                                  [ "A great deal",
                                    "A lot",
                                    "A moderate amount",
                                    "A little",
                                    "None at all"])

    so_importance = make_list_radio("8. To what extend do you agree with the following statement: 'My sexual orientation is a very important part of my identity'?",
                                    [ "Strongly Agree",
                                      "Agree",
                                      "Somewhat agree",
                                      "Neutral",
                                      "Somewhat Disagree",
                                      "Disagree",
                                      "Strongly Disagree"])
    so_hiding = make_list_radio("9. Think about your social and professional relationships. Generally speaking, how often do you actively hide signals or information about your sexual orientation?",
                                ["Always",
                                "Often",
                                "Sometimes",
                                "Rarely",
                                "Never"])
    so_family = make_list_radio("10. Thinking about your immediate family members who are still alive, to the best of your knowledge, which of the following statements most closely describes your situation?",
                                ["Everyone in my immediate family knows about my sexual orientation",
                                "Most of my immediate family knows about my sexual orientation",
                                "Some of my immediate family knows about my sexual orientation",
                                "None of my immediate family knows about my sexual orientation"])
    so_friends = make_list_radio("11. Thinking about your friends, to the best of your knowledge, which of the following statements most closely describes your situation?",
                                ["All of my friends know about my sexual orientation",
                                "Most of my friends knows about my sexual orientation",
                                "Some of my friends knows about my sexual orientation",
                                "None of my friends knows about my sexual orientation"])
    so_prof = make_list_radio("12. Think about the people in your professional life. To the best of your knowledge, which of the following statements most closely describes your situation?",
                            ["Everyone in my professional life know about my sexual orientation",
                            "Most people in my professional life knows about my sexual orientation",
                            "Some people in my professional life knows about my sexual orientation",
                            "No one in my professional life knows about my sexual orientation"])