import whois, colorama, time

def colour(id, text):
    # id = 0: red
    # id = 1: green
    # id = 2: default
    # id = 3: yellow

    str = ""

    if id == 0:
        str = colorama.Fore.RED
    elif id == 1:
        str = colorama.Fore.GREEN
    elif id == 2:
        str = colorama.Fore.RESET
    elif id == 3:
        str = colorama.Fore.YELLOW
    elif id == 4:
        str = colorama.Fore.CYAN

    return str + text + colorama.Fore.RESET

def check_registered():
    domainss = input(colour(4, 'Enter a domain name (split multiple by ","): '))

    with open("output-available-taken.txt", "w"): pass


    

    domains = domainss.split(",")
    domains = [x.strip() for x in domains]

    #print(domains)

    for domain in domains:
        TLDs = [x.split(" ")[0] for x in open("domains-price.txt", "r").readlines()]
        prices = [x.split(" ")[1] for x in open("domains-price.txt", "r").readlines()]

        output = ""

        print(colour(4, f"Checking {domain}..."))



        for i, tld in enumerate(TLDs):
            #check if registered
            trimmedprice = prices[i].replace("\n", "")
            out = ""
            try:
                data = whois.whois(domain + tld)
                if data.domain_name:
                    print(colour(0, f"{domain}{tld} is registered"))
                    out = f"{domain}{tld} registered\n"
                else:
                    print(colour(1, f"{domain}{tld} is available for {trimmedprice}"))
                    out = f"{domain}{tld} available {trimmedprice}\n"
            except Exception as e:
                print(colour(3, f"Unable to check {domain}{tld}, may be available for {trimmedprice}"))
                print(colour(0, f"Error: {str(e)[:100]}..."))
                out = f"{domain}{tld} error {trimmedprice}\n"
            output += out
            time.sleep(0.1)

        #append output to "output-available-taken.txt"
        with open("output-available-taken.txt", "a") as f:
            f.write(output)
            f.close()