#SRBA Real Estate Investment 
#EQR Real Estae Invesntment 


import numpy as np

adj_closings_sbra = adj_closings_sbra = np.loadtxt("SBRA.csv", skiprows=1, usecols=5, delimiter=',')
print(adj_closings_sbra)

#Simple Rate of return Calculation 
def simple_rate_of_return(adj_closings):
    daily_simple_ror = np.diff(adj_closings)/adj_closings[:-1]
    return daily_simple_ror

daily_simple_returns_sbra = simple_rate_of_return(adj_closings_sbra)
print(daily_simple_returns_sbra )

#Average Daily Return 
average_daily_simple_return_sbra = np.mean(daily_simple_returns_sbra)
print(average_daily_simple_return_sbra)


#Log Returns 
def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns

daily_log_returns_sbra = log_returns(adj_closings_sbra)
print(daily_log_returns_sbra)

#Annulize Daily Log

def annualize_log_return(daily_log_returns):
    average_daily_log_returns = np.mean(daily_log_returns)
    annualized_log_return = average_daily_log_returns*252 #252 trading days 
    return annualized_log_return


annualized_log_return_sbra = annualize_log_return(daily_log_returns_sbra)
print(annualized_log_return_sbra)

#Variance
daily_varaince_sbra = np.var(daily_log_returns_sbra)
print(daily_varaince_sbra)

#SD
daily_sd_sbra = np.std(daily_log_returns_sbra)
print(daily_sd_sbra)

#EQR
adj_closings_eqr = np.loadtxt("EQR.csv", skiprows=1, usecols=5, delimiter=',')
print(adj_closings_eqr)

#Simple Rate of return
daily_simple_returns_eqr = simple_rate_of_return(adj_closings_eqr)
print(daily_simple_returns_eqr)

#Average Daily return 
average_daily_simple_return_eqr = np.mean(daily_simple_returns_eqr)
print(average_daily_simple_return_eqr)

#Log 
daily_log_returns_eqr = log_returns(adj_closings_eqr)
print(daily_log_returns_eqr)

#Annulize 
annualized_log_return_eqr = annualize_log_return(daily_log_returns_eqr)
print(annualized_log_return_eqr)

#Variance log

daily_varaince_eqr = np.var(daily_log_returns_eqr)
print(daily_varaince_eqr)

#sd log
daily_sd_eqr = np.std(daily_log_returns_eqr)
print(daily_sd_eqr)

#Correlation Coefficent 
corr_sbra_eqr = np.corrcoef(daily_log_returns_sbra,daily_log_returns_eqr)
print(corr_sbra_eqr)
