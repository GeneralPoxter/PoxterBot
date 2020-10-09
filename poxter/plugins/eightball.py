import asyncio, random

import nacre

class EightBallSession:

    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    def __init__(self, poxter, config):
        self.poxter = poxter
        self.hangouts = self.poxter.hangouts
        self.config = config
        self.buildHandle()

    def build(self):
        pass

    def buildHandle(self):
        messageFilter = nacre.handle.newMessageFilter('^{}8ball\s.*$'.format(self.poxter.config['format']))
        async def handle(update):
            if nacre.handle.isMessageEvent(update):
                event = update.event_notification.event
                if messageFilter(event):
                    await self.respond(event)
        self.poxter.updateEvent.addListener(handle)

    async def respond(self, event):
        message = random.choice(self.answers)
        conversation = self.hangouts.getConversation(event=event)
        await self.hangouts.send(message, conversation)

def load(poxter, config):
    return EightBallSession(poxter, config)
