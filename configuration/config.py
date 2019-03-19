# -*- coding:utf8 -*-
"""
Configuration Module
"""

import os
import logging
from connector_pmy_api.pmy_enums import Entorno
from enum import Enum


LOGGING_LEVEL = logging.INFO if 'logging_level' not in os.environ else int(os.environ['logging_level'])


class PrimaryAPI:
    USER = os.environ['user_pmy_api']
    PASS = os.environ['pass_pmy_api']
    ENVIRONMENT = Entorno.PROD if 'env_pmy_api' not in os.environ else Entorno(int(os.environ['env_pmy_api']))


class Language(Enum):
    EN = 1
    ES = 2


class Markets(Enum):
    ROFEX = 1
    MATBA = 2


Instrument = {
    'gold': {
        'name': {Language.EN : 'gold', Language.ES : 'oro'},
        'trade_months': [5, 7, 9, 11],
        'initials': 'ORO',
        'market': Markets.ROFEX
    },
    'wti': {
        'name': {Language.EN : 'oil', Language.ES : 'petróleo'},
        'trade_months': [5, 7, 9, 11],
        'initials': 'WTI',
        'market': Markets.ROFEX
    },
    'dolar': {
        'name': {Language.EN : 'dollar', Language.ES : 'dólar'},
        'trade_months': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'initials': 'DO',
        'market': Markets.ROFEX
    },
    'rfx20': {
        'name': {Language.EN : 'rofex index', Language.ES : 'índice rofex'},
        'trade_months': [3, 6, 9, 12],
        'initials': 'RFX20',
        'market': Markets.ROFEX
    },
    'rfx20_spot': {
        'name': {Language.EN: 'ROFEX Index Spot', Language.ES : 'Spot Índice ROFEX'},
        'trade_months': [],
        'initials': 'I.RFX20',
        'market': Markets.ROFEX
    },
    'soy': {
        'name': {Language.EN: 'Soybean', Language.ES: 'Soja'},
        'trade_months': [1, 3, 5, 6, 7, 9, 11],
        'initials': 'MATBA - ELEC - SOJ.ROS/',
        'market': Markets.MATBA,
        'related': ['factory_soy', 'mini_soy', 'soy_index', 'chicago_soy']
    },
    'factory_soy': {
        'name': {Language.EN: 'Factory Soybean', Language.ES: 'Soja Fábrica'},
        'trade_months': [4, 5, 7],
        'initials': 'MATBA - ELEC - SEF.ROS/',
        'market': Markets.MATBA
    },
    'mini_soy': {
        'name': {Language.EN: 'Mini Soybean', Language.ES: 'Soja Mini'},
        'trade_months': [5, 7],
        'initials': 'MATBA - ELEC - SOJ.MIN/',
        'market': Markets.MATBA
    },
    'soy_index': {
        'name': {Language.EN: 'ROSAFE Soybean Index', Language.ES: 'Índice Soja ROSAFÉ'},
        'trade_months': [5, 7],
        'initials': 'MATBA - ELEC - ISR/',
        'market': Markets.MATBA
    },
    'chicago_soy': {
        'name': {Language.EN: 'Chicago Soybean', Language.ES: 'Soja Chicago'},
        'trade_months': [4, 6, 8],
        'initials': 'MATBA - ELEC - SOY.CME/',
        'market': Markets.MATBA
    },
    'corn': {
        'name': {Language.EN: 'Corn', Language.ES: 'Maíz'},
        'trade_months': [3, 4, 6, 7, 9, 12],
        'initials': 'MATBA - ELEC - MAI.ROS/',
        'market': Markets.MATBA,
        'related': ['mini_corn', 'chicago_corn']
    },
    'mini_corn': {
        'name': {Language.EN: 'Mini Corn', Language.ES: 'Maíz Mini'},
        'trade_months': [4, 7],
        'initials': 'MATBA - ELEC - MAI.MIN/',
        'market': Markets.MATBA
    },
    'chicago_corn': {
        'name': {Language.EN: 'Chicago Corn', Language.ES: 'Maíz Chicago'},
        'trade_months': [4, 8],
        'initials': 'MATBA - ELEC - CRN.CME/',
        'market': Markets.MATBA
    },
    'wheat': {
        'name': {Language.EN: 'Wheat', Language.ES: 'Trigo'},
        'trade_months': [1, 3, 4, 7, 10, 12],
        'initials': 'MATBA - ELEC - TRI.ROS/',
        'market': Markets.MATBA,
        'related': ['bs_as_wheat', 'mini_wheat']
    },
    'bs_as_wheat': {
        'name': {Language.EN: 'Buenos Aires Wheat', Language.ES: 'Trigo Buenos Aires'},
        'trade_months': [1, 3, 5, 7, 9],
        'initials': 'MATBA - ELEC - TRI.BA/',
        'market': Markets.MATBA
    },
    'mini_wheat': {
        'name': {Language.EN: 'Mini Wheat', Language.ES: 'Trigo Mini'},
        'trade_months': [7],
        'initials': 'MATBA - ELEC - TRI.MIN/',
        'market': Markets.MATBA
    }
}

Month = {
    '1': {'initials': 'Ene', 'text': {Language.EN : 'January', Language.ES : 'Enero'}},
    '2': {'initials': 'Feb', 'text': {Language.EN : 'February', Language.ES : 'Febrero'}},
    '3': {'initials': 'Mar', 'text': {Language.EN : 'March', Language.ES : 'Marzo'}},
    '4': {'initials': 'Abr', 'text': {Language.EN : 'April', Language.ES : 'Abril'}},
    '5': {'initials': 'May', 'text': {Language.EN : 'May', Language.ES : 'Mayo'}},
    '6': {'initials': 'Jun', 'text': {Language.EN : 'June', Language.ES : 'Junio'}},
    '7': {'initials': 'Jul', 'text': {Language.EN : 'July', Language.ES : 'Julio'}},
    '8': {'initials': 'Ago', 'text': {Language.EN : 'August', Language.ES : 'Agosto'}},
    '9': {'initials': 'Sep', 'text': {Language.EN : 'September', Language.ES : 'Septiembre'}},
    '10': {'initials': 'Oct', 'text': {Language.EN : 'October', Language.ES : 'Octubre'}},
    '11': {'initials': 'Nov', 'text': {Language.EN : 'November', Language.ES : 'Noviembre'}},
    '12': {'initials': 'Dic', 'text': {Language.EN : 'December', Language.ES : 'Diciembre'}},
}

Entries = {
    'last': {'text': {Language.EN: 'Last Price', Language.ES: 'Último Precio'}, 'symbol': 'LA', 'side': 'price'},
    'settle': {'text': {Language.EN: 'Settlement Price', Language.ES: 'Precio de Ajuste'}, 'symbol': 'SE', 'side': 'price'},
    'effec_vol': {'text': {Language.EN: 'Effective Volume', Language.ES: 'Volumen Efectivo'}, 'symbol': 'EV', 'side': 'price'},
    'nom_vol': {'text': {Language.EN: 'Nominal Volume', Language.ES: 'Volumen Nominal'}, 'symbol': 'NV', 'side': 'price'},
    'open_int': {'text': {Language.EN: 'Open Interest', Language.ES: 'Interés Abierto'}, 'symbol': 'OI', 'side': 'size'},
    'default': {'symbol': 'LA,SE'}
}