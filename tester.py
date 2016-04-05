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
        print(line_stubs)
        if len(line_stubs) != no_of_stubs:
            raise ValueError("The given data does not adhere to the required format")
        for i in range(no_of_stubs):
            if line_stubs[i][:scale[i]] == labels[i]:
                extracted_data.append(line_stubs[i][scale[i]:])
            else:
                raise ValueError("The given data does not adhere to the required format")
        print(extracted_data)

data = "Phone Number:9764543218|Date:18-02-16|Sentence:get there asap.\n" \
       "Phone Number:9764643248|Date:18-02-16|Sentence:Hi there!.\n" \
       "Phone Number:9764543218|Date:18-03-16|Sentence:c'mon, don't.\n" \
       "Phone Number:9764543218|Date:18-02-16|Sentence:shop.\n"
parse_data(data)
