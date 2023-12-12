from streamlit_carousel import carousel


def add_carousel():
    test_items = [
        dict(
            title="",
            text="Python",
            interval=None,
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/ec0e3f35-8a3c-4e17-a9b1-6fd2a4d2a332.jpg?raw=true",
        ),
        dict(
            title="",
            text="HTML",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/html_image.jpg?raw=true",
        ),
        dict(
            title="",
            text="SQL",
            img="https://github.com/NikoSchulz/streamlit_cv_2/blob/master/streamlit_cv/resource/images/sql_image.jpg?raw=true",
        ),
    ]

    return carousel(items=test_items, width=1)
