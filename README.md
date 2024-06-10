# <p align="center">Module 10 Challenge: Advanced SQL/SQLAlchemy
## Data Analytics assignment to analyze and explore climate data in a SQLite database using SQLAlchemy and Flask
### Overview
1. Data analysis
2. Data exploration
3. App design
### Features
1. Use Python, SQLAlchemy ORM queries, Pandas, and Matplotlib to analyze and visualize climate data housed in a SQLite database
2. Address assignment prompts using the above methods/tools
3. Design a Flask API to create both static and dynamic routes to return JSONified versions of assigned dictionaries/datasets/lists
### Prerequisites
- Familiarity with and use of the Python programming language, and software to interact with .py files, such as [Spyder](https://www.spyder-ide.org/)
- Familiarity with and use of [Jupyter Notebook](https://jupyter.org/) to interact with .ipynb files
- Familiarity with and use of [SQLAlchemy](https://www.sqlalchemy.org/)
- Familiarity with and use of [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- Familiarity with and use of a web browser, such as [Chrome](https://www.google.com/chrome/)
### Usage
#### .ipynb
- Download the Resources directory, and climate.ipynb and app.py files, all to the same directory/destination
    - The .csv files are there for reference, and contain data that's within the .sqlite database file
- Launch Jupyter Notebook, and open climate.ipynb
- Inspect the dependencies and ensure they're installed
- Clear outputs (if desired), and inspect/run the code cell by cell, or all at once if desired
    - Assignment prompts are listed as #comments at the top of input cells
- Have fun exploring/playing around with the data!
#### .py
- Open the app.py file with the desired code editor
- Again, inspect the dependencies and ensure they're installed
- Run the code
    - Assignment prompts are listed as #comments throughout the code
- In the console/terminal window of the editor, a link (like [http://127.0.0.1:5000](http://127.0.0.1:5000)) should be displayed; control/command-click to follow it (if possible in the editor) or copy-paste it into a browser window/tab
<p align="center">
  <img width="450" src="https://github.com/cengelhart0120/sqlalchemy-challenge/blob/main/climate-api-routes.png" alt="Screenshot of Flask API landing page">
</p>

- Visit each page listed by appending "http://127.0.0.1:5000" with what is shown on each line
- Play around with the "date" (yyyy-mm-dd) field(s) of the links; the links are dynamic and will return data for a given date if it exists in the database!
### License
[MIT License](https://opensource.org/licenses/MIT)
### Contact
[Email](mailto:cengelhart@gmail.com)\
[GitHub](https://github.com/cengelhart0120)
