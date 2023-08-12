# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"10422","system":"gprdproduct"},{"code":"11265","system":"gprdproduct"},{"code":"12547","system":"gprdproduct"},{"code":"1288","system":"gprdproduct"},{"code":"13246","system":"gprdproduct"},{"code":"13525","system":"gprdproduct"},{"code":"14738","system":"gprdproduct"},{"code":"18650","system":"gprdproduct"},{"code":"19055","system":"gprdproduct"},{"code":"19056","system":"gprdproduct"},{"code":"19195","system":"gprdproduct"},{"code":"19258","system":"gprdproduct"},{"code":"2179","system":"gprdproduct"},{"code":"25494","system":"gprdproduct"},{"code":"2961","system":"gprdproduct"},{"code":"31013","system":"gprdproduct"},{"code":"31708","system":"gprdproduct"},{"code":"32094","system":"gprdproduct"},{"code":"32837","system":"gprdproduct"},{"code":"34034","system":"gprdproduct"},{"code":"34449","system":"gprdproduct"},{"code":"34825","system":"gprdproduct"},{"code":"3517","system":"gprdproduct"},{"code":"4068","system":"gprdproduct"},{"code":"41706","system":"gprdproduct"},{"code":"43514","system":"gprdproduct"},{"code":"46674","system":"gprdproduct"},{"code":"46990","system":"gprdproduct"},{"code":"49268","system":"gprdproduct"},{"code":"51933","system":"gprdproduct"},{"code":"5249","system":"gprdproduct"},{"code":"53253","system":"gprdproduct"},{"code":"55738","system":"gprdproduct"},{"code":"56204","system":"gprdproduct"},{"code":"56975","system":"gprdproduct"},{"code":"581","system":"gprdproduct"},{"code":"605","system":"gprdproduct"},{"code":"60603","system":"gprdproduct"},{"code":"6437","system":"gprdproduct"},{"code":"6815","system":"gprdproduct"},{"code":"708","system":"gprdproduct"},{"code":"9783","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diuretics-150mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diuretics-150mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diuretics-150mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
