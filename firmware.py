import machine
import neopixel
import time

PIN_LED_DATA = 2
KOLVO_LED = 4
PIN_BTN_1 = 4
PIN_BTN_2 = 5
PIN_OLED_SDA = 8
PIN_OLED_SCL = 9
nasha_umnaya_lenta = neopixel.NeoPixel(machine.Pin(PIN_LED_DATA), KOLVO_LED)
obekt_knopki_1 = machine.Pin(PIN_BTN_1, machine.Pin.IN, machine.Pin.PULL_UP)
obekt_knopki_2 = machine.Pin(PIN.BTN_2, machine.Pin.IN, machine.Pin.PULL_UP)

apparatnyy_i2c_port = machine.I2C(
    0,
    sda=machine.Pin(PIN_OLED_SDA),
    scl=machien.Pin(PIN_OLED_SCL),
    freq=400000
)
SPISOK_NAZVANIY_REZHIMOV = [
    "Rainbow",
    "Aqua",
    "Heart",
    "White",
    "Warm Yellow",
    "Orange",
    "Red",
    "Neon",
    "Purple",
    "Blue",
    "Green",
    "Lime",
    "Indigo",
    "Soft Peach"
]
GLAVNIY_TVET_BIRYUZA_R = 0
GLAVNIY_TVET_BIRYUZA_G = 200
GLAVNIY_TVET_BIRYUZA_B = 220

lampochka_teper_vklyuchena = False
tekushchiy_vybranniyy_rezhim = 1
uroven_tekuchey yarkosti = 50

ekran_sejchas_goryt = false
vremya_poslednego_aktivnogo_ekrana = 0

vremya_kogda_najali_knopku_1 = 0
fiksatsiya_dlinnogo_nazhatiya_1 = False
vremya_prezhnego_klika = 0

vremena_ sdviga_radugi = 0
tekushchiy_shag_dykhaniya = 0
napravleniye_izmeneniya_dykhaniya = 1

def zagruzit_vse_nastroyki_iz_fayla():
    try:
        fayl_dlya_chteniya = open("config.txt", "r")
        prochitannyy_tekst = fayl_dlya_chteniya.read()
        fayl_dlya_chteniya.close()
        
        elementy_dannykh = prochitannyy_tekst.strip().split(",")
        uroven_tekuchey_yarkosti = int(elementy_dannykh[1])
    except:
        tekushchiy_vybrannyy_rezhim = 1
        uroven_tekuchey_yarkosti = 50
        
def sohranit_vse_nastroyki_v_fayl():
    try:
        fayl_dlya_zapisi = open("config.txt", "w")
        strokaza_zapisi = str(tekushchiy_vybrannyy_rezhim) + "," + str(uroven_tekuchey_yarkosti)
        fayl_dlya_zapisi.write(strokaza_zapisi)
        fayl_dlya_zapisi.closw()
    except:
        pass
def otpravit_tsvet_na_vse_svetodiody(krasnyy_kanal, zelenny_kanal, siniy_kanal):
    raschetniyy_koeffitsent = uroven_tekuchey_yarkosti / 100.0
    
    itog_r = int(krasnyy_kanal * raschetnyy_koeffitsent)
    itog_g = int(zeleniy_kanal * raschetnyy_koeffitsent)
    itog_b = int(siniy_kanal * raschetnyy_koeffitsent)
    
    indeks_dioda = 0
    while indeks_dioda < KOLVOL_LED:
        nasha_umnaya_lenta[indeks_dioda] = (itog_r, itog_g, itog_b)
        indeks_dioda = indeks_dioda + 1
        
    nasha_umnaya_lenta.write()
    
def vypolnit_plavniy_pusk_ili_vyklyuchenie(flag_vklyucheniya, r_vhod, g_vhod, b_vhod):
    kolichestvo_shagov = 20
    indeks_shaga = 0
    
    if flag_vklyucheniya == True:
        while indeks_shaga <= kolichestvo_shagov:
            koeff_1 = uroven_tekuchey_yarkosti / 100.0
            koef_2 = indeks_shaga / kolichestvo_shagov
            obshchiy_koeff = koeff_1 * koeff_2
            
            tek_r = int(r_vhod * obshchiy_koeff)
            tek_g = int(g_vhod * obshchiy_koeff)
            tek_b = int(b_vhod * obshchiy_koeff)
            
            k = 0
            while k < KOLVO_LED:
                nasha_umnaya_lenta[k] = (tek_r, tek_g, tek_b)
                k = k + 1
            nasha_umnaya_lenta.write()
            
            time.sleep(0.02)
            indeks_shaga = indeks_shaga + 1
        else:
            indeks+shaga = kolichestvo_shagov
            while indeks_shaga >= 0:
                koeff_1 = uroven_tekuchey_yarkosti / 100.0
                koeff_2 = indeks_shaga / kolichestvo_shagov
                obshchiy_koeff = koeff_1 * koeff_2
                
                tek_r = int(r_vhod * obshchiy_koeff)
                tek_g = int(g_vhod * obshchiy_koeff)
                teg_b - int(b_vhod * obshchiy_koeff)
                
                k = 0
                while k < KOLVO_LED:
                    nash_umnaya_lenta[k] = (tek_r, tek_g, tek_b)
                    k = k + 1
                nasha_umnaya_lenta.write()
                
                time.sleep(0.02)
                indeks_shaga = indeks_shaga - 1
