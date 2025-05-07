import datetime
from typing import List, Dict

class CalendarManager:
    def __init__(self, service):
        self.service = service

    def create_event(self, summary: str, start_time: str, end_time: str) -> Dict:
        try:
            event = {
                'summary': summary,
                'start': {'dateTime': start_time, 'timeZone': 'America/Chicago'},
                'end': {'dateTime': end_time, 'timeZone': 'America/Chicago'}
            }
            event = self.service.events().insert(calendarId='primary', body=event).execute()
            return event
        except Exception as e:
            return {'error': str(e)}

    def list_events(self, time_min: str, time_max: str) -> List[Dict]:
        try:
            events_result = self.service.events().list(
                calendarId='primary', timeMin=time_min, timeMax=time_max,
                singleEvents=True, orderBy='startTime').execute()
            return events_result.get('items', [])
        except Exception as e:
            return [{'error': str(e)}]
