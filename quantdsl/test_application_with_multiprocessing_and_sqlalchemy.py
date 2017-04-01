from eventsourcing.tests.sequenced_item_tests.test_sqlalchemy_active_record_strategy import \
    WithSQLAlchemyActiveRecordStrategies


from quantdsl.test_application import ContractValuationTestsTestCase


class TestQuantDslApplicationWithMultiprocessingAndSQLAlchemy(WithSQLAlchemyActiveRecordStrategies,
                                                              ContractValuationTestsTestCase):
    use_named_temporary_file = True
