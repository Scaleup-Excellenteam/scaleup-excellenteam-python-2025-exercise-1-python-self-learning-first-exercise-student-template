class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'isRead' :False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id
    def Read_message(self, username,message_id):
        inbox = self.boxes[username]
        for message in inbox:
            if message['id'] == message_id:
                message['isRead'] = True

    def read_inbox (self , username , N):
        """Read N messages from the inbox

        :Arg
            username(str) : The username of the user to read messages from
            N(int): Number of messages to read

        :return
          list(list): List of the first N messages in the inbox
        """
        inbox = self.boxes[username]
        if N is None:
           messages = [message for message in inbox]
           [self.Read_message(username, message['id']) for message in messages]
        else:
            messages = [message for message in inbox[:N]]
            [self.Read_message(username, message['id']) for message in messages[:N]]
        return messages

    def search_inbox (self, username , contained):
        """Search for messages in the inbox that are contained in contained

        :Arg
            username(str) : The username of the user to read messages from
            contained(str) : The wanted mesage to search for
        :return
            list(list): List of the message the contained in contained
        """
        inbox = self.boxes[username]
        messages = [message for message in inbox if message['body'].contains(contained)]
        return messages


if __name__ == '__main__':
    user1 = PostOffice("Matan")
    
