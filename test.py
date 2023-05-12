from playwright.sync_api import sync_playwright
import datetime
import sys

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto('https://uz-appointment.visametric.com/uz')
    page.wait_for_timeout(5000)
    page.click("a[id=confirmationbtn]")
    page.wait_for_timeout(5000)

    # first page
    country = page.select_option('select#country', label='National Visa')
    visitingcountry = page.select_option("select#visitingcountry", label='Germany')
    city = page.select_option("select#city", label='Andijan')
    office = page.select_option("select#office", label='Tashkent')
    officetype = page.select_option("select#officetype", label='NORMAL')
    totalPerson = page.select_option("select#totalPerson", label='1 arizachi')

    while page.get_by_label("Sana mavjud emas"):
        break

    # second page btnAppCountNext

    page.wait_for_timeout(5000)
    page.click("a[id=btnAppCountNext]")


    def second_page():
        if "1" in totalPerson:
            name1 = page.fill("input#name1", 'Roman')

            surname1 = page.locator("#surname1")
            surname1.wait_for()
            surname1.fill('Mammadov')

            localname1 = page.locator("#localname1")
            localname1.wait_for()
            localname1.fill('Roman Mammadov')

            nationality1 = page.select_option("select#nationality1", label='Foreign')
            birthday1 = page.select_option("select#birthday1", label='01')
            birthmonth1 = page.select_option("select#birthmonth1", label='01')
            birthyear1 = page.select_option("select#birthyear1", label='1960')

            passport1 = page.locator("#passport1")
            passport1.wait_for()
            passport1.fill('35324352')

            date = "June 2025"

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

            email1 = page.fill("input#email1", 'romanmammadov872@gmail.com')
            phone1 = page.fill("input#phone1", '0709707067')
            alternativephone1 = page.fill("input#alternativephone1", '0709707067')
        elif "2" in totalPerson:
            # first person
            name1 = page.fill("input#name1", 'Roman')

            surname1 = page.locator("#surname1")
            surname1.wait_for()
            surname1.fill('Mammadov')

            localname1 = page.locator("#localname1")
            localname1.wait_for()
            localname1.fill('Roman Mammadov')

            nationality1 = page.select_option("select#nationality1", label='Foreign')
            birthday1 = page.select_option("select#birthday1", label='01')
            birthmonth1 = page.select_option("select#birthmonth1", label='01')
            birthyear1 = page.select_option("select#birthyear1", label='1960')

            passport1 = page.locator("#passport1")
            passport1.wait_for()
            passport1.fill('35324352')

            date = "June 2025"

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

            email1 = page.fill("input#email1", 'romanmammadov872@gmail.com')
            phone1 = page.fill("input#phone1", '0709707067')
            alternativephone1 = page.fill("input#alternativephone1", '0709707067')

            # second person
            name2 = page.fill("input#name2", 'Ahmed')

            surname2 = page.locator("#surname2")
            surname2.wait_for()
            surname2.fill('Mammadov')

            localname2 = page.locator("#localname1")
            localname2.wait_for()
            localname2.fill('Roman Mammadov')

            nationality2 = page.select_option("select#nationality2", label='Foreign')
            birthday2 = page.select_option("select#birthday2", label='01')
            birthmonth2 = page.select_option("select#birthmonth2", label='01')
            birthyear2 = page.select_option("select#birthyear2", label='1960')

            passport2 = page.locator("#passport2")
            passport2.wait_for()
            passport2.fill('35321352')

            date = "June 2025"

            def datepicker(date):
                list_date = date.split(" ")
                month_and_year = list_date[0] + " " + list_date[1]

                passportExpirationDate2 = page.locator("#passportExpirationDate2")
                passportExpirationDate2.wait_for()
                passportExpirationDate2.click()

                page.wait_for_timeout(5000)
                mmY = page.locator(".datepicker-switch").nth(0)
                mmY.wait_for()
                nextbutton = page.locator(".next").nth(0)
                nextbutton.wait_for()
                while (mmY.text_content() != month_and_year):
                    nextbutton.click(force=True)

                day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")

            datepicker("June 2025 25")
            page.wait_for_timeout(3000)
            email2 = page.fill("input#email2", 'romanmammadov872@gmail.com', force=True)
            phone2 = page.fill("input#phone2", '0709707067')
            alternativephone2 = page.fill("input#alternativephone2", '0709707067')

        elif "3" in totalPerson:
            # first person
            name1 = page.fill("input#name1", 'Roman')

            surname1 = page.locator("#surname1")
            surname1.wait_for()
            surname1.fill('Mammadov')

            localname1 = page.locator("#localname1")
            localname1.wait_for()
            localname1.fill('Roman Mammadov')

            nationality1 = page.select_option("select#nationality1", label='Foreign')
            birthday1 = page.select_option("select#birthday1", label='01')
            birthmonth1 = page.select_option("select#birthmonth1", label='01')
            birthyear1 = page.select_option("select#birthyear1", label='1960')

            passport1 = page.locator("#passport1")
            passport1.wait_for()
            passport1.fill('35324352')

            date = "June 2025"

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

            email1 = page.fill("input#email1", 'romanmammadov872@gmail.com')
            phone1 = page.fill("input#phone1", '0709707067')
            alternativephone1 = page.fill("input#alternativephone1", '0709707067')

            # second person
            name2 = page.fill("input#name2", 'Roman')

            surname2 = page.locator("#surname2")
            surname2.wait_for()
            surname2.fill('Mammadov')

            localname2 = page.locator("#localname1")
            localname2.wait_for()
            localname2.fill('Roman Mammadov')

            nationality2 = page.select_option("select#nationality2", label='Foreign')
            birthday2 = page.select_option("select#birthday2", label='01')
            birthmonth2 = page.select_option("select#birthmonth2", label='01')
            birthyear2 = page.select_option("select#birthyear2", label='1960')

            passport2 = page.locator("#passport2")
            passport2.wait_for()
            passport2.fill('35324352')

            date = "June 2025"

            def datepicker(date):
                list_date = date.split(" ")
                month_and_year = list_date[0] + " " + list_date[1]

                passportExpirationDate2 = page.locator("#passportExpirationDate2")
                passportExpirationDate2.wait_for()
                passportExpirationDate2.click()

                page.wait_for_timeout(5000)
                mmY = page.locator(".datepicker-switch").nth(0)
                mmY.wait_for()
                nextbutton = page.locator(".next").nth(0)
                nextbutton.wait_for()
                while (mmY.text_content() != month_and_year):
                    nextbutton.click(force=True)

                day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")

            datepicker("June 2025 25")

            # email2 = page.fill("input#email2",'romanmammadov872@gmail.com')
            # phone2 = page.fill("input#phone2",'0709707067')
            # alternativephone2 = page.fill("input#alternativephone2",'0709707067')

            # third person
            name3 = page.fill("input#name3", 'Roman')

            surname3 = page.locator("#surname3")
            surname3.wait_for()
            surname3.fill('Mammadov')

            localname3 = page.locator("#localname3")
            localname3.wait_for()
            localname3.fill('Roman Mammadov')

            nationality3 = page.select_option("select#nationality3", label='Foreign')
            birthday3 = page.select_option("select#birthday3", label='01')
            birthmonth3 = page.select_option("select#birthmonth3", label='01')
            birthyear3 = page.select_option("select#birthyear3", label='1960')

            passport3 = page.locator("#passport3")
            passport3.wait_for()
            passport3.fill('35324352')

            date = "June 2025"

            def datepicker(date):
                list_date = date.split(" ")
                month_and_year = list_date[0] + " " + list_date[1]

                passportExpirationDate3 = page.locator("#passportExpirationDate3")
                passportExpirationDate3.wait_for()
                passportExpirationDate3.click()

                page.wait_for_timeout(5000)
                mmY = page.locator(".datepicker-switch").nth(0)
                mmY.wait_for()
                nextbutton = page.locator(".next").nth(0)
                nextbutton.wait_for()
                while (mmY.text_content() != month_and_year):
                    nextbutton.click(force=True)

                day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")

            datepicker("June 2025 25")

            email3 = page.fill("input#email1", 'romanmammadov872@gmail.com')
            phone3 = page.fill("input#phone1", '0709707067')
            alternativephone1 = page.fill("input#alternativephone1", '0709707067')

        elif "4" in totalPerson:
            # first person
            name1 = page.fill("input#name1", 'Roman')

            surname1 = page.locator("#surname1")
            surname1.wait_for()
            surname1.fill('Mammadov')

            localname1 = page.locator("#localname1")
            localname1.wait_for()
            localname1.fill('Roman Mammadov')

            nationality1 = page.select_option("select#nationality1", label='Foreign')
            birthday1 = page.select_option("select#birthday1", label='01')
            birthmonth1 = page.select_option("select#birthmonth1", label='01')
            birthyear1 = page.select_option("select#birthyear1", label='1960')

            passport1 = page.locator("#passport1")
            passport1.wait_for()
            passport1.fill('35324352')

            date = "June 2025"

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

            email1 = page.fill("input#email1", 'romanmammadov872@gmail.com')
            phone1 = page.fill("input#phone1", '0709707067')
            alternativephone1 = page.fill("input#alternativephone1", '0709707067')

            # second person
            name2 = page.fill("input#name2", 'Roman')

            surname2 = page.locator("#surname2")
            surname2.wait_for()
            surname2.fill('Mammadov')

            localname2 = page.locator("#localname1")
            localname2.wait_for()
            localname2.fill('Roman Mammadov')

            nationality2 = page.select_option("select#nationality2", label='Foreign')
            birthday2 = page.select_option("select#birthday2", label='01')
            birthmonth2 = page.select_option("select#birthmonth2", label='01')
            birthyear2 = page.select_option("select#birthyear2", label='1960')

            passport2 = page.locator("#passport2")
            passport2.wait_for()
            passport2.fill('35324352')

            date = "June 2025"

            def datepicker(date):
                list_date = date.split(" ")
                month_and_year = list_date[0] + " " + list_date[1]

                passportExpirationDate2 = page.locator("#passportExpirationDate2")
                passportExpirationDate2.wait_for()
                passportExpirationDate2.click()

                page.wait_for_timeout(5000)
                mmY = page.locator(".datepicker-switch").nth(0)
                mmY.wait_for()
                nextbutton = page.locator(".next").nth(0)
                nextbutton.wait_for()
                while (mmY.text_content() != month_and_year):
                    nextbutton.click(force=True)

                day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")

            datepicker("June 2025 25")

            # email2 = page.fill("input#email2",'romanmammadov872@gmail.com')
            # phone2 = page.fill("input#phone2",'0709707067')
            # alternativephone2 = page.fill("input#alternativephone2",'0709707067')

            # third person
            name3 = page.fill("input#name3", 'Roman')

            surname3 = page.locator("#surname3")
            surname3.wait_for()
            surname3.fill('Mammadov')

            localname3 = page.locator("#localname3")
            localname3.wait_for()
            localname3.fill('Roman Mammadov')

            nationality3 = page.select_option("select#nationality3", label='Foreign')
            birthday3 = page.select_option("select#birthday3", label='01')
            birthmonth3 = page.select_option("select#birthmonth3", label='01')
            birthyear3 = page.select_option("select#birthyear3", label='1960')

            passport3 = page.locator("#passport3")
            passport3.wait_for()
            passport3.fill('35324352')

            date = "June 2025"

            def datepicker(date):
                list_date = date.split(" ")
                month_and_year = list_date[0] + " " + list_date[1]

                passportExpirationDate3 = page.locator("#passportExpirationDate3")
                passportExpirationDate3.wait_for()
                passportExpirationDate3.click()

                page.wait_for_timeout(5000)
                mmY = page.locator(".datepicker-switch").nth(0)
                mmY.wait_for()
                nextbutton = page.locator(".next").nth(0)
                nextbutton.wait_for()
                while (mmY.text_content() != month_and_year):
                    nextbutton.click(force=True)

                day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")

            datepicker("June 2025 25")

            email3 = page.fill("input#email1", 'romanmammadov872@gmail.com')
            phone3 = page.fill("input#phone1", '0709707067')
            alternativephone3 = page.fill("input#alternativephone3", '0709707067')
            # fourth person
            name4 = page.fill("input#name4", 'Roman')

            surname4 = page.locator("#surname4")
            surname4.wait_for()
            surname4.fill('Mammadov')

            localname4 = page.locator("#localname4")
            localname4.wait_for()
            localname4.fill('Roman Mammadov')

            nationality4 = page.select_option("select#nationality4", label='Foreign')
            birthday4 = page.select_option("select#birthday4", label='01')
            birthmonth4 = page.select_option("select#birthmonth4", label='01')
            birthyear4 = page.select_option("select#birthyear4", label='1960')

            passport4 = page.locator("#passport4")
            passport4.wait_for()
            passport4.fill('35324352')

            date = "June 2025"

            def datepicker(date):
                list_date = date.split(" ")
                month_and_year = list_date[0] + " " + list_date[1]

                passportExpirationDate4 = page.locator("#passportExpirationDate4")
                passportExpirationDate4.wait_for()
                passportExpirationDate4.click()

                page.wait_for_timeout(5000)
                mmY = page.locator(".datepicker-switch").nth(0)
                mmY.wait_for()
                nextbutton = page.locator(".next").nth(0)
                nextbutton.wait_for()
                while (mmY.text_content() != month_and_year):
                    nextbutton.click(force=True)

                day = page.click(f"//td[@class='day'][text()='{list_date[2]}']")

            datepicker("June 2025 25")

            email4 = page.fill("input#email4", 'romanmammadov872@gmail.com')
            phone4 = page.fill("input#phone4", '0709707067')
            alternativephone4 = page.fill("input#alternativephone4", '0709707067')


    second_page()
    page.click("a[id=btnAppPersonalNext]")
    page.wait_for_timeout(5000)
    page.click("a[id=btnAppPreviewNext]")

    page.get_by_label("Men umumiy foydalanish shartlarini qabul qilaman va maqullayman.").check()
    page.wait_for_timeout(5000)
    page.click("button[type=button]")


    # Safar boshlanadigan sana.

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
        while not day.is_visible:
            nextbutton.click()

        if day.is_visible():
            day.click()


    timeForMeeting("June 2023 27")

    page.wait_for_timeout(300000)
