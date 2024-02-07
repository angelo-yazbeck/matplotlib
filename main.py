import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

bar_x=np.array([1,2,3,4,5])

x=np.linspace(0,10,100)
opt=st.sidebar.radio("select any graph", options=("line","bar","h-bar"))
if opt == "line": 
 fig=plt.figure()
 plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle")
 plt.plot(x,np.sin(x))
 plt.plot(x,np.cos(x),'--')
 st.write(fig)
elif opt == "bar":
 fig =plt.figure()
 plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle")
 plt.bar(bar_x,bar_x*10)
 st.write(fig)



else:
 fig =plt.figure()
 plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle")
 plt.barh(bar_x,bar_x*10)
 st.write(fig)