import logging

from pythonosc import udp_client


class VrcOscHandler:

    OSC_ENDPOINT = "/chatbox/input"

    def __init__(self, config):
        """
        :param config: a dict containing 'host'(str) and 'osc_port'(int) for sending messages
        """
        self.config = config
        self.client = udp_client.SimpleUDPClient(self.config['host'], self.config['osc_port'])

    def send_message(self, text: str, immediate=True, notify=True):
        """
        Send the text using OSC protocol to the 'host' and 'port' provided in the config dict.
        :param text: The string of text to send.
        :param immediate: If True, send text immediately, bypassing the keyboard. If False, open the keyboard with the text.
        :param notify: If False, do not trigger the notification SFX. Defaults to True if not specified.
        """
        try:
            self.client.send_message(self.OSC_ENDPOINT, [text, immediate, notify])
        except Exception as e:
            logging.error(e)
