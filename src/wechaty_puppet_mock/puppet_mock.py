"""
Code Generator - https://github.com/wj-Mcat/code-generator

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
from __future__ import annotations

from typing import List, Optional

from wechaty_puppet import (
    Puppet, FileBox, RoomQueryFilter,
    MiniProgramPayload, UrlLinkPayload, MessageQueryFilter,
    PuppetOptions
)
from wechaty_puppet.schemas.types import (
    MessagePayload,
    ContactPayload,
    FriendshipPayload,
    ImageType,
    RoomInvitationPayload,
    RoomPayload,
    RoomMemberPayload
)


class PuppetMock(Puppet):
    """mock for puppet"""
    def __init__(self, options: PuppetOptions, name: str = 'puppet-mock'):
        super().__init__(options, name)

    async def message_image(self, message_id: str,
                            image_type: ImageType) -> FileBox:
        """"""
        pass

    async def ding(self, data: Optional[str] = None):
        pass

    def on(self, event_name: str, caller):
        pass

    def listener_count(self, event_name: str) -> int:
        pass

    async def start(self) -> None:
        pass

    async def stop(self):
        pass

    async def contact_list(self) -> List[str]:
        pass

    async def tag_contact_delete(self, tag_id: str) -> None:
        pass

    async def tag_favorite_delete(self, tag_id: str) -> None:
        pass

    async def tag_contact_add(self, tag_id: str, contact_id: str):
        pass

    async def tag_favorite_add(self, tag_id: str, contact_id: str):
        pass

    async def tag_contact_remove(self, tag_id: str, contact_id: str):
        pass

    async def tag_contact_list(self,
                               contact_id: Optional[str] = None) -> List[str]:
        pass

    async def message_send_text(self, conversation_id: str, message: str,
                                mention_ids: List[str] = None) -> str:
        pass

    async def message_send_contact(self, contact_id: str,
                                   conversation_id: str) -> str:
        pass

    async def message_send_file(self, conversation_id: str,
                                file: FileBox) -> str:
        pass

    async def message_send_url(self, conversation_id: str, url: str) -> str:
        pass

    async def message_send_mini_program(
        self, conversation_id: str,
        mini_program: MiniProgramPayload
    ) -> str:
        pass

    async def message_search(self, query: Optional[MessageQueryFilter] = None
                             ) -> List[str]:
        pass

    async def message_recall(self, message_id: str) -> bool:
        pass

    async def message_payload(self, message_id: str) -> MessagePayload:
        pass

    async def message_forward(self, to_id: str, message_id: str):
        pass

    async def message_file(self, message_id: str) -> FileBox:
        pass

    async def message_contact(self, message_id: str) -> str:
        pass

    async def message_url(self, message_id: str) -> UrlLinkPayload:
        pass

    async def message_mini_program(self, message_id: str) -> MiniProgramPayload:
        pass

    async def contact_alias(self, contact_id: str,
                            alias: Optional[str] = None) -> str:
        pass

    async def contact_payload_dirty(self, contact_id: str):
        pass

    async def contact_payload(self, contact_id: str) -> ContactPayload:
        pass

    async def contact_avatar(self, contact_id: str,
                             file_box: Optional[FileBox] = None) -> FileBox:
        pass

    async def contact_tag_ids(self, contact_id: str) -> List[str]:
        pass

    def self_id(self) -> str:
        pass

    async def friendship_search(self, weixin: Optional[str] = None,
                                phone: Optional[str] = None) -> Optional[str]:
        pass

    async def friendship_add(self, contact_id: str, hello: str):
        pass

    async def friendship_payload(self, friendship_id: str,
                                 payload: Optional[FriendshipPayload] = None
                                 ) -> FriendshipPayload:
        pass

    async def friendship_accept(self, friendship_id: str):
        pass

    async def room_list(self) -> List[str]:
        pass

    async def room_create(self, contact_ids: List[str],
                          topic: str = None) -> str:
        pass

    async def room_search(self, query: RoomQueryFilter = None) -> List[str]:
        pass

    async def room_invitation_payload(self,
                                      room_invitation_id: str,
                                      payload: Optional[
                                          RoomInvitationPayload] = None
                                      ) -> RoomInvitationPayload:
        pass

    async def room_invitation_accept(self, room_invitation_id: str):
        pass

    async def contact_self_qr_code(self) -> str:
        pass

    async def contact_self_name(self, name: str):
        pass

    async def contact_signature(self, signature: str):
        pass

    async def room_payload(self, room_id: str) -> RoomPayload:
        pass

    async def room_members(self, room_id: str) -> List[str]:
        pass

    async def room_add(self, room_id: str, contact_id: str):
        pass

    async def room_delete(self, room_id: str, contact_id: str):
        pass

    async def room_quit(self, room_id: str):
        pass

    async def room_topic(self, room_id: str, new_topic: str):
        pass

    async def room_announce(self, room_id: str,
                            announcement: str = None) -> str:
        pass

    async def room_qr_code(self, room_id: str) -> str:
        pass

    async def room_member_payload(self, room_id: str,
                                  contact_id: str) -> RoomMemberPayload:
        pass

    async def room_avatar(self, room_id: str) -> FileBox:
        pass

    async def logout(self):
        pass

    async def login(self, user_id: str):
        pass
