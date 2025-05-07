
class MemoryStore:
    def __init__(self):
        self.memory = {}

    def save(self, key: str, value):
        self.memory[key.lower()] = value

    def retrieve(self, key: str):
        return self.memory.get(key.lower(), None)
