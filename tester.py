from datetime import datetime

separator = '|'
period = '.\n'
no_of_stubs = 3

def parse_data(data):
    labels = ['Phone Number:', 'Date:', 'Sentence:']
    scale = []
    extracted_data = []
    for i in range(no_of_stubs):
        scale.append( len(labels[i]) )
    #first split the text into entries
    #by splitting the text along 'period' variable
    entries = data.split(period)
    print(entries)
    #now for each entry, split along the 'separator'
    #to get the stubs
    for entry in entries:
        #handle empty string entry
        if entry == '':
            continue
        line_stubs = entry.split(separator)
        data_blobs = []
        print(line_stubs)
        if len(line_stubs) != no_of_stubs:
            raise ValueError("The given data does not adhere to the required format")
        for i in range(no_of_stubs):
            if line_stubs[i][:scale[i]] == labels[i]:
                data_blobs.append(line_stubs[i][scale[i]:])
            else:
                raise ValueError("The given data does not adhere to the required format")
        extracted_data.append(data_blobs)
        print(extracted_data)

    list_of_phone_numbers = []
    for entry in extracted_data:
        #check date is in dd-mm-yy format
        datetime.strptime(entry[1], '%d-%m-%y')
        list_of_phone_numbers.append(entry[0])
    set_of_phone_numbers = set(list_of_phone_numbers)
    print(set_of_phone_numbers)



data = "Phone Number:9764543218|Date:18-02-16|Sentence:get there asap.\n" \
       "Phone Number:9764643248|Date:18-02-16|Sentence:Hi there!.\n" \
       "Phone Number:9764543218|Date:18-03-16|Sentence:c'mon, don't.\n" \
       "Phone Number:9764543218|Date:18-02-16|Sentence:shop.\n"
parse_data(data)
