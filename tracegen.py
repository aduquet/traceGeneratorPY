
from inspect import formatargspec, getfullargspec
import inspect
import sys

def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    # print('****',formatargspec(getfullargspec(co)))
    # print(co)
    print(co.co_varnames)
    print(co.co_names)
    if event == 'call':
        print ('Call to %s on line %s of %s' % (func_name, line_no, filename))
        return trace_calls_and_returns
    elif event == 'return':
        print ('%s => %s' % (func_name, arg))
        print('===============', type(arg))
    
    # elif func_name in TRACE_INTO:
    #     # Trace into this function
    #     return trace_lines
    return

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print ('  %s line %s' % (func_name, line_no))

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
#     print( 'Call to %s on line %s of %s' % (func_name, line_no, filename))
#     if func_name in TRACE_INTO:
#         # Trace into this function
#         return trace_lines
#     return
TRACE_INTO = ['add']
# # a = [1,2,3]
# # # b = ['a',' d', 'v']
# # b = [1,2,3]
# sys.settrace(trace_calls_and_returns)
# myClass = Array_oper([1,2,3],[1,2,3])
# myClass.printArray()
# myClass.add()
# myClass.sub()
# myClass.dot_product()
# print('add', myClass.add())
# print('sub', myClass.sub())
# print('dot_product', myClass.dot_product())
