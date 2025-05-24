import streamlit as st # Bring in streamlit for UI/app interface
import time

@st.cache_data
def longproc():
  st.util.write( 'Loop micmicking data generation / long process' )
  y=0
  for x in range(20):
    time.sleep(1)
    y = y + 1
  return y

peace = st.empty()

if 'key' not in st.session_state:
  with peace:
    if(st.button('Set Key')):
      y=longproc()
  st.session_state['key'] = 'value'
  utils.st.write( f'Generated data: {y}')

if 'key' in st.session_state:
  peace.empty()

st.write(st.session_state.key)

if(st.button('Set New Session')):
  st.write('new')
  try:
    utils.st.write( f'Generated data: {y}')
  except:
    utils.st.write( f'data cleared from cache')
