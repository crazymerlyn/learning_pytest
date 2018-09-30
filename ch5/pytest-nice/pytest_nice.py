"""Code for pytest-nice plugin."""

import pytest

def pytest_addoption(parser):
    """Turn nice features on with --nice option."""
    parser.addini('nice', type='bool', help='Turn failures into opportunities.')
    group = parser.getgroup('nice')
    group.addoption('--nice', action='store_true',
                    help='nice: turn FAILED into OPPORTUNITY for improvement')

def pytest_report_header():
    """Thank tester for running tests."""
    if pytest.config.getoption('nice') or pytest.config.getini('nice'):
        return "Thanks for running the tests."

def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call':
        nice = (pytest.config.getoption('nice') or pytest.config.getini('nice'))
        if report.failed and nice:
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
