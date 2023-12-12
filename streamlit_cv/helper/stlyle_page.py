import streamlit as st


def add_bar_styling():
    return st.markdown(
        f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url("https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/grey_side_bar.jpg?raw=true");
      }}
      </style>
      """,
        unsafe_allow_html=True,
    )
