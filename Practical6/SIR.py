# create a SIR model
# import nessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define the variables in the model, beta, gamma, S, I, R, N
# S = number of susceptible individuals
# I = number of infected individuals
# R = number of recovered individuals
# N = population size
# beta = rate of infection 
# gamma = rate of recovery
# t = time
N = 1000
beta = 0.3
gamma = 0.05
# create an array to track the infecous individuals over time
# Initially, I = 1, S=999,R=0
I = 1
S = 999
R = 0
# create the title for the plot
plt.figure(figsize=(6, 4), dpi=150)
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model')
# create lists to store the number of infectious, susceptible and recovered individuals
list_infectious = []
list_susceptible = []
list_recovery = []
times = (1000)
# loop through the time steps to simulate the SIR model
for i in range(1000):
    # generate a list of random numbers 0 or 1 to simulate the infection and recovery process
    # calculate the possibility of susceptible people getting infected and infectious people recovering
    list_susceptible1 = np.random.choice(range(2), S, p=[1-beta*I/N, beta*I/N])
    list_infectious1 = np.random.choice(range(2), I, p=[gamma, 1-gamma])
    # update the number of susceptible, infectious and recovered individuals
    for j in list_susceptible1:
        if I>0:
            if j == 1:
                S -= 1
                I += 1
    for k in list_infectious1:
        if I>0:
            if k == 1:
                I += 0
            else:
                R += 1
                I -= 1
    list_infectious.append(I)
    list_susceptible.append(S)
    list_recovery.append(R)
# plot the number of infectious, susceptible and recovered individuals over time
plt.plot(list_infectious, label='Infected')
plt.plot(list_susceptible, label='Susceptible')
plt.plot(list_recovery, label='Recovered')
plt.legend()
plt.show()
