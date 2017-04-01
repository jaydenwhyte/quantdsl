from eventsourcing.domain.model.events import subscribe, unsubscribe
from quantdsl.domain.model.contract_specification import ContractSpecification
from quantdsl.domain.services.dependency_graphs import generate_dependency_graph


class DependencyGraphSubscriber(object):

    def __init__(self, contract_specification_repo, call_dependencies_repo, call_dependents_repo, call_leafs_repo,
                 call_requirement_repo):
        self.contract_specification_repo = contract_specification_repo
        self.call_dependencies_repo = call_dependencies_repo
        self.call_dependents_repo = call_dependents_repo
        self.call_leafs_repo = call_leafs_repo
        self.call_requirement_repo = call_requirement_repo
        subscribe(
            predicate=self.contract_specification_created,
            handler=self.generate_dependency_graph,
        )

    def close(self):
        unsubscribe(
            predicate=self.contract_specification_created,
            handler=self.generate_dependency_graph,
        )

    def contract_specification_created(self, event):
        return isinstance(event, ContractSpecification.Created)

    def generate_dependency_graph(self, event):
        assert isinstance(event, ContractSpecification.Created)
        contract_specification = self.contract_specification_repo[event.entity_id]
        generate_dependency_graph(contract_specification, self.call_dependencies_repo, self.call_dependents_repo,
                                  self.call_leafs_repo, self.call_requirement_repo)