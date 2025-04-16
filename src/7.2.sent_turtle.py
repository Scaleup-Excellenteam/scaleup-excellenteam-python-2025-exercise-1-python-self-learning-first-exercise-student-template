class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            subject (str, optional): The subject of the message. Defaults to empty string.
            urgent (bool, optional): Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

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

    def read_inbox(self, username, count=None):
        """Reads up to `count` messages from the user's inbox.

        Args:
            username (str): The user's username.
            count (int, optional): The number of messages to read. If None, reads all.

        Returns:
            list: The list of read messages.

        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        inbox = self.boxes[username]
        messages_to_return = inbox[:] if count is None else inbox[:count]

        for msg in messages_to_return:
            msg['unread'] = False

        return messages_to_return

    def search_inbox(self, username, query):
        """Searches for messages containing a query string in the subject or body.

        Args:
            username (str): The user's username.
            query (str): The string to search for.

        Returns:
            list: Messages matching the search query.

        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        query_lower = query.lower()
        return [
            msg for msg in self.boxes[username]
            if query_lower in msg['title'].lower() or query_lower in msg['body'].lower()
        ]

if __name__ == '__main__':
    po = PostOffice(['Sam', 'Amira'])

    po.send_message('Sam', 'Amira', 'Hi Amira!', subject='Greeting')
    po.send_message('Sam', 'Amira', 'Urgent: call me', subject='Emergency', urgent=True)
    po.send_message('Sam', 'Amira', 'Don’t forget the meeting.', subject='Reminder')

    print("Read 2 messages:")
    messages = po.read_inbox('Amira', 2)
    for m in messages:
        print(m)

    print("\nSearch for 'meeting':")
    print(po.search_inbox('Amira', 'meeting'))
