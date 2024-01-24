from selenium import webdriver
import time
import smtplib
import os

email_sender = os.environ.get("user1")
email_pass = os.environ.get("pass1")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(
    "https://www.booking.com/hotel/es/boccaccio.es.html?aid=356980;label=gog235jc-1DCAsoRkIJYm9jY2FjY2lvSApYA2hGiAEBmAEKuAEXyAEM2AED6AEB-AECiAIBqAIDuALE5LKFBsACAdICJDBiN2EyYTY0LWRjZjUtNDY4Yi1iZmQ1LTJhODBiNWM2ZGI3MdgCBOACAQ;sid=084cb010d3792eb4e6af47b7129caf6f;all_sr_blocks=1641710_295612148_0_0_0;checkin=2021-09-06;checkout=2021-09-11;dest_id=-381100;dest_type=city;dist=0;from_beach_key_ufi_sr=1;group_adults=2;group_children=0;hapos=1;highlighted_blocks=1641710_295612148_0_0_0;hp_group_set=0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=1641710_295612148_0_0_0__63800;srepoch=1621930633;srpvid=1d2e3a448e250071;type=total;ucfs=1;sig=v1_gf5mEXk#hotelTmpl")

driver.delete_all_cookies()
counter = 0
i = 0
while i == 0:
    driver.refresh()
    price1 = driver.find_element_by_xpath(
        "//*[@id=\"hotelTmpl\"]")

    if "723" not in price1.text:

        cookie = driver.find_element_by_xpath("//*[@id=\"hprt-table\"]/tbody/tr[5]/td[2]")
        cookie.location_once_scrolled_into_view

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_sender, email_pass)

            subject = "Cambios en el precio de tu estancia en el hotel Alua Boccaccio:"
            body = "https://www.booking.com/hotel/es/boccaccio.es.html?aid=356980;label=gog235jc-1DCAsoRkIJYm9jY2FjY2lvSApYA2hGiAEBmAEKuAEXyAEM2AED6AEB-AECiAIBqAIDuALE5LKFBsACAdICJDBiN2EyYTY0LWRjZjUtNDY4Yi1iZmQ1LTJhODBiNWM2ZGI3MdgCBOACAQ;sid=084cb010d3792eb4e6af47b7129caf6f;all_sr_blocks=1641710_295612148_0_0_0;checkin=2021-09-06;checkout=2021-09-11;dest_id=-381100;dest_type=city;dist=0;from_beach_key_ufi_sr=1;group_adults=2;group_children=0;hapos=1;highlighted_blocks=1641710_295612148_0_0_0;hp_group_set=0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=1641710_295612148_0_0_0__63800;srepoch=1621930633;srpvid=1d2e3a448e250071;type=total;ucfs=1;sig=v1_gf5mEXk#hotelTmpl"


            msg = f"Subject: {subject}\n\n{body}"

            smtp.sendmail(email_sender, email_sender, msg)

        time.sleep(8)

        driver.find_element_by_xpath("//*[@id=\"hotelTmpl\"]").screenshot("price1.jpg")
        print("El precio del hotel ha cambiado")

        print("El email ha sido enviado correctamente a", email_sender)
        driver.quit()
        i = i + 1
    else:
        print("MISMO PRECIO, 723 EUROS")
        counter = counter + 1
        print("numero de veces ejecutado el programa:", counter)
        time.sleep(360)
