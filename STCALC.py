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

head = """
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,user-scalable=no"><meta name="theme-color" content="#FFFFFF"><link rel="mask-icon" href="/-/build/favicon_safari_mask.png" color="#FF2B2B"><link rel="apple-touch-icon" href="/-/build/favicon_256.png"><link rel="manifest" href="/-/build/manifest.json"><script src="https://js.hs-banner.com/v2/6571207/banner.js" type="text/javascript" id="cookieBanner-6571207" data-cookieconsent="ignore" data-hs-ignore="true" data-loader="hs-scriptloader" data-hsjs-portal="6571207" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script src="https://js-na1.hs-scripts.com/6571207.js" type="text/javascript" id="hs-script-loader"></script><script type="text/javascript" async="" src="https://js.hs-analytics.net/analytics/1678388700000/6571207.js" id="hs-analytics"></script><script type="text/javascript" src="https://cdn.segment.com/next-integrations/integrations/vendor/commons.c42222c4cb2f8913500f.js.gz" async="" status="loaded"></script><script type="text/javascript" src="https://cdn.segment.com/next-integrations/integrations/hubspot/2.2.4/hubspot.dynamic.js.gz" async="" status="loaded"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://cdn.segment.com/analytics.js/v1/GI7vYWHNmWwHbyFjBrvL0jOBA1TpZOXC/analytics.min.js"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-52GRQSL"></script><script>!function(e,t,a,n,g){e[n]=e[n]||[],e[n].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var m=t.getElementsByTagName(a)[0],r=t.createElement(a);r.async=!0,r.src="https://www.googletagmanager.com/gtm.js?id=GTM-52GRQSL",m.parentNode.insertBefore(r,m)}(window,document,"script","dataLayer")</script><script>!function(){var e=window.analytics=window.analytics||[];if(!e.initialize)if(e.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{e.invoked=!0,e.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on","addSourceMiddleware","addIntegrationMiddleware","setAnonymousId","addDestinationMiddleware"],e.factory=function(t){return function(){var n=Array.prototype.slice.call(arguments);return n.unshift(t),e.push(n),e}};for(var t=0;t<e.methods.length;t++){var n=e.methods[t];e[n]=e.factory(n)}e.load=function(t,n){var a=document.createElement("script");a.type="text/javascript",a.async=!0,a.src="https://cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var r=document.getElementsByTagName("script")[0];r.parentNode.insertBefore(a,r),e._loadOptions=n},e.SNIPPET_VERSION="4.13.1",e.load("GI7vYWHNmWwHbyFjBrvL0jOBA1TpZOXC"),e.page()}}()</script><link href="/-/build/static/css/2.ef852789.chunk.css" rel="stylesheet"><link href="/-/build/static/css/main.b2fc17cd.chunk.css" rel="stylesheet"><style media=""></style><script charset="utf-8" src="/-/build/static/js/10.d56593f0.chunk.js"></script><title>Streamlit</title><link id="favicon" rel="icon" href="//statisticscalculator.streamlit.app/~/+//favicon.png"><link id="alternate-favicon" rel="alternate icon" href="//statisticscalculator.streamlit.app/~/+//favicon.png"></head>
"""

st.components.v1.html(head + naversa)

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

