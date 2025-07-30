# Task 05: Descriptive Statistics and Large Language Models

## Overview
This project fulfills the requirements for Task 5: Descriptive Statistics and Large Language Models. The goal is to use a small public sports dataset, perform data cleaning and descriptive analysis, and then challenge a large language model (LLM) to answer natural language questions about the data. The project documents both the scripting/analysis process and the LLM's performance.

## Dataset
- **Source:** MLB Max Running Speed (2020 season)
- **File:** `cleaned_mlb_speed.csv` (not included in the public repo)
- **Description:** Contains player sprint speed, position, team, age, and other relevant metrics for all MLB players in 2020.

## Project Structure
- `python_script.py`: Cleans the original dataset and outputs `cleaned_mlb_speed.csv`.
- `desc_stats.py`: Computes descriptive statistics and writes results to `desc_stats_output.txt`.
- `visualizations.py`: Generates and saves visualizations as PNG files.
- `desc_stats_output.txt`: Output of descriptive statistics (not for repo, for reporting only).
- `Task_05_report.pdf`: Full research report, including LLM prompt engineering, validation, and findings.

## How to Run
1. Place the raw data file in the appropriate location and run `python_script.py` to generate the cleaned CSV.
2. Run `desc_stats.py` to generate descriptive statistics in `desc_stats_output.txt`.
3. Run `visualizations.py` to generate all plots in the same folder.
4. Use the cleaned data and statistics to prompt an LLM (e.g., ChatGPT, Copilot, Claude) and record its answers.

## LLM Prompt Engineering & Validation
- Natural language questions were designed to probe the LLM's ability to interpret and analyze the dataset (see report for details).
- LLM responses were validated against the outputs of the scripts and visualizations.
- The process, successes, and failures are documented in `Task_05_report.pdf`.

## Notes
- **Do not include the dataset file in the public repository.**
- All scripts are modular and can be run independently.
- For any issues or questions, see the report or contact the project author.

## Files to Include in Public Repo
- `python_script.py`
- `desc_stats.py`
- `visualizations.py`
- `README.md` (this file)
- `Task_05_report.pdf` (if allowed)

## Acknowledgments
- MLB public data sources
- Syracuse University OPT Research Analyst Project

---
For more details, see the full report: `Task_05_report.pdf`.
