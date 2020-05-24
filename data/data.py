
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

def main():
    xlsx_file = "/mnt/c/Users/micha/Dropbox/Svatba/Hoste/odpovedi.xlsx"
    data = load_xlsx(xlsx_file)

    # get info
    print_msg(data)
    print_refreshment(data)

    return data