# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"12360","system":"gprdproduct"},{"code":"12926","system":"gprdproduct"},{"code":"14761","system":"gprdproduct"},{"code":"17149","system":"gprdproduct"},{"code":"19352","system":"gprdproduct"},{"code":"20538","system":"gprdproduct"},{"code":"24008","system":"gprdproduct"},{"code":"24832","system":"gprdproduct"},{"code":"24893","system":"gprdproduct"},{"code":"25500","system":"gprdproduct"},{"code":"26220","system":"gprdproduct"},{"code":"26292","system":"gprdproduct"},{"code":"30913","system":"gprdproduct"},{"code":"39447","system":"gprdproduct"},{"code":"41861","system":"gprdproduct"},{"code":"41885","system":"gprdproduct"},{"code":"43184","system":"gprdproduct"},{"code":"4406","system":"gprdproduct"},{"code":"44168","system":"gprdproduct"},{"code":"4605","system":"gprdproduct"},{"code":"59616","system":"gprdproduct"},{"code":"62066","system":"gprdproduct"},{"code":"7734","system":"gprdproduct"},{"code":"8058","system":"gprdproduct"},{"code":"8147","system":"gprdproduct"},{"code":"8303","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diuretics-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diuretics-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diuretics-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
