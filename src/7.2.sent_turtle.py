class PostOffice:
    """A Post Office class. Allows users to message each other."""

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, body, urgent=False):
        """
        Send a message to a recipient. Adds 'unread' key.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'sender': sender,
            'title': title,
            'body': body,
            'unread': True  # ✅ Required by tests
        }

        user_box = self.boxes[recipient]
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(self, user, n=None):
        """
        Read first N messages from user's inbox and mark them as read.
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        user_box = self.boxes[user]

        if n is None:
            messages = user_box
        else:
            messages = user_box[:n]

        # ✅ Mark messages as read
        for msg in messages:
            msg["unread"] = False

        return messages

    def search_inbox(self, user, query):
        """
        Search for a query in titles and bodies.
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        return [
            message for message in self.boxes[user]
            if query.lower() in message["body"].lower() or query.lower() in message["title"].lower()
        ]

if __name__ == '__main__':
    po = PostOffice(["alice", "bob"])
    po.send_message("bob", "alice", "Hello", "Hey, how are you?")
    po.send_message("bob", "alice", "Reminder", "Don't forget the meeting tomorrow!", urgent=True)
    po.send_message("bob", "alice", "Help", "Need help with the code")

    print("Search 'meeting':")
    print(po.search_inbox("alice", "meeting"))

    print("Read 1 message:")
    print(po.read_inbox("alice", 1))

    print("Read all remaining messages:")
    print(po.read_inbox("alice"))

