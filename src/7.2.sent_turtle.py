class PostOffice:
    def __init__(self, users=None):
        self.inboxes = {}
        self.message_id_counter = 1  # add this
        if users:
            for user in users:
                self.inboxes[user] = []
        self.boxes = self.inboxes

    def send_message(self, sender, recipient, subject, body, urgent=False):
        if recipient not in self.inboxes:
            raise KeyError(f"Recipient '{recipient}' not found.")

        message = {
            "id": self.message_id_counter,
            "from": sender,
            "title": subject,
            "body": body,
            "unread": True  

        }

        if urgent:
            self.inboxes[recipient].insert(0, message)
        else:
            self.inboxes[recipient].append(message)

        self.message_id_counter += 1
        return message["id"]



    def read_inbox(self, username, num_messages=None):
        if username not in self.inboxes:
            return []

        inbox = self.inboxes[username]
        unread_messages = [msg for msg in inbox if msg["unread"]]

        if num_messages is None:
            num_messages = len(unread_messages)

        messages_to_return = unread_messages[:num_messages]
        for message in messages_to_return:
            message["unread"] = False  # mark as read

        return messages_to_return

    def search_inbox(self, username, search_string):
        """
        Search for messages that contain 'search_string' in either their subject or body.
        Returns a list of messages that match the search.
        """
        if username not in self.inboxes:
            return []  # No inbox for this user

        inbox = self.inboxes[username]
        matching_messages = []

        for message in inbox:
            if (search_string.lower() in message["title"].lower()) or (search_string.lower() in message["body"].lower()):
                matching_messages.append(message)

        return matching_messages


# This block will only run when the script is executed directly, not when imported
if __name__ == '__main__':
    # Testing the PostOffice class
    post_office = PostOffice()

    # Send some messages
    post_office.send_message("john_doe", "Meeting Tomorrow", "Let's meet tomorrow at 10 AM.")
    post_office.send_message("john_doe", "Lunch Plans", "Do you want to grab lunch today?")
    post_office.send_message("alice_smith", "Hello", "Hi Alice, how are you?")

    # Read the inbox for john_doe
    print("John Doe's inbox:")
    print(post_office.read_inbox("john_doe", 1))  # Read the first unread message

    # Search for messages in john_doe's inbox containing "meeting"
    print("\nMessages containing 'meeting':")
    print(post_office.search_inbox("john_doe", "meeting"))

    # Read all unread messages for alice_smith
    print("\nAlice Smith's inbox:")
    print(post_office.read_inbox("alice_smith"))
