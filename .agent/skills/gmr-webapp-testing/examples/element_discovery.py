from playwright.sync_api import sync_playwright

# Exemplo: Descobrindo botões, links e inputs em uma página

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navega para a página e aguarda carregamento completo
    page.goto('http://localhost:5173')
    page.wait_for_load_state('networkidle')

    # Descobre todos os botões da página
    buttons = page.locator('button').all()
    print(f"Encontrados {len(buttons)} botões:")
    for i, button in enumerate(buttons):
        text = button.inner_text() if button.is_visible() else "[oculto]"
        print(f"  [{i}] {text}")

    # Descobre links
    links = page.locator('a[href]').all()
    print(f"\nEncontrados {len(links)} links:")
    for link in links[:5]:  # Mostra os primeiros 5
        text = link.inner_text().strip()
        href = link.get_attribute('href')
        print(f"  - {text} -> {href}")

    # Descobre campos de input
    inputs = page.locator('input, textarea, select').all()
    print(f"\nEncontrados {len(inputs)} campos de input:")
    for input_elem in inputs:
        name = input_elem.get_attribute('name') or input_elem.get_attribute('id') or "[sem nome]"
        input_type = input_elem.get_attribute('type') or 'text'
        print(f"  - {name} ({input_type})")

    # Captura screenshot para referência visual
    page.screenshot(path='/tmp/descoberta_pagina.png', full_page=True)
    print("\nScreenshot salva em /tmp/descoberta_pagina.png")

    browser.close()
