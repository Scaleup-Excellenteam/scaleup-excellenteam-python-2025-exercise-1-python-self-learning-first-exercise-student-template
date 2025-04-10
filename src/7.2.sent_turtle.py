"""A module defining a Post Office class for user-to-user messaging."""


class PostOffice:
    """
    A Post Office class that allows users to message each other.

    Attributes:
        message_id (int): Incremental ID of the last message sent.
        boxes (dict): Dictionary mapping usernames to their inboxes.
    """

    def __init__(self, usernames):
        """
        Initializes the Post Office with mailboxes for given usernames.

        Args:
            usernames (list): A list of usernames to create PO boxes for.
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """
        Sends a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The recipient's username.
            title (str): The title of the message.
            message_body (str): The message content.
            urgent (bool, optional): If True, message is inserted at the beginning.

        Returns:
            int: Auto-incremented message ID.

        Raises:
            KeyError: If the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'unread': True,
            'title': title,
            'urgent': urgent
        }

        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)

        return self.message_id

    def read_inbox(self, user, n=0):
        """
        Reads messages from a user's inbox and marks them as read.

        Args:
            user (str): Username of the mailbox to read.
            n (int): Number of messages to return (0 = all messages).

        Returns:
            list: A list of message dictionaries.

        Raises:
            KeyError: If the user does not exist.
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        user_box = self.boxes[user]

        if n == 0:
            messages = user_box
        else:
            messages = user_box[:n]

        for message in messages:
            message['unread'] = False

        return messages

    def search_inbox(self, username, word):
        """
        Searches a user's inbox for messages containing a specific word.

        Args:
            username (str): The username whose inbox to search.
            word (str): The word to search for in titles or bodies.

        Returns:
            list: List of messages containing the keyword.
        """
        if username not in self.boxes:
            print("User does not exist.")
            return []

        word = word.lower()
        return [
            msg for msg in self.read_inbox(username)
            if word in msg['body'].lower() or word in msg['title'].lower()
        ]
