import numpy as np

prefSims = np.zeros(1000)

for sim in range(0, 1000):
    
    numPrefFlavor = 0

    # treat pill bottle as an aray of zeros and ones
    # hardcode known values - 2 flavors, 60 pills to start, 50/50 split

    pill_bottle = np.append(np.zeros(30), np.ones(30))

    while pill_bottle.size > 0:
        np.random.shuffle(pill_bottle)
        todays_pills = pill_bottle[0:4]
        pill_bottle = pill_bottle[4:]
        numPrefFlavor += min(2, todays_pills.size - sum(todays_pills))

    print("Sim", sim, "Preferred Count:", numPrefFlavor)
    prefSims[sim] = numPrefFlavor / 30

print("Final average:", np.mean(prefSims))
print("Highest:", np.max(prefSims))
print("Lowest:", np.min(prefSims))
    
            

