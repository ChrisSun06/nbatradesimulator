from selenium import webdriver
import re

chromedriver = "C:\\Users\\Hongy\\Desktop\\chromedriver"
driver = webdriver.Chrome(chromedriver)
url = "https://www.basketball-reference.com/contracts/"
salary_xpath = list('// *[ @ id = "contracts"] / tbody / tr[x] / td[2]')
name_path = list('//*[@id="contracts"]/tbody/tr[x]/th')
NBA_CAP_MAXIMUM = 109140000


def getPlayersContracts(players: list, contracts: list, name: str):
    temp_url = url + name + '.html'
    driver.get(temp_url)
    for i in range(15): #Maximum 15 players on a team
        salary_xpath[39] = str(i+1)
        name_path[30] = str(i+1)
        salary = driver.find_element_by_xpath(''.join(salary_xpath)).text
        playername = driver.find_element_by_xpath(''.join(name_path)).text
        salary = re.sub("[^0-9]", "", salary).strip()
        if salary.isspace() or not salary:
            break
        salary_int = int(salary)
        players.append(playername)
        contracts.append(salary_int)

def checkOverCap(name: str):
    temp_url = url + name + '.html'
    driver.get(temp_url)
    total_salary = driver.find_element_by_xpath("// *[ @ id = \"contracts\"] / tfoot / tr / td[2]").text
    if int(re.sub("[^0-9]", "", total_salary).strip()) > NBA_CAP_MAXIMUM:
        return -1
    else:
        return int(re.sub("[^0-9]", "", total_salary).strip())

#//*[@id="contracts"]/tbody/tr[1]/th
#//*[@id="contracts"]/tbody/tr[2]/th
if __name__ == "__main__":
    print(checkOverCap("POR"))
    print(checkOverCap("SAC"))
