######################################
#       _           _ _ _   _
#     (_)_   _  __| (_| |_| |__
#    | | | | |/ _` | | __| '_ \
#   | | |_| | (_| | | |_| | | |
# _/ |\__,_|\__,_|_|\__|_| |_|
#|__/
#Make Holofernes pay with his head and then search 
#your bagulho which is comming de jegue 
#from the correio.
#Matheu - 2020
#Puta que pariu que ano desgraçado.
#######################################
#gonna use selenium to scrap the fuck out of this fucker
#and import time & keys from it
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from msedge.selenium_tools import Edge, EdgeOptions

#######################################

#maximus variables of this shit
#path is setted to edgedriver in this case, 
#you'll gonna need to download the apropriate version to your browser tho
#its not difficult to implement to another browser, just change the driver
#and the correct appointment in the driver section to "webriver.Yourcorrectbrowser.exe"
PATH = "..\\Judith\\msedgedriver.exe"
#read the tracking code(s) from the tracking txt file
#you can put up various tracking numbers, but dont forget to separate them with commas.
TRACKING = open('..\\Judith\\tracking.txt', 'r')
#tracking number
CODE = TRACKING.read()
#the correios website
SITE = "https://www2.correios.com.br/sistemas/rastreamento/default.cfm"
#basic config
options = EdgeOptions()                   #ebable the options or edge
options.use_chromium = True               #uses chromium engine
options.add_argument("headless")          #enable headless mode
options.add_argument("disable-gpu")
options.add_argument("log-level=3")       #disable warnings

#######################################

def judith(SITE):
   driver = Edge(PATH)
   driver.get(SITE)
   #find the element by his name, it can be by its ID or CSS tho
   element = driver.find_element_by_name("objetos")
   element.clear()
   #insert the apropriate tracking code and then proceeds to the next page
   element.send_keys(CODE)
   element.send_keys(Keys.RETURN)

   #must implement total headless mode and print in terminal the state
   #it needs to go here
   #in this exact spot

   #save a screenshot of the tracking progress bc im lazy right now to implement a callback terminal function
   driver.save_screenshot('consulta.png')
   #if the code is wrong, it'll show this output
   assert "Sem bagulhos encontrados, mano." not in driver.page_source
   #close the program and the browser window. BEWARE
   driver.close()

def title(CODE):
   title = """
      _           _ _ _   _
     (_)_   _  __| (_| |_| |__
     | | | | |/ _` | | __| '_ \\
     | | |_| | (_| | | |_| | | |
    _/ |\__,_|\__,_|_|\__|_| |_|
   |__/
                1.0
   """
   print(title)
   #the 13 digits tracking number
   print("Lendo o(s) códigos de rastreio.")
   print("Código(s) >> ", CODE)
   print("Procurando...")

#######################################

#main operations
title(CODE)

judith(SITE)

exit()