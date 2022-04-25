path = "/home/tee/Desktop/ot-harjoitustyo/digipeli/data/wordlists-test.csv"

with open(r'/home/tee/Desktop/ot-harjoitustyo/digipeli/data/wordlists-test.csv', "r") as file:
    row = file.read()
    print(row)

with open(path, "w") as file:
    row.strip()
    print(row)
    file.write(row)
        