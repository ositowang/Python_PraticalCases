from xml.etree.ElementTree import Element,tostring, ElementTree
import csv
import xlrd
import xlwt
e = Element("data")
e.set("name", "osito")
print(tostring(e))
e2 = Element("row")
e3 = Element("line")
e2.append(e3)
e.append(e2)
print(tostring(e))

et = ElementTree(e)

def toXml(fname):
    with open(fname,"rb") as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('data')
        for row in reader:
            erow = Element('Row')
            root.append(erow)
            for tag, text in zip(headers,row):
                e = Element(tag)
                e.text = text
                erow.append(e)
    return ElementTree(root)


# Read in spreadsheet

rbook = xlrd.open_workbook("demo.xlsx")
rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, "Total", None)

for row in range(1,rsheet.nrows):
    total = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc , xlrd.XL_CELL_NUMBER, total, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf("align: vertical center. horizontal center")
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save("output.xlsx")

