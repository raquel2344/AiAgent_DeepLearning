
class FeedbackManager:
    def __init__(self):
        self.logs = []

    def record_action(self, action_type: str, result: str):
        self.logs.append({'action': action_type, 'result': result})

    def get_feedback(self):
        return self.logs
