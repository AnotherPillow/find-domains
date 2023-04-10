from tika import parser # pip install tika
import re,math,sys
from check_registered import colour

def main(parse=True):
    if len(sys.argv) < 1 and not parse:
        if sys.argv[1] == '--parse':
            parse=True

    if parse:
        raw = parser.from_file('Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf')
        lines = raw['content'].splitlines()
    else:
        lines = open('domains-alphabetical.txt', 'r').readlines()

    t_a = ''

    pattern = r'^(\w+)\s+\$(\d+\.\d{2})\s+\$(\d+\.\d{2})'
    

    print(colour(1, "Sorting by alphabetical order..."))

    for line in lines:
        line = line.replace("*","")
        matched = re.search(pattern, line)
        if matched:
            name = matched.group(1)
            price1 = matched.group(2)
            #print(f"{name}: {price1}")
            t_a += f".{name} ${price1}\n"

    

#     for line in lines:

#         if line != '':
#             mo = re.search(r'^\w+\s+\$(\d+\.\d+)\*\?\s+\$(\d+\.\d+)\s+\$(\d+\.\d+)\s+\$(\d+\.\d+)\s+\w+\s*\w*'
# , line)
#             if mo != None:
#                 print(line)

#                 c = mo.group().split(' ')
#                 x = " ".join(c[0:2])
#                 #print(f'.{x}')
#                 if line.startswith(".") :
#                     t_a+=x + "\n"
#                 elif line != "":
#                     t_a+= "." + x + "\n"
#                 else:
#                     pass
                    


    print(colour(1, "Sorted by alphabetical order"))
    
    with open('domains-alphabetical.txt', 'w') as f:
        f.write(t_a)
        f.close()

    #t_a = [x.replace("\n","") for x in open('domains-alphabetical.txt', 'r').readlines() if x != '\n']
    t_a = [x.replace("\n","") for x in t_a.split("\n") if x != '\n']


    print(colour(1, "Sorting by price..."))
    prices_unsort = []
    for x in t_a:
        if x != '':
            price = x.split(" ")[1].replace("$","")
            prices_unsort.append({
                'price': float(price),
                'domain': x.split(" ")[0]

            })
    #sort the prices but keep the domain names
    prices_sort = sorted(prices_unsort, key=lambda k: k['price'])
    #give them the domain names
    prices = []
    for price in prices_sort:
        prices.append(f'{price["domain"]} ${str(price["price"])}0\n')

    with open('domains-price.txt', 'w') as f:
        f.write("".join(prices))
        f.close()
    print(colour(1, "Sorted by price"))