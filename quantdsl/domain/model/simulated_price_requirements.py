from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish


class SimulatedPriceRequirements(Entity):
    """
    Simulated price requirements are the IDs of the simulated prices required by the call requirement with the same ID.
    """
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, requirements, **kwargs):
        super(SimulatedPriceRequirements, self).__init__(**kwargs)
        self._requirements = requirements

    def __getitem__(self, item):
        return self._requirements.__getitem__(item)

    @property
    def requirements(self):
        return self._requirements


def register_simulated_price_requirements(call_requirement_id, requirements):
    assert isinstance(requirements, list), type(requirements)
    event = SimulatedPriceRequirements.Created(entity_id=call_requirement_id, requirements=requirements)
    entity = SimulatedPriceRequirements.mutate(event=event)
    publish(event)
    return entity
