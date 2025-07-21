from unittest import TestCase

from utils import format_as_chat


class UtilsTestCase(TestCase):

    def test_format_as_chat(self):
        self.user_message_1 = "Howdy!"
        self.assistant_message_1 = "Hi, how can I help you?"
        self.user_message_2 = "What's the weather today?"
        self.assistant_message_2 = "As an AI, I don't know about wheather."
        self.user_message_3 = "OK"

        self.assertEqual(
            '<|im_start|>user\nHowdy!<|im_end|>\n',
            format_as_chat(self.user_message_1, [])
        )

        self.assertEqual(
            '<|im_start|>user\nHowdy!<|im_end|>\n'
            '<|im_start|>assistant\nHi, how can I help you?<|im_end|>\n'
            '<|im_start|>user\nWhat\'s the weather today?<|im_end|>\n',
            format_as_chat(self.user_message_2, [[self.user_message_1, self.assistant_message_1]])
        )

        self.assertEqual(
            '<|im_start|>user\nHowdy!<|im_end|>\n'
            '<|im_start|>assistant\nHi, how can I help you?<|im_end|>\n'
            '<|im_start|>user\nWhat\'s the weather today?<|im_end|>\n'
            '<|im_start|>assistant\nAs an AI, I don\'t know about wheather.<|im_end|>\n'
            '<|im_start|>user\nOK<|im_end|>\n',
            format_as_chat(self.user_message_3, [[self.user_message_1, self.assistant_message_1], [self.user_message_2, self.assistant_message_2]])
        )
