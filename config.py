# just a simple config file to contain consts

#log level enum
DEBUG = 0; INFO = 1; WARNING = 2; ERROR = 3; FATAL = 4; NONE = 5; STDERR_ONLY = WARNING

TARGET_IP = "167.99.6.174"
LOGLEVEL = DEBUG
PACKET_COUNT = 99999

# set PRINT_CSV to filename to print to
# or set to log level enum to print with loglevel
# or set to False/None to not use entirely
PRINT_CSV = "packets.csv"
CSV_DELIMETER = "\t"