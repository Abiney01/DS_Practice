def unique_email(emails):
    unique = set()
    for e in emails:
        local,domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".","")
        unique.add((local,domain))
    return len(unique)

emails = ["test.email+alex@neetcode.com","test.e.mail+bob.cathy@neetcode.com","testemail+david@nee.tcode.com"]
print(unique_email(emails))