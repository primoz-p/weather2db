#!/usr/bin/env python
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def main():
    from unittest import TestLoader, TestSuite
    from xmlrunner import XMLTestRunner

    import collect_data_tests

    suites = [
        TestLoader().loadTestsFromTestCase(collect_data_tests.Test),
    ]

    tests_results_dir = "test-reports-python"
    XMLTestRunner(output=tests_results_dir).run(TestSuite(suites))


if __name__ == "__main__":
    main()
