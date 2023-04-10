from check_registered import colour

def main():
    mode = input(colour(4, "Sort by (p)rice or (l)ength? "))

    inp = open("output-available-taken.txt", "r").readlines()

    output = []
    out_path = "output-available-sorted.txt"

    if mode == "p":
        # prices = []
        # for line in inp:
        #     p1 = line.split(" ")
            
        #     if p1.__len__() == 3 or p1.__len__() == 5:
        #         p1 = p1[2].replace("$","")
        #         prices.append(float(p1))

            
        #sort input by price
        for line in inp:
            p1 = line.split(" ")
            if p1.__len__() >= 3:
                p1 = p1[2].replace("$","")
                
                output.append((line, float(p1)))
            else:
                output.append((line, float(999999)))
        output.sort(key=lambda x: x[1])

    elif mode == "l":
        #sort input by length
        for line in inp:
            length = len(line.split(" ")[0])
            output.append((line, length))
        output.sort(key=lambda x: x[1])

    with open(out_path, "w") as f:
        for line in output:
            f.write(line[0])
        f.close()
