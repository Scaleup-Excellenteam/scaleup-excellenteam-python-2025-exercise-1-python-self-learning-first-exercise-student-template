class PostOffice:
    def __init__(self):
        self.inboxes = {}

    def send(self, to, message):
        if to not in self.inboxes:
            self.inboxes[to] = []
        self.inboxes[to].append({'content': message, 'read': False})

    def read_inbox(self, username, amount=None):
        if username not in self.inboxes:
            return []

        inbox = self.inboxes[username]
        unread_messages = [msg for msg in inbox if not msg['read']]

        if amount is None:
            to_return = unread_messages
        else:
            to_return = unread_messages[:amount]

        for msg in to_return:
            msg['read'] = True

        return [msg['content'] for msg in to_return]

    def search_inbox(self, username, query):
        if username not in self.inboxes:
            return []

        return [
            msg['content']
            for msg in self.inboxes[username]
            if query in msg['content']
        ]


if __name__ == '__main__':
    office = PostOffice()
    office.send('ron', 'Letter from Harry')
    office.send('ron', 'Dinner at 8')
    office.send('ron', 'Reminder: magic class')
    office.send('ron', 'Letter from Hermione')

    print("First read:", office.read_inbox('ron', 2))
    print("Second read:", office.read_inbox('ron'))
    print("Should be empty:", office.read_inbox('ron'))

    office.send('ron', 'Letter from Dumbledore')
    print("Search 'Letter':", office.search_inbox('ron', 'Letter'))
