# vanguard-ab-test
Project status - Active

# Project objective
Vanguard, a US-based investment management company, has just launched an exciting digital experiment, and now, they’re eagerly waiting to uncover the results! Due to the ever evolving nature of the digital world, Vanguard is constantly trying to implement new changes to meet the demands of their clients. Vanguard believed that a more intuitive and modern User Interface (UI), coupled with timely in-context prompts (cues, messages, hints, or instructions provided to users directly within the context of their current task or action), could make the online process smoother for clients. 

The critical question was: *Would these changes encourage more clients to complete the process?*

# Methods

General
- Head
- Shape
- Info
- Dtypes

Cleaning 
- Drop na values
- Fill na
- Duplicated
- Nunique

Tranformation
- Merges
- Concats
- Filtering
- Grouping (loc, mask)
- Sort values
- Pandas to Datetime
- Shift 
  
Exploratory Data Analysis (EDA)
  - Value Counts
  - Info 
  - Describe (Mean, Median, Mode, Percentiles , Min, Max)  
  
# Technologies

- Python
- Pandas
- Seaborn
- Statsmodels.api
- Matplotlib.pyplot
- Numpy
- Scipy.stats
- Tableau 

# Project Description
An A/B test was set into motion from 3/15/2017 to 6/20/2017 by the team.

* **Control Group**: Clients interacted with Vanguard’s traditional online process.
* __Test Group__: Clients experienced the new, spruced-up digital interface.

Both groups navigated through an identical process sequence: an initial page, three subsequent steps, and finally, a confirmation page signaling process completion.

The goal is to see if the new design leads to a better user experience and higher process completion rates.

The experiment counted with 3 datasets:

1. Client Profiles (df_final_demo): Demographics like age, gender, and account details of our clients.
2. Digital Footprints (df_final_web_data): A detailed trace of client interactions online, divided into two parts: pt_1 and pt_2. These two files were merged into one comprehensive data frame.
3. Experiment Roster (df_final_experiment_clients): A list revealing which clients were part of the grand experiment.


# Steps
During the project we found the need to create new datafames to better utilize the data that was gathered during the experiment. 

- df_online: We discovered that we had more client profiles than those within the experiment roster, so we created a dataframe with the clients that were part of the experiment and their demographic information. 

- df_ab: We wanted to be able to know the demographic information about the users that participated and their digital footprints, so we created this dataframe to analyze this information.

To properly understand the effects of the experiment, we had to filter the afformentioned dataframe (df_ab) into two dataframes:
- df_test = The filtered data of the clients from the Test Group.

- df_control: The filtered data of the clients from the Control Group.

  We chose to utilize 2 success metrics (KPI's) for our analysis,
  - Completion Rate
  - Time Spent on Each Step

  For our hypothesis testing, we tested for 3 hypothesis:
  - Completion Rate
  - Completion Rate with a Cost-Effectiveness Threshold (5%)
  - Difference on steps


# Conclusion
After testing for the three hypothesis, we ended up with the following insights:
- Completion Rate: Reject the null hypothesis, there is a significant difference in completion rates between the test and control groups
- Completion Rate with a Cost-Effectiveness Threshold (5%): Reject the null hypothesis. The observed increase in completion rate is statistically significant but it does not meet the 5% threshold placed by the company.
-  Difference on steps: Fail to reject the null hypothesis. The means of the time per step are not significantly different.

  With this information, we can answer the question that was posed: *Would these changes encourage more clients to complete the process?*
  
The answer to that question would that our test did not provide sufficient evidence to conclude that the effect exists. Hence, we can say tha the changes did not encourage more clients to complete the process. 

# Contact
linkedin, github, medium, etc
