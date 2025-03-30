from pyexpat.errors import messages


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
            'body': message_body,
            'sender': sender,
            'unread': 1,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, recipient: str, num_of_messages: int = 0) -> list:
        """Retrieve unread messages, mark them as read, and move them to the end of the inbox.

        :param str recipient: The recipient's username.
        :param int num_of_messages: The number of unread messages to retrieve (0 for all).
        :return: A list of unread messages.
        :rtype: list
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' not found.")

        user_box = self.boxes[recipient]
        unread_messages = [msg for msg in user_box if msg['unread']]
        messages_to_read = unread_messages[:num_of_messages] if num_of_messages else unread_messages

        for message in messages_to_read:
            message['unread'] = 0
            user_box.remove(message)
            user_box.append(message)

        return messages_to_read

    def search_inbox(self, recipient: str, txt_to_search: str) -> list:
        """Search messages that contain the given text in their body.

        :param str recipient: The recipient's username.
        :param str txt_to_search: The text to search for.
        :return: A list of messages that their body contain the search text.
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' not found.")

        user_box = self.boxes[recipient]
        messages = [message for message in user_box if txt_to_search.lower() in message['body'].lower()]
        return messages



def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter')
    post_office = PostOffice(users)
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello',
    )
    print(f"Successfuly sent messages: {post_office.boxes['Newman']}")

    read_messages = post_office.read_inbox('Newman', 1)
    print(f"Read 1 message from inbox {read_messages}")

    search_messages = post_office.search_inbox('Newman', ',')
    print(f"Search the letter ',' in Newman in inbox {search_messages}")

if __name__ == '__main__':
    show_example()