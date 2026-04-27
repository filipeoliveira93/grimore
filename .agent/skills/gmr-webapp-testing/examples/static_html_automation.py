from playwright.sync_api import sync_playwright
import os

# Exemplo: Automatizando interação com arquivos HTML estáticos usando URLs file://

html_file_path = os.path.abspath('caminho/para/seu/arquivo.html')
file_url = f'file://{html_file_path}'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    # Navega para o arquivo HTML local
    page.goto(file_url)

    # Captura screenshot inicial
    page.screenshot(path='/tmp/pagina_estatica_inicial.png', full_page=True)

    # Interage com elementos
    page.click('text=Clique Aqui')
    page.fill('#nome', 'João Silva')
    page.fill('#email', 'joao@exemplo.com')

    # Envia o formulário
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    # Captura screenshot final
    page.screenshot(path='/tmp/pagina_estatica_final.png', full_page=True)

    browser.close()

print("Automação de HTML estático concluída!")
print("Screenshots: /tmp/pagina_estatica_inicial.png, /tmp/pagina_estatica_final.png")
