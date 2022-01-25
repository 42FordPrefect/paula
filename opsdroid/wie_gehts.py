import random
import paho.mqtt.subscribe as subscribe
from opsdroid.matchers import match_regex
from opsdroid.skill import Skill


class HelloByeSkill(Skill):

    @match_regex(r'hi|hello|hey|hallo', case_sensitive=False)
    async def hello(self, message):
        text = random.choice(
            ["Hi {}", "Hello {}", "Hey {}"]).format(message.user)
        await message.respond(text)

    @match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off', case_sensitive=False)
    async def goodbye(self, message):
        text = random.choice(["Bye {}", "See you {}", "Au revoir {}"]).format(message.user)
        await message.respond(text)

    @match_regex(r'wie geht', case_sensitive=False)
    async def wie_gehts(self, message):
        await msg1 = subscribe.simple("paula/erde",hostname="localhost").payload.decode('utf-8')
        await message.respond(msg1)


    @match_regex(r'wie warm', case_sensitive=False)
    async def wie_warm(self, message):
        await msg2 = subscribe.simple("paula/temp", hostname="localhost").payload.decode('utf-8')
        await message.respond(msg2)


    @match_regex(r'Luftfeuchtigkeit', case_sensitive=False)
    async def wie_humid(self, message):
        await msg3 = subscribe.simple("paula/luftfeuchtigkeit", hostname="localhost").payload.decode('utf-8')
        await message.respond(msg3)
