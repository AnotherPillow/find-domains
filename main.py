import requests, os, colorama
from check_registered import check_registered, colour

colorama.just_fix_windows_console()

def aws():
    if not os.path.exists("Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf"):
        print(colour(1, "Downloading AWS PDF..."))
        r = requests.get("https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf")
        with open("Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf", "wb") as f:
            f.write(r.content)
            f.close()
        print(colour(1, "Downloaded AWS PDF"))

    print(colour(1, "Downloading AWS TLDs..."))



    toparse = input(colour(4, "Parse AWS PDF file (may take a while and is not necessary if this is not your first run)? (y/n) ")).startswith("y")

    if toparse:
        print(colour(1, "Parsing PDF file..."))
        import parse_pdf
        parse_pdf.main()
        print(colour(1, "Parsed PDF file"))
    else:
        print(colour(1, "Skipping PDF parsing"))

def namecheap():
    pass

def ovh():
    pass


mode = input(colour(4, "What sites do you want to check? (n)amecheap, a(w)s, (o)vh, (a)ll: "))
modes = []
if mode == "a":
    modes = ["n", "w", "a", "o"]
else:
    modes.append(mode)

if "w" in modes:
    aws()
if "n" in modes:
    namecheap()
if "o" in modes:
    ovh()

if "a" in modes:
    #merge aws-domains-price.txt and namecheap-domains-price.txt into domains-price.txt and sort it
    print(colour(1, "Merging and sorting..."))
    aws_domains = open("aws-domains-price.txt", "r").readlines()
    nc_domains = open("namecheap-domains-price.txt", "r").readlines()
    ovh_domains = open("ovh-domains.txt", "r", encoding="utf-8").readlines()
    domains = aws_domains + nc_domains + ovh_domains
    domains.sort(key=lambda x: float(x.split(" ")[1].replace("$","")))
    with open("domains-price.txt", "w") as f:
        for line in domains:
            f.write(line)
        f.close()
    print(colour(1, "Merged and sorted"))

elif "w" in modes:
    print(colour(1, "Copying aws-domains-price.txt to domains-price.txt..."))
    with open("aws-domains-price.txt", "r") as f:
        with open("domains-price.txt", "w") as f2:
            for line in f.readlines():
                if "." in line.strip():
                    f2.write(line.strip() + " aws\n")
        f2.close()
    f.close()
    print(colour(1, "Copied aws-domains-price.txt to domains-price.txt"))

elif "n" in modes:
    print(colour(1, "Copying namecheap-domains-price.txt to domains-price.txt..."))
    with open("namecheap-domains-price.txt", "r") as f:
        with open("domains-price.txt", "w") as f2:
            for line in f.readlines():
                f2.write(line + " namecheap\n")
        f2.close()
    f.close()
    print(colour(1, "Copied namecheap-domains-price.txt to domains-price.txt"))
elif "o" in modes:
    print(colour(1, "Copying ovh-domains.txt to domains-price.txt..."))
    with open("ovh-domains.txt", "r") as f:
        with open("domains-price.txt", "w") as f2:
            for line in f.readlines():
                f2.write(line.strip() + "\n")
        f2.close()
    f.close()
    print(colour(1, "Copied ovh-domains.txt to domains-price.txt"))
else:
    print(colour(0, "No sites selected!"))
    exit()

check_registered()

import sort_takenavailable
sort_takenavailable.main()

print(colour(1, "Done!"))
print(colour(1, "Find your output in output-available-sorted.txt"))