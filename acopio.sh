#!/bin/bash

# Crear grupo de recursos.
echo "Creando grupo de recursos."
az group create --location francecentral --name Hito4-Francia-Central

# Crear la máquina virtual.
echo "Creando maquina virtual."
az vm create --resource-group Hito4-Francia-Central --name GestionClientes --image credativ:Debian:9:9.0.201808270 --admin-username azureuser --ssh-key-value ~/.ssh/id_rsa.pub --size Basic_A1 --public-ip-address-allocation static

# Abrir el puerto 80.
echo "Abriendo el puerto 80."
az vm open-port --port 80 --resource-group Hito4-Francia-Central --name GestionClientes
