class Poll:
    def __init__(self, question, options):
        self.question = question
        self.options = {option: 0 for option in options}

    def vote(self, option):
        if option in self.options:
            self.options[option] += 1
            return True
        return False

    def add_option(self, option):
        if option in self.options:
            return False
        self.options[option] = 0
        return True

    def remove_option(self, option):
        if option not in self.options:
            return False
        del self.options[option]
        return True

    def get_votes(self):
        return sorted(self.options.items(), key=lambda item: item[1], reverse=True)

    def get_winner(self):
        if not self.options:
            return None
        max_votes = max(self.options.values())
        for option in self.options:
            if self.options[option] == max_votes:
                return option


def cast_multiple_votes(poll, votes):
    for vote in votes:
        poll.vote(vote)


if __name__ == '__main__':
    bridge_question = Poll('What is your favourite colour?', ['Blue', 'Yellow'])
    cast_multiple_votes(bridge_question, ['Blue', 'Blue', 'Yellow'])
    print(bridge_question.get_winner() == 'Blue')
    cast_multiple_votes(bridge_question, ['Yellow', 'Yellow'])
    print(bridge_question.get_winner() == 'Yellow')
    print(bridge_question.get_votes() == [('Yellow', 3), ('Blue', 2)])
    bridge_question.remove_option('Yellow')
    print(bridge_question.get_winner() == 'Blue')
    print(bridge_question.get_votes() == [('Blue', 2)])
    bridge_question.add_option('Yellow')
    print(bridge_question.get_votes() == [('Blue', 2), ('Yellow', 0)])
    print(not bridge_question.add_option('Blue'))
    print(bridge_question.get_votes() == [('Blue', 2), ('Yellow', 0)])
