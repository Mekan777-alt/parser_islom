from playwright.sync_api import BrowserContext, sync_playwright

from undetected_playwright import stealth_sync




def bytedance():
   with sync_playwright() as playwright:
        driver = playwright.firefox
        browser = driver.launch(headless=False,slow_mo=100)
        context = browser.new_context()
        stealth_sync(context)
        page = browser.new_page()
        page.goto('https://uz-appointment.visametric.com/uz')
        page.wait_for_timeout(5000)
        page.click("a[id=confirmationbtn]")
        page.wait_for_timeout(5000)
        page.locator(".country").select_option("National Visa")
        page.wait_for_timeout(5000)
        
        #first page
        country = page.locator(".country")
        country.wait_for()
        country.select_option("National Visa")
        
        visitingcountry = page.locator(".visitingcountry")
        visitingcountry.wait_for()
        visitingcountry.select_option("Germany")

        city = page.locator("#city")
        city.wait_for()
        city.select_option("Andijan")

        office = page.locator("#office")
        office.wait_for()
        office.select_option("Tashkent")
        
        
        officetype = page.locator(".officetype")
        officetype.wait_for()
        officetype.select_option("NORMAL")
        
        totalPerson = page.locator(".totalPerson")
        totalPerson.wait_for()
        totalPerson.select_option("1 arizachi")
        
        #second page btnAppCountNext
        page.wait_for_timeout(5000)
        page.click("a[id=btnAppCountNext]")
        
        name1 = page.locator("#name1")
        name1.wait_for()
        name1.fill('Roman')
        
        surname1 = page.locator("#surname1")
        surname1.wait_for()
        surname1.fill('Mammadov')
        
        localname1 = page.locator("#localname1")
        localname1.wait_for()
        localname1.fill('Roman Mammadov')
        
        nationality1 = page.locator("#nationality1")
        nationality1.wait_for()
        nationality1.select_option("Uzbekistan")
        
        birthday1 = page.locator("#birthday1")
        birthday1.wait_for()
        birthday1.select_option("01")
        
        birthmonth1 = page.locator("#birthmonth1")
        birthmonth1.wait_for()
        birthmonth1.select_option("01")
        
        birthyear1 = page.locator("#birthyear1")
        birthyear1.wait_for()
        birthyear1.select_option("1950")
        
        passport1 = page.locator("#passport1")
        passport1.wait_for()
        passport1.fill('35324352')
        
        date = "June 2025"
        
        def datepicker(date):
            list_date = date.split("-")
            
            passportExpirationDate1 = page.locator("#passportExpirationDate1")
            passportExpirationDate1.wait_for()
            passportExpirationDate1.click()
            
            mmY = page.locator("(//table[@class='table-condensed']//th[@class='datepicker-switch'])[1]")
            mmY.wait_for()
            nextbutton = page.locator("(//table[@class='table-condensed']//th[@class='next'])[1]")
            nextbutton.wait_for()
            while (mmY.text_content() != date):
                nextbutton.click(force=True)
                
        datepicker("June 2023")    
            
        page.wait_for_timeout(30000)


if __name__ == "__main__":
    bytedance()