from datetime import datetime

from .models import conversation

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
    #print(entries)
    #now for each entry, split along the 'separator'
    #to get the stubs
    for entry in entries:
        #handle empty string entry
        if entry == '':
            continue
        line_stubs = entry.split(separator)
        data_blobs = []
        #print(line_stubs)
        if len(line_stubs) != no_of_stubs:
            raise ValueError("The given data does not adhere to the required format")
        for i in range(no_of_stubs):
            if line_stubs[i][:scale[i]] == labels[i]:
                data_blobs.append(line_stubs[i][scale[i]:])
            else:
                raise ValueError("The given data does not adhere to the required format")
        extracted_data.append(data_blobs)
        #print(extracted_data)

    #extracted_data is a list of lists
    return extracted_data

def commit_extracted_data(extracted_data):
    for entry in extracted_data:
        # check date is in dd-mm-yy format
        valid_datetime = datetime.strptime(entry[1], '%d-%m-%y')
        c = conversation(phone_number=entry[0], date=valid_datetime, content=entry[2])
        c.save()

def get_formatted_conversations():
    list = []
    conversations = conversation.objects.all().order_by('phone_number', 'date')
    prev_no = conversations[0].phone_number
    prev_date = conversations[0].date
    dict = {}
    dict['phone_number'] = prev_no
    dict['conversations'] = []
    d={}
    d['content'] = ''
    for c in conversations:
        if c.phone_number == prev_no:
            if c.date != prev_date:
                dict['conversations'].append(d)
                d={}
                d['content'] = ''

        else:
            dict['conversations'].append(d)
            list.append(dict)
            dict = {}
            dict['phone_number'] = c.phone_number
            dict['conversations'] = []
            d = {}
            d['content'] = ''

        d['date'] = c.date.strftime('%m-%d-%y')
        d['content'] += c.content + '\n'

        prev_no = c.phone_number
        prev_date = c.date
    dict['conversations'].append(d)
    list.append(dict)

    return list