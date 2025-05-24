import streamlit as st # Bring in streamlit for UI/app interface
import time

progress_bar = st.progress( 0, text='Generating data...')

@st.cache_data
def longproc():
  st.util.write( 'Loop micmicking data generation / long process' )
  y=0
  for x in range(20):
    progress_bar.progress( x/20, text='Generating data...')
    time.sleep(1)
    y = y + 1
  return y
progress_bar.empty()

peace = st.empty()

if 'key' not in st.session_state:
  with peace:
    if(st.button('Calc data')):
      y=longproc()
      u tils.st.write( f'Generated data: {y}')
  st.session_state['key'] = 'value'
  
if 'key' in st.session_state:
  peace.empty()

st.write(st.session_state.key)

if(st.button('Set New Session')):
  st.write('new')
  try:
    utils.st.write( f'Generated data: {y}')
  except:
    utils.st.write( f'data cleared from cache')
