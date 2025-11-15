import dns.name
import dns.message
import dns.query
import dns.rdatatype
import dns.resolver
import csv

#helpter function for each resolver to get TTL and IPs
def resolver(resolver, website):
    try:
        answers = resolver.resolve(website, 'A')
    except Exception as e:
        return "", -1
    else:
        ips = ", ".join(rdata.address for rdata in answers.rrset)
        ttl = answers.ttl
        return ips, ttl


main_header = ['Website', 'Carleton IP addresses', 'Carleton TTL', 'Google IP addresses', 'Google TTL']
websites = []

#Open CSV file to write results
with open('answers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(main_header)

    with open('top500.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(f"Header: {header}")
        for row in reader:
            websites.append(row[0])

    # This constructs a domain name object
    carleton_resolver = dns.resolver.make_resolver_at('137.22.1.7')
    google_resolver = dns.resolver.make_resolver_at('8.8.8.8')
    
    #Querying each website
    for w in websites:

        #Getting IPS and TTLs from both resolvers
        carleton_ips, carleton_ttl = resolver(carleton_resolver, w)
        google_ips, google_ttl = resolver(google_resolver, w)   

        #Appending results to CSV
        row = [w, carleton_ips, carleton_ttl, google_ips, google_ttl]
        print(row)
        writer.writerow(row)