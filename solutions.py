##  Questions...

"""
1. Create an assert statement that throws an AssertionError if the variable spam is a 
negative integer.
2. Write an assert statement that triggers an AssertionError if the variables eggs 
and bacon contain
strings that are the same as each other, even if their cases are different 
(that is, &#39;hello&#39; and &#39;hello&#39; are
considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same).
3. Create an assert statement that throws an AssertionError every time.
4. What are the two lines that must be present in your software in order to call 
logging.debug()?
5. What are the two lines that your program must have in order to have logging.debug() send a
logging message to a file named programLog.txt?
6. What are the five levels of logging?
7. What line of code would you add to your software to disable all logging messages?
8.Why is using logging messages better than using print() to display the same message?
9. What are the differences between the Step Over, Step In, and Step Out buttons in the 
debugger?
10.After you click Continue, when will the debugger stop ?
11. What is the concept of a breakpoint?

"""

## Answers...

"""
1. assert spam >= 0, 'spam should be a non-negative integer'

-------------------------------------------------------------------------------------------------------------

2. assert eggs.lower() != bacon.lower(), 'eggs and bacon should have different values'

-------------------------------------------------------------------------------------------------------------

3. assert False, 'This assertion always fails'

-------------------------------------------------------------------------------------------------------------

4.The two lines that must be present in your software in order to call logging.debug() are:

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

-------------------------------------------------------------------------------------------------------------

5.To have logging.debug() send a logging message to a file named programLog.txt, you need to add 
the following two lines of code:

import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
6.The five levels of logging are:
DEBUG
INFO
WARNING
ERROR
CRITICAL

-------------------------------------------------------------------------------------------------------------

7. To disable all logging messages, you can add the following line of code:

logging.disable(logging.CRITICAL)

-------------------------------------------------------------------------------------------------------------

8.Using logging messages is better than using print() because:

i) Logging messages can be easily turned on and off by changing the logging level, whereas print 
statements require code changes.

ii) Logging messages can be directed to different output destinations (such as files, emails, or syslog) 
using handlers, whereas print statements are always sent to the console.

iii) Logging messages can include timestamps, log levels, and other metadata that can be helpful for 
debugging and auditing.

-------------------------------------------------------------------------------------------------------------

9.The Step Over button allows you to execute the current line of code and move to the next line, 
without stepping into any function calls. The Step In button allows you to step into the current 
function call and continue debugging inside the function. The Step Out button allows you to continue 
execution until the current function returns and control is returned to the calling function.

-------------------------------------------------------------------------------------------------------------

10.The debugger will stop again when it encounters the next breakpoint or when the program finishes executing.

-------------------------------------------------------------------------------------------------------------

11. A breakpoint is a specific point in the code where the debugger should pause execution so that 
you can inspect the program's state and variables. You can set breakpoints in your code using your 
IDE or debugger, and you can also remove or disable them as needed.

-------------------------------------------------------------------------------------------------------------


"""