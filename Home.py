import streamlit as st # Bring in streamlit for UI/app interface
import time

@st.cache_data
def longproc():
  y=0
  for x in range(5):
    time.sleep(1)
    y = y + 1
  return y

peace = st.empty()

if 'key' not in st.session_state:
  with peace:
    if(st.button('Set Key')):
      y=longproc()
  st.session_state['key'] = y

if 'key' in st.session_state:
  peace.empty()

st.write(st.session_state.key)

if(st.button('Set New Session')):
  st.write('new')
  