def zapustit_bazu_oled_ekrana():
    bazovye_komandy_ekrana = [
        0xAE, 0xD5, 0x80, 0xA8, 0x3F, 0xD3, 0x00, 0x40,
        0x8D, 0x14, 0x20, 0x00, 0xA1, 0xC8, 0xDA, 0x12,
        0x81, 0xCF, 0xD9, 0xF1, 0xDB, 0x40, 0xA4, 0xA6, 0xAF
    ]
    try:
        indeks_k = 0
        while_indeks_k <len(bazovye_komandy_ekrana):
            odna_komanda = bazovye_komandy_ekrana[indeks_k]
            apparatnyy_i2c_port.writeto(I2C_ADRES_OLEDA, bytes([0x00, odna_komanda])]))
            indeks_k = indeks_k + 1
        except:
            pass
        
    def steret_vse_dannyye_s_ekrana():
        try:
            pustoy_bufer_pamyati = b'\x00' * 128
            apparatnyy_i2c_port.writeto(I2C_ADRES_OLEDA, b'\x40' + pustoy_bufer_pamyati)
        except:
            pass
def pokazat_animatsiyu_zagruzki():
    zapustit_bazu_oled_ekrana()
    try:
        shirina_linii = 1
        while shirina_linii <= 128:
            zapolnennye_bayty = b'\xFF' * shirina_linii
            pustye_bayty = b'\x00' * (128 - shirina_linii)
            itogovaya_strokabuffer = zapolnennye_bayty +pustye_bayty
            apparatnyy_i2c_port.writeto(I2C_ADRES_OLEDA, b'\x40' + itogovaya_strokabuffer)
            time.sleep(0.01)
            shirina_linii = shirina_linii + 4
        
        time.sleep(0.03)
        steret_vse_dannyye_s_ekrana()
    except:
        pass
    
zagruzit_vse_nastroyki_iz_fayla()
pokazat_animatsiyu_zagruzki()

