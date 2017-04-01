import uuid
from collections import namedtuple
from uuid import UUID

from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish

StubbedCall = namedtuple('StubbedCall', ['call_id', 'dsl_expr', 'effective_present_time', 'requirements'])


class CallRequirement(Entity):
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, dsl_source, effective_present_time, call_id, **kwargs):
        super(CallRequirement, self).__init__(**kwargs)
        self._dsl_source = dsl_source
        self._effective_present_time = effective_present_time
        self._call_id = call_id
        self._dsl_expr = None

    @property
    def dsl_source(self):
        return self._dsl_source

    @property
    def effective_present_time(self):
        return self._effective_present_time


def register_call_requirement(call_id, dsl_source, effective_present_time):
    created_event = CallRequirement.Created(
        entity_id=call_requirement_id_from_call_id(call_id),
        call_id=call_id,
        dsl_source=dsl_source,
        effective_present_time=effective_present_time
    )
    call_requirement = CallRequirement.mutate(event=created_event)
    publish(created_event)
    return call_requirement


def call_requirement_id_from_call_id(call_id):
    return uuid.uuid5(NAMESPACE_CALL_REQUIREMENT_ID, str(call_id))


NAMESPACE_CALL_REQUIREMENT_ID = UUID('94090a4c-5690-46d2-ba3e-893dd1e6af16')