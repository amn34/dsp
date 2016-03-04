emaillist = find_emails(faclist)


def csv_writer(data, path):

    csvfile = open(path, 'wb')
    wr = csv.writer(csvfile, delimiter='\n')
    wr.writerow(data)

csv_writer(emaillist, 'emails.csv')
