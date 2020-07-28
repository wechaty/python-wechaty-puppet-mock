"""room mock code"""
import asyncio
from typing import cast, Union
import random

from wechaty import (
    Message,
    Room,
    Contact,
    Wechaty,
    WechatyOptions
)

from wechaty_puppet import (
    Puppet,
    FileBox
)

from wechaty_puppet_mock import (
    PuppetMock,
    PuppetMockOptions,
    EnvironmentMock,
    Mocker
)


async def mocker_example():
    # init the mocker
    environment = EnvironmentMock()
    mocker = Mocker()
    mocker.use(environment)

    # init the puppet_mock
    puppet_options = PuppetMockOptions(mocker=mocker)
    puppet = PuppetMock(puppet_options)

    # init the wechaty
    wechaty_options = WechatyOptions(
        puppet=cast(Puppet, puppet),
        puppet_options=puppet_options
    )
    bot = Wechaty(wechaty_options)

    async def on_message(msg: Message):
        from_contact = msg.talker()
        text = msg.text()
        room = msg.room()
        if text == '#ding':
            conversation: Union[
                Room, Contact] = from_contact if room is None else room
            await conversation.ready()
            await conversation.say('dong')

    bot.on('message', on_message)

    await bot.start()

    # send the message to a room
    room = mocker.new_room()
    members = await room.member_list()
    one_of_member = random.choice(members)
    mocker.send_message(
        talker=one_of_member,
        conversation=room,
        msg='ding'
    )


if __name__ == '__main__':
    asyncio.run(mocker_example())
