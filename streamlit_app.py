import asyncio
import datetime

import streamlit as st

# Start the timer
if not st.session_state.get('timer'):
    st.session_state['timer'] = datetime.datetime.now()


@st.fragment(run_every=1)
def timer_countdown(container):
    time_left = (st.session_state['timer'] + datetime.timedelta(minutes=3)) - datetime.datetime.now()

    container.text(
        f'Time left: #{time_left.total_seconds()}'
    )


placeholder = st.empty()

password = st.text_input('password')
if password == st.secrets['password']:
    st.write('Bingo')

timer_countdown(placeholder)
