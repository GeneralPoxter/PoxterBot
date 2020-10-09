import asyncio

import nacre

import hangups

from os import listdir

class FileSession:

    files = {}
    for f in listdir("custom/files"):
        [name, ext] = f.split(".")
        files[name] = ext

    def __init__(self, poxter, config):
        self.poxter = poxter
        self.hangouts = self.poxter.hangouts
        self.config = config
        self.buildHandle()

    def build(self):
        pass

    def buildHandle(self):
        exp = ('^{}(' + "|".join([i for i in self.files]) + ')$').format(self.poxter.config['format'])
        messageFilter = nacre.handle.newMessageFilter(exp)
        async def handle(update):
            if nacre.handle.isMessageEvent(update):
                event = update.event_notification.event
                if messageFilter(event):
                    await self.respond(event)
        self.poxter.updateEvent.addListener(handle)

    async def respond(self, event):
        conversation = self.hangouts.getConversation(event=event)
        text = hangups.ChatMessageEvent(event).text[2:]
        await self.hangouts.sendFile(conversation, "custom/files/" + text + "." + self.files[text])

def load(poxter, config):
    return FileSession(poxter, config)
