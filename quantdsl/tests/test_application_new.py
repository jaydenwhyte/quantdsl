import scipy
from eventsourcing.tests.sequenced_item_tests.base import WithActiveRecordStrategies
from eventsourcing.tests.sequenced_item_tests.test_sqlalchemy_active_record_strategy import \
    WithSQLAlchemyActiveRecordStrategies

from quantdsl.application.base import QuantdslApplication
from quantdsl.domain.model.market_calibration import MarketCalibration


class WithQuantdslApplication(WithActiveRecordStrategies):
    NUMBER_DAYS = 5
    NUMBER_MARKETS = 2
    NUMBER_WORKERS = 30
    PATH_COUNT = 2000

    def construct_application(self):
        app = QuantdslApplication(
            integer_sequenced_active_record_strategy=self.integer_sequence_active_record_strategy,
            timestamp_sequenced_active_record_strategy=self.timestamp_sequence_active_record_strategy,
        )
        return app

    def setUp(self):
        super(WithQuantdslApplication, self).setUp()
        scipy.random.seed(1354802735)
        self.app = self.construct_application()


class TestQuantDslApplication(WithSQLAlchemyActiveRecordStrategies, WithQuantdslApplication):
    def test_entities_and_registers(self):
        self.assertTrue(self.app)
        market_calibration = self.app.register_market_calibration('priceprocess1', calibration_params={})
        self.assertIsInstance(market_calibration, MarketCalibration)
        self.assertIn(market_calibration.id, self.app.market_calibration_repo)
        self.assertEqual(self.app.market_calibration_repo[market_calibration.id].id, market_calibration.id)
