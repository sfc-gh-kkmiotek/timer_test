import asyncio
import datetime

import streamlit as st

# Start the timer
if not st.session_state.get('timer'):
    st.session_state['timer'] = datetime.datetime.now()


@st.fragment(run_every=1)
def timer_countdown(container):
    time_left = (st.session_state['timer'] + datetime.timedelta(seconds=20)) - datetime.datetime.now()

    if time_left < datetime.timedelta(seconds=0):
        container.text('Times Out!')
    else:
        container.text(
            f'Time left: #{time_left.total_seconds()}'
        )


placeholder = st.empty()

password = st.text_input('password')
time_left = (st.session_state['timer'] + datetime.timedelta(seconds=20)) - datetime.datetime.now()
if password == st.secrets['password'] and time_left > datetime.timedelta(seconds=0):
    st.write('Bingo')

timer_countdown(placeholder)
