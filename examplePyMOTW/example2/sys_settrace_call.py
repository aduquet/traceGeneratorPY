# import sys
# import threading

# def trace_calls(frame, event, arg):
#     if event != 'call':
#         return
#     co = frame.f_code
#     func_name = co.co_name
#     if func_name == 'write':
#         # Ignore write() calls from print statements
#         return
#     func_line_no = frame.f_lineno
#     func_filename = co.co_filename
#     caller = frame.f_back
#     caller_line_no = caller.f_lineno
#     caller_filename = caller.f_code.co_filename
#     print( 'Call to %s on line %s of %s from line %s of %s' % \
#         (func_name, func_line_no, func_filename,
#          caller_line_no, caller_filename))
#     return

# def b():
#     print ('in b()')

# def a():
#     print ('in a()')
#     b()

# sys.settrace(trace_calls)
# a()

#!/usr/bin/env python
# encoding: utf-8

# import sys

# def trace_lines(frame, event, arg):
#     if event != 'line':
#         return
#     co = frame.f_code
#     func_name = co.co_name
#     line_no = frame.f_lineno
#     filename = co.co_filename
#     print( '  %s line %s' % (func_name, line_no))

# def trace_calls(frame, event, arg):
#     if event != 'call':
#         return
#     co = frame.f_code
#     func_name = co.co_name
#     if func_name == 'write':
#         # Ignore write() calls from print statements
#         return
#     line_no = frame.f_lineno
#     filename = co.co_filename
#     print ('Call to %s on line %s of %s' % (func_name, line_no, filename))
#     if (func_name in TRACE_INTO):
#         # Trace into this function
#         return trace_lines
#     return

# def c(input):
#     print( 'input =', input)
#     print( 'Leaving c()')

# def b(arg):
#     val = arg * 5
#     c(val)
#     print( 'Leaving b()')

# def a():
#     b(2)
#     print( 'Leaving a()')
    
# TRACE_INTO = ['a']

# sys.settrace(trace_calls)
# a()

import sys
from prueba import *

def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print ('Call to %s on line %s of %s' % (func_name, line_no, filename))
        return trace_calls_and_returns
    elif event == 'return':
        print ('%s => %s' % (func_name, arg))
    return


sys.settrace(trace_calls_and_returns)
a()