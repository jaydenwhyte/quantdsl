import uuid
from uuid import UUID

from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish


class CallLink(Entity):
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, call_id, **kwargs):
        super(CallLink, self).__init__(**kwargs)
        self._call_id = call_id

    @property
    def call_id(self):
        return self._call_id


def register_call_link(link_id, call_id):
    created_event = CallLink.Created(entity_id=link_id, call_id=call_id)
    call_link = CallLink.mutate(event=created_event)
    publish(created_event)
    return call_link


def call_link_id_from_call_id(call_id):
    return uuid.uuid5(NAMESPACE_CALL_LINK_ID, str(call_id))


NAMESPACE_CALL_LINK_ID = UUID('a4b644f2-1fe0-4730-90f7-eec649104686')
