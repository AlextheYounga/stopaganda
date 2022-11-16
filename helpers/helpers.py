import os
from tabulate import tabulate

def get_project_path(windows=False):
    dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if (windows):
        return dir_name.replace("\\", '/')
    return dir_name

def print_tabs(data, headers=[], tablefmt='simple'):
    """ 
    Parameters
    ----------
    data     :  list of lists
                first list must be list headers
    tablefmt : string
                see https://pypi.org/project/tabulate/ for supported text formats
    """
    tabdata = []
    if (type(data) == dict):
        for h, v in data.items():
            tabrow = [h, v]
            tabdata.append(tabrow)
        print(tabulate(tabdata, headers, tablefmt))
    if (type(data) == list):
        tabdata = data
        print(tabulate(tabdata, headers, tablefmt))