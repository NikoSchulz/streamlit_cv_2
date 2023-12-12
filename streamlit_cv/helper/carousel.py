from streamlit_carousel import carousel


def add_carousel():
    test_items = [
        dict(
            title="Python",
            text="",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/pyton.jpg?raw=true",
        ),
        dict(
            title="HTML",
            text="",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/html.jpg?raw=true",
        ),
        dict(
            title="SQL",
            text="",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/sql.jpg?raw=true",
        ),
    ]

    return carousel(items=test_items, width=1)
