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
    Union,
    TYPE_CHECKING
)
from uuid import uuid4
from collections import defaultdict
from pyee import AsyncIOEventEmitter
import json
from datetime import datetime
from dataclasses import dataclass
from wechaty_puppet import (
    ContactPayload,
    RoomPayload,
    MessagePayload,
    Puppet,
    get_logger,
    EventType,
    FileBox,
    MessageType
)
from wechaty import (
    Contact,
    Room,
    Message
)

if TYPE_CHECKING:
    from wechaty import Contact

from wechaty_puppet_mock.mock.envrioment import EnvironmentMock
from wechaty_puppet_mock.exceptions import WechatyPuppetMockError

log = get_logger('Mocker')


@dataclass
class MockerResponse:
    """this is the common data-structure for mocker"""
    type: int
    payload: str


class Mocker(AsyncIOEventEmitter):
    """mock fake data"""
    def __init__(self):
        super().__init__()
        self.id: str = str(uuid4())

        # login user is set when the method login
        self.login_user: Optional[Contact] = None
        self.has_login: bool = False

        self._contact_payload_pool: Dict[str, ContactPayload] = \
            defaultdict(ContactPayload)
        self._room_payload_pool: Dict[str, RoomPayload] = \
            defaultdict(RoomPayload)
        self._message_payload_pool: Dict[str, MessagePayload] = \
            defaultdict(MessagePayload)

        self._environment: Optional[EnvironmentMock] = None
        self.Contact: Type[Contact] = Contact
        self.Room: Type[Room] = Room
        self.Message: Type[Message] = Message

    def init_puppet(self, puppet: Puppet):
        """init the puppet """
        self.Contact.set_puppet(puppet)
        self.Room.set_puppet(puppet)
        self.Message.set_puppet(puppet)

    @property
    def environment(self) -> EnvironmentMock:
        """get the environment for mocker"""
        log.info('use the environment')
        if not self._environment:
            raise WechatyPuppetMockError('environment not found')
        return self._environment

    def use(self, environment: EnvironmentMock):
        """use the environment to support rooms contacts"""
        log.info('use the environment <{%s}>', environment)

        self._contact_payload_pool = environment.get_room_payloads()
        self._room_payload_pool = environment.get_room_payloads()

        self._environment = environment

    def new_room(self) -> Room:
        """create random room"""
        payload = self._environment.new_room_payload()
        room = self.Room.load(payload.id)
        room.payload = payload

        log.info('create random room <%s>', room)
        return room

    def new_contact(self) -> Contact:
        """create random contact"""
        payload = self.environment.new_contact_payload()
        contact = self.Contact.load(payload.id)
        contact.payload = contact

        log.info('create random contact <%s>')
        return contact

    def scan(self, scan_code: str):
        """emit the scan event"""
        log.info('emit the scan event')
        scan_event_payload = {
            'qrcode': scan_code,
            'status': 3
        }
        response = MockerResponse(
            type=int(EventType.EVENT_TYPE_SCAN),
            payload=json.dumps(scan_event_payload)
        )
        self.emit('scan', response)

    def login(self, user: Contact):
        """emit the login user event"""
        log.info('mock the user <%s> login event', user)
        login_event_payload = {
            'contactId': user.contact_id
        }
        response = MockerResponse(
            type=int(EventType.EVENT_TYPE_LOGIN),
            payload=json.dumps(login_event_payload)
        )
        self.emit('event', response)

    def send_message(self,
                     talker: Contact,
                     conversation: Union[Contact, Room],
                     msg: Union[str, FileBox],
                     msg_type: MessageType):
        """mock the talker send message event

        In this version, we will only support str and FileBox message type
        """
        log.info('mock send message event')
        message_payload = MessagePayload(
            id=str(uuid4()),
            from_id=talker.contact_id,
            timestamp=int(datetime.now().timestamp() * 1000),
            type=msg_type
        )
        if isinstance(conversation, Contact):
            message_payload.to_id = conversation.contact_id
        else:
            message_payload.room_id = conversation.room_id

        if isinstance(msg, str):
            message_payload.text = msg
        else:
            message_payload.filename = msg.name

        # save the message payload to environment
        self.environment.add_message_payload(message_payload)

        response = MockerResponse(
            type=int(EventType.EVENT_TYPE_MESSAGE),
            payload=json.dumps({
                'messageId': message_payload.id
            })
        )
        self.emit('event', response)
