class PostOffice:
    def __init__(self, usernames):
        """
        Initializes a post office with an inbox for each user.
        :param usernames: list of usernames.
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, body, urgent=False):
        """
        Sends a message to a recipient. Urgent messages go to the top of the inbox.
        :return: the unique message id.
        """
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

    def read_message(self, username, message_id):
        """
        Marks the message with the given ID as read in the user's inbox.
        """
        for message in self.boxes[username]:
            if message['id'] == message_id:
                message['unread'] = False

    def read_inbox(self, username, n=None):
        """
        Returns the first n unread messages from the user's inbox.
        Marks them as read and removes them from the inbox.
        If n is not specified, returns all unread messages.
        """
        inbox = self.boxes[username]
        messages = inbox[:n] if n is not None else inbox
        for message in messages:
            self.read_message(username, message['id'])
        return messages

    def search_inbox(self, username, contained):
        """
        Returns all messages that contain the given substring
        in the title or body. The search is case-insensitive.
        Only searches messages still in the inbox.
        """
        inbox = self.boxes.get(username, [])
        contained_lower = contained.lower()
        return [
            msg for msg in inbox
            if contained_lower in msg['title'].lower() or contained_lower in msg['body'].lower()
        ]
