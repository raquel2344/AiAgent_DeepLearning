class InputValidator:
    def __init__(self):
        self.keywords = ["cliff", "kill", "suicide"]

    def is_safe(self, message: str) -> bool:
        return not any(word in message.lower() for word in self.keywords)
