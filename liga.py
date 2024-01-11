def liga_dict(matches: str) -> dict:
    with open(matches, "r") as fhi:
        table: dict = {}
        for line in fhi:
            match = line.split(";")
            team1 = match[0]
            team2 = match[1]

            if int(match[2]) > int(match[3]):
                points = (3,0)
            elif int(match[2]) < int(match[3]):
                points = (0,3)
            else:
                points = (1,1)

            for i in range(0,2):
                if match[i] in table:
                    table[match[i]] = table[match[i]] + int(points[i])
                else:
                    table[match[i]] = points[i]

    return table

print(liga_dict("liga.csv"))