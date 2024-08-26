import unittest
from unittest.mock import patch, Mock
from currency_exchanger import CurrencyExchanger

class TestCurrencyExchanger(unittest.TestCase):

    @patch('requests.get')
    def test_currency_exchange_thb_to_krw(self, mock_get):
        # Mock response for the API
        mock_response = Mock()
        expected_json = {'base': 'THB', 'result': {'KRW': 38.69}}
        mock_response.json.return_value = expected_json
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Create an instance of the CurrencyExchanger
        exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")

        # Test the currency_exchange method with a specific amount
        amount_in_thb = 100
        result = exchanger.currency_exchange(amount_in_thb)

        # Calculate the expected result
        expected_result = amount_in_thb * expected_json['result']['KRW']

        # Assert the result is as expected
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()