# RLogger

## Overview

**RLogger** is a versatile logging utility designed to simplify logging in Python applications. With easy-to-use methods and customizable handlers, it provides a straightforward approach to incorporate both console and file logging.

## Features

- **Easy Setup**: Quickly initialize both console and file logging.
- **Customizable Formats**: Define the format that suits your logging needs.
- **Context-Aware Logging**: Enhance logs with contextual information.
- **Rotating File Logs**: Ensure your applications don't run out of disk space with rotating logs.

## Quickstart

Here's a simple demonstration of RLogger in action:

```python
from rlogger import RLogger

# Initialize the logger
logger = RLogger(filename="app.log")

# Log some messages
logger.info("This is an info message.")
logger.warning("This is a warning message.", data={"user": "John Doe"})
logger.error("An error occurred!")
```

## Configuration

Customize **RLogger** to your needs during initialization:

```python
logger = RLogger(
    filename="app.log", 
    log_level=logging.DEBUG, 
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    max_log_size=10, 
    backup_count=5,
    log_to_console=True
)
```

For more in-depth configurations and advanced use-cases, please refer to the official documentation.

## Contribution

Your contributions are always welcome! Feel free to submit pull requests for enhancements, bugfixes, or any additional features.

## License
RLogger is proudly released under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).