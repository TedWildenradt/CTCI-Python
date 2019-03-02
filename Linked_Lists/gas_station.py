def completeTrip(gas, cost):
  diff = []
  for i in range(len(gas)):
    diff.append(gas[i] - cost[i])
  
  min_idx = 0
  min_pos = diff[0]
  for i in range(1,len(diff)):
    if diff[i] <= min_pos:
      min_pos = diff[i]
      min_idx = i
  if sum(diff) < 0:
    return -1
  else:
    return (min_idx + 1) % len(gas)



gas  = [5,8,2,8]
cost = [6,5,6,6]
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
completeTrip(gas,cost)