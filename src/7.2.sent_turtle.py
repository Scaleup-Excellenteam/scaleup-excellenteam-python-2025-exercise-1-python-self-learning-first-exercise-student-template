class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.
    """

    def __init__(self, usernames):
        """
        :param list usernames: Users for which we should create PO Boxes.
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, title=""):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param str title: The title of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'title': title
        }

        user_box = self.boxes[recipient]
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(self, user, n=None):
        """Read and remove the first n messages from the user's inbox.

        :param str user: The username to read messages for.
        :param int n: Optional number of messages to read. If None, read all.
        :return: List of messages read.
        :rtype: list[dict]
        :raises KeyError: if the user does not exist.
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        user_box = self.boxes[user]
        if n is None:
            messages = user_box[:]
            self.boxes[user] = []
        else:
            messages = user_box[:n]
            self.boxes[user] = user_box[n:]

        return messages

    def search_inbox(self, user, query):
        """Search messages in a user's inbox for a given string.

        :param str user: The username to search messages for.
        :param str query: The string to search for in titles or bodies.
        :return: List of messages matching the query.
        :rtype: list[dict]
        :raises KeyError: if the user does not exist.
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        return [
            message for message in self.boxes[user]
            if query.lower() in message['body'].lower() or query.lower() in message['title'].lower()
        ]


if __name__ == '__main__':
    po = PostOffice(["alice", "bob"])

    po.send_message("bob", "alice", "Hey, how are you?", title="Hello")
    po.send_message("bob", "alice", "Don't forget the meeting tomorrow!", title="Reminder", urgent=True)
    po.send_message("bob", "alice", "Need help with the code", title="Help")


    print("Search 'meeting':")
    print(po.search_inbox("alice", "meeting"))

    print("Read 1 message:")
    print(po.read_inbox("alice", 1))

    print("Read all remaining messages:")
    print(po.read_inbox("alice"))

