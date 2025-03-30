

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.
        Adds another key to the message details that indicates if a message was read.
        Includes a try-except block to check if the recipient exists in the boxes.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        try:
            user_box = self.boxes[recipient]
        except KeyError:
           raise KeyError("recipient not found")
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'was read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self,user_name,N=0):
        """Retrieve unread messages from a user's inbox and mark them as read.

        :param str user_name: The username whose inbox is being accessed.
        :param int N: The maximum number of unread messages to retrieve.
                      If N=0, all unread messages are returned.
        :return: A list of unread messages, each represented as a dictionary.
        :rtype: list[dict]
        :raises KeyError: If the user does not exist.
        """
        try:
            user_box = self.boxes[user_name]
        except KeyError:
            raise KeyError("User not found")

        N = len(user_box) if N == 0 else N
        message_number = min(len(user_box), N)
        read_number = 0
        read_messages = []
        while read_number < message_number:
            if not user_box[read_number].get('was read'):
                read_messages.append(user_box[read_number])
                user_box[read_number]['was read'] = True
                read_number += 1
            else:
                read_number += 1
                message_number += 1

        return read_messages

    def search_inbox(self,user_name,string):
        """Search for messages containing a specific substring in a user's inbox.

        :param str user_name: The username whose inbox is being searched.
        :param str string: The substring to search for within message bodies.
        :return: A list of messages that contain the search string.
        :rtype: list[dict]
        :raises KeyError: If the user does not exist.
        """
        try:
            user_box = self.boxes[user_name]
        except KeyError:
            raise KeyError("User not found")

        return_messages = []
        for message in user_box:
            if string in message['body']:
                return_messages.append(message)

        return return_messages
