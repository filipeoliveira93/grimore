from playwright.sync_api import sync_playwright

# Exemplo: Capturando logs do console durante automação de browser

url = 'http://localhost:5173'  # Substitua pela URL do seu app

console_logs = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    # Configura captura de logs do console
    def handle_console_message(msg):
        console_logs.append(f"[{msg.type}] {msg.text}")
        print(f"Console: [{msg.type}] {msg.text}")

    page.on("console", handle_console_message)

    # Navega para a página
    page.goto(url)
    page.wait_for_load_state('networkidle')

    # Interaja com a página (dispara logs do console)
    page.click('text=Dashboard')
    page.wait_for_timeout(1000)

    browser.close()

# Salva logs do console em arquivo
import os
output_dir = '/tmp'
log_path = os.path.join(output_dir, 'console.log')
with open(log_path, 'w') as f:
    f.write('\n'.join(console_logs))

print(f"\nCapturadas {len(console_logs)} mensagens do console")
print(f"Logs salvos em: {log_path}")
