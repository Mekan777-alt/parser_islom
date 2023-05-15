import datetime
import sys
from playwright.sync_api import BrowserContext, sync_playwright
from playwright.async_api import async_playwright,expect
from undetected_playwright import stealth_sync
import asyncio

async def bytedance():
   async with async_playwright() as playwright:
        driver =  playwright.firefox
        browser = await driver.launch(headless=False,slow_mo=100)
        context = await browser.new_context()
        stealth_sync(context)
        page = await browser.new_page()
        await page.goto('https://uz-appointment.visametric.com/uz')
        await page.wait_for_timeout(5000)
        await page.click("a[id=confirmationbtn]")
        await page.wait_for_timeout(5000)        
        
        #first page
        country = await page.select_option('select#country', label='National Visa')
        visitingcountry = await page.select_option("select#visitingcountry",label='Germany')
        city = await page.select_option("select#city",label='Andijan')
        office = await page.select_option("select#office",label='Tashkent')
        officetype = await  page.select_option("select#officetype",label='NORMAL')
        totalPerson = await page.select_option("select#totalPerson",label='1 arizachi')
        
        while page.get_by_label("Sana mavjud emas"):
            break
        
        #second page btnAppCountNext
        
        await page.wait_for_timeout(5000)
        await page.click("a[id=btnAppCountNext]")
        async def second_page():
            
            if "1" in totalPerson:
                name1 = await page.fill("input#name1",'Roman')
                surname1 = await page.fill("#surname1",'Mammadov')
                localname1 = await page.fill("#localname1",'Roman Mammadov')
                nationality1 = await page.select_option("select#nationality1",label='Foreign')
                birthday1 = await page.select_option("select#birthday1",label='01')
                birthmonth1 = await page.select_option("select#birthmonth1",label='01')  
                birthyear1 = await page.select_option("select#birthyear1",label='1960')
                passport1 = await page.fill("#passport1",'35324352')
                
                async def datepicker(date):
                    list_date = date.split(" ")
                    month_and_year = list_date[0] + " " + list_date[1]
                    
                    passportExpirationDate1 = page.locator("#passportExpirationDate1")
                    await passportExpirationDate1.wait_for()
                    await passportExpirationDate1.click()
                    
                    await page.wait_for_timeout(5000)
                    mmY =  page.locator(".datepicker-switch").nth(0)
                    await mmY.wait_for()
                    nextbutton =  page.locator(".next").nth(0)
                    await nextbutton.wait_for()
                    while (await mmY.text_content() != month_and_year):
                        await nextbutton.click(force=True)
                        
                    day = await page.click(f"//td[@class='day'][text()='{list_date[2]}']")  
                    
                await datepicker("June 2025 25")  
                
                email1 = await page.fill("input#email1",'romanmammadov872@gmail.com')  
                phone1 = await page.fill("input#phone1",'0709707067')  
                alternativephone1 = await page.fill("input#alternativephone1",'0709707067')  
                
        await second_page()      
        
        await page.click("a[id=btnAppPersonalNext]")
        await page.wait_for_timeout(5000)
        await page.click("a[id=btnAppPreviewNext]")
        await page.wait_for_timeout(5000)        
        await page.get_by_label("Men umumiy foydalanish shartlarini qabul qilaman va maqullayman.").check()
        await page.wait_for_timeout(5000)
        await page.click("button[type=button]")
        
        #Safar boshlanadigan sana.
        
        async def tripStart(date):
            list_date = date.split(" ")
            month_and_year = list_date[0] + " " + list_date[1]
                    
            tripStart = page.locator("input[name='travelStartDate']")
            await tripStart.wait_for()
            await tripStart.click()
                    
            await page.wait_for_timeout(5000)
            mmY =  page.locator(".datepicker-switch").nth(0)
            await mmY.wait_for()
            nextbutton =  page.locator(".next").nth(0)
            await nextbutton.wait_for()
            while (await mmY.text_content() != month_and_year):
                await nextbutton.click(force=True)
                        
            day = await page.click(f"//td[@class='day'][text()='{list_date[2]}']")  
                    
        await tripStart("November 2023 11") 
        
        async def tripEndFunc(date):
            list_date = date.split(" ")
            month_and_year = list_date[0] + " " + list_date[1]
                    
            tripEnd =  page.locator("input[name='travelEndDate']")
            await tripEnd.wait_for()
            await tripEnd.click()
                    
            await page.wait_for_timeout(5000)
            mmY = page.locator(".datepicker-switch").nth(0)
            await mmY.wait_for()
            nextbutton = page.locator(".next").nth(0)
            await nextbutton.wait_for()
            while (await mmY.text_content() != month_and_year):
               await nextbutton.click(force=True)
                        
            day = await page.click(f"//td[@class='day'][text()='{list_date[2]}']")  
                    
        await tripEndFunc("December 2023 29") 
        
        async def timeForMeeting():
            meeting = page.locator(".form-control.calendarinput")
            await meeting.wait_for()
            await meeting.click()
                    
            await page.wait_for_timeout(5000)
            mmY = page.locator(".datepicker-switch").nth(0)
            await mmY.wait_for()
            nextbutton = page.locator(".next").nth(0)
            await nextbutton.wait_for()
            index = 0
            days_list = []
            nujniy_den = None
            while nujniy_den is None:
                count = await page.locator(".day").count()
                print(nujniy_den)
                for i in range(1,count+1):
                    days = page.locator(".day").nth(i)
                    print(str(i) + "---" + str(count))
                    if await days.get_attribute("class") == "day":
                        try:
                            print("dsokdpqwodipo")
                            await days.click()
                            index += 1
                            nujniy_den = days
                            break
                        except TimeoutError:
                            pass
                    if i == count and await nextbutton.is_visible():
                        print("dsjdhsjdhska")
                        await nextbutton.click()
            if index == 0:
                await bytedance()
            print(f"the index is {str(index)}")
                    
        await timeForMeeting()
        
        await page.wait_for_timeout(300000)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bytedance())