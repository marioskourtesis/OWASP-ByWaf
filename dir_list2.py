import re
import urllib

__author__ = '@asim_jaweesh'

app = None

options = {}


class UserAgent(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/99.0'

useragent = UserAgent()

def main_function(url, check):
    if 'localhost' in url:
        host = 'localhost'
    else:
        host = url.split('//')[1]

    opener = urllib.urlopen(url)
    vuln = 0
    if str(5) in str(opener.code):
        app.print_line("Server Error!")

    request = useragent.open(url)
    html = request.readlines()
    for line in html:
        checker = re.findall(check, line)
        if len(checker) != 0:
            vuln = vuln + 1
            app.print_line("[*] Bingo! : %s " % url)
            #app.db.dir_list.add(session=app.db.get_session(), path=str(url) , hid=host)


    if vuln == 0:
        app.print_line("[!] Target is not vulnerable!")



def do_list(url):
    check = re.compile('Index of /', re.I)
    main_function(url, check)
