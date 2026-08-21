# just a simple config file to contain consts

#log level enum
DEBUG = 0; INFO = 1; WARNING = 2; ERROR = 3; FATAL = 4; NONE = 5; STDERR_ONLY = WARNING

SRO_PORT = 31261
LOGLEVEL = DEBUG
PACKET_COUNT = 10

# set PRINT_CSV to filename to print to
# or set to log level enum to print with loglevel
# or set to False/None to not use entirely
PRINT_CSV = "packets.csv"
CSV_DELIMETER = "\t"