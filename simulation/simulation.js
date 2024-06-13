function simulatePostOffice(minutes) {
    let queue = [];
    let clerks = [null, null];
    let totalTime = 0;
    let totalCustomers = 0;
    let customersLeft = 0;
    let idleTime = 0;

    for (let minute = 0; minute < minutes; minute++) {
        if (Math.random() < 0.6) {
            queue.push(minute);
            totalCustomers++;
        }
        queue = queue.filter(() => {
            if (Math.random() < 0.05) {
                customersLeft++;
                return false;
            }
            return true;
        });
        clerks.forEach((clerk, i) => {
            if (clerk === null && queue.length > 0) {
                clerks[i] = queue.shift();
            } else if (clerk !== null) {
                if (Math.random() < 0.25) {
                    totalTime += (minute - clerks[i]);
                    clerks[i] = null;
                }
            }
        });
        idleTime =idleTime+ clerks.filter(clerk => clerk === null).length;
    }
    let avgTime = totalTime / totalCustomers;
    let percentLeft = (customersLeft / totalCustomers) * 100;
    let percentIdleTime = (idleTime / (minutes * clerks.length)) * 100;
    return {
        averageTime: avgTime,
        percentageLeft: percentLeft,
        percentageIdleTime: percentIdleTime
    };
}
let simulationResults = simulatePostOffice(10080);

console.log("Average time:", simulationResults.averageTime);
console.log("Percentage left without being served:", simulationResults.percentageLeft);
console.log("Percentage idle time:", simulationResults.percentageIdleTime);
