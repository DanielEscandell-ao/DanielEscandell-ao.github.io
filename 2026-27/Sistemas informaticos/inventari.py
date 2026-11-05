"""
inventari.py - inventari dels perifèrics de l'equip (Windows 11 o Linux Mint)

Genera inventari.csv, amb una fila per dispositiu.
Execució:  py inventari.py (Windows)  ·  python3 inventari.py (Linux)

Has de completar els 5 TODO. No cal tocar res de la zona "NO CAL MODIFICAR".
"""

import csv
import os
import platform
import subprocess

FITXER_SORTIDA = "inventari.csv"

# Codis de classe USB (bInterfaceClass) i el seu nom
CLASSES_USB = {
    "01": "Àudio",
    "02": "Comunicació",
    "03": "HID",
    "06": "Imatge",
    "07": "Impressora",
    "08": "Emmagatzematge massiu",
    "09": "Concentrador (hub)",
    "0a": "Comunicació",
    "0b": "Targeta intel·ligent",
    "0e": "Vídeo",
    "e0": "Sense fil (Bluetooth)",
    "ef": "Miscel·lània",
    "fe": "Específica d'aplicació",
    "ff": "Específica del fabricant",
}

# TODO 2: tipus de cada classe: "entrada", "sortida", "mixt",
# "mixt (emmagatzematge)" o "mixt (comunicació)".
# Si a l'inventari et surt una classe que no hi és, afegeix-la.
CLASSIFICACIO = {
    # Windows
    "Keyboard": "entrada",
    "Monitor": "sortida",
    "Mouse": "entrada",
    "Camera": "entrada",
    "Image": "entrada",                 
    "Display": "sortida",
    "Printer": "sortida",
    "AudioEndpoint": "mixt",           
    "MEDIA": "mixt",                   
    "DiskDrive": "mixt (emmagatzematge)",
    "Net": "mixt (comunicació)",
    "Bluetooth": "mixt (comunicació)",
    # Linux, PCI (lspci)
    "VGA compatible controller": "sortida",
    "Audio device": "mixt",
    "Network controller": "mixt (comunicació)",
    "Ethernet controller": "mixt (comunicació)",
    "Non-Volatile memory controller": "mixt (emmagatzematge)",
    "SATA controller": "mixt (emmagatzematge)",
    # Linux, USB
    "HID": "entrada",                   
    "Vídeo": "entrada",                 
    "Àudio": "mixt",
    "Emmagatzematge massiu": "mixt (emmagatzematge)",
    "Sense fil (Bluetooth)": "mixt (comunicació)",
}


# ===========================================================================
# NO CAL MODIFICAR: lectura dels dispositius
# ===========================================================================

# --- Linux ---

def llegir_fitxer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read().strip()
    except OSError:
        return ""


def dispositius_pci_linux():
    # lspci -vmm -k dona un bloc per dispositiu, amb línies "Clau:<tab>Valor"
    resultat = subprocess.run(["lspci", "-vmm", "-k"],
                              capture_output=True, text=True)
    dispositius = []
    for bloc in resultat.stdout.strip().split("\n\n"):
        camps = {}
        for linia in bloc.splitlines():
            if ":\t" in linia:
                clau, valor = linia.split(":\t", 1)
                camps[clau] = valor
        if not camps:
            continue
        dispositius.append({
            "nom": camps.get("Vendor", "") + " " + camps.get("Device", ""),
            "connexio": "PCI (intern)",
            "classe": camps.get("Class", ""),
            "driver": camps.get("Driver", ""),
            "estat": "",
        })
    return dispositius


def dispositius_usb_linux(arrel="/sys/bus/usb/devices"):
    # Una carpeta per dispositiu (1-2) i una per cada interfície (1-2:1.0, 1-2:1.1...)
    if not os.path.isdir(arrel):
        return []
    dispositius = []
    for entrada in sorted(os.listdir(arrel)):
        if entrada.startswith("usb") or ":" in entrada:   # concentradors arrel i interfícies
            continue
        carpeta = os.path.join(arrel, entrada)
        fabricant = llegir_fitxer(os.path.join(carpeta, "manufacturer"))
        producte = llegir_fitxer(os.path.join(carpeta, "product"))
        identificador = (llegir_fitxer(os.path.join(carpeta, "idVendor")) + ":" +
                         llegir_fitxer(os.path.join(carpeta, "idProduct")))
        classes = []
        drivers = []
        for subcarpeta in sorted(os.listdir(arrel)):
            if not subcarpeta.startswith(entrada + ":"):
                continue
            ruta_interficie = os.path.join(arrel, subcarpeta)
            codi = llegir_fitxer(os.path.join(ruta_interficie, "bInterfaceClass")).lower()
            nom_classe = CLASSES_USB.get(codi, "Desconeguda (" + codi + ")")
            if nom_classe not in classes:
                classes.append(nom_classe)
            enllac = os.path.join(ruta_interficie, "driver")
            if os.path.islink(enllac):
                nom_driver = os.path.basename(os.readlink(enllac))
                if nom_driver not in drivers:
                    drivers.append(nom_driver)
        nom = (fabricant + " " + producte).strip() or "Dispositiu " + identificador
        dispositius.append({
            "nom": nom,
            "connexio": "USB",
            "classe": " + ".join(classes),
            "driver": ", ".join(drivers),
            "estat": "",
        })
    return dispositius


