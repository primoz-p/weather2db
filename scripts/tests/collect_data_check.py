#!/usr/bin/env python
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def main():
    from unittest import TestLoader, TestSuite
    from xmlrunner import XMLTestRunner

    import db_checks

    suites = [
        TestLoader().loadTestsFromTestCase(db_checks.Test),
    ]

    tests_results_dir = "test-reports-python"
    result = XMLTestRunner(output=tests_results_dir).run(TestSuite(suites))
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    main()
