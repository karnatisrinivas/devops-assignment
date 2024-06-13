### Simulate the following situation. Attach the code as part of your submission.

* At a post office, customers enter a single line waiting to be served by any one of two clerks. 
* Every minute there is a 60% chance that a new customer arrives. 
* If there is no one in line and a server is free, the customer does not wait to be served. 
* When a customer is being served there is a 25% chance every minute that they complete their business and leave. 
* When the clerk is free he will take the next customer in line, in the order that they arrived. 
* Every minute, there is a 5% chance that a person standing in line will give up and leave. 
* The post office is always open (24/7/365).
* Note: For simplicity you can assume customers will always arrive at the beginning of the minute and if they leave they do so at the end of the minute.

* What is the average amount of time a customer spends in the post office (including those not served)?
* What percentage of customers leave without being served?
* What percentage of time are the clerks idle?


### Logic: 
- There are two clerks available at the post office.
- Customers always wait in a single line.
- There is a 60% chance (0.60) that a new customer arrives every minute.
- When a customer is being served, there is a 25% chance (0.25) that they complete their business and leave every minute.
- If a clerk is free, the next customer in line is served in a first-in, first-out (FIFO) manner.
- There is a 5% chance (0.05) every minute that a customer in line gives up and leaves.
- The post office is open 24/7/365, but for the simulation, we are considering the number of minutes in a week (10080 minutes).
- We are not considering any fractional part of a minute.

### code flow:

- every minute the customer count increases by 0.60.
- every minute the customer will left without served by 0.05.
- every minute the customer is served and leaves by 0.25. 
- If no one is in queue, clerk will be idle. 

### Functions used: 
- Math.random() - we used this function as we are talking about the percentage of chances. 

### Simulation results:

```
Average time: 6.9553615549332894
Percentage left without being served: 35.776643057156974
Percentage idle time: 20.887896825396826
```

