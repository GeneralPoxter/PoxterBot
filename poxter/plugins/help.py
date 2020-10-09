import asyncio

import nacre

class HelpSession:

    def __init__(self, poxter, config):
        self.poxter = poxter
        self.hangouts = self.poxter.hangouts
        self.config = config
        self.buildUsage()
        self.buildHandle()

    def build(self):
        pass

    def buildUsage(self):
        self.usage = "Usage: {}[<i>command</i>]<br>Commands:".format(self.poxter.config['format'])
        for command in self.config['commands']:
            self.usage += '<br><b>{}</b>: {}'.format(command, self.config['commands'][command])

    def buildHandle(self):
        messageFilter = nacre.handle.newMessageFilter('^{}help$'.format(self.poxter.config['format']))
        async def handle(update):
            if nacre.handle.isMessageEvent(update):
                event = update.event_notification.event
                if messageFilter(event):
                    await self.respond(event)
        self.poxter.updateEvent.addListener(handle)

    async def respond(self, event):
        message = self.usage
        conversation = self.hangouts.getConversation(event=event)
        await self.hangouts.send(message, conversation)

def load(poxter, config):
    return HelpSession(poxter, config)
