import os
import tabula
from zipfile import ZipFile

def main():
  extractTables()
  zipFiles()

def extractTables():
  # Extrair quadro 30 da página 114 e converter para .csv
  tabula.convert_into("padrao-tiss_componente-organizacional_202111.pdf",
  "quadro30.csv",
  output_format="csv",
  java_options="-Dfile.encoding=UTF8",
  pages=114)
  # Extrair quadro 31 das páginas 115-120 e converter para .csv
  tabula.convert_into("padrao-tiss_componente-organizacional_202111.pdf",
  "quadro31.csv",
  output_format="csv",
  java_options="-Dfile.encoding=UTF8",
  pages='115-120')
  # Extrair quadro 32 da página 120 e converter para .csv
  tabula.convert_into("padrao-tiss_componente-organizacional_202111.pdf",
  "quadro32.csv",
  output_format="csv",
  java_options="-Dfile.encoding=UTF8",
  pages=120)

def zipFiles():
  # Criar pasta .zip chamada "Teste_William.zip"
  zipObj = ZipFile("Teste_William.zip","w")
  # Adicionar arquivos requeridos na pasta
  zipObj.write("quadro30.csv")
  zipObj.write("quadro31.csv")
  zipObj.write("quadro32.csv")
  zipObj.close()
  # Limpar arquivos fora da pasta .zip
  os.remove("quadro30.csv")
  os.remove("quadro31.csv")
  os.remove("quadro32.csv")
