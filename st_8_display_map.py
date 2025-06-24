import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(50, 2) / [50, 50] + [16.980, 82.24], columns=['lat', 'lon'])
st.map(df)