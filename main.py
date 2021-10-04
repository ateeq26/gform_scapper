from selenium import webdriver
from random import randrange, randint

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")

for i in range(59):
    browser = webdriver.Chrome(
        executable_path='C:/Users/AteeqPC/Downloads/chromedriver_win32/chromedriver.exe', options=option)

    browser.get("https://forms.gle/VkjmvnkJAzKLo1yr6")

    age_pick = randrange(0, 1)
    age_id = 'i9' if age_pick == 0 else 'i12'

    # name_text = browser.find_element_by_class_name(
    #     'quantumWizTextinputPaperinputInput')

    age_radio = browser.find_element_by_id(age_id)
    age_radio.click()

    ethnicity_radio = browser.find_element_by_id('i19')
    ethnicity_radio.click()

    weight_text = browser.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    weight_pick = randrange(43, 79)
    weight = str(weight_pick) + ' kg'
    weight_text.send_keys(weight)

    height_text = browser.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    height_pick = randrange(147, 182)
    height = str(height_pick) + ' cm'
    height_text.send_keys(height)

    # education
    education_pick = randrange(1, 5)
    if education_pick == 1:
        education_id = 'i37'
    elif education_pick == 2:
        education_id = 'i40'
    elif education_pick == 3:
        education_id = 'i43'
    else:
        education_id = 'i46'

    education_radio = browser.find_element_by_id(education_id)
    education_radio.click()

    # physical_activity
    physical_pick = randrange(1, 3)
    if physical_pick == 1:
        physical_id = 'i65'
    elif physical_pick == 2:
        physical_id = 'i62'
    else:
        physical_id = 'i59'

    physical_radio = browser.find_element_by_id(physical_id)
    physical_radio.click()

    # eats
    eats_pick = randrange(1, 5)
    if eats_pick == 1:
        eats_id = 'i72'
    elif eats_pick == 2:
        eats_id = 'i75'
    elif eats_pick == 3:
        eats_id = 'i78'
    else:
        eats_id = 'i81'

    eats_radio = browser.find_element_by_id(eats_id)
    eats_radio.click()

    # gender
    gender_pick = randrange(1, 2)
    if gender_pick == '1':
        gender_id = 'i88'
    else:
        gender_id = 'i91'

    gender_radio = browser.find_element_by_id(gender_id)
    gender_radio.click()

    # watch videos
    watch_pick = randrange(1, 70)
    if watch_pick >= 1 and watch_pick <= 30:
        watch_id = 'i104'
    elif watch_pick >= 31 and watch_pick <= 50:
        watch_id = 'i107'
    else:
        watch_id = 'i110'

    watch_radio = browser.find_element_by_id(watch_id)
    watch_radio.click()

    # habits
    habits_pick = randrange(1, 70)
    if habits_pick >= 1 and habits_pick <= 30:
        habits_id = 'i117'
    elif habits_pick >= 31 and habits_pick <= 50:
        habits_id = 'i120'
    else:
        habits_id = 'i123'

    habits_radio = browser.find_element_by_id(habits_id)
    habits_radio.click()

    # celeb
    celeb_pick = randrange(1, 3)
    if celeb_pick == 1:
        celeb_id = 'i130'
    elif celeb_pick == 2:
        celeb_id = 'i133'
    else:
        celeb_id = 'i136'

    celeb_radio = browser.find_element_by_id(celeb_id)
    celeb_radio.click()

    # advice
    advice_pick = randrange(1, 5)
    if advice_pick == 1:
        advice_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div'
    elif advice_pick == 2:
        advice_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div'
    elif advice_pick == 3:
        advice_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div'
    elif advice_pick == 4:
        advice_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div'
    else:
        advice_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div'

    advice_radio = browser.find_element_by_xpath(advice_path)
    advice_radio.click()

    # supplements
    supplement_pick = randrange(1, 3)
    if supplement_pick == 1:
        supplement_id = 'i147'
    elif supplement_pick == 2:
        supplement_id = 'i150'
    else:
        supplement_id = 'i153'

    supplement_radio = browser.find_element_by_id(supplement_id)
    supplement_radio.click()

    # dyk
    dyk_pick = randrange(1, 3)
    if dyk_pick == 1:
        dyk_id = 'i160'
    elif dyk_pick == 2:
        dyk_id = 'i163'
    else:
        dyk_id = 'i166'

    dyk_radio = browser.find_element_by_id(dyk_id)
    dyk_radio.click()

    submit_path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    submit_btn = browser.find_element_by_xpath(submit_path)
    submit_btn.click()

    browser.close()
    print("count: ", i)
