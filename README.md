# COMP7034 Example Repository

This repository contains a GitHub Action Workflow that performs a HTTP GET request on a URL, 
processes the data in python and writes the resulting data (in this case the weather forecast in Oxford) to a timestamped file.

It is on a scheduled job to run each week, but will also run every time a commit is pushed to the repository. 

`workflow.yml` calls a single python script `script.py`.

Although the workflow is called weekly, the data stored has a to the second filename.
