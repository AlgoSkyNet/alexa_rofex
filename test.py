import unittest
import inspect
from alexa_handlers.AlexaBaseHandler import AlexaBaseHandler
from alexa_handlers.AlexaForRFXHandler import AlexaForRFXHandler

class TestAlexaHandler(AlexaBaseHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def on_launch(self, launch_request, session):
        print(inspect.stack()[0][3])

    def on_session_started(self, session_started_request, session):
        print(inspect.stack()[0][3])

    def on_intent(self, intent_request, session):
        print(inspect.stack()[0][3])

    def on_session_ended(self, session_end_request, session):
        print(inspect.stack()[0][3])


class AlexaParticleTests(unittest.TestCase):

    def test_1(self):
        event = {
                    "version": "1.0",
                    "session": {
                        "new": False,
                        "sessionId": "amzn1.echo-api.session.e743fabc-399d-4983-b8d8-7a740246f37d",
                        "application": {
                            "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                        },
                        "user": {
                            "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                        }
                    },
                    "context": {
                        "System": {
                            "application": {
                                "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                            },
                            "user": {
                                "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                            },
                            "device": {
                                "deviceId": "amzn1.ask.device.AE4TFO23PLFLM25D3QZGWH74J2PBEWQO5LMS4DAG4IN4GAOAT7AKKZCDXYXO3MNLF2IPEA5GZIRXZTB2F6FEISMCQEHDLXR5KXWPMY4JCMMX6KJXH6AY3LQGUBOJ2JNUFJMYJK7BDMCME56W4SZTK52T6BYQ",
                                "supportedInterfaces": {}
                            },
                            "apiEndpoint": "https://api.amazonalexa.com",
                            "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjA3ZjczODU4LWQ5ZmItNDNhMC04OWI1LWFiMTdlNmYzYTY2MiIsImV4cCI6MTUzNzkwNjQ5MywiaWF0IjoxNTM3OTAyODkzLCJuYmYiOjE1Mzc5MDI4OTMsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU0VEZPMjNQTEZMTTI1RDNRWkdXSDc0SjJQQkVXUU81TE1TNERBRzRJTjRHQU9BVDdBS0taQ0RYWVhPM01OTEYySVBFQTVHWklSWFpUQjJGNkZFSVNNQ1FFSERMWFI1S1hXUE1ZNEpDTU1YNktKWEg2QVkzTFFHVUJPSjJKTlVGSk1ZSks3QkRNQ01FNTZXNFNaVEs1MlQ2QllRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUhaSFJORDNNQVhXNEU3UFhCWFdISkk2SFpGTTVBUVpGVlFBUVc1NEJZWU1SWTNTVk1DT0RIUlhVNEVBWlhGUFRWTjJITDJOVVFMVldOQTM0QTVUUlBIUUtESlNCWk1CRExGQzJBS0k0M1RMRExWUkw0WEVGUFdCR1VLQ041UzNENEdTT0dHVVI1WVlaRk8yQjIzSlNFSkRDRkozU0s3R0NLVDJIRE5NTVJVMlBTUjNQTTQyM1FWRURUTERMSEdXNlNNNjJaWlhWRUZJSVNRIn19.If8q3WKCilT2g8WukhhOhA57w4jMP4GegSHnvVMC4otNnG7anhc2d5aK8oiSClIV12HTAScvbjM-4q4CKlAlLeIY2LzxWd3BF5dFspLWJhGlQJVc_vv1ZQ8V2lsJP8cRv3_k3qU-CiR4FVzmqY3K-IHlZrYsvJBxbd_-4XhO7wLYNLvkyaznOBRSmVeUos4II1VkWsn1KqtQx7dxD1eTp_IQgLa0UquTjkUghLX4lTF0lkx9KyGAH0Stgk88JXTwVO7y8qQ3LkPE9uYp0YEQlcuJFAk4kXczhBpDoiBKRFKQotZvAGPcvCt9eqWdx68xbv9kW1ic7tj3Ls01tidjhw"
                        }
                    },
                    "request": {
                        "type": "IntentRequest",
                        "requestId": "amzn1.echo-api.request.5848877b-d03c-4da8-bee1-a4d14904165f",
                        "timestamp": "2018-09-25T19:14:53Z",
                        "locale": "en-US",
                        "intent": {
                            "name": "LastPriceIntent",
                            "confirmationStatus": "NONE",
                            "slots": {
                                "Product": {
                                    "name": "Producto",
                                    "value": "dolar",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.PRODUCT_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "dolar",
                                                            "id": "dolar"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                },
                                "Mes": {
                                    "name": "Mes",
                                    "value": "September",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.MONTH_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "september",
                                                            "id": "9"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                }
                            }
                        }
                    }
                }

        alexa = AlexaForRFXHandler()
        alexa.process_request(event, None)

    def test_2(self):
        event = {
            "version": "1.0",
            "session": {
                "new": False,
                "sessionId": "amzn1.echo-api.session.e743fabc-399d-4983-b8d8-7a740246f37d",
                "application": {
                    "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                },
                "user": {
                    "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                }
            },
            "context": {
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                    },
                    "device": {
                        "deviceId": "amzn1.ask.device.AE4TFO23PLFLM25D3QZGWH74J2PBEWQO5LMS4DAG4IN4GAOAT7AKKZCDXYXO3MNLF2IPEA5GZIRXZTB2F6FEISMCQEHDLXR5KXWPMY4JCMMX6KJXH6AY3LQGUBOJ2JNUFJMYJK7BDMCME56W4SZTK52T6BYQ",
                        "supportedInterfaces": {}
                    },
                    "apiEndpoint": "https://api.amazonalexa.com",
                    "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjA3ZjczODU4LWQ5ZmItNDNhMC04OWI1LWFiMTdlNmYzYTY2MiIsImV4cCI6MTUzNzkwNjMzMSwiaWF0IjoxNTM3OTAyNzMxLCJuYmYiOjE1Mzc5MDI3MzEsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU0VEZPMjNQTEZMTTI1RDNRWkdXSDc0SjJQQkVXUU81TE1TNERBRzRJTjRHQU9BVDdBS0taQ0RYWVhPM01OTEYySVBFQTVHWklSWFpUQjJGNkZFSVNNQ1FFSERMWFI1S1hXUE1ZNEpDTU1YNktKWEg2QVkzTFFHVUJPSjJKTlVGSk1ZSks3QkRNQ01FNTZXNFNaVEs1MlQ2QllRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUhaSFJORDNNQVhXNEU3UFhCWFdISkk2SFpGTTVBUVpGVlFBUVc1NEJZWU1SWTNTVk1DT0RIUlhVNEVBWlhGUFRWTjJITDJOVVFMVldOQTM0QTVUUlBIUUtESlNCWk1CRExGQzJBS0k0M1RMRExWUkw0WEVGUFdCR1VLQ041UzNENEdTT0dHVVI1WVlaRk8yQjIzSlNFSkRDRkozU0s3R0NLVDJIRE5NTVJVMlBTUjNQTTQyM1FWRURUTERMSEdXNlNNNjJaWlhWRUZJSVNRIn19.hDxcppzQUlJzHnw2kz7D2Yv23oMFuFZ65-yKGVrgaNMPEl1XkmWZ77CCqaq1ZphUhh7KZ6TlnqVwbAB3UqP-nQGxuZvxwBFa4gsKYP7dIP9wN8r0HJEt8YBzIm8FT1kR9hsfPhYbi4mHvk6JdI-nz67DlElplvn6XgJ3Ia-1gTRu5ozPwOWHcvbeX-7BTIHSWsnTBpE2QQBlip7cPFfJoxo_llo3fNglOX05CZ0XjlKQesaQ5rL90mjDuuLnaG4cNzFLRSURMJn6c3B8NiCFP8Z54yGHmcujaZZQPUoL59Fl5DF5SjWbIex4CYau431_qRnnAQChlvwIqE4WqAhz4Q"
                }
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "amzn1.echo-api.request.d25b817d-805c-435e-a927-1f5c1b41604e",
                "timestamp": "2018-09-25T19:12:11Z",
                "locale": "en-US",
                "intent": {
                    "name": "LastPriceIntent",
                    "confirmationStatus": "NONE",
                    "slots": {
                        "Product": {
                            "name": "Producto",
                            "value": "dolar",
                            "resolutions": {
                                "resolutionsPerAuthority": [
                                    {
                                        "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.PRODUCT_TYPE",
                                        "status": {
                                            "code": "ER_SUCCESS_MATCH"
                                        },
                                        "values": [
                                            {
                                                "value": {
                                                    "name": "dolar",
                                                    "id": "dolar"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            "confirmationStatus": "NONE"
                        },
                        "Mes": {
                            "name": "Mes",
                            "confirmationStatus": "NONE"
                        }
                    }
                }
            }
        }

        alexa = AlexaForRFXHandler()
        alexa.process_request(event, None)

    def test_3(self):
        event = {
                    "version": "1.0",
                    "session": {
                        "new": False,
                        "sessionId": "amzn1.echo-api.session.86858c68-11e4-4aad-a19f-13e3a01385e7",
                        "application": {
                            "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                        },
                        "user": {
                            "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                        }
                    },
                    "context": {
                        "System": {
                            "application": {
                                "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                            },
                            "user": {
                                "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                            },
                            "device": {
                                "deviceId": "amzn1.ask.device.AE4TFO23PLFLM25D3QZGWH74J2PBEWQO5LMS4DAG4IN4GAOAT7AKKZCDXYXO3MNLF2IPEA5GZIRXZTB2F6FEISMCQEHDLXR5KXWPMY4JCMMX6KJXH6AY3LQGUBOJ2JNUFJMYJK7BDMCME56W4SZTK52T6BYQ",
                                "supportedInterfaces": {}
                            },
                            "apiEndpoint": "https://api.amazonalexa.com",
                            "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjA3ZjczODU4LWQ5ZmItNDNhMC04OWI1LWFiMTdlNmYzYTY2MiIsImV4cCI6MTUzNzkwNjY3MywiaWF0IjoxNTM3OTAzMDczLCJuYmYiOjE1Mzc5MDMwNzMsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU0VEZPMjNQTEZMTTI1RDNRWkdXSDc0SjJQQkVXUU81TE1TNERBRzRJTjRHQU9BVDdBS0taQ0RYWVhPM01OTEYySVBFQTVHWklSWFpUQjJGNkZFSVNNQ1FFSERMWFI1S1hXUE1ZNEpDTU1YNktKWEg2QVkzTFFHVUJPSjJKTlVGSk1ZSks3QkRNQ01FNTZXNFNaVEs1MlQ2QllRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUhaSFJORDNNQVhXNEU3UFhCWFdISkk2SFpGTTVBUVpGVlFBUVc1NEJZWU1SWTNTVk1DT0RIUlhVNEVBWlhGUFRWTjJITDJOVVFMVldOQTM0QTVUUlBIUUtESlNCWk1CRExGQzJBS0k0M1RMRExWUkw0WEVGUFdCR1VLQ041UzNENEdTT0dHVVI1WVlaRk8yQjIzSlNFSkRDRkozU0s3R0NLVDJIRE5NTVJVMlBTUjNQTTQyM1FWRURUTERMSEdXNlNNNjJaWlhWRUZJSVNRIn19.Z7zJqQw8JkJUtf8zWFwYg5aH1GwdN-uxCCzBIOul9WRNEwfPIPrYBq-xmYNuCLfje7QYdQfz6VUFMIRuNZqSoJLJV8YxhW30LCitAZbDOPkX4wlRSXRKlmg35aAF_URDbuNov4lk3o9KtdoekHGvVJ4RLshkwYlj2ccJwaaVVv18n_PSelfvtAdxflsMYunvkqvWnx_rIbBy2dpzO7fUTIRlr05-OwrOnFTV3LSonMU-x6LArLb2Oml24NTRnA3gsuu3P_EW73whXmASbnLzPx3zPX0x1ne2cXp3rBgkF42OCE_xbHmn2IuiuxcEUtWc2P2_8YDLKUDQQQtpETghng"
                        }
                    },
                    "request": {
                        "type": "IntentRequest",
                        "requestId": "amzn1.echo-api.request.a49d7d74-10dd-42e8-981b-5e842302de80",
                        "timestamp": "2018-09-25T19:17:53Z",
                        "locale": "en-US",
                        "intent": {
                            "name": "LastPriceIntent",
                            "confirmationStatus": "NONE",
                            "slots": {
                                "Product": {
                                    "name": "Producto",
                                    "value": "dolar",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.PRODUCT_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "dolar",
                                                            "id": "dolar"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                },
                                "Mes": {
                                    "name": "Mes",
                                    "confirmationStatus": "NONE"
                                }
                            }
                        }
                    }
                }

        alexa = AlexaForRFXHandler()
        alexa.process_request(event, None)

    def test_4(self):
        event = {
                    "version": "1.0",
                    "session": {
                        "new": False,
                        "sessionId": "amzn1.echo-api.session.0b674d45-f877-48c0-9308-099d62db6f3a",
                        "application": {
                            "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                        },
                        "user": {
                            "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                        }
                    },
                    "context": {
                        "System": {
                            "application": {
                                "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                            },
                            "user": {
                                "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                            },
                            "device": {
                                "deviceId": "amzn1.ask.device.AE4TFO23PLFLM25D3QZGWH74J2PBEWQO5LMS4DAG4IN4GAOAT7AKKZCDXYXO3MNLF2IPEA5GZIRXZTB2F6FEISMCQEHDLXR5KXWPMY4JCMMX6KJXH6AY3LQGUBOJ2JNUFJMYJK7BDMCME56W4SZTK52T6BYQ",
                                "supportedInterfaces": {}
                            },
                            "apiEndpoint": "https://api.amazonalexa.com",
                            "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjA3ZjczODU4LWQ5ZmItNDNhMC04OWI1LWFiMTdlNmYzYTY2MiIsImV4cCI6MTUzODE1MjcxMCwiaWF0IjoxNTM4MTQ5MTEwLCJuYmYiOjE1MzgxNDkxMTAsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU0VEZPMjNQTEZMTTI1RDNRWkdXSDc0SjJQQkVXUU81TE1TNERBRzRJTjRHQU9BVDdBS0taQ0RYWVhPM01OTEYySVBFQTVHWklSWFpUQjJGNkZFSVNNQ1FFSERMWFI1S1hXUE1ZNEpDTU1YNktKWEg2QVkzTFFHVUJPSjJKTlVGSk1ZSks3QkRNQ01FNTZXNFNaVEs1MlQ2QllRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUhaSFJORDNNQVhXNEU3UFhCWFdISkk2SFpGTTVBUVpGVlFBUVc1NEJZWU1SWTNTVk1DT0RIUlhVNEVBWlhGUFRWTjJITDJOVVFMVldOQTM0QTVUUlBIUUtESlNCWk1CRExGQzJBS0k0M1RMRExWUkw0WEVGUFdCR1VLQ041UzNENEdTT0dHVVI1WVlaRk8yQjIzSlNFSkRDRkozU0s3R0NLVDJIRE5NTVJVMlBTUjNQTTQyM1FWRURUTERMSEdXNlNNNjJaWlhWRUZJSVNRIn19.TCbNLXQYHpe_krtiDTaaMX1yPAymn84kwJ4jaZ-SWH6Co8bOHu0YNXm4CfhcgZKpiHhkOpbuhDCJ1rvyxUAGzD9NQXwJRp-CtErm9u_u8ain0bKZzI99-zbTafPk5xwOukD7OgxKR7-KT6paKBLYR79nu-Pk3Kx-ORKXcK2PssCwzfHP3LDfgF9Z6Us9UqUqwO0CWjNIgdc2gcGqQGuMveh7nf57sTpSKXhws-WT184abmtPZXhhAmRcvvhSXQJnkptAeE3UxSjaVpQoiV5JDNMqg3pjXWU0C_WqwtmvEi5QJfRYwkc5Kqhdq-QfBED9qMn6a0jHUSyrLitEFl0zhg"
                        }
                    },
                    "request": {
                        "type": "IntentRequest",
                        "requestId": "amzn1.echo-api.request.1fc5b906-148b-4c52-a281-9214a4fc679e",
                        "timestamp": "2018-09-28T15:38:30Z",
                        "locale": "en-US",
                        "intent": {
                            "name": "LastPriceIntent",
                            "confirmationStatus": "NONE",
                            "slots": {
                                "Product": {
                                    "name": "Producto",
                                    "value": "gold",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.PRODUCT_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "gold",
                                                            "id": "gold"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                },
                                "Mes": {
                                    "name": "Mes",
                                    "value": "January",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.MONTH_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "january",
                                                            "id": "1"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                }
                            }
                        }
                    }
                }


        alexa = AlexaForRFXHandler()
        alexa.process_request(event, None)

    def test_5(self):
        event = {
                    "version": "1.0",
                    "session": {
                        "new": False,
                        "sessionId": "amzn1.echo-api.session.35d0b2cc-5d62-4843-8a50-6f61e9e9a4f7",
                        "application": {
                            "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                        },
                        "user": {
                            "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                        }
                    },
                    "context": {
                        "System": {
                            "application": {
                                "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                            },
                            "user": {
                                "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                            },
                            "device": {
                                "deviceId": "amzn1.ask.device.AE4TFO23PLFLM25D3QZGWH74J2PBEWQO5LMS4DAG4IN4GAOAT7AKKZCDXYXO3MNLF2IPEA5GZIRXZTB2F6FEISMCQEHDLXR5KXWPMY4JCMMX6KJXH6AY3LQGUBOJ2JNUFJMYJK7BDMCME56W4SZTK52T6BYQ",
                                "supportedInterfaces": {}
                            },
                            "apiEndpoint": "https://api.amazonalexa.com",
                            "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjA3ZjczODU4LWQ5ZmItNDNhMC04OWI1LWFiMTdlNmYzYTY2MiIsImV4cCI6MTUzODE1MzAwMywiaWF0IjoxNTM4MTQ5NDAzLCJuYmYiOjE1MzgxNDk0MDMsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU0VEZPMjNQTEZMTTI1RDNRWkdXSDc0SjJQQkVXUU81TE1TNERBRzRJTjRHQU9BVDdBS0taQ0RYWVhPM01OTEYySVBFQTVHWklSWFpUQjJGNkZFSVNNQ1FFSERMWFI1S1hXUE1ZNEpDTU1YNktKWEg2QVkzTFFHVUJPSjJKTlVGSk1ZSks3QkRNQ01FNTZXNFNaVEs1MlQ2QllRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUhaSFJORDNNQVhXNEU3UFhCWFdISkk2SFpGTTVBUVpGVlFBUVc1NEJZWU1SWTNTVk1DT0RIUlhVNEVBWlhGUFRWTjJITDJOVVFMVldOQTM0QTVUUlBIUUtESlNCWk1CRExGQzJBS0k0M1RMRExWUkw0WEVGUFdCR1VLQ041UzNENEdTT0dHVVI1WVlaRk8yQjIzSlNFSkRDRkozU0s3R0NLVDJIRE5NTVJVMlBTUjNQTTQyM1FWRURUTERMSEdXNlNNNjJaWlhWRUZJSVNRIn19.cxKfHjpM6MSKs1go31ADluKgfyZQbJnuXC8JVzz6AbBck6pAsXWil1kXSsPuxte4i8r13dpKdA6HNBKZKccGesiEAjyclDYSWA6K7DEI9LgTmm7mvgHCSvepfRe9PMLDAoYCma9Wki1krWz-C0-E6kpPu5HbMiLtZ1erEcIadydP28aQzeOrjttyC5B63OyUNexZ7W-5ZiGhtQ4xS1Jz6l8PX0Lyfo0J4EgHGMcWWwxAGQ23EI4kr8bJLmIHhLudm90IflP3zvVhpfeS72HsvLd47Kcu4Z5p57ouIdQB3GaEI3SWIZiR0H2iu96i0Xf5g06bLBqsKOZlxrC-j0drQg"
                        }
                    },
                    "request": {
                        "type": "IntentRequest",
                        "requestId": "amzn1.echo-api.request.4713bcb8-0b20-423a-b21d-a32b4df58a4e",
                        "timestamp": "2018-09-28T15:43:23Z",
                        "locale": "en-US",
                        "intent": {
                            "name": "LastPriceIntent",
                            "confirmationStatus": "NONE",
                            "slots": {
                                "Product": {
                                    "name": "Producto",
                                    "value": "oil",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.PRODUCT_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "oil",
                                                            "id": "wti"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                },
                                "Mes": {
                                    "name": "Mes",
                                    "value": "January",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.MONTH_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "january",
                                                            "id": "1"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                }
                            }
                        }
                    }
                }

        alexa = AlexaForRFXHandler()
        alexa.process_request(event, None)

    def test_6(self):

        event = {
                    "version": "1.0",
                    "session": {
                        "new": False,
                        "sessionId": "amzn1.echo-api.session.cfe6236b-c821-4fa5-b739-e9a21b4b8cbc",
                        "application": {
                            "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                        },
                        "user": {
                            "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                        }
                    },
                    "context": {
                        "System": {
                            "application": {
                                "applicationId": "amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662"
                            },
                            "user": {
                                "userId": "amzn1.ask.account.AHZHRND3MAXW4E7PXBXWHJI6HZFM5AQZFVQAQW54BYYMRY3SVMCODHRXU4EAZXFPTVN2HL2NUQLVWNA34A5TRPHQKDJSBZMBDLFC2AKI43TLDLVRL4XEFPWBGUKCN5S3D4GSOGGUR5YYZFO2B23JSEJDCFJ3SK7GCKT2HDNMMRU2PSR3PM423QVEDTLDLHGW6SM62ZZXVEFIISQ"
                            },
                            "device": {
                                "deviceId": "amzn1.ask.device.AE4TFO23PLFLM25D3QZGWH74J2PBEWQO5LMS4DAG4IN4GAOAT7AKKZCDXYXO3MNLF2IPEA5GZIRXZTB2F6FEISMCQEHDLXR5KXWPMY4JCMMX6KJXH6AY3LQGUBOJ2JNUFJMYJK7BDMCME56W4SZTK52T6BYQ",
                                "supportedInterfaces": {}
                            },
                            "apiEndpoint": "https://api.amazonalexa.com",
                            "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjA3ZjczODU4LWQ5ZmItNDNhMC04OWI1LWFiMTdlNmYzYTY2MiIsImV4cCI6MTUzODE1MzMxOSwiaWF0IjoxNTM4MTQ5NzE5LCJuYmYiOjE1MzgxNDk3MTksInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU0VEZPMjNQTEZMTTI1RDNRWkdXSDc0SjJQQkVXUU81TE1TNERBRzRJTjRHQU9BVDdBS0taQ0RYWVhPM01OTEYySVBFQTVHWklSWFpUQjJGNkZFSVNNQ1FFSERMWFI1S1hXUE1ZNEpDTU1YNktKWEg2QVkzTFFHVUJPSjJKTlVGSk1ZSks3QkRNQ01FNTZXNFNaVEs1MlQ2QllRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUhaSFJORDNNQVhXNEU3UFhCWFdISkk2SFpGTTVBUVpGVlFBUVc1NEJZWU1SWTNTVk1DT0RIUlhVNEVBWlhGUFRWTjJITDJOVVFMVldOQTM0QTVUUlBIUUtESlNCWk1CRExGQzJBS0k0M1RMRExWUkw0WEVGUFdCR1VLQ041UzNENEdTT0dHVVI1WVlaRk8yQjIzSlNFSkRDRkozU0s3R0NLVDJIRE5NTVJVMlBTUjNQTTQyM1FWRURUTERMSEdXNlNNNjJaWlhWRUZJSVNRIn19.bd_JVCpUMbypAD-m-yIQjpXX-FGBFDgh9Xovm0WSGlBDe6zYVEi_MS_yiXdgs1XlP5UQsXOJq1_McmrmH3B21vTkPvNY_h-h_vDvsDTeYJWY0yYm2lDI7zVIcvj_Q1m4GTGYYwqBEt9Tepv4g_aRJJKW8wDXcplJtojER77Wi2W-_V7Hrrhpk-Q0uins5SQQrJzwh3em7OYvT1IR-OaRimqazqkLU_n5ctPGuVarkF6L8lOQNuRHeZjURdQtascy-Os6SP9adGH9M7Fangxr_ow66T27Gwbf0D-qpV6ffKw3UHVww_AlDSg3coFfft5uIxYxy-9117CXeWNhGeikJQ"
                        }
                    },
                    "request": {
                        "type": "IntentRequest",
                        "requestId": "amzn1.echo-api.request.31d59d54-0a78-4857-b501-52638e568912",
                        "timestamp": "2018-09-28T15:48:39Z",
                        "locale": "en-US",
                        "intent": {
                            "name": "LastPriceIntent",
                            "confirmationStatus": "NONE",
                            "slots": {
                                "Product": {
                                    "name": "Producto",
                                    "value": "dolar",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.PRODUCT_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "dolar",
                                                            "id": "dolar"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                },
                                "Mes": {
                                    "name": "Mes",
                                    "value": "june",
                                    "resolutions": {
                                        "resolutionsPerAuthority": [
                                            {
                                                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.07f73858-d9fb-43a0-89b5-ab17e6f3a662.MONTH_TYPE",
                                                "status": {
                                                    "code": "ER_SUCCESS_MATCH"
                                                },
                                                "values": [
                                                    {
                                                        "value": {
                                                            "name": "june",
                                                            "id": "6"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "confirmationStatus": "NONE"
                                }
                            }
                        }
                    }
                }

        alexa = AlexaForRFXHandler()
        alexa.process_request(event, None)
