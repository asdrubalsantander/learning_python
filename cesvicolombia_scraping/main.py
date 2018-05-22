from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("http://desarrollos.cesvicolombia.com/pctweb/Master/frmConsultas.aspx")

    select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboPaises'))
    select.select_by_visible_text('Colombia')

    sleep(0.5)
    departamentos = ['Norte de Santander de Santander', 'Santander']
    segmentos = ['1 - LIVIANOS', '2 - PESADOS']

    for _, departamento in enumerate(departamentos):
        select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboDepartamentos'))
        select.select_by_visible_text(departamento)

        sleep(0.5)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        municipios = soup.find('select', id="ctl00_ContentPlaceHolder2_cboMunicipio")

        for municipio in municipios.stripped_strings:
            select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboMunicipio'))
            select.select_by_visible_text(municipio)

            sleep(0.5)

            for segmento in segmentos:
                select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboSegmento'))
                select.select_by_visible_text(segmento)

                sleep(0.5)

                select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboMarcas'))
                select.select_by_visible_text('todas')

                submit_button = driver.find_element_by_id('ctl00_ContentPlaceHolder2_btnConsultar')
                submit_button.click()

                sleep(2.5)

                try:
                    table = driver.find_element_by_id('ctl00_ContentPlaceHolder1_DataList1')
                except NoSuchElementException:
                    submit_button = driver.find_element_by_id('ctl00_ContentPlaceHolder2_ImageButton10')
                    submit_button.click()
                    print("Para la ciudad: {} con el segmento: {} y todas las marcas no se encontro resultado."
                          .format(municipio, segmento))


if __name__ == '__main__':
    main()




