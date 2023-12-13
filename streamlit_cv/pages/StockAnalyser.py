import time
from st_aggrid import AgGrid
import pandas as pd
from st_aggrid import GridUpdateMode, GridOptionsBuilder
import pandas as pd
import plotly.express as px
import streamlit as st
import yfinance as yf
from prophet import Prophet
import numpy as np

from helper.stlyle_page import add_bar_styling

st.set_page_config(layout='wide')


class FinanceAnalyser:
    def __init__(self):
        self.symbol_mapping = pd.read_csv(r"streamlit_cv/resource/csv_data/nasdaq_screener.csv", usecols=["Symbol", "Name"])
        self.filter_special_values()
        self.example_symbols = self.symbol_mapping
        self.symbol = "META"
        self.company_name = ""
        self.data = None
        self.option = ""
        st.markdown("# ")

    def filter_special_values(self):
        symbols = ('GOOGL', 'MSFT', 'AAPL', 'BTC-USD')
        top_df = self.symbol_mapping[self.symbol_mapping['Symbol'].isin(symbols)]
        random_int = 30
        bot_df = self.symbol_mapping.iloc[random_int: random_int + 5]
        df = pd.concat([top_df, bot_df])
        self.symbol_mapping = df

    def insert_example_table(self):
        with st.expander("Click here for symbols"):
            builder = GridOptionsBuilder.from_dataframe(self.symbol_mapping)
            builder.configure_selection(use_checkbox=True)
            go = builder.build()
            table = AgGrid(self.symbol_mapping, update_mode=GridUpdateMode.MODEL_CHANGED, gridOptions=go)
            print(table)
            try:
                symbol_value = table.selected_rows[0]['Symbol']
            except:
                symbol_value = ''
                print('mmm')
                print(symbol_value)
            if symbol_value:
                print('mmm')
                print(symbol_value)
                # self.start_analyse(symbol_value)
            # st.dataframe(self.symbol_mapping, use_container_width=True, hide_index=True)
            st.markdown('# ')
        return table

    def start_analyse(self, symbol):
        self.update_symbol(symbol)
        self.plot_line_graph()
        function_calls = (self.load_data, self.plot_line_graph, self.training_model)
        progress_text = "Operation in progress. Please wait"
        my_bar = st.progress(0, text=progress_text)
        for count, generator_object in enumerate(function_calls, start=1):
            time.sleep(0.5)
            value = ' '.join(list(generator_object()))
            progress_value = calculate_percent(len(function_calls), count)
            print(progress_value)
            my_bar.progress(progress_value, text=value)
        st.toast("Yeah! Forecast calculated")

    def load_data(self):
        self.data = yf.Ticker(self.symbol).history(period='5y')
        yield "loading data .."

    def plot_line_graph(self):
        data = self.data
        my_labels = {'Close': r"$"}
        self.company_name = self.get_company_name()
        title = "Current course: " + self.company_name + " Symbol:" + self.symbol
        st.plotly_chart(px.line(data, y="Close", labels=my_labels, title=title), use_container_width=True)
        yield "plotting .."

    def get_company_symbol(self):
        try:
            name = self.symbol_mapping[self.symbol_mapping['Name'] == self.symbol].iloc[0].at["Symbol"]
        except:
            name = ""
        return name

    def get_company_name(self):
        try:
            name = self.symbol_mapping[self.symbol_mapping['Symbol'] == self.symbol].iloc[0].at["Name"]
        except:
            name = ""
        return name

    def update_symbol(self, new_symbol):
        self.symbol = new_symbol

    def training_model(self):
        data = self.data.reset_index()
        print(data.columns.tolist())
        df_train = data[['Date', 'Close']]
        df_train['Date'] = df_train['Date'].dt.tz_localize(None)
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
        m = Prophet(daily_seasonality=True)
        m.fit(df_train)
        future = m.make_future_dataframe(periods=90)
        forecast = m.predict(future)
        title = f"Prophet forecast for company: {self.company_name}"
        st.plotly_chart(px.line(forecast, x="ds", y="trend", title=title), use_container_width=True)
        yield "calculate forcast .."


def calculate_percent(max_value, current):
    return current / max_value


add_bar_styling()
symbol_as_text = st.text_input("Type finance Symbol for starting analysis: Default value = META", value="META",
                               key="placeholder")
finance_analyser = FinanceAnalyser()
table_data = finance_analyser.insert_example_table()
try:
    symbol_value = table_data.selected_rows[0]['Symbol']
except:
    symbol_value = ''

symbol_as_text = symbol_value or symbol_as_text
finance_analyser.start_analyse(symbol_as_text)
