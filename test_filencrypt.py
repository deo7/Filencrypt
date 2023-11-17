import unittest
from unittest.mock import patch, MagicMock
from filencrypt import contact

class FilencryptTest(unittest.TestCase):
    @patch('filencrypt.DiscordWebhook')
    @patch('filencrypt.Request')
    @patch('filencrypt.urllib.request.urlopen')
    @patch('filencrypt.input')
    @patch('filencrypt.open')
    def test_contact_success(self, mock_open, mock_input, mock_urlopen, mock_request, mock_webhook):
        # Mock the necessary objects and functions
        mock_webhook_instance = MagicMock()
        mock_webhook.return_value = mock_webhook_instance

        mock_request_instance = MagicMock()
        mock_request.return_value = mock_request_instance

        mock_response = MagicMock()
        mock_response.read.return_value = b"Response"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        mock_input.side_effect = ["email@example.com", "Subject", "Message", "n"]

        # Run the function under test
        contact()

        # Assert that the necessary objects and functions were called correctly
        mock_webhook.assert_called_once_with(url="https://discord.com/api/webhooks/908820502343188501/uljt9W1cqtff0PH5ZzAjvZKxTDfPCioFwYwM8WAgRXBPYbLFRCTGdBz5CvAD4_8_Hzcl")
        mock_request.assert_called_once_with(url="https://discord.com/api/webhooks/908820502343188501/uljt9W1cqtff0PH5ZzAjvZKxTDfPCioFwYwM8WAgRXBPYbLFRCTGdBz5CvAD4_8_Hzcl", headers={"User-Agent": "Mozilla/5.0"})
        mock_urlopen.assert_called_once_with(mock_request_instance)
        mock_input.assert_called_with("\nEmail or discord to be contacted : ")
        mock_open.assert_not_called()
        mock_webhook_instance.add_file.assert_not_called()
        mock_webhook_instance.add_embed.assert_called_once()
        mock_webhook_instance.execute.assert_called_once()

    @patch('filencrypt.DiscordWebhook')
    @patch('filencrypt.Request')
    @patch('filencrypt.urllib.request.urlopen')
    @patch('filencrypt.input')
    @patch('filencrypt.open')
    def test_contact_empty_inputs(self, mock_open, mock_input, mock_urlopen, mock_request, mock_webhook):
        # Mock the necessary objects and functions
        mock_webhook_instance = MagicMock()
        mock_webhook.return_value = mock_webhook_instance

        mock_request_instance = MagicMock()
        mock_request.return_value = mock_request_instance

        mock_response = MagicMock()
        mock_response.read.return_value = b"Response"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        mock_input.side_effect = ["", "", "", "n"]

        # Run the function under test
        with self.assertRaises(SystemExit):
            contact()

        # Assert that the necessary objects and functions were called correctly
        mock_webhook.assert_called_once_with(url="https://discord.com/api/webhooks/908820502343188501/uljt9W1cqtff0PH5ZzAjvZKxTDfPCioFwYwM8WAgRXBPYbLFRCTGdBz5CvAD4_8_Hzcl")
        mock_request.assert_called_once_with(url="https://discord.com/api/webhooks/908820502343188501/uljt9W1cqtff0PH5ZzAjvZKxTDfPCioFwYwM8WAgRXBPYbLFRCTGdBz5CvAD4_8_Hzcl", headers={"User-Agent": "Mozilla/5.0"})
        mock_urlopen.assert_called_once_with(mock_request_instance)
        mock_input.assert_called_with("\nEmail or discord to be contacted : ")
        mock_open.assert_not_called()
        mock_webhook_instance.add_file.assert_not_called()
        mock_webhook_instance.add_embed.assert_not_called()
        mock_webhook_instance.execute.assert_not_called()

if __name__ == '__main__':
    unittest.main()