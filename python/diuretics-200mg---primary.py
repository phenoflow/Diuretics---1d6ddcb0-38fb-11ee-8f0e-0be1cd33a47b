# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1021","system":"gprdproduct"},{"code":"14126","system":"gprdproduct"},{"code":"18200","system":"gprdproduct"},{"code":"19194","system":"gprdproduct"},{"code":"21231","system":"gprdproduct"},{"code":"27926","system":"gprdproduct"},{"code":"29780","system":"gprdproduct"},{"code":"30625","system":"gprdproduct"},{"code":"31548","system":"gprdproduct"},{"code":"32918","system":"gprdproduct"},{"code":"33353","system":"gprdproduct"},{"code":"35162","system":"gprdproduct"},{"code":"35380","system":"gprdproduct"},{"code":"4044","system":"gprdproduct"},{"code":"41292","system":"gprdproduct"},{"code":"4258","system":"gprdproduct"},{"code":"4661","system":"gprdproduct"},{"code":"4705","system":"gprdproduct"},{"code":"47815","system":"gprdproduct"},{"code":"5189","system":"gprdproduct"},{"code":"52887","system":"gprdproduct"},{"code":"53967","system":"gprdproduct"},{"code":"54201","system":"gprdproduct"},{"code":"54825","system":"gprdproduct"},{"code":"55","system":"gprdproduct"},{"code":"55399","system":"gprdproduct"},{"code":"56051","system":"gprdproduct"},{"code":"56244","system":"gprdproduct"},{"code":"57104","system":"gprdproduct"},{"code":"57600","system":"gprdproduct"},{"code":"57610","system":"gprdproduct"},{"code":"58757","system":"gprdproduct"},{"code":"59030","system":"gprdproduct"},{"code":"59290","system":"gprdproduct"},{"code":"59884","system":"gprdproduct"},{"code":"59939","system":"gprdproduct"},{"code":"61025","system":"gprdproduct"},{"code":"6118","system":"gprdproduct"},{"code":"61475","system":"gprdproduct"},{"code":"6468","system":"gprdproduct"},{"code":"7441","system":"gprdproduct"},{"code":"7618","system":"gprdproduct"},{"code":"7799","system":"gprdproduct"},{"code":"8189","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diuretics-200mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diuretics-200mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diuretics-200mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
