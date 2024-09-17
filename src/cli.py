import argparse

from autorganon import *


def cli():
    parser = argparse.ArgumentParser(description="Autorganon Command Line Interface")

    subparsers = parser.add_subparsers(dest='command', help='commands')

    ctg_parser = subparsers.add_parser('ctg', help='Generate .ctg file')
    ctg_parser.add_argument('input', help='Input file')

    def_parser = subparsers.add_parser('def', help='Generate .def file')
    def_parser.add_argument('input', help='Input file')

    spt_parser = subparsers.add_parser('spt', help='Generate .spt file')
    spt_parser.add_argument('input', help='Input file')

    run_parser = subparsers.add_parser('run', help='Executes the Organon process with the specified .spt script file.')
    run_parser.add_argument('input', help='Input file')

    add_parser = subparsers.add_parser('add', help='Add a load to the specified bus')
    add_parser.add_argument('--load', help='Load value', type=float, required=True)
    add_parser.add_argument('--bus', help='Bus number', type=int, required=True)
    add_parser.add_argument('--pf', help='Power factor', type=float, required=True)
    add_parser.add_argument('--path', help='Path to the folder containing the .PWF files', required=True)

    compare_parser = subparsers.add_parser('compare', help='Compare cases')
    compare_parser.add_argument('--base', help='Base path', required=True)
    compare_parser.add_argument('--sensitivity', help='Sensitivity path', required=True)

    sensitivity_parser = subparsers.add_parser('sensitivity', help='Run sensitivity analysis and compare cases')
    sensitivity_parser.add_argument('--load', help='Load value', type=float, required=True)
    sensitivity_parser.add_argument('--bus', help='Bus number', type=int, required=True)
    sensitivity_parser.add_argument('--pf', help='Power factor', type=float, required=True)
    sensitivity_parser.add_argument('--path', help='Path to the folder containing the .PWF files', required=True)

    args = parser.parse_args()

    if args.command:
        if args.command == 'add':
            add_load(args.load, args.bus, args.pf, args.path)

        elif args.command == 'run':
            run_organon(args.input)

        elif args.command == 'compare':
            compare_cases(args.base, args.sensitivity)

        elif args.command == 'sensitivity':
            root_path = os.path.dirname(args.path)
            sensitivity_path = os.path.join(root_path, f"sensitivity_{args.load}")
            shutil.copytree(args.path, sensitivity_path)
            add_load(args.load, args.bus, args.pf, sensitivity_path)
            gen_spt(sensitivity_path, "cases.csv")
            run_organon(os.path.join(sensitivity_path, "script.spt"))
            compare_cases(args.path, sensitivity_path)

        else:
            config = load_values(args.input)
            if args.command == 'ctg':
                run_gen_ctg(config)
            elif args.command == 'def':
                run_gen_def(config)
            elif args.command == 'spt':
                run_gen_spt(config)


if __name__ == '__main__':
    cli()