from os import environ
import json

if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
    APPS_DEBUG = False
else:
    DEBUG = True
    APPS_DEBUG = True   # also enables random fill in of forms


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
sample_participants = []
with open('sample_participants.json') as sample_participants:
    sample_participants=json.load(sample_participants)
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.50, doc="",
    data_pages_enabled=True,
    sample_participants=sample_participants,
    num_sample_participants=10,
    consent_additional_message = """""",
    round_values = ["1.00"],
    piece_rate = 0.25,
    seconds_for_counting_task=5,
    guess_rate = 0.20,
    delay = False,
    consent_link = False,
    consent_url = 'xxxxx'
)


SESSION_CONFIGS = [
    dict(
        name='qsp_recip',
        display_name="QSP Recipient",
        num_demo_participants=3,
        app_sequence=[
                        'prolific_ID_begin',
                        'informed_consent',
                        'qsp_dg_recip_intro',
                        'qsp_dg_recip_id',
                        'dg_recip_survey',
                        'qsp_dg_recip_id_2',
                        'dg_recip_survey_p2',
                        'survey_demographics_qsp',
                        'feedback_survey',
                        'prolific_ID_end'
                        ],
        participation_fee = 2.00,
        recip = True,
        delay = True,
        consent = 'flag_survey/consent.pdf',
        consent_url = 'https://virtual-experimental-lab.github.io/virtual-experimental-lab.github.io/1932%20IRB%20Approved%20Consent%20Form%208%2018%2020.pdf',
        consent_link = True,
        p_completion_link = 'xxxxxxxx',
    ),
    dict(
        name='qsp_dictator',
        display_name="QSP Dictator",
        num_demo_participants=1,
        pw = 'qsp_testing',
        app_sequence=[
                    'prolific_ID_begin',
                    'informed_consent',
                    'qsp_dg_dict_intro',
                      'qsp_dg_dict_instructions',
                      'dg_qsp',
                      'dg_qsp_survey',
                      'survey_demographics_qsp',
                        'iat_so',
                    'feedback_survey',
                    'prolific_ID_end'
                      ],
        participation_fee = 2.00,
        recip=False,
        delay = True,
        consent = 'flag_survey/consent.pdf',
        consent_url = 'https://virtual-experimental-lab.github.io/virtual-experimental-lab.github.io/1932%20IRB%20Approved%20Consent%20Form%208%2018%2020.pdf',
        consent_link = True,
        p_completion_link = 'xxxxxxxx',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """
    ),
    dict(
        name='Simple_survey_flag',
        display_name="QSP Survey 1",
        num_demo_participants=3,
        app_sequence=['prolific_ID_begin',
                      'simple_survey_flag',
                      'survey_demographics',
                      'prolific_ID_end'],
        participation_fee = 2.00,
        p_completion_link = 'xxxxxxxx',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """ 
    ),
    dict(
        name='Simple_survey_may_22',
        display_name="May Survey",
        num_demo_participants=3,
        app_sequence=['prolific_ID_begin',
                      'informed_consent',
                      'survey_may',
                      'prolific_ID_end'],
        p_completion_link = 'xxxxxxxx',
        consent = 'flag_survey/consent.pdf',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """ 
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(name='prolific_qsp', display_name='Prolific Room for QSP (no participant labels)'),
    dict(
        name='rpi_lab',
        display_name='RPI Virtual Econ Laboratory'
    ),
    dict(
        name='rpi_lab_qsp_1',
        display_name='RPI Virtual Econ Laboratory: QSP 1'
    ),
    dict(
        name='rpi_lab_qsp_2',
        display_name='RPI Virtual Econ Laboratory: QSP 2'
    ),
    dict(
        name='rpi_lab_qsp_3',
        display_name='RPI Virtual Econ Laboratory: QSP 3'
    ),
    dict(
        name='rpi_lab_qsp_4',
        display_name='RPI Virtual Econ Laboratory: QSP 4'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""
# extra settings for otreeutils
# ROOT_URLCONF = 'iat_so.urls'
# CHANNEL_ROUTING = 'iat_so.routing.channel_routing'
# don't share this with anybody.
SECRET_KEY = '7vfsh(zo@d)v)zizkf#@xqzb3q%juzu65zoh4r+#$tckdfji5r'

INSTALLED_APPS = ['otree',
                  'custom_templates',
                  'django.contrib.humanize',
                  'otreeutils'
                  ]
EXTENSION_APPS = ['slider_puzzle']
# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
