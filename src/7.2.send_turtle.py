class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False  # Added to track unread messages
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    # Reads N messages and marks them as read
    def read_inbox(self, username, n=None):
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
        
        unread_messages = [msg for msg in self.boxes[username] if not msg['read']]
        messages_to_return = unread_messages[:n] if n is not None else unread_messages
        
        # Mark returned messages as read
        for msg in messages_to_return:
            msg['read'] = True
            
        # Return without 'read' status (clean output)
        return [{'id': m['id'], 'sender': m['sender'], 'body': m['body']} 
                for m in messages_to_return]

    # Searches for query in sender or message body
    def search_inbox(self, username, query):
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")
            
        return [
            {'id': msg['id'], 'sender': msg['sender'], 'body': msg['body']}
            for msg in self.boxes[username]
            if query in msg['sender'] or query in msg['body']
        ]