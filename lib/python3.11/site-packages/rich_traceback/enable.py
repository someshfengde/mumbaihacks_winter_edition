#
# Copyright (C)2014 Laurentiu Badea
#
"""
Monkey patch Formatter in global logging module with RichTracebackFormatter
Also install exception hook that prints out rich traceback.

Usage:

  import rich_traceback.enable
  import logging

  log = logging.getLogger('root')
  log.warning("message")
  ...

"""
import sys
from .formatter import RichTracebackFormatter
import logging

if not issubclass(logging.Formatter, RichTracebackFormatter):
    logging.Formatter = RichTracebackFormatter

def uncaught_exception(*exc_info):
    logging.error("Uncaught Exception", exc_info=exc_info)
    fmt = RichTracebackFormatter(datefmt=" ")
    print >>sys.stderr, fmt.formatException(*exc_info)

# Set up global exception handler as the above function
sys.excepthook = uncaught_exception
