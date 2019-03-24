from mycroft import MycroftSkill, intent_file_handler


class Oumuamua(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('oumuamua.intent')
    def handle_oumuamua(self, message):
        self.speak_dialog('oumuamua')


def create_skill():
    return Oumuamua()

