"""room mock code"""
import asyncio
from typing import cast
from wechaty import Wechaty, WechatyOptions

from wechaty_puppet import Puppet

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
    await bot.start()



if __name__ == '__main__':
    asyncio.run(mocker_example())
