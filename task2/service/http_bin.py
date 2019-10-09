import requests


class HttpBin:
    GET = "get"
    STREAM = "stream/%s"
    POST = "post"
    BASIC_AUTH = "basic-auth/{user}/{password}"
    status_code = None

    def get_response_headers(self, url, headers):
        request_url = url + self.GET
        response = requests.get(request_url, headers=headers)
        self.status_code = response.status_code
        return response.json()['headers']

    def get_response_number_of_lines(self, url, number):
        request_url = (url + self.STREAM) % str(number)
        response = requests.get(request_url, stream=True)
        self.status_code = response.status_code
        number_of_lines = 0
        for line in response.iter_lines():
            number_of_lines += 1
        return number_of_lines

    def is_authentication_successful(
            self, url, correct_login, correct_password, login, password):
        request_url = url + self.BASIC_AUTH.format(
            user=correct_login, password=correct_password)
        response = requests.get(request_url, auth=(login, password))
        self.status_code = response.status_code
        if self.status_code == 200:
            return True
        else:
            return False

    def get_response_params(self, url, params):
        request_url = url + self.POST
        response = requests.post(request_url, params=params)
        self.status_code = response.status_code
        return response.json()['args']

    def get_response_data(self, url, data):
        request_url = url + self.POST
        response = requests.post(request_url, data=data)
        self.status_code = response.status_code
        return response.json()['data']
