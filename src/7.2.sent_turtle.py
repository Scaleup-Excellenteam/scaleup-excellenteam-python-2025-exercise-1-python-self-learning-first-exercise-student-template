class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title,
                     message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'unread': True,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=-1):
        """Read n messages from username's inbox.

        :param str username: The inbox to read messages from.
        :param int n: The number of messages to read.
        :return: The n first messages from username's inbox.
        :rtype: list(dict)
        :raises KeyError: if the recipient does not exist.
        """

        messages = []
        box = self.boxes[username]
        if n == -1:
            messages = [message for message in box
                        if message['unread'] is True]
            for message in box:
                message['unread'] = False
            assert self.boxes[username][0]['unread'] is False
        elif n <= 0:
            return None
        else:
            for i in range(len(box)):
                if box[i]['unread'] is True:
                    messages.append(box[i])
                    box[i]['unread'] = False
                n -= 1
                if n == 0:
                    break
        return messages

    def search_inbox(self, username, substring):
        """Search username's inbox for a title or body matching substring

        :param str username: The inbox to read messages from.
        :param str substring: The substring to match.
        :return: A list of matched messages.
        :rtype: list(dict)
        :raises KeyError: if the recipient does not exist.
        """
        messages = []
        for message in self.boxes[username]:
            if (
                    substring.lower() in message['title'].lower() or
                    substring.lower() in message['body'].lower()
            ):
                messages.append(message)

        return messages
