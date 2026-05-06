
metric = [1, 2, 3, 4]
metric2 = [1, 2, 3, 4]

# Add two metrics (lists) using nested loops (element-wise)
sumMetrics = []
for i in range(len(metric)):
    for _ in range(1):
        sumMetrics.append(metric[i] + metric2[i])

print("metric:", metric)
print("metric2:", metric2)
print("sumMetrics:", sumMetrics)