def dispositius_linux():
    return dispositius_pci_linux() + dispositius_usb_linux()


# --- Windows ---

# Bus de connexió, segons com comença l'identificador (USB\..., PCI\...)
BUSOS_WINDOWS = {
    "USB": "USB",
    "HID": "HID (USB o Bluetooth)",
    "PCI": "PCI (intern)",
    "BTHENUM": "Bluetooth",
    "BTHLE": "Bluetooth",
    "BTHLEDEVICE": "Bluetooth",
    "DISPLAY": "Vídeo",
    "MONITOR": "Vídeo",
    "SCSI": "Emmagatzematge",
    "NVME": "Emmagatzematge",
    "STORAGE": "Emmagatzematge",
    "ACPI": "Placa base (ACPI)",
    "SWD": "Programari (virtual)",
    "ROOT": "Programari (virtual)",
}

# Els dispositius de l'Administrador de dispositius, amb proveïdor i versió del driver
ORDRE_POWERSHELL = r"""
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$drivers = @{}
Get-CimInstance Win32_PnPSignedDriver | ForEach-Object {
    if ($_.DeviceID) { $drivers[$_.DeviceID] = $_ }
}
Get-PnpDevice -PresentOnly | ForEach-Object {
    $d = $drivers[$_.InstanceId]
    [pscustomobject]@{
        Nom       = $_.FriendlyName
        Classe    = $_.Class
        Estat     = $_.Status
        Proveidor = $d.DriverProviderName
        Versio    = $d.DriverVersion
        Instancia = $_.InstanceId
    }
} | ConvertTo-Csv -NoTypeInformation
"""


def dispositius_windows():
    resultat = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ORDRE_POWERSHELL],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    linies = resultat.stdout.lstrip("﻿").splitlines()
    dispositius = []
    for fila in csv.DictReader(linies):
        if not fila.get("Nom"):
            continue
        driver = (fila.get("Proveidor") or "")
        if fila.get("Versio"):
            driver += " " + fila["Versio"]
        bus = (fila.get("Instancia") or "").split("\\")[0].upper()
        dispositius.append({
            "nom": fila["Nom"],
            "connexio": BUSOS_WINDOWS.get(bus, bus),
            "classe": fila.get("Classe") or "",
            "driver": driver.strip(),
            "estat": fila.get("Estat") or "",
        })
    return dispositius


# ===========================================================================
# FI DE LA ZONA NO CAL MODIFICAR
# ===========================================================================

def tipus_de(dispositiu):
    classe = dispositiu["classe"].split(" + ")[0]   # si en té diverses, la primera
    tipus = CLASSIFICACIO.get(classe, "sense classificar")
    if tipus == "TODO":
        return "sense classificar (TODO 2)"
    return tipus


def te_problema(dispositiu):
    # TODO 3: retorna True si el dispositiu té un problema.
    # Dades: dispositiu["estat"] (només a Windows) i dispositiu["driver"] ("" si no en té).
    if platform.system() == "Windows":
        if dispositiu['estat'] != 'OK':
            return True
    else: 
        if dispositiu["driver"] == "":
            return True


def main():
    sistema = platform.system()

    # TODO 1: el nom de cada sistema, tal com el retorna platform.system()
    if sistema == "Linux":
        dispositius = dispositius_linux()
    elif sistema == "Windows":
        dispositius = dispositius_windows()
    else:
        print("Sistema no reconegut:", sistema)
        return

    for d in dispositius:
        d["tipus"] = tipus_de(d)
        d["problema"] = "SÍ" if te_problema(d) else "no"

    columnes = ["nom", "connexio", "classe", "tipus", "driver", "estat", "problema"]
    with open(FITXER_SORTIDA, "w", newline="", encoding="utf-8-sig") as f:
        escriptor = csv.DictWriter(f, fieldnames=columnes, delimiter=";")
        escriptor.writeheader()
        # TODO 4: escriu cada dispositiu al fitxer amb escriptor.writerow(...)
        for d in dispositius:
            escriptor.writerow(d)
    # TODO 5: compta quants dispositius hi ha de cada tipus
    # (pista: recompte.get(tipus, 0) val 0 si aquell tipus encara no hi és)
    recompte = {}
    for d in dispositius:
        recompte[d["tipus"]] = recompte.get(d["tipus"], 0) + 1
    
    print(f"Sistema: {sistema}. Dispositius trobats: {len(dispositius)}")
    for tipus, quantitat in sorted(recompte.items()):
        print(f"  {tipus:<25} {quantitat}")
    problemes = [d["nom"] for d in dispositius if d["problema"] == "SÍ"]
    print(f"Dispositius amb possibles problemes: {len(problemes)}")
    for nom in problemes:
        print("  -", nom)
    print(f"Inventari desat a {FITXER_SORTIDA}")


if __name__ == "__main__":
    main()