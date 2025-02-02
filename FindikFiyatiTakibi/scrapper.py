# """
# Trabzon Ticaret Borsasi Findi Fiyatlari Serbest Piyasa

# """
# import requests     #HTML içeriğini almak için
# from bs4 import BeautifulSoup   ## HTML ve XML dosyalarından veri çekmek ve işlemek için

# __EVENTTARGET = "ctl00$ContentPlaceHolder1$GrafikGetir"
# __VIEWSTATE = "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"
# __EVENTVALIDATION = "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"


# def get_data(year, month, day):
#     url = 'https://www.tb.org.tr/tr/findik-fiyatlari'
#     day = "0{}".format(day) if day < 10 else day
#     month = "0{}".format(month) if month < 10 else day
#     payload = {
#         "__EVENTTARGET": __EVENTTARGET,
#         "__VIEWSTATE": __VIEWSTATE,
#         "__EVENTVALIDATION": __EVENTVALIDATION,
#         "ctl00$ContentPlaceHolder1$DropDownGun": day,
#         "ctl00$ContentPlaceHolder1$DropDownAy": month,
#         "ctl00$ContentPlaceHolder1$DropDownYil": year,
#     }
#     response = requests.post(url, payload)  
#     content = response.content
#     soup = BeautifulSoup(content, 'html.parser')
#     result = soup.find_all("span",{"class":"middle col-md-9"})
#     # result = soup.select('.js_slide .highchart1 td')
#     return [i.get_text(strip=True) for i in result]

############################################################################
# url = 'https://www.tb.org.tr/tr/findik-fiyatlari'
# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
# # URL'den veriyi çek
# page = requests.get(url, headers=header)

# # BeautifulSoup ile sayfanın içeriğini çözümle
# soup = BeautifulSoup(page.content, "html.parser")

# # 'tbody' ve 'tr' elementlerini bulun
# table = soup.find_all('tbody')

# # 'tbody' içindeki 'tr' elementlerini dolaşın
# for tbody in table:
#     rows = tbody.find_all('tr')
#     for row in rows:
#         cells = row.find_all('td')
#         cell_texts = [cell.text.strip() for cell in cells]
#         print(cell_texts)
#############################################################################
import requests
from bs4 import BeautifulSoup

def get_max_price(year, month, day):
    url = "https://www.tb.org.tr/tr/findik-fiyatlari"  
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tabloyu bul
    table = soup.find('table', {'border': '1', 'cellpadding': '1', 'cellspacing': '1'})  # Table elementini uygun özelliklere göre bul
    rows = table.find_all('tr')
    
    max_price = None
    for row in rows[1:]:  # İlk satırı atla (başlık satırı)
        cols = row.find_all('td')
        date = cols[3].text.strip().split()[0]  # Tarihi al, zaman bilgisini at
        price_max = float(cols[1].text.strip().replace(',', '.'))  # Virgül yerine nokta kullan
        
        if date == f"{year}-{month:02d}-{day:02d}":  # Verilen tarih ile eşleşen satırları bul
            if max_price is None or price_max > max_price:
                max_price = price_max
    
    return max_price if max_price is not None else "Veri Bulunamadı"

# Örnek kullanım:
# year = 2024
# month = 3
# day = 22
# print(get_max_price(year, month, day))



