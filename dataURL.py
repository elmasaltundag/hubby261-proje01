import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    dataFile ="https://madran.net"
    dataFile ="https://hacettepe.edu.tr"
    kontrolhttp = dataFile[:7]
    kontrolhttps = dataFile[:8]
    if siteURL in "http://" or "https://":
      print("Geçerli adres")
      dataOpen.write(siteURL+"\n")
    else:
      print("http:// ön ekini kullanarak geçerli bir aadres giriniz ")
      print(siteURL)
    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')

    #file check

    if os.stat(self.dataFile).st_size == 0:
      print("Henüz kaydedilmiş adres yok!")
    else:
      for dataShow in dataOpen:
        print(dataShow)
    dataOpen.close()