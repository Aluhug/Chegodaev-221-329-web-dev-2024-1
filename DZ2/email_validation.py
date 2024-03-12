import re

def fun(s):
    if s.count('@') != 1: return False
    user_name, domain = s.split('@')
    if domain.count('.') != 1: return False
    site_name, extension = domain.split('.')
    user_name_pattern = r'^[a-zA-Z0-9_-]+$'
    if not re.match(user_name_pattern, user_name): return False
    site_name_pattern = r'^[a-zA-Z0-9]+$'
    if not re.match(site_name_pattern, site_name): return False
    extension_pattern = r'^[a-zA-Z]+$'
    if not re.match(extension_pattern, extension): return False
    if len(extension) > 3: return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(0, n):
        emails.append(input())
        
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
