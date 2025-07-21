from typing import List

from transformers import pipeline

def format_as_chat(message: str, history: List[List[str]]) -> str:
    """
    Given a message and a history of previous messages, returns a string that formats the conversation as a chat.
    Uses the format expected by SmolLM2-135M-Instruct.

    :param message: A string containing the user's most recent message
    :param history: A list of lists of previous messages, where each sublist is a conversation turn:
        [[user_message1, assistant_reply1], [user_message2, assistant_reply2], ...]
    """
    formatted = ""

    for turn in history:
        if len(turn) == 2:
            user_message, assistant_reply = turn
            formatted += f"<|im_start|>user\n{user_message}<|im_end|>\n"
            formatted += f"<|im_start|>assistant\n{assistant_reply}<|im_end|>\n"
    formatted += f"<|im_start|>user\n{message}<|im_end|>\n"
    return formatted
