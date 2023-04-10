import colorama
from check_registered import check_registered, colour

colorama.just_fix_windows_console()

toparse = input(colour(4, "Parse PDF file (may take a while and is not necessary if this is not your first run)? (y/n) ")).startswith("y")

if toparse:
    print(colour(1, "Parsing PDF file..."))
    import parse_pdf
    parse_pdf.main()
    print(colour(1, "Parsed PDF file"))
else:
    print(colour(1, "Skipping PDF parsing"))


check_registered()

import sort_takenavailable
sort_takenavailable.main()