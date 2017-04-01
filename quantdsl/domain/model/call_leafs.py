import uuid
from uuid import UUID

from eventsourcing.domain.model.events import publish

from quantdsl.domain.model.base import Entity


class CallLeafs(Entity):
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, leaf_ids, dependency_graph_id, **kwargs):
        super(CallLeafs, self).__init__(**kwargs)
        self._leaf_ids = leaf_ids
        self._dependency_graph_id = dependency_graph_id

    @property
    def leaf_ids(self):
        return self._leaf_ids

    @property
    def dependency_graph_id(self):
        return self._dependency_graph_id


def register_call_leafs(dependency_graph_id, leaf_ids):
    created_event = CallLeafs.Created(
        entity_id=call_leafs_id_from_dependency_graph_id(dependency_graph_id),
        dependency_graph_id=dependency_graph_id,
        leaf_ids=leaf_ids,
    )
    call_leafs = CallLeafs.mutate(event=created_event)
    publish(created_event)
    return call_leafs


def call_leafs_id_from_dependency_graph_id(dependency_graph_id):
    return uuid.uuid5(NAMESPACE_CALL_LEAFS_ID, str(dependency_graph_id))


NAMESPACE_CALL_LEAFS_ID = UUID('1c0e6e9a-f83b-4b3d-b62f-b635f8d577ca')
