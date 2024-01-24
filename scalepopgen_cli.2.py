import os
import os.path
import time
import re
import prompt_toolkit
from prompt_toolkit.completion import PathCompleter
from beaupy.spinners import *
from beaupy import confirm, prompt, select
from rich.console import Console
import pyfiglet
import yaml
from yaml.loader import SafeLoader
from workflow_dict import worfklow_dict as dictionary

console = Console()


class util:
    def print_header(self):
        f = pyfiglet.figlet_format("scale popgen", font="starwars")
        print(f)

    def clear_screen(self):
        os.system("clear")

    def read_options(self, dict):
        gpl = []
        for key in dict:
            gpl.append(f"{key}: {dict[key]}")
        gpl.append("back")
        name = select(gpl, cursor="🢧", cursor_style="cyan")
        name = str(name).split(":")[0]
        return name

    def is_file_exit(self, file, default_param):
        lc = 0
        is_vcf = False if file.endswith(".p.csv") else True
        with open(file) as source:
            for line in source:
                line = line.rstrip().split(",")
                if lc == 0:
                    lc += 1
                else:
                    if not os.path.isfile(line[1]) or not os.path.isfile(line[2]):
                        console.print(
                            f"[red]vcf or index does not exits for {line}[/red]"
                        )
                        time.sleep(2)

    def read_file_prompt(self, param, help_message, default_param, ext):
        console.print(help_message)
        param_var = param + ":"
        param_f = prompt_toolkit.prompt(
            param_var,
            completer=PathCompleter(),
        )
        if param_f == "n":
            return default_param
        elif not os.path.isfile(param_f) or not param_f.endswith(ext):
            console.print(
                f"[red]{param_var}{param_f} does not exist or does not end with {ext}[/red]"
            )
            time.sleep(2)
            return default_param
        else:
            param_f = (
                self.is_file_exit(param_f, default_param)
                if param == "input"
                else param_f
            )
            return param_f

    def read_string_prompt(self, param, help_message, default_param):
        string_o = default_param
        console.print(help_message)
        param_var = param + ":"
        string_o = prompt(param_var, target_type=str)
        return string_o if string_o != "n" else default_param

    def read_string_args_prompt(
        self, param, help_message, default_param, exp_args_list
    ):
        string_o = default_param
        console.print(help_message)
        param_var = param + ":"
        is_broken = False
        string_o = prompt(param_var, target_type=str)
        if string_o == "n":
            return default_param
        else:
            pattern = re.compile(r"[\-A-Za-z]+")
            obs_args_list = re.findall(pattern, string_o)
            for args in obs_args_list:
                if args not in exp_args_list:
                    console.print(
                        f"[red]the parameter {args} is not the expected argument for {param}[/red]"
                    )
                    is_broken = True
                    time.sleep(2)
                    break
            if is_broken:
                return default_param
            else:
                return string_o

    def read_int_prompt(self, param, help_message, default_param, min_i, max_i):
        console.print(help_message)
        param_var = param + ":"
        int_o = prompt(param_var)
        if int_o == "n":
            return default_param
        elif float(int_o) < float(min_i) or float(int_o) > float(max_i):
            console.print(
                f"[red]the parameter {param_var} should be greater than or equal to {min_i} and smaller than or equal to {max_i}[/red]"
            )
            time.sleep(2)
            return default_param
        else:
            return float(int_o)

    def read_bool_confirm(self, param, help_message):
        console.print(help_message)
        param_var = param + " ?:"
        if confirm(param_var):
            return True
        else:
            return False


class ReadYml:
    def __init__(self, yml):
        self.d = dictionary()
        self.param_general = self.d.param_general
        self.param_filtering = self.d.param_filtering
        self.yml = yml

    def set_params(self):
        with open(self.yml, "r") as p:
            yaml_params = yaml.load(p, Loader=SafeLoader)
            for key in self.param_general:
                if key in yaml_params:
                    self.param_general[key] = yaml_params[key]
            for key in self.param_filtering:
                if key in yaml_params:
                    self.param_filtering[key] = yaml_params[key]


