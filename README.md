# Streamlit Practice - DS-Live-062722

![deploy gif from tenor](https://c.tenor.com/im-8kxzdMzwAAAAd/deploy.gif)

## Pre-Requisites

1. Fork this repository
2. Clone your fork of this repo
3. Create a new conda environment from the yml file in this repo
    - In your terminal, navigate to your clone of this repo, then run: 
    ```
    conda env create -n streamlit --file st-environment.yml
    ```

**BONUS:** The session will go a lot smoother if you have a code editor installed! I'll be using [VS Code](https://code.visualstudio.com/).

> By default for Windows users, VS Code will create a `code` command you can use from Git Bash to launch VS Code easily.
>
> Mac users can set up the same command by following the instructions found [here](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line).

## Run of Show:

1. Explore [Streamlit documentation](https://docs.streamlit.io/) and create a simple app.py file
    - Using `st.write()`
    - Creating and displaying data
    - Creating and displaying visualizations
    - Utilizing inputs through input widgets

2. Walk through an example project to be deployed
    - How to think about model inputs when designing your model
    - How to pickle a fit sklearn model
    - How to test using a pickled model before deployment

3. Create a Streamlit app to take in inputs, transform data appropriately, load a pickled model, and make predictions on new incoming data