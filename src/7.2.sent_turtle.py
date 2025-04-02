class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.boxes:
            raise KeyError(f"User {recipient} does not exist.")
            
        self.message_id += 1
        message = {
            'id': self.message_id,
            'title': title,
            'body': body,
            'sender': sender,
            'unread': True
        }
        
        if urgent:
            self.boxes[recipient].insert(0, message)
        else:
            self.boxes[recipient].append(message)
            
        return self.message_id

    def read_inbox(self, username, n=None):
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
            
        unread_msgs = [m for m in self.boxes[username] if m['unread']]
        messages = unread_msgs[:n] if n is not None else unread_msgs
        
        for msg in messages:
            msg['unread'] = False
            
        return [{
            'id': m['id'],
            'title': m['title'],
            'body': m['body'],
            'sender': m['sender'],
            'unread': False
        } for m in messages]

    def search_inbox(self, username, query):
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
            
        query = query.lower()
        return [{
            'id': m['id'],
            'title': m['title'],
            'body': m['body'],
            'sender': m['sender']
        } for m in self.boxes[username]
            if query in m['title'].lower() or 
               query in m['body'].lower()]