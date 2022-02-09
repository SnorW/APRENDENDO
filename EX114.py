import urllib.request

try:
    rqst = urllib.request.urlopen('https://www.facebook.com/?sk=h_chr').getcode()
except:
    print('Esse site não está disponível')
else:
    print('Esse site está acessível')
