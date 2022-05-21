import	requests
import	os
import logging


class Client:

    #DEBUGING MODES
    DEBUG       = 0
    INFO        = 1
    WARNING     = 2
    ERROR       = 3
    CRITICAL    = 4

    __OKGREEN 	= '\033[92m'
    __FAIL 		= '\033[91m'
    __ENDC 		= '\033[0m'
    login_api   = None
    token_key   = None
    refresh_key = None
    user_key    = None
    token_key   = None
    password_key    = None
    header_token    = None
    logging_level   = [
        logging.basicConfig(level=logging.DEBUG),
        logging.basicConfig(level=logging.INFO),
        logging.basicConfig(level=logging.WARNING),
        logging.basicConfig(level=logging.ERROR),
        logging.basicConfig(level=logging.CRITICAL)
        ]

    def	__init__(self, root):
        self.root = root
        #self.headers = {
        #        "Accept" : "application/json",
        #        "Content-Type" : "application/json",
        #}
        #self.ip             = ip
        #self.port           = port
        #self.token          = ""
        #self.refresh        = ""
        #self.keyset         = {}
        #self.params         = {}
        #self.credentials    = {}
        #self.root           = "http://" + self.ip + ":" + self.port + "/api"

    def	__str__(self):
        prompt = "token: " + self.token + '\n'
        #prompt += "refresh_token: " + self.refresh + '\n'
        #prompt += self.credentials[self.keywords.get("user")] + '\n'
        #prompt += self.credentials[self.keywords.get("password")] + '\n'
        #prompt += "ip: : " + self.ip + '\n'
        #prompt += "login : " + self.keywords.get("login") + '\n'
        #prompt += "Status Code: " + self.status_code + '\n'
        return prompt

    def init(self, user, password):
        self.credentials[self.user_key] = user
        self.credentials[self.password_key] = password
        self.headers[self.header_token] = ""
            
    def check(self):
        self.__http_get(None)

    def	login(self):
        try:
                response = requests.post(self.root + self.login_api, json=self.credentials, headers=self.headers, timeout=10.0)
                self.status_code = str(response.status_code)
                if response.status_code == 200:
                        print(f"{self.__OKGREEN}SUCCESS, SYNC WITH CHIRPSTACK{self.__ENDC}")
                        response = response.json()
                        self.token = response.get(self.token_key)
                        if self.refresh_key:
                            self.refresh = str(response.get("refresh"))
                        self.bearer = "Bearer " + self.token
                        self.headers[self.header_token] = self.bearer
                else:
                        self.__error_log(response)
                        print(self.credentials)
                        print(self.headers)
                        print(self.root + self.login_api)
                return 1
        except Exception as error:
                self.status_code = "502"
                print(self.root + self.login_api)
                print(error)
                print(f"{self.__FAIL}SOMETHING WENT WRONG{self.__ENDC}")
                return 0

    def	__error_log(self, response):
        print(f"{self.__FAIL}SOMETHING WENT WRONG{self.__ENDC}")
        print(response.status_code)

    def get_token(self):
        return self.token

    def get_headers(self):
        return self.headers

    def	get_last_status_code(self):
        return self.status_code

    def	set_params(self, params):
        self.params = params

    def __http_get(self, url, headers=None, params=None):
        if url:
            self.root + url
        self.__handle_requests(requests.get(self.root, headers=headers, params=params))

    def set_logging(self, mode):
        if mode < 5:
            self.logging_level[mode]
        else:
            print("WRONG LOGIGNG MODE!")

    def __handle_requests(self, res):
        if res.status_code != 200:
            logging.WARNING("SOMETHINGS WENT WRONG " + res.status_code)
        self.status_code = res.status_code
