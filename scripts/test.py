from auto_organon import gen_ctg, gen_def, gen_spt

CASE_PATH = r"D:\dev\auto_organon\cases"
line_file = "2028Lines.csv"
trf_file = "2028Transfo.csv"
bus = 7190
levels = 3
gen_ctg(CASE_PATH, line_file, trf_file, bus, levels)

areas = [773, 772, 771, 761]
gen_def(areas, CASE_PATH)

cases_file = "cases.csv"
gen_spt(CASE_PATH, cases_file)