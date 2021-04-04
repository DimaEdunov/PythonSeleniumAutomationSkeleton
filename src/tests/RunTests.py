# This class will make our lives easier once running test suites
import os
""" NOTICE : 
1) When you run a suite, make sure that all commands are in comment, beside 1
2) Edit the 'developer' variable value, and place your own name
3) Edit the brand you are running on = newforexstage2, analystq and so on
4) Edit Headless True/False
"""

"""Run regression suite """
#os.system("pytest -v -s --alluredir="'C:\AllureReports\Data'" --html=report.html --self-contained-html -m=regression --brand=newforexstage2 --dist=loadfile -n=2 --headless=False")


"""Run dev suite """
os.system("pytest -v -s --alluredir="'C:\AllureReports\Data'" --html=report.html --developer=dima --self-contained-html -m=dev --brand=analystq --headless=False")

"""Run environment preparation suite """
#os.system("pytest -v -s --alluredir="'C:\AllureReports\Data'" --html=report.html --developer=dima --self-contained-html -m=environment --brand=onorio --dist=loadfile -n=2 --headless=False")
