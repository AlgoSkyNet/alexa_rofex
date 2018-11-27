"""
Configuration Module
"""

from connector_pmy_api.pmy_enums import Entorno


class Primary_API:
    USER = ''
    PASS = ''
    ENVIRONMENT = Entorno.demo

Instrument = {
    'soy': {'last_instrument': 'SNov18', 'last_month': 'november', 'initials': 'S'},
    'gold': {'last_instrument': 'ORONov18', 'last_month': 'november', 'initials': 'ORO'},
    'dolar': {'last_instrument': 'DONov18', 'last_month': 'november', 'initials': 'DO'},
    'rfx20': {'last_instrument': 'RFX20Dic18', 'last_month': 'december', 'initials': 'RFX20'},
    'wti': {'last_instrument': 'WTINov18', 'last_month': 'november', 'initials': 'WTI'}
}

Month = {
    '1': {'initials': 'Ene', 'text': 'january'},
    '2': {'initials': 'Feb', 'text': 'february'},
    '3': {'initials': 'Mar', 'text': 'march'},
    '4': {'initials': 'Abr', 'text': 'april'},
    '5': {'initials': 'May', 'text': 'may'},
    '6': {'initials': 'Jun', 'text': 'june'},
    '7': {'initials': 'Jul', 'text': 'july'},
    '8': {'initials': 'Ago', 'text': 'august'},
    '9': {'initials': 'Sep', 'text': 'september'},
    '10': {'initials': 'Oct', 'text': 'october'},
    '11': {'initials': 'Nov', 'text': 'november'},
    '12': {'initials': 'Dic', 'text': 'december'},
}