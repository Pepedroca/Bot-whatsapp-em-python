"""

obs:
1- Primeira mente instale um executavel chamado chromedriver.exe link downloads
para linux ou windowns: https://chromedriver.chromium.org/downloads
e so jogar na raiz da sua pasta onde esta o seu codigo

2 vai ficar pedindo pra vc conectar o seu whats no web.whatsapp quando executar o codigo entao o "sleep(16)"
na linha "55" vai ser util para dar o tempo pra voce conectar o celular com o  codigo de barra  qualquer
coisa so aumentar o tempo 

3- installar o selenium no python 
"""

from email import message
from webbrowser import Chrome
from selenium import webdriver
from time import sleep


class WhatsAppBot:
    def __init__(self):
        self.messagem = 'Salve!'
        self.contatos = ['Mames', 'Pai']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        # este self.chrome serve para abrir o chromedriver.exe quando ele for chamado
        self.chrome = webdriver.Chrome(executable_path='./chromedriver.exe')
        
    def acessar_site(self, link):
        self.chrome.get(link)
    
    
    def sair_chrome(self):
        self.chrome.close()
        
        
    def enviar_msg(self):
        # <span dir="auto" title="Mames" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Mames</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        for contato in self.contatos:
            contato = self.chrome.find_element_by_xpath(f'//span[@title="{contato}"]')
            sleep(3)
            contato.click()
            chat_box = self.chrome.find_element_by_class_name('p3_M1')
            chat_box.click()
            chat_box.send_keys(self.messagem)
            bt_enviar = self.chrome.find_element_by_xpath('//span[@data-icon="send"]')
            sleep(2)
            bt_enviar.click()
            
        

        
if __name__ == '__main__':
    bot = WhatsAppBot()
    bot.acessar_site('https://web.whatsapp.com/')
    sleep(15)
    # bot.enviar_msg()
