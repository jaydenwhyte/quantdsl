from quantdsl.domain.model.base import Entity
from eventsourcing.domain.model.events import publish
from quantdsl.domain.services.uuids import create_uuid4


class MarketCalibration(Entity):
    class Created(Entity.Created):
        pass

    class Discarded(Entity.Discarded):
        pass

    def __init__(self, price_process_name, calibration_params, **kwargs):
        super(MarketCalibration, self).__init__(**kwargs)
        self._price_process_name = price_process_name
        self._calibration_params = calibration_params

    @property
    def price_process_name(self):
        return self._price_process_name

    @property
    def calibration_params(self):
        return self._calibration_params


def register_market_calibration(price_process_name, calibration_params):
    created_event = MarketCalibration.Created(entity_id=create_uuid4(),
                                              price_process_name=price_process_name,
                                              calibration_params=calibration_params)
    call_result = MarketCalibration.mutate(event=created_event)
    publish(created_event)
    return call_result


def compute_market_calibration_params(price_process_name, historical_data):
    # Todo: Generate model params from historical price data.
    return {}


