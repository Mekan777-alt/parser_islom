import datetime
import sys
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
        
        #first page
        country = page.select_option('select#country', label='National Visa')
        visitingcountry = page.select_option("select#visitingcountry",label='Germany')
        city = page.select_option("select#city",label='Andijan')
        office = page.select_option("select#office",label='Tashkent')
        officetype = page.select_option("select#officetype",label='NORMAL')
        totalPerson = page.select_option("select#totalPerson",label='1 arizachi')
        
        while page.get_by_label("Sana mavjud emas"):
            break
        
        #second page btnAppCountNext
        
        page.wait_for_timeout(5000)
        page.click("a[id=btnAppCountNext]")
        def second_page():
            
            if "1" in totalPerson:
                name1 = page.fill("input#name1",'Roman')
                surname1 = page.fill("#surname1",'Mammadov')
                localname1 = page.fill("#localname1",'Roman Mammadov')
                nationality1 = page.select_option("select#nationality1",label='Foreign')
                birthday1 = page.select_option("select#birthday1",label='01')
                birthmonth1 = page.select_option("select#birthmonth1",label='01')  
                birthyear1 = page.select_option("select#birthyear1",label='1960')
                passport1 = page.fill("#passport1",'35324352')
                
                def datepicker(date):
                    list_date = date.split(" ")
                    month_and_year = list_date[0] + " " + list_date[1]
                    
                    passportExpirationDate1 = page.locator("#passportExpirationDate1")
                    passportExpirationDate1.wait_for()
                    passportExpirationDate1.click()
                    
                    page.wait_for_timeout(5000)
                    mmY = page.locator(".datepicker-switch").nth(0)
                    mmY.wait_for()
                    nextbutton = page.locator(".next").nth(0)
                    nextbutton.wait_for()
                    while (mmY.text_content() != month_and_year):
                        nextbutton.click(force=True)
                        
                    day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")  
                    
                datepicker("June 2025 25")  
                
                email1 = page.fill("input#email1",'romanmammadov872@gmail.com')  
                phone1 = page.fill("input#phone1",'0709707067')  
                alternativephone1 = page.fill("input#alternativephone1",'0709707067')  
                
        second_page()      
        
        page.click("a[id=btnAppPersonalNext]")
        page.wait_for_timeout(5000)
        page.click("a[id=btnAppPreviewNext]")
        
        page.get_by_label("Men umumiy foydalanish shartlarini qabul qilaman va maqullayman.").check()
        page.wait_for_timeout(5000)
        page.click("button[type=button]")
        
        #Safar boshlanadigan sana.
        
        def tripStart(date):
            list_date = date.split(" ")
            month_and_year = list_date[0] + " " + list_date[1]
                    
            tripStart = page.locator("input[name='travelStartDate']")
            tripStart.wait_for()
            tripStart.click()
                    
            page.wait_for_timeout(5000)
            mmY = page.locator(".datepicker-switch").nth(0)
            mmY.wait_for()
            nextbutton = page.locator(".next").nth(0)
            nextbutton.wait_for()
            while (mmY.text_content() != month_and_year):
                nextbutton.click(force=True)
                        
            day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")  
                    
        tripStart("June 2023 25") 
        
        def tripEndFunc(date):
            list_date = date.split(" ")
            month_and_year = list_date[0] + " " + list_date[1]
                    
            tripEnd = page.locator("input[name='travelEndDate']")
            tripEnd.wait_for()
            tripEnd.click()
                    
            page.wait_for_timeout(5000)
            mmY = page.locator(".datepicker-switch").nth(0)
            mmY.wait_for()
            nextbutton = page.locator(".next").nth(0)
            nextbutton.wait_for()
            while (mmY.text_content() != month_and_year):
                nextbutton.click(force=True)
                        
            day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")  
                    
        tripEndFunc("June 2023 29") 
        
        def timeForMeeting(date):
            list_date = date.split(" ")
            month_and_year = list_date[0] + " " + list_date[1]
                            
            meeting = page.locator(".form-control.calendarinput")
            meeting.wait_for()
            meeting.click()
                    
            page.wait_for_timeout(5000)
            mmY = page.locator(".datepicker-switch").nth(0)
            mmY.wait_for()
            nextbutton = page.locator(".next").nth(0)
            nextbutton.wait_for()
            day = page.locator("//td[@class='day'][text()='{list_date[2]}']") 
            while True:
                if not day.is_visible():
                    bytedance()

            if day.is_visible():
                day.click()
                    
        timeForMeeting("June 2023 27") 
        
        page.wait_for_timeout(300000)


if __name__ == "__main__":
    bytedance()