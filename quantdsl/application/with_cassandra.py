from eventsourcing.application.with_cassandra import EventSourcingWithCassandra
from quantdsl.application.base import QuantdslApplication


DEFAULT_QUANTDSL_CASSANDRA_KEYSPACE = 'quantdsl'


class QuantDslApplicationWithCassandra(EventSourcingWithCassandra, QuantdslApplication):

    def __init__(self, default_keyspace=DEFAULT_QUANTDSL_CASSANDRA_KEYSPACE, *args, **kwargs):
        super(QuantDslApplicationWithCassandra, self).__init__(default_keyspace=default_keyspace, *args, **kwargs)


