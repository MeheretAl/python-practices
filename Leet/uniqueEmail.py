def numUniqueEmails(emails: list[str]) -> int:
    check = set()
    for email in emails:
        name, domain = email.split('@')
        localName = name.split('+')
        localName = localName[0].replace('.', '')
        check.add(localName + '@' + domain)

    return len(check)


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))
