
class Logic:
    def __init__(self):
        self.valid_users = {
            "1": "1",  # username: password
            
        }
        self.subtotal= 0.0

        
    def validate_user(self, username, password):
        return self.valid_users.get(username) == password
    
