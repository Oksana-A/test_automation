import pytest

from service.http_bin import HttpBin
from utils.config_reader import ConfigReader


class TestHttpBin:
    http_bin = HttpBin()
    success_code = 200

    def test_headers_presence(self):
        headers = self.http_bin.get_response_headers(
            ConfigReader.get_inst().service_url,
            ConfigReader.get_inst().headers)
        assert self.http_bin.status_code == self.success_code
        keys = ConfigReader.get_inst().headers.keys()
        for key in keys:
            assert ConfigReader.get_inst().headers.get(key) \
                   == headers.get(key.title())

    @pytest.mark.parametrize('number', [50, 150])
    def test_number_of_returned_lines(self, number):
        resulting_number = self.http_bin.get_response_number_of_lines(
            ConfigReader.get_inst().service_url, number)
        assert self.http_bin.status_code == self.success_code
        assert resulting_number >= number

    @pytest.mark.parametrize(
        'login_and_password',
        [ConfigReader.get_inst().valid_login_and_password,
         ConfigReader.get_inst().invalid_login_and_password])
    def test_authentication(self, login_and_password):
        assert self.http_bin.is_authentication_successful(
            ConfigReader.get_inst().service_url,
            ConfigReader.get_inst().valid_login_and_password["login"],
            ConfigReader.get_inst().valid_login_and_password["password"],
            login_and_password["login"],
            login_and_password["password"]) is True
        assert self.http_bin.status_code == self.success_code

    def test_params_presence(self):
        params = self.http_bin.get_response_params(
            ConfigReader.get_inst().service_url,
            ConfigReader.get_inst().params)
        assert self.http_bin.status_code == self.success_code
        keys = ConfigReader.get_inst().params.keys()
        for key in keys:
            assert ConfigReader.get_inst().params.get(key) == params.get(key)

    def test_data_presence(self):
        data = self.http_bin.get_response_data(
            ConfigReader.get_inst().service_url, ConfigReader.get_inst().data)
        assert self.http_bin.status_code == self.success_code
        assert ConfigReader.get_inst().data == data
