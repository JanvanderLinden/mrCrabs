import sys
import os
import subprocess
import re
import optparse
import time

import printer
import crab

# option parser
parser = optparse.OptionParser(usage="mrcrab [opts] [args=projects]")
parser = crab.setup_crab_query_parser(parser)
(opts, args) = parser.parse_args()

# collect all crab porjects
projects = []
for p in args:
    if "*" in p:
        projects += glob.glob(p)
    else:
        projects += [p]

printer.printInfo("checking jobs:")
for p in projects: printer.printPath("\t"+p) 
printer.printDelim("=",30)

results = []
for project in projects:
    printer.printAction("querying job {}".format(project))
    
    result = crab.crab_query(project, opts)
    results.append(result)

crab.print_crab_summary(results)
