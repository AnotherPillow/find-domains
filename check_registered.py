import whois, colorama, time, json
from datetime import datetime

def colour(id, text):
    # id = 0: red
    # id = 1: green
    # id = 2: default
    # id = 3: yellow

    out = ""

    if id == 0:
        out = colorama.Fore.RED
    elif id == 1:
        out = colorama.Fore.GREEN
    elif id == 2:
        out = colorama.Fore.RESET
    elif id == 3:
        out = colorama.Fore.YELLOW
    elif id == 4:
        out = colorama.Fore.CYAN

    return out + text + colorama.Fore.RESET

def check_registered(debug_mode=False):
    domainss = input(colour(4, 'Enter a domain name (split multiple by ","): '))

    with open("output-available-taken.txt", "w"): pass

    debug_json = {
        "domains": []
    }
    

    domains = domainss.split(",")
    domains = [x.strip() for x in domains]

    #print(domains)

    for domain in domains:
        TLDs = [x.split(" ")[0] for x in open("domains-price.txt", "r").readlines()]
        prices = [x.split(" ")[1] for x in open("domains-price.txt", "r").readlines()]
        sources = [x.split(" ")[2] for x in open("domains-price.txt", "r").readlines()]

        output = ""

        print(colour(4, f"Checking {domain}..."))



        for i, tld in enumerate(TLDs):
            #check if registered
            trimmedprice = prices[i].replace("\n", "")
            out = ""
            source = sources[i].strip()
            try:
                data = whois.whois(domain + tld)
                # print(colour(0, f"Whois for {domain}{tld}"))
                # print(data)
                dn = data.domain_name[0] if type(data.domain_name) is list else data.domain_name
                
                if dn is not None and dn.lower() == f"{domain}{'.' if not tld.startswith('.') else ''}{tld}".lower():
                    print(colour(0, f"{domain}{tld} is registered"))
                    out = f"{domain}{tld} registered\n"
                else:
                    print(colour(1, f"{domain}{tld} is available for {trimmedprice} from {source}"))
                    out = f"{domain}{tld} available {trimmedprice} from {source}\n"
            except Exception as e:
                print(colour(3, f"Unable to check {domain}{tld}, may be available for {trimmedprice} from {source}"))
                print(colour(0, f"Error: {str(e)[:100]}..."))
                out = f"{domain}{tld} error {trimmedprice} from {source}\n"
            
            debug_json["domains"].append({
                "domain": domain + tld,
                "status": out,
                "price": trimmedprice,
                "source": source,
                "data": data,
            })

            output += out
            time.sleep(0.1)

        #append output to "output-available-taken.txt"
        with open("output-available-taken.txt", "a") as f:
            f.write(output)
            f.close()

        if debug_mode:
            print(debug_json)
            with open("debug.json", "w") as f:
                f.write(json.dumps(debug_json, indent=4, default=str))
                f.close()