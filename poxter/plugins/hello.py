import asyncio

import nacre

class HelloSession:

    hello = "Hello {}!"

    def __init__(self, poxter, config):
        self.poxter = poxter
        self.hangouts = self.poxter.hangouts
        self.config = config
        self.buildHandle()

    def build(self):
        pass

    def buildHandle(self):
        messageFilter = nacre.handle.newMessageFilter('^{}hello$'.format(self.poxter.config['format']))
        async def handle(update):
            if nacre.handle.isMessageEvent(update):
                event = update.event_notification.event
                if messageFilter(event):
                    await self.respond(event)
        self.poxter.updateEvent.addListener(handle)

    async def respond(self, event):
        message = self.hello.format(self.hangouts.getUser(event=event).first_name)
        conversation = self.hangouts.getConversation(event=event)
        await self.hangouts.send(message, conversation)

def load(poxter, config):
    return HelloSession(poxter, config)
