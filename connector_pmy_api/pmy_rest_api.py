# coding: utf-8

import requests
import simplejson

from connector_pmy_api.pmy_enums import Entorno
from connector_pmy_api.pmy_exceptions import PMYAPIException


class RestClient:

    # Endpoints
    endpointRestDemo = "http://demo-api.primary.com.ar/"
    endpointRestProd = "https://api.primary.com.ar/"

    def __init__(self, user, password, entorno, account=0):

        self.user = user
        self.password = password
        self.account = account
        self.token = None
        self.islogin = False
        self.initialized = True
        self.marketID = "ROFX"
        self.entorno = entorno

        if self.entorno.value is Entorno.demo.value:
            self.activeEndpoint = RestClient.endpointRestDemo
            self.verify_https = False
        elif self.entorno.value is Entorno.produccion.value:
            self.activeEndpoint = RestClient.endpointRestProd
            self.verify_https = True
        else:
            self.initialized = False
            print("Entorno incorrecto")

    def api_request(self, url):
        if not self.login:
            raise PMYAPIException("Usuario no Autenticado.")
        else:
            headers = {'X-Auth-Token': self.token}
            r = requests.get(url, headers=headers, verify=self.verify_https)
            if r.status_code == 401:
                raise PMYAPIException("Token Invalido.")
            else:
                return simplejson.loads(r.content)

    def instrumentos(self):
        url = self.activeEndpoint + "rest/instruments/all"
        return self.api_request(url)

    def market_data(self, symbol, entries):
        url = self.activeEndpoint + "rest/marketdata/get?marketId={m}&symbol={s}&entries={e}".format(m=self.marketID,s=symbol,e=entries)
        return self.api_request(url)

    def login(self):

        # Validamos que se inicializaron los parametros
        if not self.initialized:
            raise PMYAPIException("Parametros no inicializados.")

        if not self.islogin:
            url = self.activeEndpoint + "auth/getToken"
            headers = {'X-Username': self.user, 'X-Password': self.password}
            login_response = requests.post(url, headers=headers, verify=self.verify_https)

            # Checkeamos si la respuesta del request fue correcta,
            # un ok va a ser un response code 200 (OK)
            if login_response.ok:
                self.token = login_response.headers['X-Auth-Token']
                success = True
            else:
                print("Error al autenticarnos...")
                success = False
            self.islogin = True
        else:
            print("Ya estamos logueados")
            success = True

        return success
        
if __name__ == "__main__":

    from configuration.config import Primary_API

    restClient = RestClient(Primary_API.USER, Primary_API.PASS, Primary_API.ENVIRONMENT)
    is_login = restClient.login()

    print ("¿Estamos logueados a Primary API? " + str(is_login))

    if is_login:
        print(restClient.market_data("DODic18", "BI,OF,LA"))



