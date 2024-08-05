# Python Logging

It's good practice to record important information during the execution of a program, this enable the dev team to understand the working condition of the program, or even discover adnormalities.
Logging module is a standard Python library with the main feature of loggin module is the logger.

The records been stored are called logs and can help understand the work flow of an application.

By default the `logging` module uses the root logger.

```python
import logging
logging.warning("This a warning!")
# WARNING:root:This a warning!
# Severity level:logger name: message
```

You'll notice that the output shows the severity level and logger name before the message, root is the default logger name given by the `logging` module.

What does severity level mean?, this is used to basically indicate the severity or importance of the message been passed. By default, there a five standard levels, each having a function used to log events at that level of severity.

|level|Function|Numeric value|Description|
|---|---|---|---|
|DEBUG| `logging.debug()`|10|Detailed information, typically only of interest to a developer trying to diagnose a problem.|
|INFO|`logging.info()`|20|Confirmation that things are working as expected.|
|WARNING|`logging.warning()`|30|An indication that something unexpected happened, or that a problem might occur in the near future (e.g. 'disk space low'). The software is still working as expected.|
|ERROR|`logging.error()`|40|Due to a more serious problem, the software has not been able to perform some function.|
|CRITICAL|`logging.critical()`|50|A serious error, indicating that the program itself may be unable to continue running.|


# REFERENCE

- [logging module](https://docs.python.org/3/library/logging.html)
- [under the source code](https://realpython.com/python-logging-source-code/)
- [article on python logging](https://realpython.com/python-logging/)
