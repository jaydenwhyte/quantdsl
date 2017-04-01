from quantdsl.application.with_multithreading_and_python_objects import \
    QuantDslApplicationWithMultithreadingAndPythonObjects
from quantdsl.test_application import TestCase, ContractValuationTestsTestCase


class TestApplicationWithPythonObjectsAndMultithreading(TestCase, ContractValuationTestsTestCase):

    def setup_application(self):
        self.app = QuantDslApplicationWithMultithreadingAndPythonObjects(num_workers=self.NUMBER_WORKERS)
