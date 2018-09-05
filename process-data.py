import csv


def format_label(label):
    label = label.replace('-', ' ')
    label = label.strip()

    return label


with open('data/chatdata.csv', 'r', newline='', encoding='mac_roman') as data_file:
    data = csv.reader(data_file, delimiter=',')

    for row in data:
        if len(row[0]) > 5:
            reply = row[1]
            if 'contact-us' in reply:
                label = 'General enquiry'
            elif '#find-a-research-guide' in reply:
                label = 'General research guide enquiry'
            elif 'research-guides' in reply:
                bits = reply.split('/')
                for i,bit in enumerate(bits):
                    if bit == 'research-guides':
                        label = bits[i+1]
            elif 'discovery-help' in reply:
                bits = reply.split('/')
                for i, bit in enumerate(bits):
                    if bit == 'discovery-help':
                        label = bits[i + 1] + ' ' + bits[i + 2]
            else:
                label = 'General research help enquiry'

            label = label.capitalize()
            label = format_label(label)
            with open('data/newdata.csv', 'a') as new_csv:
                writer = csv.writer(new_csv)
                row_data = [format_label(row[0]), row[1].strip(), format_label(row[2]), label]
                writer.writerow(row_data)
            new_csv.close()

data_file.close()
