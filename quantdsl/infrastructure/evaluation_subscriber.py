from eventsourcing.domain.model.events import subscribe, unsubscribe

from quantdsl.domain.model.contract_valuation import ContractValuation
from quantdsl.domain.services.contract_valuations import generate_contract_valuation


class EvaluationSubscriber(object):

    def __init__(self, contract_valuation_repo, call_link_repo, call_dependencies_repo, call_requirement_repo,
                 call_result_repo, simulated_price_repo, market_simulation_repo, call_leafs_repo,
                 call_evaluation_queue, result_counters, usage_counters, call_dependents_repo,
                 perturbation_dependencies_repo, simulated_price_requirements_repo):
        self.contract_valuation_repo = contract_valuation_repo
        self.call_link_repo = call_link_repo
        self.call_dependencies_repo = call_dependencies_repo
        self.call_requirement_repo = call_requirement_repo
        self.call_result_repo = call_result_repo
        self.simulated_price_repo = simulated_price_repo
        self.market_simulation_repo = market_simulation_repo
        self.call_leafs_repo = call_leafs_repo
        self.call_evaluation_queue = call_evaluation_queue
        self.result_counters = result_counters
        self.usage_counters = usage_counters
        self.call_dependents_repo = call_dependents_repo
        self.perturbation_dependencies_repo = perturbation_dependencies_repo
        self.simulated_price_dependencies_repo = simulated_price_requirements_repo
        subscribe(
            predicate=self.contract_valuation_created,
            handler=self.generate_contract_valuation
        )

    def close(self):
        unsubscribe(
            predicate=self.contract_valuation_created,
            handler=self.generate_contract_valuation
        )

    def contract_valuation_created(self, event):
        return isinstance(event, ContractValuation.Created)

    def generate_contract_valuation(self, event):
        assert isinstance(event, ContractValuation.Created)
        generate_contract_valuation(contract_valuation_id=event.entity_id,
                                    call_dependencies_repo=self.call_dependencies_repo,
                                    call_evaluation_queue=self.call_evaluation_queue,
                                    call_leafs_repo=self.call_leafs_repo,
                                    call_link_repo=self.call_link_repo,
                                    call_requirement_repo=self.call_requirement_repo,
                                    call_result_repo=self.call_result_repo,
                                    contract_valuation_repo=self.contract_valuation_repo,
                                    market_simulation_repo=self.market_simulation_repo,
                                    simulated_price_repo=self.simulated_price_repo,
                                    result_counters=self.result_counters,
                                    usage_counters=self.usage_counters,
                                    call_dependents_repo=self.call_dependents_repo,
                                    perturbation_dependencies_repo=self.perturbation_dependencies_repo,
                                    simulated_price_dependencies_repo=self.simulated_price_dependencies_repo,
                                    )
