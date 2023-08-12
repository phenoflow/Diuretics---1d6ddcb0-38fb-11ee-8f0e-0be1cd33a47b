# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1211","system":"gprdproduct"},{"code":"1213","system":"gprdproduct"},{"code":"13871","system":"gprdproduct"},{"code":"1776","system":"gprdproduct"},{"code":"17960","system":"gprdproduct"},{"code":"18606","system":"gprdproduct"},{"code":"20093","system":"gprdproduct"},{"code":"20431","system":"gprdproduct"},{"code":"23505","system":"gprdproduct"},{"code":"33659","system":"gprdproduct"},{"code":"4429","system":"gprdproduct"},{"code":"46675","system":"gprdproduct"},{"code":"5112","system":"gprdproduct"},{"code":"60020","system":"gprdproduct"},{"code":"7582","system":"gprdproduct"},{"code":"8102","system":"gprdproduct"},{"code":"8369","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diuretics-modified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diuretics-modified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diuretics-modified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
