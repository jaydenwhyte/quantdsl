from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish


class DependencyGraph(Entity):
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, contract_specification_id, **kwargs):
        super(DependencyGraph, self).__init__(**kwargs)
        self._contract_specification_id = contract_specification_id

    @property
    def contract_specification_id(self):
        return self._contract_specification_id


def register_dependency_graph(contract_specification_id):
    created_event = DependencyGraph.Created(entity_id=contract_specification_id, contract_specification_id=contract_specification_id)
    contract_specification = DependencyGraph.mutate(event=created_event)
    publish(created_event)
    return contract_specification


