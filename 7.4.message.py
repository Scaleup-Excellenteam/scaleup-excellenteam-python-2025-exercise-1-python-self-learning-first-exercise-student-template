from typing import Optional, List, Dict, Union


class Message:
    def __init__(self, title: str, body: str) -> None:
        self.title = title
        self.body = body

    def __str__(self) -> str:
        return f"{self.title}\n{'-' * len(self.title)}\n{self.body}"

    def __len__(self) -> int:
        return len(self.body)


class PostOffice:
    def __init__(self) -> None:
        self.inboxes: Dict[str, List[Dict[str, Union[Message, bool]]]] = {}

    def send(self, recipient: str, message_obj: Message) -> None:
        if recipient not in self.inboxes:
            self.inboxes[recipient] = []
        self.inboxes[recipient].append({'content': message_obj, 'read': False})

    def read_inbox(self, username: str, amount: Optional[int] = None) -> List[Message]:
        if username not in self.inboxes:
            return []

        inbox = self.inboxes[username]
        unread_entries = [entry for entry in inbox if not entry['read']]
        selected_entries = unread_entries if amount is None else unread_entries[:amount]

        for entry in selected_entries:
            entry['read'] = True

        return [entry['content'] for entry in selected_entries if isinstance(entry['content'], Message)]

    def search_inbox(self, username: str, query: str) -> List[Message]:
        if username not in self.inboxes:
            return []

        return [
            entry['content']
            for entry in self.inboxes[username]
            if isinstance(entry['content'], Message) and (
                query in entry['content'].title or query in entry['content'].body)
        ]


if __name__ == '__main__':
    office = PostOffice()

    message1 = Message("Lunch Plans", "Meet at 12.")
    message2 = Message("Reminder", "Finish the potion homework.")
    message3 = Message("Lunch Plans", "Location changed to Three Broomsticks.")

    office.send("harry", message1)
    office.send("harry", message2)
    office.send("harry", message3)

    print("Reading inbox:")
    for m in office.read_inbox("harry"):
        print(m)
        print(f"Length of body: {len(m)}")

    print("\nSearch 'Lunch':")
    for m in office.search_inbox("harry", "Lunch"):
        print(m)
