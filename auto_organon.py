import csv
import os
import shutil


class Line:
	def __init__(self, row):
		self.from_bus, self.to_bus, self.circ, self.from_name, self.to_name = extract_circuit_data(row)

	def __str__(self):
		return f"<{self.__class__} {self.from_bus} {self.to_bus} {self.circ}>"

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		return (self.from_bus == other.from_bus and self.to_bus == other.to_bus) or \
				(self.from_bus == other.to_bus and self.to_bus == other.from_bus)

	def __hash__(self):
		return self.from_bus +10000* self.to_bus


class Transformer(Line):
	pass


def extract_circuit_data(row: list) -> tuple:
	from_bus = int(row[0])
	from_name = row[1].strip()
	to_bus, circ = tuple(map(lambda x: int(x.strip()), row[2].split("#")))
	to_name = row[3]

	return from_bus, to_bus, circ, from_name, to_name


def get_circuits_connected_to(circuits: list, bus_number: int) -> list:
	captured = []
	for circuit in circuits:
		if circuit.from_bus == bus_number or circuit.to_bus == bus_number:
			if not circuit in captured:
				captured.append(circuit)
	return captured


def get_unique_bus_numbers(circuits: list) -> list:
	buses = set()
	for circuit in circuits:
		buses.add(circuit.from_bus)
		buses.add(circuit.to_bus)
	return list(buses)


def extract_voltage_value(name: str) -> int:
    for length in range(3, 0, -1):
        try:
            return int(name[-length:])
        except ValueError:
            continue
    return None

def get_neighboring_circuits(circuits: list, central_bus: int, levels: int) -> list:
    captured = set()
    buses_to_visit = [central_bus, ]
    already_visited = []
    while levels >= 1:
        new_circuits = set()
        for bus in buses_to_visit:
            if bus not in already_visited:
                connected_circuits = get_circuits_connected_to(circuits, bus)
                for circuit in connected_circuits:
                    from_voltage = extract_voltage_value(circuit.from_name)
                    to_voltage = extract_voltage_value(circuit.to_name)

                    if (from_voltage is None or from_voltage >= 230 or from_voltage == 0) and \
                       (to_voltage is None or to_voltage >= 230 or to_voltage == 0):
                        new_circuits.add(circuit)

                already_visited.append(bus)

        buses_to_visit = get_unique_bus_numbers(new_circuits)
        captured.update(new_circuits)
        levels = levels - 1
    return list(captured)


def gen_ctg(CASE_PATH, line_file_name, trf_file_name, input_bus, input_levels):

	lines = []
	transformers = []

	with open(CASE_PATH +"\\" + line_file_name, "r") as lines_file:
		reader = csv.reader(lines_file, delimiter=";")
		next(reader)
		next(reader)
		for row in reader:
			if len(row) > 1:
				lines.append(Line(row))

	with open(CASE_PATH +"\\" + trf_file_name, "r") as trf_file:
		reader = csv.reader(trf_file, delimiter=";")
		next(reader)
		next(reader)
		for row in reader:
			if len(row) > 1:
				transformers.append(Transformer(row))

	circuits = []
	circuits.extend(lines)
	circuits.extend(transformers)

	first_circuits = get_circuits_connected_to(circuits, input_bus)
	buses = get_unique_bus_numbers(first_circuits)

	circs = get_neighboring_circuits(circuits, input_bus, input_levels)

	organon_ctg = """  '{name:60s}' 
	BRANCH      {from_b:5d}        {to_b:5d}       {circ:02d}
			END /
	"""

	with open(CASE_PATH + "\\" + "contigencies.ctg", "w") as file:
		for circ in circs:
			file.write(organon_ctg.format(name=f"{circ.from_name}({circ.from_bus}) {circ.to_name}({circ.to_bus}) #{circ.circ}",
											from_b=circ.from_bus, to_b=circ.to_bus, circ=circ.circ))


def gen_spt(CASE_PATH, cases_file_name = "cases.csv", RUN_CONTINGENCY = True):
	#SCRIPT INPUTS
	CASES_FILE = CASE_PATH + "\\" + cases_file_name
	OUTPUT_SCRIPT = CASE_PATH + "\\" + "script.spt"
	DEF_FILE = CASE_PATH + "\\" + "definitions.def"
	CTG_FILE = CASE_PATH + "\\" + "contigencies.ctg"
	OUTPUT_PATH = CASE_PATH + "\\" + "auto-organon_output/"


	# SCRIPT
	input_file_paths = []
	with open(CASES_FILE, "r") as case_file:
		for row in csv.reader(case_file):
			file_path = CASE_PATH + "\\" + row[0]

			if os.path.exists(file_path):

				input_file_paths.append(file_path)
			else:
				print(f"File does not exist: {file_path}")


	spt_lines = []

	for ifile, file_path in enumerate(input_file_paths):
		base_name, ext = os.path.splitext(os.path.basename(file_path))
		output_folder_path = os.path.join(OUTPUT_PATH, base_name)
		os.makedirs(output_folder_path, exist_ok=True)
		output_file_path = os.path.join(output_folder_path, base_name + ext)
		shutil.copyfile(file_path, output_file_path)


		abs_file_path = os.path.abspath(output_file_path)
		spt_lines.append(f"OPEN {abs_file_path}")
		spt_lines.append(f"OPEN {DEF_FILE}")
		spt_lines.append(f"OPEN {CTG_FILE}")
		spt_lines.append("")
		spt_lines.append("NEWTON")
		spt_lines.append("CSV PWF03")
		spt_lines.append("CSV PWF05")
		spt_lines.append("CSV PWF16")
		spt_lines.append("")
		if RUN_CONTINGENCY:
			spt_lines.append("PFCTG")
			spt_lines.append("CSV CTG01")
			spt_lines.append("CSV CTG02")
			spt_lines.append("CSV CTG03")
		spt_lines.append("")

		if ifile < len(input_file_paths) - 1:
			spt_lines.append("")
			spt_lines.append("! ---")
			spt_lines.append("")


	with open(OUTPUT_SCRIPT, "w") as spt_file:
		spt_file.write("\n".join(spt_lines))


def gen_def(areas, CASE_PATH):
	monitor_template = " AREA      {number:5d}     230.0  999.0 ONE  /\n"

	with open(CASE_PATH + "\\" + "definitions.def", "w") as file:
		file.write(" MONITOR\n")
		for area in areas:
			line = monitor_template.format(number=area)
			file.write(line)

		file.write(" END /\n")
