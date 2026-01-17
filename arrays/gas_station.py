def can_complete_circuit(cost,gas):
    total_cost = sum(cost)
    total_gas = sum(gas)
    start = 0
    current_gas = 0
    for i in range(len(cost)):
        current_gas+=(gas[i]-cost[i])
        if current_gas < 0:
            current_gas = 0
            start = i+1
    return start 

cost = [3,4,5,1,2]
gas = [1,2,3,4,5]
print(can_complete_circuit(cost,gas))