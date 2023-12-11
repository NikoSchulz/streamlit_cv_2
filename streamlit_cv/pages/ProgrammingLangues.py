import pandas as pd
import plotly.express as px
import streamlit as st
from ipyvizzu import Chart, Data, Config, Style
from st_vizzu import vizzu_plot

st.set_page_config(layout='wide')


def process_dataframe():
    df = pd.read_csv(r"streamlit_cv/resource/csv_data/gh-push-event.json.csv")
    df = df.pipe(group_data).pipe(filter_data)
    return df


def group_data(df):
    return df.groupby(['name', 'year'])['count'].sum()


def filter_data(df):
    df = df.reset_index()
    print(df)
    return df.loc[df['name'].isin(['Python', 'Java', 'JavaScript', 'C++', 'HTML'])]


def configure_data_visualization():
    data = Data()
    data.add_df(process_dataframe())
    config = {
        "channels": {
            "y": {
                "set": ["name"],
            },
            "x": {"set": ["count"]},
            "label": {"set": ["count"]},
            "color": {"set": ["name"]},
        },
        "sort": "byValue",
    }

    style = Style(
        {
            "plot": {
                "paddingLeft": 100,
                "paddingTop": 25,
                "yAxis": {
                    "color": "#ffffff00",
                    "label": {"paddingRight": 10},
                },
                "xAxis": {
                    "title": {"color": "#ffffff00"},
                    "label": {
                        "color": "#ffffff00",
                        "numberFormat": "grouped",
                    },
                },
                "marker": {
                    "colorPalette": "#b74c20FF #c47f58FF #1c9761FF"
                                    + " #ea4549FF #875792FF #3562b6FF"
                                    + " #ee7c34FF #efae3aFF"
                },
            },
        }
    )

    chart = Chart(width="600px",
                  height="600px", display="manual")

    chart.animate(data, style)

    for year in range(2000, 2024):
        config["title"] = f"Github Pull Request - Year by Year {year}"
        chart.animate(
            Data.filter(f"parseInt(record.year) == {year}"),
            Config(config),
            duration=0.4,
            x={"easing": "linear", "delay": 0},
            y={"delay": 0},
            show={"delay": 0},
            hide={"delay": 0},
            title={"duration": 0, "delay": 0},
        )
        chart.feature("tooltip", True)
    return chart


executable_chart = configure_data_visualization()
with st.container():  # Maintaining the aspect ratio
    st.button("Animate")

    vizzu_plot(executable_chart)
    st.plotly_chart(px.line(data_frame=process_dataframe(), x='year', y='count', color='name'),
                    use_container_width=True)
