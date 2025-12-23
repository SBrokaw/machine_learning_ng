# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: .venv (3.12.3)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Optional Lab:  Brief Introduction to Python and Jupyter Notebooks
# Welcome to the first optional lab! 
# Optional labs are available to:
# - provide information - like this notebook
# - reinforce lecture material with hands-on examples
# - provide working examples of routines used in the graded labs

# %% [markdown]
# ## Goals
# In this lab, you will:
# - Get a brief introduction to Jupyter notebooks
# - Take a tour of Jupyter notebooks
# - Learn the difference between markdown cells and code cells
# - Practice some basic python
#

# %% [markdown]
# The easiest way to become familiar with Jupyter notebooks is to take the tour available above in the Help menu:

# %% [markdown]
# <figure>
#     <center> <img src="../images/C1W1L1_Tour.PNG"  alt='missing' width="400"  ><center/>
# <figure/>

# %% [markdown]
# Jupyter notebooks have two types of cells that are used in this course. Cells such as this which contain documentation called `Markdown Cells`. The name is derived from the simple formatting language used in the cells. You will not be required to produce markdown cells. Its useful to understand the `cell pulldown` shown in graphic below. Occasionally, a cell will end up in the wrong mode and you may need to restore it to the right state:

# %% [markdown]
# <figure>
#    <img src="../images/C1W1L1_Markdown.PNG"  alt='missing' width="400"  >
# <figure/>

# %% [markdown]
# The other type of cell is the `code cell` where you will write your code:

# %% height=47
#This is  a 'Code' Cell
print("This is  code cell")

# %% [markdown]
# ## Python
# You can write your code in the code cells. 
# To run the code, select the cell and either
# - hold the shift-key down and hit 'enter' or 'return'
# - click the 'run' arrow above
# <figure>
#     <img src="../images/C1W1L1_Run.PNG"  width="400"  >
# <figure/>
#
#  

# %% [markdown]
# ### Print statement
# Print statements will generally use the python f-string style.  
# Try creating your own print in the following cell.  
# Try both methods of running the cell.

# %% height=64
# print statements
variable = "right in the gramma!"
print(f"f strings allow you to embed variables {variable}")

# %% [markdown]
# # Congratulations!
# You now know how to find your way around a Jupyter Notebook.

# %% height=30
