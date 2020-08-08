from random import choice
from typing import cast

import pytest
from wechaty import WechatyOptions, Wechaty, Message
from wechaty_puppet import Puppet, get_logger

from wechaty_puppet_mock import EnvironmentMock, Mocker, PuppetMockOptions, \
    PuppetMock

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio

log = get_logger('TestDingDong')


@pytest.fixture
def mocker() -> Mocker:
    environment = EnvironmentMock()
    mocker = Mocker()
    mocker.use(environment)
    return mocker


@pytest.fixture
async def bot(mocker) -> Wechaty:
    puppet_options = PuppetMockOptions(mocker=mocker)
    puppet = PuppetMock(puppet_options)

    # init the wechaty
    wechaty_options = WechatyOptions(
        puppet=cast(Puppet, puppet),
        puppet_options=puppet_options
    )
    bot = Wechaty(wechaty_options)
    mocker.init(puppet, mocker)
    await bot.start()
    return bot


async def test_ding_dong(bot, mocker):
    # send the message to a room

    async def on_message(msg: Message):
        log.info('ding-dong-test: receive the message')
        assert 1 == 2

    bot.on_message = on_message
    room = mocker.new_room()
    members = await room.member_list()
    one_of_member = choice(members)
    mocker.send_message(
        talker=one_of_member,
        conversation=room,
        msg='ding'
    )
