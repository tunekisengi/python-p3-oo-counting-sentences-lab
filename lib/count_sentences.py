import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    # -------------------------
    # Sentence type checks
    # -------------------------
    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    # -------------------------
    # Sentence counter
    # -------------------------
    def count_sentences(self):
        cleaned = re.sub(r"[.!?]+", ".", self.value)
        parts = cleaned.split(".")
        sentences = [s for s in parts if s.strip()]
        return len(sentences)
