import streamlit as st

st.set_page_config(
    page_title="Sleep Health and Life"
)

objective1 = st.Page('objective1.py', title='Demographic', icon=":material/groups:")

objective2 = st.Page('objective2.py', title='Comparison', icon=":material/balance:")

objective3 = st.Page('objective3.py', title='Correlation', icon=":material/data_usage:")

pg = st.navigation(
    {
        "Menu": [objective1, objective2, objective3]
    }
)

pg.run()
