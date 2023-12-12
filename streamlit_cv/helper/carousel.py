from streamlit_carousel import carousel


def add_carousel():
    test_items = [
        dict(
            title="",
            text="Python",
            interval=None,
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/pyton.jpg?raw=true",
        ),
        dict(
            title="",
            text="HTML",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/html.jpg?raw=true",
        ),
        dict(
            title="",
            text="SQL",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/sql.jpg?raw=true",
        ),
    ]

    return carousel(items=test_items, width=1)
