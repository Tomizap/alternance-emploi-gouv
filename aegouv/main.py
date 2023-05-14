# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class AegouvFr:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        # Test name: alternance.emploi.gouv.fr
        # Step # | name | target | value | comment
        # 1 | open | https://www.alternance.emploi.gouv.fr/bourse-a-l-emploi-recherche-prive |  |
        self.driver.get("https://www.alternance.emploi.gouv.fr/bourse-a-l-emploi-recherche-prive")
        # 2 | setWindowSize | 1296x696 |  |
        self.driver.set_window_size(1296, 696)
        # 3 | selectFrame | index=0 |  |
        self.driver.switch_to.frame(0)

    def application_loop(self):
        self.login()
        # 4 | click | id=lang-switcher-input |  |
        self.driver.find_element(By.ID, "lang-switcher-input").click()
        # 5 | type | id=lang-switcher-input | ndrc |
        self.driver.find_element(By.ID, "lang-switcher-input").send_keys("ndrc")
        # 6 | click | id=lang-switcher-item-0 |  |
        self.driver.find_element(By.ID, "lang-switcher-item-0").click()
        # 7 | click | css=.css-1kw2fa0 #lang-switcher-input |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1kw2fa0 #lang-switcher-input").click()
        # 8 | type | css=.css-1kw2fa0 #lang-switcher-input | paris |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1kw2fa0 #lang-switcher-input").send_keys("paris")
        # 9 | click | css=.css-1kw2fa0 .chakra-stack |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1kw2fa0 .chakra-stack").click()
        # 10 | click | id=lang-switcher-item-0 |  |
        self.driver.find_element(By.ID, "lang-switcher-item-0").click()
        # 11 | click | css=.css-10s59ld |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-10s59ld").click()
        for i in range(9999):
            self.application()
            time.sleep(3)

    def application(self):
        # 16 | click | css=.css-1kii3bs |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1kii3bs").click()
        # 19 | click | id=lastName |  |
        self.driver.find_element(By.ID, "lastName").click()
        # 20 | type | id=lastName | Guetzo |
        self.driver.find_element(By.ID, "lastName").send_keys("Guetzo")
        # 21 | click | id=firstName |  |
        self.driver.find_element(By.ID, "firstName").click()
        # 22 | type | id=firstName | Nathan |
        self.driver.find_element(By.ID, "firstName").send_keys("Nathan")
        # 23 | click | id=email |  |
        self.driver.find_element(By.ID, "email").click()
        # 24 | type | id=email | nathan.guetzo@gmail.com |
        self.driver.find_element(By.ID, "email").send_keys("nathan.guetzo@gmail.com")
        # 25 | click | id=phone |  |
        self.driver.find_element(By.ID, "phone").click()
        # 26 | type | id=phone | 0756108412 |
        self.driver.find_element(By.ID, "phone").send_keys("0756108412")
        # 27 | click | id=message |  |
        self.driver.find_element(By.ID, "message").click()
        # 28 | type | id=message | Madame, Monsieur,\n\nActuellement en quête d'une entreprise pour effectuer mon alternance en BTS Négociation et Relation Client, je me permets de vous proposer ma candidature.\n\nPassionné par les métiers de la vente et de la négociation, je suis convaincu que l'alternance est une véritable opportunité pour acquérir une expérience professionnelle solide tout en obtenant une formation théorique de qualité. Votre entreprise, renommée pour son savoir-faire et son professionnalisme, m'apparaît comme le lieu idéal pour me former dans le domaine de la négociation et de la relation client.\n\nGrâce à mon parcours scolaire et mes différentes expériences professionnelles, j'ai développé de solides compétences relationnelles et commerciales. De plus, mon goût pour les challenges et ma persévérance m'ont permis de réaliser de nombreux objectifs commerciaux, notamment lors de mes précédentes missions.\n\nL'alternance en BTS Négociation et Relation Client est une étape importante dans mon projet professionnel, qui est de devenir un commercial accompli et performant. J'aimerais rejoindre votre entreprise pour bénéficier de votre expertise, apprendre de vos collaborateurs et développer mes compétences commerciales.\n\nJe suis persuadé que mon enthousiasme, ma motivation et mes compétences pourront être des atouts pour votre entreprise. Je suis également prêt à m'investir pleinement dans les missions qui me seront confiées et à participer activement à la vie de votre entreprise.\n\nJe vous remercie pour l'attention que vous porterez à ma candidature et j'espère avoir l'opportunité de vous rencontrer pour vous convaincre de ma motivation et de mon sérieux. |
        self.driver.find_element(By.ID, "message").send_keys(
            "Madame, Monsieur,\\n\\nActuellement en quête d\'une entreprise pour effectuer mon alternance en BTS Négociation et Relation Client, je me permets de vous proposer ma candidature.\\n\\nPassionné par les métiers de la vente et de la négociation, je suis convaincu que l\'alternance est une véritable opportunité pour acquérir une expérience professionnelle solide tout en obtenant une formation théorique de qualité. Votre entreprise, renommée pour son savoir-faire et son professionnalisme, m\'apparaît comme le lieu idéal pour me former dans le domaine de la négociation et de la relation client.\\n\\nGrâce à mon parcours scolaire et mes différentes expériences professionnelles, j\'ai développé de solides compétences relationnelles et commerciales. De plus, mon goût pour les challenges et ma persévérance m\'ont permis de réaliser de nombreux objectifs commerciaux, notamment lors de mes précédentes missions.\\n\\nL\'alternance en BTS Négociation et Relation Client est une étape importante dans mon projet professionnel, qui est de devenir un commercial accompli et performant. J\'aimerais rejoindre votre entreprise pour bénéficier de votre expertise, apprendre de vos collaborateurs et développer mes compétences commerciales.\\n\\nJe suis persuadé que mon enthousiasme, ma motivation et mes compétences pourront être des atouts pour votre entreprise. Je suis également prêt à m\'investir pleinement dans les missions qui me seront confiées et à participer activement à la vie de votre entreprise.\\n\\nJe vous remercie pour l\'attention que vous porterez à ma candidature et j\'espère avoir l\'opportunité de vous rencontrer pour vous convaincre de ma motivation et de mon sérieux.")
        # 29 | click | css=.css-1mz17vg |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1mz17vg").click()
        # 30 | type | id=field-:ra: | C:\fakepath\CV.pdf |
        self.driver.find_element(By.ID, "field-:ra:").send_keys("C:\\fakepath\\CV.pdf")
        # 31 | click | css=.css-1p7sw3d |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1p7sw3d").click()
        # 32 | mouseOver | css=.css-1p7sw3d |  |
        element = self.driver.find_element(By.CSS_SELECTOR, ".css-1p7sw3d")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 33 | click | css=.css-bo6137 |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-bo6137").click()
        # 34 | click | css=.css-1v4xcoh:nth-child(3) .chakra-image |  |
        self.driver.find_element(By.CSS_SELECTOR, ".css-1v4xcoh:nth-child(3) .chakra-image").click()
