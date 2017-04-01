from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish


class PerturbationDependencies(Entity):
    """
    Perturbation requirements are the names of the perturbed values required by call requirement with this entity ID.
    """
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, dependencies, **kwargs):
        super(PerturbationDependencies, self).__init__(**kwargs)
        self._dependencies = dependencies

    def __getitem__(self, item):
        return self._dependencies.__getitem__(item)

    @property
    def dependencies(self):
        return self._dependencies


def register_perturbation_dependencies(call_requirement_id, dependencies):
    created_event = PerturbationDependencies.Created(entity_id=call_requirement_id, dependencies=dependencies)
    perturbation_dependencies = PerturbationDependencies.mutate(event=created_event)
    publish(created_event)
    return perturbation_dependencies