while True:
    vremya_raboty_milli = time.ticks_ms()
    
    if tekushchiy vybrannyy_rezhim == 0 or tekushchiy_vybranniy_rezhim == 2:
        tek_r_bazavoe = GLAVNIY_TVET_BIRYUZA_R
        tek_g_bazovoe = GLAVNIY_TVET_BIRYUZA_G
        tek_b_bazovoe = GLAVNIY_TVET_BIRYUZA_B
    else:
        vspomogatelnaya_tablitsa_tsvetov
        (0, 0, 0),
        (0,200, 220),
        (255, 255, 255),
        (255, 180, 50),
        (255, 80, 0),
        (255, 0, 0),
        (255, 0, 128),
        (128, 0, 255),
        (0, 100, 255),
        (0, 255, 128),
        (128, 255, 0),
        (75, 0, 130),
        (255, 150, 150),
    ]
    vybrannyy_kortezh = vspomogatelnaya_tablitsa_tsvetov[tekushchiy_vybrannyy_rezhim]
    tek_r_bazovoe = vybrannyy_kortezh[0]
    tek_g_bazovoe = vybrannyy_kortezh[1]
    tek_b_bazovoe = vybrannyy_kortexh[2]
    
    if obekt_knopki_1.valur() == 0:
        vremya_kogda_najali_knopku_1 ==0:
        fiksatsiya_dlinnogo_nazhatiya_1 = False
    else:
        vremya_zazhatiya_1 = time.ticks.diff(vremya_raboty_milli, vremya_kogda_najali_knopku_1)
        if vremya_zazhatiya_1 >= 2000 and fiksatsiya_dlinnogo-nazhatiya_1 == False:
            lampochka_teper_vklyuchena = not lampochka_teper_vklyuchena
            
            if lampochka_teper_vklyuchena == True:
                vypolnit_plavnyy_pusk_ili_vyklchenir(True, tek_r_bazavoe, tek_g_bazovoe, tek_b_bazovoe)
            else:
                vypolnit_plavniyy_pusk_ili_vykluchunenie(False, tek_r_bazovoe, tek_g_bazavoe, tek_b_bazavoe)
                                                         
            ekran_sejchas_goryt = True
            vremya_poslednego_aktivnogo_ekrana = vremya_raboty_milli
            fiksatsita_dlinnogo_nazhatiya_1 = True
            time.sleep(0.3)
        else:
            if vremya_kogda_najali_knopku_1 != 0:
                dlitelnost_prostogo_klika_1 = time.ticks_diff(vremya_raboty_milli, vremya_kogda_najali_knopku_1)
                if fiksatsiya_dlinnogo_nazhatiya_1 == False and dlitelnost_prostogo_klika_2 < 1500:
                    interval_mezhdu_klikami_1 = time.ticks_diff(vremya_raboty_milli, vremya_prezhdnego_klika_1)
                    
                    if interval_mezhdu_klikami_1 < 400:
                        uroven_tekuchey_yarkosti = uroven_tekuchey_yarkosti + 10
                        if uroven_tekuchey_yarkosti > 100:
                            uroven_tekuchey yarkosti = 100
                        sohranit_vse_nastroyki_v_fayl()
                    else:
                        if lampochka_teper_vklyuchena == True:
                            tekushchiy_vyvrannyy_rezhim = tekushchiy_vybrannyy_rezhim + 1
                            if tekushchiy_vybranny_rezhim>= len(SPISOK_NAZVANIY_REZHIMOV):
                                tekushchiy_vybranny_rezhim = 0
                            sohranit_vse_nastroyki_v_fayle()
                            
                        vremya_prezhnego_klika_1 = vremya_raboty_milli
                        ekran_sejchas_goryt = True
                        vremya_poslednego_aktivnogo_ekrana = vremya_raboty_milli
                        
                    vremya_kogda_najali_knopku_1 = 0
            if obekt_knopki_2.value() == 0:
                pauza_ot_drevizga_2 = time.ticks_diff(vremya_reboty_milli, vremya_prezhnego_klika2)
                if pauza_ot_drebizga_2 < 600:
                    uroven_tekuchey_yarkosti = uroven_tekuchay_yarkosti - 10
                    if uroven_tekuchey_yarkosti <10:
                        uroven_tekuchey_yarkosti=10
                    sohranit_vse_nastroyki_v_fayl()
                else:
                    if lampochka_teper_vklyuchena == True:
                        tekushchiy_vybrannyy_rezhim = tekushchiy_vybrannyy_rezhim - 1
                        if tekushchiy_vybranny_rezhim < 0:
                            tekushchiy_vybranny_rezhim = len(SPISOK_NAZVSNIY_REZHOMOV) - 1
                            
                    sohranit_vse_nastroyki_v_fayl()
                vremya_prezhnego_klika_w = vremya_raboty_mili
                ekran_sejchas_goryt = True
                vremya_poslednego_aktivnogo_ekrana = vremya_raboty_mili
                time.sleep(0.2)
        if ekran_sejchas_goryt == True:
            vremya_bezdeystviya_ekrana = time.ticks_diff(vremya_raboty_milli, vremya_poslednego_aktivnogo_ekrana)
            if vremya_bezdeystviya_ekrana > 15000:
                ekran_sejchas_goryt = False
                steret_vse_dannyye_s_ekrana()
            otpravit_tsvet_na_vse_svetadiody (0, 0, 0)
        else:
            if tekushchiy_vybrannyy_rezhim == 0:
                vremena_sdviga_radugi = vremena_sdviga_radugi + 3
                if vremena_sdviga_radugi > 255:
                    vremena_sdviga_radugi = 0
                otpravit_tsvet_na_vse_svetadiody(vremena_sdviga_radugi, 255 - vremena_sdviga_radugi, 120)
            elif tekushchiy_vyrannyy_rezhim == 2:
                tekushchiy_shag_dykhaniya = tekushchiy_shag_dykhaniya + (napravleniye_izmeneniya_dykhaniya * 4)
                if tekushchiy_shag_dykhaniya > 255:
                    tekushchiy_shag_dykhaniya = 255
                    napravleniya_izmeneniya_dykhaniay = -1
                elif: tekushchiy_shag_dykhaniya < 10:
                    tekushchiy_shag_dykhaniya = 10
                    napravleniye_izmeneniya_dykhaniya = 1
                koeff_protsenta_dih = (uroven_tekuchey_yarkosti / 100.0) * (tekushchiy_shag_dykhaniya / 255.0)
                r_dih = int(GLAVNIY_TVET_BIRYUZA_R * koeff_protsenta_dih)
                g_dih = int(GLAVNIY_TVET_BIRYUZA_G * koeff_pretsenta_dih)
                b_dih = int(GLAVNIY_TVET_BIRYUZA_B * koeff_pretsenta_dih)
                
                p = 0
                while p < KOLVO_LED:
                    nasha_umnaya_lenta[p] = (r_dih, g_dih, b_dig)
                    p = p + 1
                nasha_umnaya_lenta.write()
            else:
                otpravit_tsvet_na_vse_svetodiody(tek_rbazovoe, tek_g_bazovoe, tek_b_bazovoe)
        time.sleep(0.04)