from mycroft import MycroftSkill, intent_file_handler


class Superficies(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('superficies.intent')
    def handle_superficies(self, message):
        self.speak_dialog('superficies')


def create_skill():
    return Superficies()

