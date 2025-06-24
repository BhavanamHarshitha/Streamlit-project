import streamlit as st
import time
st.balloons() 

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.balloons()   

st.balloons()
st.subheader("Progress Bar")
st.progress(10)

st.subheader("wait for it...")
with st.spinner('Wait for it...'):
    time.sleep(10)


st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))