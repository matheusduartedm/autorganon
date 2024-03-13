import argparse
import flet as ft
import json
from auto_organon import gen_ctg, gen_def, gen_spt

CONFIG_FILE = "configs.json"
DEFAULT_VALUES = {
    "case_path": r"D:\dev\auto_organon\cases",
    "line_file": "2028Lines.csv",
    "trf_file": "2028Transfo.csv",
    "bus": "7190",
    "levels": "3",
    "areas": "773, 772, 771, 761",
    "cases_file": "cases.csv"
}

def load_values():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_VALUES

def save_values(updated_values):
    values = load_values()
    values.update(updated_values)
    with open(CONFIG_FILE, "w") as file:
        json.dump(values, file, indent=4)

class AutoOrganonGUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Organon Automation"
        self.page.theme_mode = "light"
        self.saved_values = load_values()
        self.setup_ui()

    def setup_ui(self):
        self.case_path = ft.TextField(label="Case Path", value=self.saved_values.get("case_path", DEFAULT_VALUES["case_path"]))
        self.line_file_input = ft.TextField(label="Line File Name", value=self.saved_values.get("line_file", DEFAULT_VALUES["line_file"]))
        self.trf_file_input = ft.TextField(label="Transfo File Name", value=self.saved_values.get("trf_file", DEFAULT_VALUES["trf_file"]))
        self.bus_input = ft.TextField(label="Bus Number", value=self.saved_values.get("bus", DEFAULT_VALUES["bus"]))
        self.levels_input = ft.TextField(label="Levels", value=self.saved_values.get("levels", DEFAULT_VALUES["levels"]))
        self.areas_input = ft.TextField(label="Areas (comma-separated)", value=self.saved_values.get("areas", DEFAULT_VALUES["areas"]))
        self.cases_file_input = ft.TextField(label="Cases File Name", value=self.saved_values.get("cases_file", DEFAULT_VALUES["cases_file"]))

        self.gen_ctg_button = ft.ElevatedButton("Generate .ctg", on_click=lambda _: self.run_gen_ctg())
        self.gen_def_button = ft.ElevatedButton("Generate .def", on_click=lambda _: self.run_gen_def())
        self.gen_spt_button = ft.ElevatedButton("Generate .spt", on_click=lambda _: self.run_gen_spt())

        self.page.add(self.case_path, self.line_file_input, self.trf_file_input, 
                      self.bus_input, self.levels_input, self.areas_input, 
                      self.cases_file_input, self.gen_ctg_button, self.gen_def_button, self.gen_spt_button)

    def run_gen_ctg(self):
        updated_values = {
            "case_path": self.case_path.value,
            "line_file": self.line_file_input.value,
            "trf_file": self.trf_file_input.value,
            "bus": self.bus_input.value,
            "levels": self.levels_input.value
        }
        save_values(updated_values)
        try:
            bus = int(self.bus_input.value)
            levels = int(self.levels_input.value)
            gen_ctg(self.case_path.value, self.line_file_input.value, self.trf_file_input.value, bus, levels)
            self.page.add(ft.Text(".ctg generated successfully!"))
        except ValueError:
            self.page.add(ft.Text("Error in .ctg generation: Invalid numeric values."))

    def run_gen_def(self):
        updated_values = {
            "case_path": self.case_path.value,
            "areas": self.areas_input.value
        }
        save_values(updated_values)
        try:
            areas = [int(area.strip()) for area in self.areas_input.value.split(',')]
            gen_def(areas, self.case_path.value)
            self.page.add(ft.Text(".def generated successfully!"))
        except ValueError:
            self.page.add(ft.Text("Error in .def generation: Invalid numeric values."))

    def run_gen_spt(self):
        updated_values = {
            "case_path": self.case_path.value,
            "cases_file": self.cases_file_input.value
        }
        save_values(updated_values)
        gen_spt(self.case_path.value, self.cases_file_input.value)
        self.page.add(ft.Text(".spt generated successfully!"))

class AutoOrganonCLI:
    def __init__(self, config_file):
        self.config = load_values(config_file)
        self.parser = self.create_parser()

    def create_parser(self):
        parser = argparse.ArgumentParser(description="Auto Organon Command Line Interface")
        parser.add_argument("--input", required=True, help="Path to the configuration file")
        parser.add_argument("--gen_ctg", action="store_true", help="Generate .ctg file")
        parser.add_argument("--gen_def", action="store_true", help="Generate .def file")
        parser.add_argument("--gen_spt", action="store_true", help="Generate .spt file")
        return parser

    def run(self, args):
        try:
            if args.gen_ctg:
                self.run_gen_ctg()
            elif args.gen_def:
                self.run_gen_def()
            elif args.gen_spt:
                self.run_gen_spt()
        except ValueError as e:
            print(f"Error: {e}")

    def run_gen_ctg(self):
        try:
            bus = int(self.config.get("bus", 0))
            levels = int(self.config.get("levels", 0))
            gen_ctg(self.config.get("case_path"), self.config.get("line_file"), 
                    self.config.get("trf_file"), bus, levels)
            print(".ctg generated successfully!")
        except ValueError as e:
            print(f"Error in .ctg generation: {e}")

    def run_gen_def(self):
        try:
            areas = [int(area.strip()) for area in self.config.get("areas", "").split(',')]
            gen_def(areas, self.config.get("case_path"))
            print(".def generated successfully!")
        except ValueError as e:
            print(f"Error in .def generation: {e}")

    def run_gen_spt(self):
        try:
            gen_spt(self.config.get("case_path"), self.config.get("cases_file"))
            print(".spt generated successfully!")
        except Exception as e:
            print(f"Error in .spt generation: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        cli = AutoOrganonCLI(sys.argv[1])
        args = cli.parser.parse_args()
        cli.run(args)
    else:
        ft.app(target=lambda page: AutoOrganonGUI(page))