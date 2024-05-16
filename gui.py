import flet as ft
from autorganon import *

class AutoOrganonGUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Organon Automation"
        self.page.theme_mode = "light"
        self.saved_values = load_values()
        self.setup_ui()

    def setup_ui(self):
        self.case_path = ft.TextField(label="Case Path",
                                      value=self.saved_values.get("case_path", DEFAULT_VALUES["case_path"]))
        self.line_file_input = ft.TextField(label="Line File Name",
                                            value=self.saved_values.get("line_file", DEFAULT_VALUES["line_file"]))
        self.trf_file_input = ft.TextField(label="Transfo File Name",
                                           value=self.saved_values.get("trf_file", DEFAULT_VALUES["trf_file"]))
        self.bus_input = ft.TextField(label="Bus Number", value=self.saved_values.get("bus", DEFAULT_VALUES["bus"]))
        self.levels_input = ft.TextField(label="Levels",
                                         value=self.saved_values.get("levels", DEFAULT_VALUES["levels"]))
        self.areas_input = ft.TextField(label="Areas (comma-separated)",
                                        value=self.saved_values.get("areas", DEFAULT_VALUES["areas"]))
        self.cases_file_input = ft.TextField(label="Cases File Name",
                                             value=self.saved_values.get("cases_file", DEFAULT_VALUES["cases_file"]))

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