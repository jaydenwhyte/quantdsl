from eventsourcing.domain.model.events import subscribe, unsubscribe

from quantdsl.domain.model.market_simulation import MarketSimulation
from quantdsl.domain.services.simulated_prices import generate_simulated_prices


class SimulationSubscriber(object):
    # When a market simulation is created, generate and register all the simulated prices.

    def __init__(self, market_calibration_repo, market_simulation_repo):
        self.market_calibration_repo = market_calibration_repo
        self.market_simulation_repo = market_simulation_repo
        subscribe(
            predicate=self.is_market_simulation_created,
            handler=self.generate_simulated_prices_for_market_simulation,
        )

    def close(self):
        unsubscribe(
            predicate=self.is_market_simulation_created,
            handler=self.generate_simulated_prices_for_market_simulation,
        )

    def is_market_simulation_created(self, event):
        return isinstance(event, MarketSimulation.Created)

    def generate_simulated_prices_for_market_simulation(self, event):
        assert isinstance(event, MarketSimulation.Created)
        market_simulation = self.market_simulation_repo[event.entity_id]
        market_calibration = self.market_calibration_repo[event.market_calibration_id]
        generate_simulated_prices(market_simulation, market_calibration)
