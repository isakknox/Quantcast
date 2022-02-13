import unittest
import subprocess
import sys
from io import StringIO

class TestActiveCookies(unittest.TestCase):
# I use writing and reading to a file output.txt to test my print statements because print has no return value
# and this seemed to be the most effective way to store the printed value in the other script.
    def __init__(self):
        return

    def testDefault():
        # Test if it returns correct output on normal set with one answer
        file = open('output.txt','r+')
        subprocess.run(["python", "most_active_cookie.py", "cookie_log.csv", "-d", "2018-12-09"])
        printedMessage = file.readlines()
        file.close()
        printedMessage[0] = printedMessage[0].split()
        assert(printedMessage[0][0] == 'AtY0laUfhglK3lC7')
        # Test if it returns correct output for same set with nultiple answers
        file = open('output.txt','r+')
        subprocess.run(["python", "most_active_cookie.py", "cookie_log.csv", "-d", "2018-12-08"])
        printedMessage = file.readlines()
        file.close()
        for i in range(len(printedMessage)):
            printedMessage[i] = printedMessage[i].split()
        assert(printedMessage[0][0] == 'SAZuXPGUrfbcn5UA' and printedMessage[1][0] == '4sMM2LxV07bPJzwf' and printedMessage[2][0] == 'fbcn5UAVanZf6UtG')

    def testLonger():
        # Test if it works on a bigger set
        file = open('output.txt','r+')
        subprocess.run(["python", "most_active_cookie.py", "cookie_log2.csv", "-d", "2019-11-12"])
        printedMessage = file.readlines()
        file.close()
        printedMessage[0] = printedMessage[0].split()
        assert(printedMessage[0][0] == 'cJdjJSVC6e73Hcjd')
        # Test again for multiple outputs on a bigger set
        file = open('output.txt','r+')
        subprocess.run(["python", "most_active_cookie.py", "cookie_log2.csv", "-d", "2019-11-14"])
        printedMessage = file.readlines()
        file.close()
        printedMessage[0] = printedMessage[0].split()
        assert(printedMessage[0][0] == 'RtY4laMMT6nU91hJ')

TestActiveCookies.testDefault()
TestActiveCookies.testLonger()
print("All test cases passed! Congrats!")
