import streamlit as st
from pydantic import BaseModel
from collections import namedtuple
import time

from info_storage.education_info import get_education_list
from info_storage.skills_info import get_ide_info, get_version_control_info, get_languages, get_python_libs_info

SkillsInfo = namedtuple("Skills", ["topic", "tools", "description"])


class EducationData(BaseModel):
    name: str
    link: str
    info: list
    period: str


st.set_page_config(layout='wide')
# st.markdown(
#     """
#     <style>
#         div[data-testid="column"]:nth-of-type(1)
#         {
#             border:1px solid red;
#             text-align: center;
#         }
#
#         div[data-testid="column"]:nth-of-type(2)
#         {
#             border:1px solid blue;
#             text-align: center;
#         }
#     </style>
#     """,unsafe_allow_html=True
# )

top_data, top_d_second = st.columns(2)
first_col, second_col = st.columns(2)
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0.5 rem;
    }
    </style>
    """,unsafe_allow_html=True)

tooltip_style = """
<style>
div[data-baseweb="tooltip"] {
  width: 800px; font-size: 40px;
}
</style>
"""
st.markdown(tooltip_style, unsafe_allow_html=True)


# skills_list = [{}
#     "IDE\n\n- Visual Studio Code\n\n- Jupyter Notebook\n\n- PyCharm",
#                "Version control\n\n- Bitbucket(GIT)\n\n- Github\n\n- SVN",
#                "Cloudtools\n\n- Jira\n\n- Confluence"
#
# ]

education_infos = []
for education_info in get_education_list():
    education_infos.append(EducationData(**education_info))

with top_data:
    st.snow()
    st.header("Softwareentwickler/Data Analyst")
    st.subheader(":red[Wer aufhört, besser zu werden, hat aufgehört, gut zu sein!]")
    st.image("resource/images/Passbild.jpg", width=300)
    st.subheader(""":blue[Hover over question mark for more information]:dark_sunglasses:""")

# with top_d_second:
#     st.markdown("***")
#     st.header(":rainbow[Wer aufhört, besser zu werden, hat aufgehört, gut zu sein]")
with first_col:

    # st.link_button("Akkodis Homepage", "https://www.akkodis.com/de", help="")
    with st.expander("Skills"):
        get_ide_info()
        get_version_control_info()
        get_languages()
        get_python_libs_info()

with second_col:
    st.markdown('O')

col1, col2 = st.columns(2)


def header_props(name, link):
    return f"""<a style='display: block; text-align: left;font-size: 20px;'
            href="{link}">{name}</a>
            """


with col1:
    with st.expander("Education"):
        for education_data in education_infos:
            st.markdown(header_props(education_data.name, education_data.link), help=education_data.period, unsafe_allow_html=True)
            for subinfo in education_data.info:
                st.markdown(subinfo)
        # st.markdown("Hochschule München\n\n- Elektrotechnik und Informationstechnik")
        # st.markdown(f"## Berufliche Oberschule, Traunstein [Homepage](https://www.fosbos-ts.de/)\n\n"
        #             f"- Fachgebundene Hochschulreife", help="09/2013 bis 07/2015")

with col2:
    with st.expander("Experience"):
        st.markdown("Akkodis")
# st.markdown("My markdown", help="More info here")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
