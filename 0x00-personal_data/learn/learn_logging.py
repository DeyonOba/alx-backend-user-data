#!/usr/bin/env python3
import logging
import sys

# # Setting logging level to DEBUG and 
# level = logging.DEBUG
# format = "{levelname}-{name}-{message}"
# logging.basicConfig(level=level, format=format, style="{")

# logging.debug("power function used")
# logging.info("Hello application is working")
# logging.warning("Slow signal recieved.")
# logging.error("Signal not recieved.")
# logging.critical("Bad signal argument.")


# logging.basicConfig(
#     filename="app.log",
#     encoding="utf-8",
#     filemode="a",
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
# )

# donuts = 5
# guests = 0
# try:
#     donuts_per_guest = donuts / guests
# except ZeroDivisionError:
#     logging.error("DonutCalculationError", exc_info=True)

## Instantiating a Logger
# logger = logging.getLogger(__name__)
# logger.warning("New Logger Created.")

## Instantiation a Logger and add Handlers
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(
    filename="app.log",
    encoding="utf-8",
    mode="a",
)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

print(logger.handlers)
logger.warning("No!!!")
formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

console_handler.setFormatter(formatter)
logger.warning("Again!!!")
print(logger.level)