from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
from time import sleep


SLEEP_TIME = 2


def write_data(data):
    with open('data.txt', 'a') as file:
        for _, text in enumerate(data):
            file.write(text)


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("http://desarrollos.cesvicolombia.com/pctweb/Master/frmConsultas.aspx")

    select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboPaises'))
    select.select_by_visible_text('Colombia')

    sleep(SLEEP_TIME)
    departamentos = ['Norte de Santander de Santander', 'Santander']
    segmentos = ['1 - LIVIANOS', '2 - PESADOS']

    for _, departamento in enumerate(departamentos):
        select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboDepartamentos'))
        select.select_by_visible_text(departamento)

        sleep(SLEEP_TIME)

        html_municipios = driver.page_source
        soup_municipios = BeautifulSoup(html_municipios, "html.parser")

        municipios = soup_municipios.find('select', id="ctl00_ContentPlaceHolder2_cboMunicipio")

        for municipio in municipios.stripped_strings:
            select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboMunicipio'))
            select.select_by_visible_text(municipio)

            sleep(SLEEP_TIME)

            for segmento in segmentos:
                select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboSegmento'))
                select.select_by_visible_text(segmento)

                sleep(SLEEP_TIME)

                select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder2_cboMarcas'))
                select.select_by_visible_text('todas')

                submit_button = driver.find_element_by_id('ctl00_ContentPlaceHolder2_btnConsultar')
                submit_button.click()

                sleep(SLEEP_TIME * 3)

                try:
                    data = []
                    table = driver.find_element_by_id('ctl00_ContentPlaceHolder1_DataList1')
                except StaleElementReferenceException:
                    pass
                except NoSuchElementException:
                    submit_button = driver.find_element_by_id('ctl00_ContentPlaceHolder2_ImageButton10')
                    submit_button.click()
                    data.append("************************************\n"
                                "Para la ciudad: {} con el segmento: {} y todas las marcas no se encontro resultado.\n"
                                "************************************\n"
                                .format(municipio, segmento))
                    write_data(data)
                    sleep(SLEEP_TIME)
                else:
                    html_datos = driver.page_source
                    soup_datos = BeautifulSoup(html_datos, "html.parser")

                    tds = soup_datos.find_all("td", {"class": "style73"})

                    data.append("************************************\n"
                                "Para la ciudad: {} con el segmento: {} y todas las marcas se encontro:\n"
                                .format(municipio, segmento))

                    write_data(data)

                    for i, td in enumerate(tds):
                        span = td.find("span")
                        info = span.text

                        indentation = '\t\t'

                        if i % 3 == 0:
                            indentation = '\t'
                        if info == '':
                            info = 'No se encontro información'
                        write_data(indentation + info + '\n')


if __name__ == '__main__':
    main()




