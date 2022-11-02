import json
import pytest
from unittest.mock import MagicMock, patch

import titan_client
from .test_params import test_params


class TestAPIResponses:
    configuration = titan_client.Configuration()

    @patch('titan_client.rest.RESTClientObject')
    @pytest.mark.parametrize('api_cls_name, method_name, kwargs, filename', test_params.values(), ids=test_params.keys())
    def test_api_responses(self, rest_client_class_mock, api_cls_name, method_name, kwargs, filename):
        rest_client_response = MagicMock()
        rest_client_response.status = 200
        rest_client_response.reason = 'OK'
        rest_client_response.getheader.return_value = 'application/json; charset=utf-8'
        with open(f'fixtures/api_responses/{filename}.json', 'r') as f:
            response = json.load(f)
        rest_client_response.data = json.dumps(response).encode('utf-8')

        rest_client_instance_mock = MagicMock()
        rest_client_instance_mock.GET.return_value = rest_client_response

        rest_client_class_mock.side_effect = [rest_client_instance_mock]

        with titan_client.ApiClient(self.configuration) as api_client:
            api_instance = getattr(titan_client, api_cls_name)(api_client)
            api_response = getattr(api_instance, method_name)(**kwargs)
            assert api_response.to_dict(serialize=True) == response
