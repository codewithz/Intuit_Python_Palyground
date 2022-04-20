# Logging Basics

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

# Basic Logging
# Notice: All of them will not be printed

def test():
    print("-"*20)
    level=logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f"Log Level: {level}")
    logging.debug("Debug message here")
    logging.info("Info message here")
    logging.warning("Warning message here")
    logging.error("Error message here")
    logging.critical("Critical message here")
    print("-"*20)

test()


# Logging Levels
# Getting and Setting the Logging Levels
# Allows for filtering

# Get the Root Logger

root_log=logging.getLogger()
level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
print(f"Log Level: {level}")

# Set it to DEBUG

root_log.setLevel(logging.DEBUG)
test()

# Log it to a file

# logging.basicConfig(filename="logs.txt",filemode="w",format="%(levelname)s:%(message)s",level=logging.DEBUG)
# logging.debug(" Hello")

handler=logging.FileHandler("logs.txt")
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' );

handler.setFormatter(formatter)
root_log.addHandler(handler)
test()
