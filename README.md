# AutoCenter

AutoCenter is a Python program designed to synchronize desktop shortcuts across multiple Windows devices, ensuring a consistent user interface for users. By leveraging a shared network directory, AutoCenter copies shortcuts to and from the desktop, maintaining a uniform set of shortcuts across all devices.

## Features

- Synchronizes `.lnk` shortcut files between a shared network directory and the user's desktop.
- Automatically updates shortcuts on all connected devices.
- Simple and easy-to-use script with minimal setup.

## Prerequisites

To use AutoCenter, you need:

- Python 3.x installed on your Windows devices.
- Access to a shared network directory where shortcuts will be stored.

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/autocenter.git
   ```

2. Navigate to the repository directory.
   ```bash
   cd autocenter
   ```

3. Update the `SHARED_DIRECTORY` variable in `autocenter.py` with the path to your shared network directory.

## Usage

To run the AutoCenter script, execute the following command:

```bash
python autocenter.py
```

The script will automatically synchronize the desktop shortcuts from the shared directory to the desktop and vice versa.

## Contributing

Contributions to AutoCenter are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for a consistent user interface across multiple devices.