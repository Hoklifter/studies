#!/usr/bin/env python3


'''
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''
from datetime import datetime
print(f"""Current date and time :
{str(datetime.now())[:-7]}""")
