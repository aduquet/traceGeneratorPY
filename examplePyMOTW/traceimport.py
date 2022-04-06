import trace

from sympy import false, true
from recurse import recurse

# tracer = trace.Trace(count=true, trace=false)
# # tracer.run('recurse(2)')
# tracer.runfunc(recurse, 2)

# results = tracer.results()
# results.write_results(summary=True, coverdir='coverdir2')\
    
import trace
from recurse import recurse

tracer = trace.Trace(count=True, trace=False, outfile='trace_report2.txt')
tracer.runfunc(recurse, 2)

report_tracer = trace.Trace(count=False, trace=False, infile='trace_report2.txt')
results = tracer.results()
results.write_results(summary=True, coverdir='/tmp')