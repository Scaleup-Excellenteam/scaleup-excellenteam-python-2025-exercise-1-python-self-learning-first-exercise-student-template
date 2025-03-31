class PostOffice:
    """A Post Office class. Allows users to message each other."""

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, body, urgent=False):

        if recipient not in self.boxes:
            raise KeyError(f"User '{recipient}' does not exist")

        self.message_id += 1

        message = {
            'id': self.message_id,
            'sender': sender,
            'title': title,
            'body': body,
            'unread': True
        }

        if urgent:
            self.boxes[recipient].insert(0, message)
        else:
            self.boxes[recipient].append(message)

        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Read messages from a user's inbox and returns - list messages that were read.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist")

        inbox = self.boxes[username]

        if num_messages is None:
            num_messages = len(inbox)

        num_messages = min(num_messages, len(inbox))

        messages = inbox[:num_messages]

        for message in messages:
            message['unread'] = False

        return messages

    def search_inbox(self, username, search_string):
        """Search for messages containing a specific string in title or body and returns - list messages that match the
        search criteria.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist")

        matching_messages = []

        for message in self.boxes[username]:
            if (search_string.lower() in message['title'].lower() or
                    search_string.lower() in message['body'].lower()):
                matching_messages.append(message)

        return matching_messages


def sent_turtle():
    """Main function to demonstrate the PostOffice functionality."""
    post_office = PostOffice(['alice', 'bob', 'charlie'])

    post_office.send_message('alice', 'bob', 'Urgent Message', 'Hello Bob!', urgent=True)
    post_office.send_message('charlie', 'bob', 'Meeting', 'Meeting tomorrow')
    post_office.send_message('alice', 'bob', 'Lunch', 'Don\'t forget lunch')

    print("Bob reading 2 messages:")
    messages = post_office.read_inbox('bob', 2)
    for msg in messages:
        print(f"From: {msg['sender']}, Title: {msg['title']}, Message: {msg['body']}, Unread: {msg['unread']}")

    post_office.send_message('charlie', 'bob', 'Project Update', 'Project updates')

    print("\nBob reading all remaining messages:")
    messages = post_office.read_inbox('bob')
    for msg in messages:
        print(f"From: {msg['sender']}, Title: {msg['title']}, Message: {msg['body']}, Unread: {msg['unread']}")

    print("\nSearching Bob's messages for 'meeting':")
    results = post_office.search_inbox('bob', 'meeting')
    for msg in results:
        print(f"From: {msg['sender']}, Title: {msg['title']}, Message: {msg['body']}")


if __name__ == "__main__":
    sent_turtle()
