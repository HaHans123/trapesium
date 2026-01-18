import streamlit as st
import numpy as np
import synpy as sp
import matplotlib.pyplot as plt

st.title("trapesium")

fungsi = st.text_input("masukkan fungsi f(x):","x**2")
a = st.number_input("batas bawah (a)", value=0.0)
b = st.number_input("batas atas (b)", value=1.0)
n = st.number_input("jumlah interval(n)", value=10, step=1)

x = sp.symbols('x')

if st.button("hitung"):
    try:
        f = sp.lambdify(x, sp.sympify(fungsi), "numpy")
        h = (b - a) / n
        x_val = np.linspace(a, b n+1)
        y_val = f(x_val)

        hasil = (h/2) * (y_val[0] + 2*sum(y_val[1:-1]) + y_val[-1])
        st.success(f"trapesium ≈ {hasil}")

        fig, ax = plt.subplots()
        ax.plot(x_val, y_val, marker='o')
        ax.set_title("trapesium")
        st.pyplot(fig)

    except:
        st.error("Fungsi tidak valid")
