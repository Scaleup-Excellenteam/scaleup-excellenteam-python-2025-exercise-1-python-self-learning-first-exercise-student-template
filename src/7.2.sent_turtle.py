"""
This module defines a PostOffice class that allows users to send and receive messages,
including features such as unread status and urgency handling.
"""

class PostOffice:
    """A Post Office class. Allows users to message each other."""

    def __init__(self, usernames):
        """
        Initialize the post office with mailboxes for each user.

        :param usernames: List of usernames to create inboxes for.
        """
        self.message_id = 0  # Counter for assigning unique message IDs
        self.boxes = {user: [] for user in usernames}  # Mailboxes for each user

    def send_message(self, sender, recipient, title, body, urgent=False):
        """
        Send a message to a recipient. Adds an 'unread' flag to each message.

        :param sender: The sender's username
        :param recipient: The recipient's username
        :param title: The message title
        :param body: The message body
        :param urgent: If True, message will be inserted at the top of the inbox
        :return: The unique ID of the sent message
        """
        # Check recipient exists
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1  # Increment message ID counter

        # Create the message dictionary
        message_details = {
            'id': self.message_id,
            'sender': sender,
            'title': title,
            'body': body,
            'unread': True  # Flag required by the tests
        }

        user_box = self.boxes[recipient]

        # Insert at top if urgent, else append to end
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(self, user, n=None):
        """
        Read and return the first n messages from a user's inbox.
        Marks the messages as read but does not delete them.

        :param user: Username of the inbox to read
        :param n: Number of messages to read; if None, read all
        :return: List of read messages
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        user_box = self.boxes[user]

        # Get all or the first n messages
        if n is None:
            messages = user_box
        else:
            messages = user_box[:n]

        # Mark each message as read
        for msg in messages:
            msg["unread"] = False

        return messages

    def search_inbox(self, user, query):
        """
        Search for messages containing the query string in the title or body.

        :param user: Username to search messages for
        :param query: Text to search for
        :return: List of matching messages
        """
        if user not in self.boxes:
            raise KeyError(f"User '{user}' does not exist.")

        return [
            message for message in self.boxes[user]
            if query.lower() in message["body"].lower() or query.lower() in message["title"].lower()
        ]


if __name__ == '__main__':
    po = PostOffice(["alice", "bob"])

    # Send some example messages to alice
    po.send_message("bob", "alice", "Hello", "Hey, how are you?")
    po.send_message("bob", "alice", "Reminder", "Don't forget the meeting tomorrow!", urgent=True)
    po.send_message("bob", "alice", "Help", "Need help with the code")

    # Search alice's inbox for messages containing "meeting"
    print("Search 'meeting':")
    print(po.search_inbox("alice", "meeting"))

    # Read the first message from alice's inbox
    print("Read 1 message:")
    print(po.read_inbox("alice", 1))

    # Read all remaining messages from alice's inbox
    print("Read all remaining messages:")
    print(po.read_inbox("alice"))
