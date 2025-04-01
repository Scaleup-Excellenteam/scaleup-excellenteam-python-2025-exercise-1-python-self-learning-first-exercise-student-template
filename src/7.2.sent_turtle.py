class PostOffice:
    """
    A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """
        Send a message to a recipient.

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
            # Added to check message read status
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username: str, N: int = None) -> list:
        """
        Returns the first N messages from the user's inbox.

        :param str username: The username that we are searching for.
        :param int N: The number of messages to show (default is all messages).
        :return: A list of messages from the user's inbox.
        :rtype: list
        :raises KeyError: if the username does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"Username doesn't exist.")

        inbox = self.boxes[username]
        unread = [message for message in inbox if message['read'] == False]
        ret = []

        # If N isn't provided or bigger than the user's inbox, it will show all unread messages so marked as the length.
        if N == None or N > len(inbox):
            n = len(inbox)
        else:
            n = N

        # Change the read status from False to True
        for message in unread[:n]:
            ret.append(message)
            message['read'] = True

        return ret

    def search_inbox(self, username: str, keyword: str) -> list:
        """
        Search for messages with specific keywords in the inbox of the user.

        :param str username: The username that we are searching for.
        :param str keyword: The keyword that we are searching for.
        :return: A list of messages containing the keyword.
        :rtype: list
        :raises KeyError: if the username does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"Username doesn't exist.")

        inbox = self.boxes[username]

        # Checks messages body and adds to the list if it contains the keyword. (There is no title?)
        return [message for message in inbox if keyword.lower() in message['body'].lower()]


if __name__ == '__main__':
    # Create a PostOffice
    po = PostOffice(["Lior", "Noa", "Dan"])

    # Messages from Lior to Noa
    po.send_message("Lior", "Noa", "Hello Noa, how are you?")
    po.send_message("Lior", "Noa", "Did you eat the fish I left in the kitchen?")
    po.send_message("Lior", "Noa", "Urgent: Don't eat the fish, its rotten!")

    # Messages from Noa to Lior
    po.send_message("Noa", "Lior", "Hi Lior, the fish had flies on it, of course I didn't eat it")

    # Messages from Dan to Lior
    po.send_message("Dan", "Lior", "Lior, can I take one of your shirts?")

    print("read_inbox first test to read 2 messages")
    read_messages = po.read_inbox("Noa", 2)
    print("Noa's first 2 unread messages:", read_messages)
    print("read_inbox second test to read 2 messages")
    read_messages = po.read_inbox("Noa", 2)
    print("Noa's next 2 unread messages:", read_messages)

    read_messages = po.read_inbox("Lior", -1)
    print("All of Lior's messages:", read_messages)
    read_messages = po.read_inbox("Lior")
    print("Lior's messages after reading all:", read_messages)

    print("\n\nsearch_inbox first test to search for messages with keywords")
    search_messages = po.search_inbox("Noa", "fish")
    print("Messages containing 'fish' in Noa's inbox:", search_messages)

    search_messages = po.search_inbox("Lior", "course")
    print("Messages containing 'course' in Lior's inbox:", search_messages)

    search_messages = po.search_inbox("Dan", "nothing")
    print("Messages containing 'nothing' in Dan's inbox:", search_messages)
