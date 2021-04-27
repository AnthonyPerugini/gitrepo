import sys
import os
from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# CHANGE THESE TO MATCH YOUR DOWNLOAD LOCATIONS FOR YOUR BROWSER AND BROWSERDRIVER
options.binary_loaction = r"/usr/bin/google-chrome-stable"
executable_path = r"/usr/bin/chromedriver"

def main():
    user_name = input('Github Username: ')
    password = getpass()

    # get repo_name, and make a new directory.  If no name provided, use the current working directory.
    if len(sys.argv) == 2:
        repo_name = sys.argv[1]
        try:
            os.mkdir(repo_name)
            os.chdir(repo_name)
        except OSError as e:
            print(e)
            print('Exiting: use a different repo name to avoid overwriting!')
            exit(1)
    else:
        repo_name = os.path.basename(os.getcwd())


    with webdriver.Chrome(executable_path=executable_path, options=options) as driver:
        driver.get('https://github.com/login')

        login_field = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.ID, 'login_field')))
        login_field.send_keys(user_name)

        password_field = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.ID, 'password')))
        password_field.send_keys(password)

        driver.find_element_by_name('commit').click()
        driver.get('https://github.com/new')


        name_field = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.ID, 'repository_name')))
        name_field.send_keys(f'{repo_name}')

        
        responce = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "[id^=input-check]")))
        # assert responce.text == f'{repo_name} is available.', responce.text
        
        button_xpath = '//*[@id="new_repository"]/div[4]/button'
        driver.find_element_by_xpath(button_xpath).click()

    if '.git' not in os.listdir():
        os.system('git init')

    if 'README.md' not in os.listdir():
        os.system('touch README.md')

    os.system('git add .')
    os.system('git commit -m "initial commit"')
    os.system(f'git remote add origin git@github.com:{user_name}/{repo_name}.git')
    os.system('git push -u origin master')

if __name__ == '__main__':
    main()
