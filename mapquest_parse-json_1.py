import urllib.parse
import requests
urlprincipalapi = "https://www.mapquestapi.com/directions/v2/route?"
clave = "zXMxoJpdYJIikz7lofKhXTjAYViZQ8rL"

while True:
    origennn = input("ubicacion inicial o desde que ciudad quiere comenzar: ")
    if origennn == "salir" or origennn == "s":
        break

    destino = input("destino a que ciudad quiere llegar: ")
    if destino == "salir" or destino == "s":
        break

    url = urlprincipalapi + urllib.parse.urlencode({"key" :clave, "from" :origennn, "to" :destino})
    print("URL: " + (url))

    json_datos = requests.get(url).json()
    json_estatus = json_datos ["info"] ["statuscode"]

    if json_estatus == 0:
        print("API estatus: " + str(json_estatus) + " = la llamada en busca de la ruta a sido EXITOSA.\n")
        print("=============================================")
        print("direcciones desde" + (origennn) + " hacia " + (destino))
        print("tiempo del viaje estimado:   " + (json_datos["route"]["formattedTime"]))
        print("kilometros a recorrer:           " + str("{:.2f}".format((json_datos["route"]["distance"])*1.61)))
        print("=============================================")
        for cada in json_datos["route"]["legs"][0]["maneuvers"]:
            print((cada["narrative"]) + " (" + str("{:.2f}".format((cada["distance"])*1.61) + " km)"))
            print("=============================================\n")