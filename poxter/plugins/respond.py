import asyncio

import nacre

import hangups

import json

class RespondSession:

    with open('custom/respond.json') as json_file:
        responses = json.load(json_file)

    with open('private/auth.json') as json_file:
        email = json.load(json_file)['email']

    def __init__(self, poxter, config):
        self.poxter = poxter
        self.hangouts = self.poxter.hangouts
        self.config = config
        self.buildHandle()

    def build(self):
        pass

    def buildHandle(self):
        async def handle(update):
            if nacre.handle.isMessageEvent(update):
                event = update.event_notification.event
                await self.respond(event)

        self.poxter.updateEvent.addListener(handle)

    async def respond(self, event):
        message = hangups.ChatMessageEvent(event).text.lower()
        conversation = self.hangouts.getConversation(event=event)

        uid = hangups.ConversationEvent(event).user_id
        if self.email != str(conversation.get_user(uid).emails[0]):
            message = (
                message
                .encode('ascii', 'ignore')
                .decode('utf-8')
                .strip()
            )

        for res in self.responses:
            if message in self.responses[res]:
                await self.hangouts.send(res + '\uFEFF', conversation)

def load(poxter, config):
    return RespondSession(poxter, config)