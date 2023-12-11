import streamlit as st
from collections import namedtuple

from info_storage.description import get_ide_description, get_version_control_description, get_programming_languages, \
    get_python_libs_description

SkillsInfo = namedtuple("Skills", ["topic", "tools"])
IDEDescription = namedtuple("IDE_Infos", ["vs_code", "jupyter", "pycharm"])

ide_description = IDEDescription(*get_ide_description())
ide_infos = SkillsInfo("IDE", ["- Visual Studio Code", "- Jupyter Notebook", "- PyCharm"])
version_control = SkillsInfo("Version control", ["- Bitbucket", "- Github", "- GIT", "- SVN"])
coding_skills = SkillsInfo("Programming languages", ["- Python3", "- HTML", "- CSS", "- SQL", "- NoSQL"])


def insert_hyphen(info):
    """

    Args:
        info:

    Returns:

    """
    return ["- " + i for i in info.split(", ")]


python_libs = SkillsInfo("Python libraries", insert_hyphen("Pandas, Polars, NumPy, Tkinter, PyQT, asammdf, "
                                                           "python-pptx, Plotly, Matplotlib, Pandera, Pydantic, "
                                                           "Selenium, Xlsxwriter, OpenPyXL, Hypothesis, Pytest, "
                                                           "itertools, Dash, Streamlit"))


def get_ide_info():
    return info_generator(ide_infos, get_ide_description())


def get_version_control_info():
    return info_generator(version_control, get_version_control_description())


def get_languages():
    return info_generator(coding_skills, get_programming_languages())


def get_python_libs_info():
    return info_generator(python_libs, get_python_libs_description())


def info_generator(skill_info, description):
    return st.markdown(skill_info.topic), [st.markdown(tool_name, help=description) for tool_name, description in
                                           zip(skill_info.tools, description)]
