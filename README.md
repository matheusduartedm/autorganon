# AutoOrganon

AutoOrganon is a Python-based automation tool for Organon, a power systems analysis software. It simplifies the process of generating and running scripts for power flow and contingency analysis.

## Features

- Generate `.ctg` (contingency) files
- Generate `.def` (definition) files
- Generate `.spt` (script) files for Organon
- Run Organon processes
- Add loads to specified buses
- Compare base cases with sensitivity analysis
- GUI for easy configuration and execution

## Requirements

- Python 3.6+
- Organon software installed
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository
2. Run `make_venv.bat` to create a virtual environment and install dependencies
3. Configure `configs.json` with your specific settings

## Usage

You can use AutoOrganon via command line or GUI:

### Command Line

```
python main.py <command> [options]
```

Available commands:
- `ctg`: Generate .ctg file
- `def`: Generate .def file
- `spt`: Generate .spt file
- `run`: Execute Organon process
- `add`: Add load to specified bus
- `compare`: Compare cases
- `sensitivity`: Run sensitivity analysis

### GUI

Run `python main.py` without arguments to launch the GUI.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.