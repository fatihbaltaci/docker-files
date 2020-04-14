import os
import subprocess

PACKAGES = """
    opencv-contrib-python==4.1.0.25
    mlflow==0.9.1 
    youtube_dl 
    scikit-image==0.16.2 
    matplotlib==3.1.0 
    Pillow==5.3.0 
    Cython==0.29.9 
    wget==3.2 
    future==0.17.1 
    jupyterlab==1.2.4 
    ipywidgets 
    tqdm 
    pandas 
    numpy 
    scipy 
    seaborn 
    scikit-learn 
    plotly
"""


def run_command(command):
    out = subprocess.run(command, shell=True, check=True, capture_output=True, encoding='UTF-8')
    return out.stdout.splitlines()


def get_packages_list(packages):
    return [package.split("==")[0].strip() for package in packages.split("\n") if package]

def get_version_from_single_line(line):
    """
        line: e.g: opencv-contrib-python (4.2.0.34)
        return: 4.2.0.34
    """
    return line.split("(")[1].split(")")[0].strip()


def prepare_pip_install_command(packages_dict):
    print_str = f"pip3 install --no-cache-dir install \\ \n"

    for package_name, version in packages_dict.items():
        print_str += f"\t{package_name}=={version} \\ \n"

    print(print_str[:-3])   # omit last slash


if __name__ == "__main__":

    packages_list = get_packages_list(PACKAGES)
    print(packages_list)
    packages_dict = dict()


    for package in packages_list:
        command = f"pip3 search {package}"
        command_lines = run_command(command)
        only_package_line = [line for line in command_lines if line.lower().startswith(f"{package.lower()} (")][0]
        package_version = get_version_from_single_line(only_package_line)
        packages_dict[package] = package_version

        print(only_package_line)

    prepare_pip_install_command(packages_dict)

