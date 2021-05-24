# DBMS_final_project
## Commit Info
commit message:
\
"[date]-[contributor]-[update-info]"

## Run
streamlit run dashboard.py


## Status
project status
data to database => Thu
analyze data, show data on streamlit => Fri, Sat, Sun

state:
    choose ticker:
	try to query =>
	    no result = empty database:
		grab data from yfinance, then query again
 	    has result = non-empty database:
		query using info from database
		up to user => update database

empty => grab up to date info
non-empty => no auto update => user select update button