class SetGeneralParameters:
    def __init__(self, param_general):
        self.d = dictionary()
        self.u = util()
        self.help_general = self.d.help_general
        self.param_general = param_general

    def print_header(self):
        console.print(f"[yellow]setting the general parameters[/yellow]")
        console.print(f"[green]type n to skip entering any parameter[/green]")

    def main_function(self):
        self.u.print_header()
        self.print_header()
        name = self.u.read_options(self.param_general)
        map_ext_dict = {
            "sample_map": ".map",
            "chrom_length_map": ".map",
            "color_map": ".map",
            "input": ".csv",
            "fasta": ".fna",
        }
        str_list = ["outprefix", "outgroup"]
        while name != "back":
            if name in map_ext_dict:
                update_param = self.u.read_file_prompt(
                    name,
                    self.help_general[name],
                    self.param_general[name],
                    map_ext_dict[name],
                )
            if name in str_list:
                update_param = self.u.read_string_prompt(
                    name, self.help_general[name], self.param_general[name]
                )
            if name == "max_chrom":
                update_param = self.u.read_int_prompt(
                    name, self.help_general[name], self.param_general[name], 1, 100
                )
            if name == "allow_extra_chrom":
                update_param = self.u.read_bool_confirm(name, self.help_general[name])
            self.param_general[name] = update_param
            self.u.clear_screen()
            self.u.print_header()
            self.print_header()
            name = self.u.read_options(self.param_general)
        self.u.clear_screen()
        return self.param_general


class SetGeneticStructureParam:
    def __init__(self, param_genetic_structure):
        self.d = dictionary()
        self.u = util()
        self.help_genetic_structure = self.d.help_genetic_structure
        self.param_genetic_structure = param_genetic_structure
        self.tool_args = self.d.tool_args

    def print_header(self):
        console.print(
            f"[yellow]setting the parameters for the analyses to explore genetic structure, note that if genetic_structure is set to false, then all the below-mentioned analyses will be skipped [/yellow]"
        )
        console.print(f"[green]type n to skip entering any parameter[/green]")

    def main_function(self):
        self.u.print_header()
        self.print_header()
        name = self.u.read_options(self.param_genetic_structure)
        map_ext_dict = {
            "rem_indi_structure": ".txt",
            "smartpca_param": ".txt",
            "pca_plot_yml": ".yml",
            "marker_map": ".map",
            "chrom_map": ".map",
            "admixture_colors": ".txt",
            "admixture_plot_yml": ".yml",
            "admixture_plot_pop_order": ".txt",
            "fst_plot_yml": ".yml",
            "ibs_plot_yml": ".yml",
        }
        int_param_dict = {
            "ld_window_size": [1, 10000000],
            "ld_step_size": [1, 10000000],
            "r2_threshold": [0, 1],
            "start_k": [0, 9999],
            "end_k": [0, 9999],
        }
        bool_list = [
            "genetic_structure",
            "ld_filt",
            "smartpca",
            "admixture",
            "pairwise_global_fst",
            "ibs_dist",
        ]
        args_list = ["admixture_args"]
        while name != "back":
            if name in int_param_dict:
                update_param = self.u.read_int_prompt(
                    name,
                    self.help_genetic_structure[name],
                    self.param_genetic_structure[name],
                    int_param_dict[name][0],
                    int_param_dict[name][1],
                )
            if name in map_ext_dict:
                update_param = self.u.read_file_prompt(
                    name,
                    self.help_genetic_structure[name],
                    self.param_genetic_structure[name],
                    map_ext_dict[name],
                )
            if name in bool_list:
                update_param = self.u.read_bool_confirm(
                    name, self.help_genetic_structure[name]
                )
            if name in args_list:
                update_param = self.u.read_string_args_prompt(
                    name,
                    self.help_genetic_structure[name],
                    self.param_genetic_structure[name],
                    self.tool_args[name],
                )
            self.param_genetic_structure[name] = update_param
            self.u.clear_screen()
            self.u.print_header()
            self.print_header()
            name = self.u.read_options(self.param_genetic_structure)
        self.u.clear_screen()
        return self.param_genetic_structure


class SetSnpFilteringParam:
    def __init__(self, param_snp_filtering):
        self.d = dictionary()
        self.u = util()
        self.help_snp_filtering = self.d.help_snp_filtering
        self.param_snp_filtering = param_snp_filtering

    def print_header(self):
        console.print(
            f"[yellow]setting the parameters for filtering the SNPs, note that if apply_snp_filters is set to false, then the SNP-filtering step is skipped entirely [/yellow]"
        )
        console.print(f"[green]type n to skip entering any parameter[/green]")

    def main_function(self):
        self.u.print_header()
        self.print_header()
        name = self.u.read_options(self.param_snp_filtering)
        map_ext_dict = {"rem_snps": ".txt"}
        int_param_dict = {
            "maf": [0, 1],
            "min_meanDP": [0, 9999],
            "max_meanDP": [0, 9999],
            "max_missing": [0, 1],
            "hwe": [0, 1],
            "minQ": [0, 9999],
        }
        bool_list = [
            "apply_snp_filters",
        ]
        while name != "back":
            if name in int_param_dict:
                update_param = self.u.read_int_prompt(
                    name,
                    self.help_snp_filtering[name],
                    self.param_snp_filtering[name],
                    int_param_dict[name][0],
                    int_param_dict[name][1],
                )
            if name in bool_list:
                update_param = self.u.read_bool_confirm(
                    name, self.help_snp_filtering[name]
                )
            if name in map_ext_dict:
                update_param = self.u.read_file_prompt(
                    name,
                    self.help_snp_filtering[name],
                    self.param_snp_filtering[name],
                    map_ext_dict[name],
                )
            self.param_snp_filtering[name] = update_param
            self.u.clear_screen()
            self.u.print_header()
            self.print_header()
            name = self.u.read_options(self.param_snp_filtering)
        self.u.clear_screen()
        return self.param_snp_filtering


