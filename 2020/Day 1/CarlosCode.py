def main():
    data = fetch(1)
    lines = data.split('\n')
    lines = [int(x) for x in lines]
    thesum = 0
    while thesum != 2020:
        for i in range(len(lines)):
            if thesum == 2020:
                break
            for j in range(len(lines)-(i+1)):
                if thesum == 2020:
                    break
                partial_sum = lines[i]+lines[j]
                if partial_sum < 2020:
                    for k in range(len(lines)-(j+1)):
                        thesum = lines[i]+lines[j]+lines[k]
                        if thesum == 2020:
                            print([lines[i], lines[j], lines[k], thesum])
                            print(lines[i]*lines[j]*lines[k])
                            break