from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Abra a pagina inicial do Urban Routes
driver.get('https://cnt-b98cc485-26cb-47cb-b2ae-eaed4f65415e.containerhub.tripleten-services.com?lng=pt')
# Verifique se a URL contém tripleten-services
assert 'tripleten-services.com' in driver.current_url
# Feche o navegador
driver.quit()