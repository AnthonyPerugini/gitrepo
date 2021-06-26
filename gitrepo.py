import sys
import os
import shutil
from getpass import getpass
import pyperclip
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

# change options.binary_location and executable_path to match your browser and driver locations
options.binary_location = r"/usr/bin/google-chrome-stable"
executable_path = os.path.dirname(os.path.abspath(__file__)) + "/chromedriver"

def main():

    user_name, password = get_credentials()

    # get repo_name, and make a new directory.  If no name provided, use the current working directory.
    if len(sys.argv) == 2:
        repo_name = sys.argv[1]
        try:
            os.mkdir(repo_name)
            os.chdir(repo_name)
        except OSError as e:
            print(e)
            print('A directory with that name already exists in this location, exiting to avoid overwrite')
            tearDown(local_name=repo_name)
            exit(1)
    else:
        repo_name = os.path.basename(os.getcwd())

    try:
        with webdriver.Chrome(executable_path=executable_path, options=options) as driver:

            github_login(driver)

            # create new repo
            driver.get('https://github.com/new')

            name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'repository_name')))
            name_field.send_keys(f'{repo_name}')

            # make sure repo name is available, then create
            confirmation_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id^=input-check]")))
            assert confirmation_message.text == f'{repo_name} is available.', confirmation_message.text
            
            submit_button_xpath = '//*[@id="new_repository"]/div[4]/button'
            driver.find_element_by_xpath(submit_button_xpath).click()


        # check if .git and README already exist. If not, create them
        if '.git' not in os.listdir():
            os.system('git init')
        if 'README.md' not in os.listdir():
            os.system('touch README.md')

        os.system('git add .')
        os.system('git commit -m "initial commit"')

        # HTTPS vs SSH remote origin
        if input('Choose 0 for HTTPS, 1 for SSH: ') == 1:
            os.system(f'git remote add origin git@github.com:{user_name}/{repo_name}.git')
        else:
            os.system(f'git remote add origin https://github.com/{user_name}/{repo_name}.git')

        os.system('git push -u origin master')
        pyperclip.copy(f'github.com/{user_name}/{repo_name}')
        os.system('echo "Github URL successfully copied to clipboard!"')

    except Exception as e:
        print(e)
        tearDown(local_name=repo_name, remote_name=repo_name)


def github_login(driver):

    user_name, password = get_credentials()

    driver.get('https://github.com/login')

    login_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_field')))
    login_field.send_keys(user_name)

    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
    password_field.send_keys(password)

    driver.find_element_by_name('commit').click()


def tearDown(local_name=None, remote_name=None):
    if local_name is not None:
        print('tearing down local files...')
        shutil.rmtree(local_name)
        print('local repo tear down sucessful!')

    if remote_name is not None:
        print('tearing down remote github repo...')

        user_name, password = get_credentials()
        
        with webdriver.Chrome(executable_path=executable_path, options=options) as driver:

            github_login(driver)

            driver.get(f'https://github.com/{user_name}/{remote_name}/settings')

            delete_button_xpath = '//*[@id="options_bucket"]/div[10]/ul/li[4]/details/summary'
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, delete_button_xpath))).click()

            confirmation_field_xpath = '//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input'
            confirmation_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, confirmation_field_xpath)))
            confirmation_field.send_keys(f'{user_name}/{remote_name}')

            confirm_delete_xpath = '//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button/span[1]'
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, confirm_delete_xpath))).click()

        print('remote tear down sucessful!')


def get_credentials():
    if os.path.exists('pass.txt'):
        with open('pass.txt') as f:
            credentials = f.readlines()
            credentials = [cred.strip() for cred in credentials]
            user_name, password = credentials
    else:
        user_name = input('Github Username: ')
        password = getpass()

    return user_name, password


if __name__ == '__main__':
    main()
