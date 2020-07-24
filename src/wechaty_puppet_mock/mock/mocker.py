"""
Code Generator - https://github.com/wj-Mcat/python-wechaty-puppet-mock

Authors:    Jingjing WU (吴京京) <https://github.com/wj-Mcat>

2020-now @ Copyright wj-Mcat

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from typing import (
    Optional,
    Dict,
    Type,
    List,
    Union
)
from uuid import uuid4
from collections import defaultdict
from wechaty_puppet import (
    ContactPayload,
    RoomPayload,
    MessagePayload
)
from wechaty import (
    Contact,
    Room
)

from wechaty_puppet_mock.mock.envrioment import MockEnvironment
from wechaty_puppet_mock.exceptions import WechatyPuppetMockError


class Mocker:
    """mock fake data"""
    def __init__(self):
        self.id: str = str(uuid4())
        self._contact_payload_pool: Dict[str, ContactPayload] = \
            defaultdict(ContactPayload)
        self._room_payload_pool: Dict[str, RoomPayload] = \
            defaultdict(RoomPayload)
        self._message_payload_pool: Dict[str, MessagePayload] = \
            defaultdict(MessagePayload)

        self._environment: Optional[MockEnvironment] = None

    @property
    def environment(self) -> MockEnvironment:
        """get the environment for mocker"""
        if not self._environment:
            raise WechatyPuppetMockError('environment not found')
        return self._environment

    def use(self, environment: MockEnvironment):
        """use the environment to support rooms contacts"""
        self._contact_payload_pool = environment.get_room_payloads()
        self._room_payload_pool = environment.get_room_payloads()

        self._environment = environment

    def create_contact(self) -> Contact:
        """create random contact"""
        self







