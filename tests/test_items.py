from selenium.webdriver.common.by import By
import pytest
from Bibliotiki import *

from selenium.webdriver.chrome.options import Options

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


languages = {
    "ar" : "أضف الى سلة التسوق",
    "ca" : "Afegeix a la cistella",
    "cs" : "Vložit do košíku",
    "da" : "Læg i kurv",
    "de" : "In Warenkorb legen",
    "en-gb" : "Add to basket",
    "el" : "Προσθήκη στο καλάθι",
    "es" : "Añadir al carrito",
    "fi" : "Lisää koriin",
    "fr" : "Ajouter au panier",
    "it" :  "Aggiungi al carrello",
    "ko" :  "장바구니 담기",
    "nl" : "Voeg aan winkelmand toe",
    "pl" : "Dodaj do koszyka",
    "pt" : "Adicionar ao carrinho",
    "pt-br" : "Adicionar à cesta",
    "ro" : "Adauga in cos",
    "ru" : "Добавить в корзину",
    "sk" : "Pridať do košíka",
    "uk" : "Додати в кошик",
    "zh-hans" : "Add to basket"
}

def test_text_button_language(browser, request):
    browser.get(link)
    language = request.config.getoption("language")
    time.sleep(1)
    try:
        button_add_item = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button.btn-add-to-basket[type='submit']")), "not visible button 'Add item'")
    except:
        assert False, "not visible button 'Add item'"
    assert button_add_item.text == languages[language], "Name at France language invalid"
    

             