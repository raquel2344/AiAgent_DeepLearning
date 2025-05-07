class ContactManager:
    def __init__(self, people_service):
        self.service = people_service

    def create_contact(self, name: str, email: str, phone: str) -> Dict:
        try:
            contact = {
                'names': [{'givenName': name}],
                'emailAddresses': [{'value': email}],
                'phoneNumbers': [{'value': phone}]
            }
            self.service.people().createContact(body=contact).execute()
            return {'status': 'success'}
        except Exception as e:
            return {'error': str(e)}

    def get_contact(self, name: str) -> Dict:
        # Simplified memory or database lookup placeholder
        return {'name': name, 'email': 'example@email.com', 'phone': '000-000-0000'}
