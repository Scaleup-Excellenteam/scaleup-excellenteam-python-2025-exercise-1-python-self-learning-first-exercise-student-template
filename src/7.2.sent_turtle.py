"""
Module: post_office

This module provides a simple messaging system between users, simulating a post office.
Each user has an inbox where they can receive, read, and search messages. Messages include
metadata such as title, sender, read/unread status, and support for urgent delivery which
places messages at the top of the inbox.

Key Features:
- Create inboxes for multiple users.
- Send messages with optional urgency.
- Read messages and mark them as read.
- Search inboxes by message title or body.
"""
class PostOffice:
    """
    A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental ID of the last message sent.
    :ivar dict boxes: Users' inboxes, mapping usernames to a list of their messages.

    :param list usernames: Users for which we should create PO Boxes.
    """
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}


    def send_message(self, sender, recipient, title_of_the_msg, message_body, urgent=False):
        """
        Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str title_of_the_msg: The title of the message.
        :param str message_body: The body of the message.
        :param bool urgent: Whether the message should be treated as urgent (optional).

        :return: The message ID, auto-incremented.
        :rtype: int

        :raises KeyError: If the recipient does not exist.

        Notes:
            - 'title': Stores the message's title.
            - 'unread': Tracks whether a message has been read.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'title': title_of_the_msg,
            'unread': True
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id


    def read_inbox(self, user, number=0):
        """
        Reads messages from a user's inbox, marking them as read.

        :param str user: The user whose inbox is being accessed.
        :param int number: The number of messages to read. If 0, reads all messages.

        :return: A list of messages read from the user's inbox.
        :rtype: list
        """
        if user not in self.boxes:
            print("User not found")
            return []
        box = self.boxes[user]
        if number == 0 or number > len(box):
            number = len(box)
        for i in range(number):
            box[i]['unread'] = False
        return box[:number]


    def search_inbox(self, user, str_search):
        """
        Searches a user's inbox for messages containing the specified string.

        :param str user: The user whose inbox is being searched.
        :param str str_search: The search term.

        :return: A list of messages containing the string.
        :rtype: list
        """
        if user not in self.boxes:
            print("User not found")
            return []
        str_search = str_search.lower()
        return [
            msg for msg in self.boxes[user]
            if str_search in msg['body'].lower() or str_search in msg['title'].lower()
        ]


