# -*- coding:utf8 -*-
"""
Configuration Module
"""

from connector_pmy_api.pmy_enums import Entorno
from enum import Enum
import os


class Primary_API:
    USER = os.environ['user_pmy_api']
    PASS = os.environ['pass_pmy_api']
    ENVIRONMENT = Entorno.produccion


class Language(Enum):
    EN = 1
    ES = 2

Instrument = {
    'soy': {
        'name': {Language.EN : 'soy', Language.ES : 'soja'},
        'trade_months': [5, 11],
        'initials': 'S'
    },
    'gold': {
        'name': {Language.EN : 'gold', Language.ES : 'oro'},
        'trade_months': [3, 5, 7, 9, 11],
        'initials': 'ORO'
    },
    'wti': {
        'name': {Language.EN : 'oil', Language.ES : 'petróleo'},
        'trade_months': [3, 5, 7, 9, 11],
        'initials': 'WTI'
    },
    'dolar': {
        'name': {Language.EN : 'dollar', Language.ES : 'dólar'},
        'trade_months': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'initials': 'DO'
    },
    'rfx20': {
        'name': {Language.EN : 'rofex index', Language.ES : 'índice rofex'},
        'trade_months': [3, 6, 9, 12],
        'initials': 'RFX20'
    }
}

Month = {
    '1': {'initials': 'Ene', 'text': {Language.EN : 'january', Language.ES : 'enero'}},
    '2': {'initials': 'Feb', 'text': {Language.EN : 'february', Language.ES : 'febrero'}},
    '3': {'initials': 'Mar', 'text': {Language.EN : 'march', Language.ES : 'marzo'}},
    '4': {'initials': 'Abr', 'text': {Language.EN : 'april', Language.ES : 'abril'}},
    '5': {'initials': 'May', 'text': {Language.EN : 'may', Language.ES : 'mayo'}},
    '6': {'initials': 'Jun', 'text': {Language.EN : 'june', Language.ES : 'junio'}},
    '7': {'initials': 'Jul', 'text': {Language.EN : 'july', Language.ES : 'julio'}},
    '8': {'initials': 'Ago', 'text': {Language.EN : 'august', Language.ES : 'agosto'}},
    '9': {'initials': 'Sep', 'text': {Language.EN : 'september', Language.ES : 'septiembre'}},
    '10': {'initials': 'Oct', 'text': {Language.EN : 'october', Language.ES : 'octubre'}},
    '11': {'initials': 'Nov', 'text': {Language.EN : 'november', Language.ES : 'noviembre'}},
    '12': {'initials': 'Dic', 'text': {Language.EN : 'december', Language.ES : 'diciembre'}},
}

