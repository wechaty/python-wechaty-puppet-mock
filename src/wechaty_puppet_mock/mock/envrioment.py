"""
python wechaty - https://github.com/wj-Mcat/python-wechaty-puppet-mock

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
import os
from collections import defaultdict
from typing import (
    Dict,
    Optional,
    List
)
import random
from wechaty_puppet import (
    ContactPayload,
    ContactGender,
    ContactType,

    RoomPayload,
    MessagePayload,

    FileBox
)
from wechaty_puppet_mock.config import get_image_base64_data
from faker import Faker

faker = Faker('zh-CH')

BASE_URL = os.path.abspath(os.path.basename(__file__))


class MockEnvironment:
    """get the simple mock environment"""

    def __init__(self,
                 room_num: int = 3,
                 contact_num: int = 30,
                 message_num: int = 10):
        """init the environment for mocker"""
        self._contact_payload_pool: Dict[str, ContactPayload] = \
            defaultdict(ContactPayload)
        self._room_payload_pool: Dict[str, RoomPayload] = \
            defaultdict(RoomPayload)
        self._message_payload_pool: Dict[str, MessagePayload] = \
            defaultdict(MessagePayload)

        self._login_user_payload = self._get_random_contact_payload()

        self._init_contacts(contact_num)

    @staticmethod
    def _get_random_contact_payload() -> ContactPayload:
        """get random contact payload"""
        temp_id = faker.uuid4()
        payload = ContactPayload(
            id=f'contact-{temp_id}',
            gender=ContactGender(faker.random.randint(0, 3)),
            type=ContactType(faker.random.randint(0, 3)),
            name=faker.name(),
            avatar=get_image_base64_data(),
            address=faker.address(),
            alias=faker.name(),
            city=faker.city(),
            friend=True,
            province=faker.province(),
            signature=faker.sentence(),
            star=(faker.random.randint(0, 2) % 2 == 0),
            weixin=f'weixin-{temp_id}'
        )
        return payload

    def _init_contacts(self, contact_num: int):
        """init contacts payload"""
        # read sample file content from FileBox
        for i in range(contact_num):
            random_payload = self._get_random_contact_payload()
            self._contact_payload_pool[random_payload.id] = random_payload

    def _init_rooms(self, room_num: int):
        """init rooms payload after contacts created"""
        avatar = get_image_base64_data()
        contact_ids = list(self._contact_payload_pool.keys())
        for i in range(room_num):
            temp_id = faker.uuid4()
            random_payload = RoomPayload(
                id=f'room-{temp_id}',
                topic=faker.sentence(),
                avatar=avatar,
                owner_id=self._login_user_payload.id,
                admin_ids=[],
                member_ids=random.sample(
                    contact_ids,
                    random.randint(0, len(contact_ids))
                )
            )
            self._room_payload_pool[random_payload.id] = random_payload

    def get_room_payloads(self) -> List[RoomPayload]:
        """get fake room payloads"""
        return list(self._room_payload_pool.values())

    def get_contact_payloads(self) -> List[ContactPayload]:
        """get fake contact payloads"""
        return list(self._contact_payload_pool.values())
