import asyncio

import nacre

class AboutSession:

    about = "PoxterBot is a bot for Google Hangouts. You can view source code at https://github.com/GeneralPoxter/PoxterBot -- Thanks!"

    def __init__(self, poxter, config):
        self.poxter = poxter
        self.hangouts = self.poxter.hangouts
        self.config = config
        self.buildHandle()

    def build(self):
        pass

    def buildHandle(self):
        messageFilter = nacre.handle.newMessageFilter('^{}about$'.format(self.poxter.config['format']))
        async def handle(update):
            if nacre.handle.isMessageEvent(update):
                event = update.event_notification.event
                if messageFilter(event):
                    await self.respond(event)
        self.poxter.updateEvent.addListener(handle)

    async def respond(self, event):
        message = self.about
        conversation = self.hangouts.getConversation(event=event)
        await self.hangouts.send(message, conversation)

def load(poxter, config):
    return AboutSession(poxter, config)
