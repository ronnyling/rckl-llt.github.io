from robot.api import SuiteVisitor


class TestStatusChecker(SuiteVisitor):

    def __init__(self, *args):
        pass

    def visit_test(self, test):
        if 'PASS' in test.message and 'Re-executed test has been merged' in test.message:
            test.status = 'PASS'
            test.message = 'Test passed because it passed at least once.'
