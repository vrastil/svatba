
import urllib.parse
import openpyxl
from IPython.display import Markdown, display
import collections

def get_raw_data(sheet):
    return [row[2].value for row in sheet[2:sheet.max_row-1] if row[0].value]

def parse_raw_data(data):
    parsed_data = []
    for rec in data:
        rec = rec.split('\n')
        encodedStr = rec[0]
        parsed_rec = urllib.parse.parse_qs(encodedStr)
        parsed_data.append({
            "name": parsed_rec["name"][0],
            "email": parsed_rec["email"][0],
            "message": parsed_rec.get("message", [""])[0],
            "food" : rec[1] if len(rec) > 1 else "",
            "drink" : rec[2] if len(rec) > 2 else "",
        })
    return parsed_data

def fix_data(data):
    for rec in data:
        if rec["name"] == "Vašek Pavlík":
            rec["food"] = "Krůtí steak šťouchané brambory, listový špenát"
            rec["drink"] = "Hrňte to do mě všechno, je mi to fuk."
        elif rec["name"] == "Šimon Klein":
            rec["food"] = "Svíčková na smetaně, karlovarský knedlík"
            rec["drink"] = "Hrňte to do mě všechno, je mi to fuk."
        elif rec["name"] == "Martin Korbel ":
            rec["name"] = "Martin Korbel"
            rec["food"] = "je mi to fuk"
            rec["drink"] = "Hrňte to do mě všechno, je mi to fuk."

        if rec["food"] == "":
            rec["food"] = "je mi to fuk"
        if rec["drink"] == "":
            rec["drink"] = "Hrňte to do mě všechno, je mi to fuk."
            

def load_xlsx(xlsx_file, sheet_name="raw"):
    """ open xlsx file 'xlsx_file' and load data from sheets 'sheet_name'"""
    # load all data
    wb = openpyxl.load_workbook(xlsx_file)
    sheet = wb[sheet_name]
    data = get_raw_data(sheet)

    # parse and fix data
    data = parse_raw_data(data)
    fix_data(data)
    print("Nacteno %i zaznamu." % len(data))

    return data

def print_msg(data):
    for rec in data:
        display(Markdown('---'))
        print(f"{rec['name']}: {rec['message']}")

def print_get(data, key="drink"):
    sub_data = [x[key] for x in data]
    num = len(sub_data)
    counter = collections.Counter(sub_data)
    for most, count in counter.most_common():
        per = (100.0 * count) / num
        print(f"{count} ({per:.0f}%): {most}")

def print_refreshment(data):
    display(Markdown('---'))
    print("Piti:\n")
    print_get(data, key="drink")
    display(Markdown('---'))
    print("Jidlo:\n")
    print_get(data, key="food")

def print_get_drink_distr(data):
    # get raw
    all_drink = len(data)
    nealko = len([x for x in data if "Alkohol nepiju" in x["drink"]])
    alko = all_drink - nealko
    either = len([x for x in data if "Hrňte to do mě všechno, je mi to fuk." == x["drink"]])
    alko_reduced = alko - either
    white = len([x for x in data if "Víno bílé, nic jiného do mě nedostanete." == x["drink"]])
    red = len([x for x in data if "Víno červené, nic jiného do mě nedostanete." == x["drink"]])
    beer = len([x for x in data if "Pouze pivo, nic jiného do mě nedostanete." == x["drink"]])
    beerish = len([x for x in data if "Asi pivo, ale když bude víno tak ochutnám." == x["drink"]])
    whinish = len([x for x in data if "Asi víno, pivo jen k masu." == x["drink"]])

    # check
    if alko_reduced != (white + red + beer + beerish + whinish):
        print(f"ERROR (check 1/3): alko_reduced != (white + red + beer + beerish + whinish)\n\t{alko_reduced} != {(white + red + beer + beerish + whinish)}")

    # proccess
    whine = red + white
    rw = red / whine
    ww = white / whine
    red += rw * whinish * 0.7
    white += ww * whinish * 0.7
    beer += whinish*0.3

    # check
    if alko_reduced != (white + red + beer + beerish ):
        print(f"ERROR (check 2/3): alko_reduced != (white + red + beer + beerish)\n\t{alko_reduced} != {(white + red + beer + beerish )}")

    beer += beerish * 0.7
    red += rw * beerish * 0.3
    white += ww * beerish * 0.3
    
    # check
    if alko_reduced != (white + red + beer ):
        print(f"ERROR (check 3/3): alko_reduced != (white + red + beer)\n\t{alko_reduced} != {(white + red + beer )}")
    
    # abs
    all_p_us = 55
    all_p_us_al = all_p_us*alko/all_drink

    # print
    display(Markdown('---'))
    print("Rozpis piti:\n")
    print(f"Nealko: {100*nealko/all_drink:.0f}% z celkem {all_p_us:.0f} je {nealko/all_drink*all_p_us:.0f}")
    print(f"Alko: {100*alko/all_drink:.0f}% z celkem {all_p_us:.0f} je {alko/all_drink*all_p_us:.0f}")
    print(f"Cokoli: {100*either/alko:.0f}% z celkem {all_p_us_al:.0f} je {either/alko*all_p_us_al:.0f}")
    print(f"Bile: {100*white/alko_reduced:.0f}% z celkem {all_p_us_al:.0f} je {white/alko_reduced*all_p_us_al:.0f}")
    print(f"Cervene: {100*red/alko_reduced:.0f}% z celkem {all_p_us_al:.0f} je {red/alko_reduced*all_p_us_al:.0f}")
    print(f"Pivo: {100*beer/alko_reduced:.0f}% z celkem {all_p_us_al:.0f} je {beer/alko_reduced*all_p_us_al:.0f}")

def main():
    xlsx_file = "/mnt/c/Users/micha/Dropbox/Svatba/Hoste/odpovedi.xlsx"
    data = load_xlsx(xlsx_file)

    # get info
    print_msg(data)
    print_refreshment(data)
    print_get_drink_distr(data)

    return data