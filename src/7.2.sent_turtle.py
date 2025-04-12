class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        

    def send_message(self, sender, recipient, title, body, *, urgent=False):

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
            'title': title,
            'body': body,
            'sender': sender,
            'unread': True
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id


    def read_inbox(self, username, message_count=-1):
        """
        At This Function Will Return The First 'message count' Messages of The user 'username',
        That This User Don't Read. 
        """

        # Init A Empty List For The Messages, And Get All User Messages
        result_message_list = []
        user_message_list = self.boxes.get(username, [])

        # Get How Many Message Will Read.
        if message_count == -1:
            message_count = len(user_message_list)

        for i in range(min(message_count, len(user_message_list))):

            # Check If The User Hasn't Read This Message.
            if user_message_list[i]['unread']:
                # Add The Message To The List, And Change His Status To Read.
                result_message_list.append(user_message_list[i])
                user_message_list[i]['unread'] = False

        return result_message_list


    def search_inbox(self, username, search_message):
        """
        At This Method Will Get UserName, And Message To Search, And Will Return 
        List That Will Contain All The User Messages That Conatin This Message. 
        """

        message_result = []
        massege_to_search_lower = search_message.lower()

        # Get All The Messages Of The User.
        for message in self.boxes.get(username, []):

            if massege_to_search_lower in message['title'].lower() or massege_to_search_lower in message['body'].lower():
                message_result.append(message)

        return message_result
