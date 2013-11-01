import whois
import sys
import itertools

def is_available(domain):
    try:
        w = whois.query(domain)
        if w:
            return False
    except:
        return True

def permute(domains):
    permutations = list(itertools.permutations(domains))
    return [''.join(list(words)) + '.com' for words in permutations]
     
if __name__ == "__main__":
    domains = sys.argv[1:]
    permutations = permute(domains)
    for domain in permutations:
        if is_available(domain):
            print "%s is available!" % domain
