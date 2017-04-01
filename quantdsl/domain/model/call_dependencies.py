import uuid
from uuid import UUID

from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish


class CallDependencies(Entity):
    """
    A call dependency is a call that must be evaluated before this call can be evaluated.
    """
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, dependencies, call_id, **kwargs):
        super(CallDependencies, self).__init__(**kwargs)
        self._dependencies = dependencies
        self._call_id = call_id

    def __getitem__(self, item):
        return self._dependencies.__getitem__(item)

    @property
    def dependencies(self):
        return self._dependencies

    @property
    def call_id(self):
        return self._call_id


def register_call_dependencies(call_id, dependencies):
    created_event = CallDependencies.Created(
        entity_id=call_dependencies_id_from_call_id(call_id),
        call_id=call_id,
        dependencies=dependencies,
    )
    call_dependencies = CallDependencies.mutate(event=created_event)
    publish(created_event)
    return call_dependencies


def call_dependencies_id_from_call_id(call_id):
    return uuid.uuid5(NAMESPACE_CALL_DEPENDENCIES_ID, str(call_id))


NAMESPACE_CALL_DEPENDENCIES_ID = UUID('c25801e7-1665-4483-9eed-6452d8c0431a')
