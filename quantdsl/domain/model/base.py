from eventsourcing.domain.model.entity import TimestampedVersionedEntity, Created, Discarded


class Entity(TimestampedVersionedEntity):

    class Created(Created):
        pass

    class Discarded(Discarded):
        pass