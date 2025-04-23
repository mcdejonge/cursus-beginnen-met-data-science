Source: https://rdrr.io/cran/ISLR/man/Carseats.html

A simulated data set containing sales of child car seats at 400 different stores.

Created for "ISLR: Data for an Introduction to Statistical Learning with Applications in R"

carseats.csv:

    -Sales: Unit sales (in thousands) at each location
    -CompPrice: Price charged by competitor at each location
    -Income: Community income level (in thousands of dollars)
    -Advertising: Local advertising budget for company at each location (in thousands of dollars)
    -Population: Population size in region (in thousands)
    -Price: Price company charges for carseats at each site
    -ShelveLoc: A factor with levels Bad, Good and Medium indicating the quality of the shelving location for the carseats at each site
    -Age: Average age of the local population
    -Education Education level at each location
    -Urban: A factor with levels No and Yes to indicate whether the store is an urban or non urban location
    -US A factor indicating the location is in- our outside the US

carseats.processed.csv:
    Like carseats.csv but with binary features and multi level features encoded as 1 / 0 and with an extra column 'Above_Below_Avg' that indicates whether the sales number is above (1) or below the average sales number and 'Above_Below_Avg_Loc' that indicates wether the sales number is above (1) or below the average sales number for the specific ShelveLoc.
