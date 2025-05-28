# create a SIR model
# import nessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define the variables in the model, beta, gamma, S, I, R, N
# S = number of susceptible individuals
# I = number of infected individuals
# R = number of recovered individuals
# N = total population
# beta = rate of infection 
# gamma = rate of recovery
N = 1000
beta = 0.3
gamma = 0.05
# create an array to track the infecous individuals over time
# Initially, I = 1, S=999,R=0
plt.figure(figsize=(6, 4), dpi=150)
plt.xlabel('time')
plt.ylabel('Number of people')
plt.title('SIR Model with different vaccination rates')
# create a list of probability of immunization
# loop through the list of probability of immunization
# for each probability of immunization, calculate the number of infectious individuals
list_probabitity = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for IM in list_probabitity:
    S=int(999-N*IM)
    I=1
    R=0
    # create lists to store the number of infectious, susceptible and recovered individuals
    list_infectious = []
    # simulate the SIR model for 1000 time steps under different vaccination rates
    for i in range(1000):
        # generate a list of random numbers 0 or 1 to simulate the infection and recovery process
        list_susceptible1 = np.random.choice(range(2), S, p=[1-beta*I/N, beta*I/N])
        list_infectious1 = np.random.choice(range(2), I, p=[gamma, 1-gamma])
        # if the number is 1, it means the susceptible individual gets infected, if the number is 0, it means the infectious individual recovers
        for j in list_susceptible1:
            if I>0:
                if j == 1:
                    S -= 1
                    I += 1
        # if the number is 0, it means the infectious individual recovers, if the number is 1, it means the infectious individual stays infectious
        for k in list_infectious1:
            if I>0:
                if k == 1:
                    I += 0
                else:
                    R += 1
                    I -= 1
    # append the number of infectious individuals to the list
        list_infectious.append(I)
    # plot the number of infectious individuals over time for each vaccination rate
    plt.plot(list_infectious, label='the vaccination rate='+str(IM))
plt.legend()
plt.show()