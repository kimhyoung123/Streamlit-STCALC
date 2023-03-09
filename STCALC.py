import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.linear_model import LinearRegression
from streamlit.components.v1 import html

naversa = """
<meta name="naver-site-verification" content="c6e48c866638bf91242179525a9f22478aed3e55" />
"""

additional_html = f"<head>{naversa}</head>"
st.components.v1.html(additional_html)

st.title("STCALC")

tab1, tab2, tab3= st.tabs(['Statistics Calculator' , 'Standard Normal Distribution Table', 'Regression'])

with tab1:
    st.subheader("Statistics Calculator")
    # Get user input
    nums_str = st.text_input("Enter numbers (comma or space separated)", "1,2,3,4,5")
    nums_str = nums_str.replace(",", " ")
    nums = [float(x.strip()) for x in nums_str.split()]

    # Calculate statistics
    mean = np.mean(nums)
    std = np.std(nums)
    var = np.var(nums)

    if st.button("Calculate"):
        # Display results
        st.write(f"Input: {nums}")
        st.write(f"Mean: {mean:.2f}")
        st.write(f"Standard Deviation: {std:.2f}")
        st.write(f"Variance: {var:.2f}")

        # Show dataframe
        df = pd.DataFrame(nums, columns=["nums"], index=range(1, len(nums)+1))
        st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

        # Plot histogram
        fig, ax = plt.subplots()
        ax.plot(nums, 'o-')
        plt.xticks(range(1, len(nums)+1))
        plt.yticks(range(0, int(max(nums))+1))
        st.pyplot(fig)

with tab2:
    st.subheader("Standard Normal Distribution Table")

    # Get user input
    z = st.number_input("Enter z-value")

    if st.button("Confirm"):
        # Calculate probability using SciPy
        prob = norm.cdf(z)

        # Generate x values
        x = np.linspace(-3, 3, 1000)

        # Generate y values for standard normal distribution
        y = norm.pdf(x)

        # Create a figure and plot the standard normal distribution
        fig, ax = plt.subplots()
        ax.plot(x, y)

        # Highlight area corresponding to user input
        ax.fill_between(x, 0, y, where=(x >= z), alpha=0.5)

        # Set axis labels and title
        ax.set_xlabel("z")
        ax.set_ylabel("Probability Density")
        ax.set_title("Standard Normal Distribution")

        # Display the plot in Streamlit
        st.pyplot(fig)
        st.success(f"Probability: {prob:.4f}")

with tab3:
    st.subheader("Regression")

    # Get user input
    x_vals = st.text_input("Enter x-values (comma or space separated)", "1,2,3,4,5")
    x_vals = x_vals.replace(",", " ")
    x_arr = [float(x.strip()) for x in x_vals.split()]
    x_ary = np.array(x_arr)

    y_vals = st.text_input("Enter y-values (comma or space separated)", "1,2,3,4,5")
    y_vals = y_vals.replace(",", " ")
    y_arr = [float(y.strip()) for y in y_vals.split()]
    y_ary = np.array(y_arr)

    if len(x_ary) != len(y_ary):
        st.error("Number of x-values must equal number of y-values")

    if st.button("Calc"):
        x_2d = x_ary.reshape(-1, 1)
        y_2d = y_ary.reshape(-1, 1)

        # Perform linear regression and predict y values
        reg = LinearRegression().fit(x_2d, y_2d)
        y_pred = reg.predict(x_2d)

        # Plot data points and regression line
        fig, ax = plt.subplots()
        ax.scatter(x_ary, y_ary, label="Data Points")
        ax.plot(x_ary, y_pred, color="r", label="Regression Line")

        # Set axis labels and title
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Linear Regression")

        # Display plot in Streamlit
        st.pyplot(fig)

        # Display regression coefficients
        st.success(f"Slope: {reg.coef_[0][0]:.2f}")
        st.success(f"Intercept: {reg.intercept_[0]:.2f}")

        # Display R-squared value
        st.success(f"R-squared: {reg.score(x_2d, y_2d):.2f}")

