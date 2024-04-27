#!/usr/bin/env python3

""" Test for Task1: Checking the functionality in 'task1.py' using assertions """

import unittest
import io
import sys
import runpy  # not importing task1 directly, this is later run using runpy.run_path


class Test(unittest.TestCase):

    def test_task1(self):
        task1_stdout_stream = io.StringIO()
        sys.stdout = task1_stdout_stream  # start redirection of stdout
        runpy.run_path("task1.py", run_name="__main__")
        sys.stdout = sys.__stdout__  # stop redirection of stdout
        task1_stdout = task1_stdout_stream.getvalue()

        self.assertTrue("210" in task1_stdout,
                        "result of 'sum from 1 to 20' not present in output")

        self.assertTrue("1024" in task1_stdout,
                        "result of '2 to the power of 10' not present in output")

        self.assertTrue("1048576" in task1_stdout,
                        "result of '2 to the power of 20' not present in output")


if __name__ == "__main__":
    unittest.main()
