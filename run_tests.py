#!/usr/bin/env python
# import os, sys
import sys
from unittest import TestSuite

from boot_django import boot_django

# call the django setup routine
boot_django()


def get_suite():
    from django.test.runner import DiscoverRunner
    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(["lumberjack.tests"])
    if failures:
        sys.exit(failures)

    # in case this is called from setup tools, return a test suite
    return TestSuite()


if __name__ == "__main__":
    get_suite()