class SetIndiFilteringParam:
    def __init__(self, param_indi_filtering):
        self.d = dictionary()
        self.u = util()
        self.help_indi_filtering = self.d.help_indi_filtering
        self.param_indi_filtering = param_indi_filtering

    def print_header(self):
        console.print(
            f"[yellow]setting the parameters for filtering samples, note that if apply_indi_filters is set to false, then the sample-filtering step is skipped entirely [/yellow]"
        )
        console.print(f"[green]type n to skip entering any parameter[/green]")

    def main_function(self):
        self.u.print_header()
        self.print_header()
        name = self.u.read_options(self.param_indi_filtering)
        map_ext_dict = {"rem_indi": ".txt"}
        int_param_dict = {
            "mind": [0, 1],
            "king_cutoff": [0, 1],
            "maf": [0, 1],
        }
        bool_list = [
            "apply_indi_filters",
        ]
        while name != "back":
            if name in int_param_dict:
                update_param = self.u.read_int_prompt(
                    name,
                    self.help_indi_filtering[name],
                    self.param_indi_filtering[name],
                    int_param_dict[name][0],
                    int_param_dict[name][1],
                )
            if name in map_ext_dict:
                update_param = self.u.read_file_prompt(
                    name,
                    self.help_indi_filtering[name],
                    self.param_indi_filtering[name],
                    map_ext_dict[name],
                )
            if name in bool_list:
                update_param = self.u.read_bool_confirm(
                    name, self.help_indi_filtering[name]
                )
            self.param_indi_filtering[name] = update_param
            self.u.clear_screen()
            self.u.print_header()
            self.print_header()
            name = self.u.read_options(self.param_indi_filtering)
        self.u.clear_screen()
        return self.param_indi_filtering


class ScalepopgenCli:
    def __init__(self):
        self.d = dictionary()
        self.u = util()
        self.param_general = self.d.param_general
        self.param_indi_filtering = self.d.param_indi_filtering
        self.param_snp_filtering = self.d.param_snp_filtering
        self.param_genetic_structure = self.d.param_genetic_structure

    def read_yaml(self):
        if confirm("[yellow]read existing yaml file of the parameters?[/yellow]"):
            console.print("[yellow]enter the path to the yaml file[/yellow]")
            yaml_file = prompt_toolkit.prompt("yaml:", completer=PathCompleter())
            if yaml_file != "n":
                spinner_animation = ["▉▉", "▌▐", "  ", "▌▐", "▉▉"]
                spinner = Spinner(spinner_animation, "reading yaml file ...")
                spinner.start()
                time.sleep(2)
                spinner.stop()
                self.y = ReadYml(yaml_file)
                self.y.set_params()
                console.print(
                    f"[green]yaml file was read and the parameters have been saved[/green]"
                )
                time.sleep(1)
                self.param_general = self.y.param_general
        os.system("clear")

    def main_function(self):
        self.u.clear_screen()
        self.u.print_header()
        self.read_yaml()
        self.u.print_header()
        analyses = [
            "the general input, output and other global parameters",
            "the parameters to remove samples",
            "the parameters to remove SNPs",
            "the parameters to explore genetic structure",
            "the parameters for treemix analysis",
            "the parameters to identify signatures of selection",
            "save & exit",
        ]
        console.print("[yellow]Set or view:[/yellow]")
        analysis = select(analyses, cursor="🢧", cursor_style="cyan")
        while analysis != "save & exit":
            self.u.clear_screen()
            if analysis == analyses[0]:
                g = SetGeneralParameters(self.param_general)
                self.param_general = g.main_function()
            if analysis == analyses[1]:
                fi = SetIndiFilteringParam(self.param_indi_filtering)
                self.param_indi_filtering = fi.main_function()
            if analysis == analyses[2]:
                fs = SetSnpFilteringParam(self.param_snp_filtering)
                self.param_snp_filtering = fs.main_function()
            if analysis == analyses[3]:
                gs = SetGeneticStructureParam(self.param_genetic_structure)
                self.param_genetic_structure = gs.main_function()
            self.u.print_header()
            console.print("[yellow]Set or view:[/yellow]")
            analysis = select(analyses, cursor="🢧", cursor_style="cyan")
        self.u.clear_screen()


scalepopgencli = ScalepopgenCli()
scalepopgencli.main_function()
