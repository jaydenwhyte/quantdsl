import uuid
from uuid import UUID

from eventsourcing.domain.model.events import publish

from quantdsl.domain.model.base import Entity


class CallDependents(Entity):
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, dependents, call_id, **kwargs):
        super(CallDependents, self).__init__(**kwargs)
        self._dependents = dependents
        self._call_id = call_id

    def __getitem__(self, item):
        return self._dependents.__getitem__(item)

    @property
    def dependents(self):
        return self._dependents

    @property
    def call_id(self):
        return self._call_id


def register_call_dependents(call_id, dependents):
    created_event = CallDependents.Created(
        entity_id=call_dependents_id_from_call_id(call_id),
        call_id=call_id,
        dependents=dependents,
    )
    call_dependents = CallDependents.mutate(event=created_event)
    publish(created_event)
    return call_dependents


def call_dependents_id_from_call_id(call_id):
    return uuid.uuid5(NAMESPACE_CALL_DEPENDENTS_ID, str(call_id))


NAMESPACE_CALL_DEPENDENTS_ID = UUID('302c66cb-19b0-47fa-af00-56fce9d9930f')
