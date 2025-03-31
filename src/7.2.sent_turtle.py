class PostOffice:
    """A Post Office class. Allows users to message each other.

       :ivar int message_id: Incremental id of the last message sent.
       :ivar dict boxes: Users' inboxes.

       :param list usernames: Users for which we should create PO Boxes.
       """
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}


    def send_message(self, sender, recipient,title_of_the_msg, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.

        I have added these :
            'title': title_of_the_msg -> To store the message's title, making it easier for users to identify messages at a glance.
            'unread': True -> To track whether a message has been read or not, allowing you to implement features like marking messages as read when opened.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
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

    def read_inbox(self,user,number=0):
        """
            This function reads messages from a user's inbox. It marks the messages as read and returns a list of messages.

            Parameters:
            user (str): The user whose inbox is being read.
            number (int): The number of messages to read. Defaults to 0, meaning all messages will be read.

            Returns:
            list: A list of messages read from the user's inbox.
            """
        if user in self.boxes:
            box = self.boxes[user]
            if number==0 or number > len(box) :
                number = len(box)
            for i in range(number):
                box[i]['unread'] = False
            return box[:number]
        else:
            print("User not found")
            return []

    def search_inbox(self,user,str_search):
        """
           This function searches for messages in a user's inbox that contain the specified string.

           Parameters:
           user (str): The user whose inbox is being searched.
           str_search (str): The string to search for in the message body or sender.

           Returns:
           list: A list of messages that contain the specified string.
           """
        if user not in self.boxes:
            print("User not found")
            return []
        str_search = str_search.lower()
        return [
            msg for msg in self.boxes[user] if str_search in msg['body'].lower() or str_search in msg['title'].lower()
        ]


