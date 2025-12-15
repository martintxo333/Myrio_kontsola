
# ==================================================================
# MyRIO-a UMEENTZAKO KONTSOLA BIHURTZEN DUEN PROGRAMA - Martin Maiz
# ==================================================================
"""
Programa honek NI myRIO gailua kontsola interaktibo bihurtzen du, bere azelerometroa eta
MXP-board-eko sentsoreak eta botoiak zuzenean erabiltzen dituzten minijoko batzuekin.
Azelerometroaren, RGB LED-aren, argi-sentsorearen, tenperatura-sentsorearen
eta botoi digitalen bidez, erabiltzaileak lau jarduera desberdin egin ditzake:

    1) LED bat itzali eta botoi bat ahalik eta azkarren sakatzean 
oinarritutako erreflexu-joko bat.
    2) Gelako argitasuna asmatzeko joko bat, non jokalariak benetako baliora 
hurbiltzen doan, pistak jasoz koloretako LEDen bidez.
    3) Gelako tenperatura asmatzeko jolasa, aurrekoaren antzekoa baina
sentsore termikoarekin.
    4) "Eskialariaren jokoa", joko elaboratuago bat non Myrioaren inklinazioa kontrolatzen
dan oztopoak gainditzeko, zailtasuna igoz ronda bakoitzean.

Programak puntuaketa-erregistroak kudeatzen ditu, sarrera-erroreak detektatzen ditu,
eta erantzun-denborak neurtzen ditu, errekorra ezarriz denbora hoberenari. 
Guztia funtzio desberdinetan antolatuta dago eta menu nagusi bat dauka, erabiltzaileari
jokoa erabakitzen ahalbidetzen diona eta nahi adina errepikatzen.

"""
#=======================================================================================================

import myrio_base as myRIO # KONTUZ! myRIO_base ere izan daiteke 
import time  
import random  

# MyRIO objetua hasieratu 
myrio1 = myRIO.MyRIO()  

# Aldagai globalak jolasen erregistroen jarraipena egiteko 
record_reflejoak = float('inf')  
record_argia = float('inf')  
record_tenperatura = float('inf')  
koloreak = ["red", "green", "blue", "white"] 

# LED-ak pizteko funtzioak: (mxp-board-tests.py) 

def turn_on_led(color):  

    if color == "red": 
        myrio1.write_MXP_RGB_LED(myRIO.RED)  

    elif color == "green":  
        myrio1.write_MXP_RGB_LED(myRIO.GREEN)  

    elif color == "blue":  
        myrio1.write_MXP_RGB_LED(myRIO.BLUE)  

    elif color == "white":  
        myrio1.write_MXP_RGB_LED(myRIO.WHITE) 

def turn_off_led():  
    myrio1.write_MXP_RGB_LED(myRIO.RGB_OFF)   

# ------------------- ERREFLEJU JOKOA -------------------  

def errefleju_jokoa():  

    global record_reflejoak  
    print("\nOngi etorri errefleju jokora!") 
    print("Sakatu botoia LED argia itzaltzen denean, ahalik eta azkarren")
    print("Ez egin tranparik! Denbora guztian botoia sakatuta mantentzen baduzu edo goizegi ematen badiozu, 2 segunduko penalizazioa izango duzu")    
    time.sleep(7) 

    while True:  
        itxarote_denbora = random.uniform(2, 5)  
        print("Kontzentratzen... Itxarote denbora: %.2f segundu." % itxarote_denbora)  
        time.sleep(itxarote_denbora)  

        aukeratutako_kolorea = random.choice(koloreak)

        print("\n GOAZEN!")  
        turn_on_led(aukeratutako_kolorea)

        time.sleep(random.uniform(1, 3))  

        turn_off_led()  
        print("\nLED-a ITZALI DA! KORRI!!")  

        hasi_denbora = time.time()  

        while True:  

            if myrio1.read_digital_input(3, port="A"):  

                amaierako_denbora = time.time()  
                zure_denbora = amaierako_denbora - hasi_denbora  

                print("Oso ondo! zure denbora da: %.4f segundu." % zure_denbora)  

                break  
 

            elif myrio1.read_digital_input(4, port="A"):  

                amaierako_denbora = time.time()  
                zure_denbora = amaierako_denbora - hasi_denbora  

                print("Oso ondo! zure denbora da: %.4f segundu." % zure_denbora)  

                break  

        if zure_denbora < 0.1:  

            print("Goizegi! Penalizazio bat duzu")  

            zure_denbora += 1.0  

        if zure_denbora < record_reflejoak:  

            record_reflejoak = zure_denbora  

            print("Record berria! %.4f segundu." % record_reflejoak)  

        else:  

            print("Zure denbora: %.4f. record-a: %.4f." % (zure_denbora, record_reflejoak))  

        
        berriro_jolastu = input("\nBerriro jolastu nahi? sakatu b (bai) edo e (ez): ")  

        
        if berriro_jolastu.lower() != 'b':  

            print("Eskerrik asko! Errefleju jokotik ateratzen...")  

            break  

# ------------------- ARGITASUNA ASMATZEKO JOKOA -------------------  

def argitasun_jokoa():  

    global record_argia  

    print("\nOngi etorri argitasuna asmatzeko jokora" ) 
    print("Saiatu asmatzen sentsoreak jasotzen duen argitasuna (ehunekotan)")
    print("Zenbaki txikiegia esaten baduzu, LED urdina piztuko da (ilunegi), zenbaki handiegia esaten baduzu aldiz, argi gorria (argiegi)")
    print("Argi berdea piztutzen bada, Zorionak! Argitasun egokia asmatu duzu")
    time.sleep(7)  

    while True:  
        hasi_denbora = time.time()  
        saiakera = -1  

        while True:  
            # Sentsoretik argitasuna irakurri (ehunekotan)
                          
            argia = myrio1.read_MXP_luminosity() 
            argia_osoa = int(argia)  

            print("Sentsoreak detektatzen duen argitasuna (jokalariari izkutatuta egongo da, baina nik programa egiterakoan zuzentzeko)", argia_osoa)  # Lerro hau komentatuko nuke programa definitiboan
            
            # Eskatu jokalariari bere saiakera:
            try:
                saiakera = int(input("Ze argitasun jasotzen duela uste dezu (0-100)? : "))  

            except ValueError:  
                print("Baliogabeko zenbakia. Sartu zenbaki oso bat 0 eta 100 artean")

                continue  

            if saiakera == argia_osoa:  

                amaierako_denbora = time.time()  
                zure_denbora = amaierako_denbora - hasi_denbora  

                print("Zorionak!!! Benetako argitasuna asmatu duzu. Zure denbora: %.4f segundu." % zure_denbora)  
                turn_on_led("green")  

                break  

            elif saiakera < argia_osoa: 

                print("Baxuegi! (Ilunegi)")  
                turn_on_led("blue")  

            else:

                print("Altuegi! (Argiegi)")  
                turn_on_led("red")  

            time.sleep(1)  
            turn_off_led()   

        if zure_denbora < record_argia: 

            record_argia = zure_denbora  
            print("Record berria! %.4f segundu." % record_argia)  

        else:  
            print("Zure denbora: %.4f. record-a: %.4f." % (zure_denbora, record_argia))  

        berriro_jolastu = input("\nBerriro jolastu nahi? sakatu b (bai) edo e (ez): ")  

        if berriro_jolastu.lower() != 'b': 
            print("Eskerrik asko! Argitasun jokotik ateratzen...")  

            break  

# ------------------- TENPERATURA ASMATZEKO JOKOA -------------------  

def tenperatura_jokoa():  
    
    global record_tenperatura  

    print("\nOngi etorri tenperatura asmatzeko jokora:")   
    print("Saiatu asmatzen sentsoreak jasotzen duen tenperatura")
    print("Zenbaki txikiegia esaten baduzu, LED urdina piztuko da (hotzegi), zenbaki handiegia esaten baduzu aldiz, argi gorria (beroegi)")
    print("Argi berdea piztutzen bada, Zorionak! Argitasun egokia asmatu duzu") 

    time.sleep(7)  

    while True:  

        hasi_denbora = time.time()  
        saiakera = -1  

        while True:  

            tenperatura_sentsorea_float = myrio1.read_MXP_temperature()  

            tenperatura = int(tenperatura_sentsorea_float) 

            print("Sentsoreak detektatzen duen tenperatura (jokalariari izkutatuta egongo da, baina nik programa egiterakoan zuzentzeko)", tenperatura)  # Lerro hau komentatuko nuke programa definitiboan 

            try:  
                saiakera = int(input("Enter your saiakera for temperature (C): "))  

            except ValueError:  
                print("Baliogabeko zenbakia. Sartu zenbaki oso bat")  

                continue  

            if abs(saiakera - tenperatura) < 0.5:  # hau float-ekin saiatu naizenean jarri dut, baina azkenean zenbaki osoekin egingo dut  

                amaierako_denbora = time.time()  
                zure_denbora = amaierako_denbora - hasi_denbora  

                print("Zorionak!!! Benetako tenperatura asmatu duzu. Zure denbora: %.4f segundu." % zure_denbora)  
                turn_on_led("green")  

                break  

            elif saiakera < tenperatura:  

                print("Baxuegi! (Hotzegi)")  
                turn_on_led("blue")  

            else:  

                print("Altuegi! (Beroegi)")  
                turn_on_led("red")  

            time.sleep(1)  
            turn_off_led()  

        if zure_denbora < record_tenperatura:  

            record_tenperatura = zure_denbora  
            print("Record berria! %.4f segundu." % record_tenperatura)  
 
        else:  
            print("Zure denbora: %.4f. record-a: %.4f." % (zure_denbora, record_tenperatura))   

        berriro_jolastu = input("\nBerriro jolastu nahi? sakatu b (bai) edo e (ez): ")  

        if berriro_jolastu.lower() != 'b':  
            print("Eskerrik asko! Tenperatura jokotik ateratzen...")  

            break 

def eskialariaren_jokoa(myrio1):

    import time
    import random

    UMBRAL = 0.5          # Mugimenduari sentsibilitatea (maximo ezkerra mxp pantailari begira jarriz 1g da eta maximo eskubi -1, beraz 0.5tik aurrera ya giratu dezula suposatuko da)
    hasierako_denb = 4    # Hasieran daukazun denbora mugimendua egiteko
    NIBEL_denb = 0.15     # Zenbat denbora kentzen da ronda bakoitzeko (geroz eta azkarrago doa)

    # ============================
    # JOLASA HASTEN DUEN FUNTZIOA
    # ============================
    def jokatu(introdukzioa):

        if introdukzioa: #instrukzioak bakarrik lehenengo aldian agertuko dira, geroago galdetzen zaizunean ea jolastu nahi dezun ta baiet ematerakoan, hau saltatuko du (introduzkioa=False)
            print("\n=== ESKIALARIAREN JOKOA ===")
            print("Hara hara! Eskiatzen zure lehenengo aldia da, baina nahigabe pista beltzean sartu zara. Inklinatu myrioa zuhaitzak eskibatzeko,")
            print("baina kontuz, aldapa jetsi ahala abaila hartzen zoaz eta geroz eta azkarrago zoazerantzun beharko dezu!!!")
            print("Inklinatu Myrioa eskatzen den aldera. Hasieran 4 segundu dituzu, baina asmatzen duzun ronda bakoitzeko denbora-muga hori jeisten jungo da.")
            print("✖: Aldez konfunditzen bazera eta beste aldera giratzen baduzu, zuhaitz baten aurka joko zara eta jokoa galduko duzu.")
            print("🤷‍♂️:Rondaz pasatzerakoan, myrioa OREKAN egon behar du, eskialari bat zuzen joan behar duen modura")
            print("\nOHARRA: BEHIN INKLINAZIOA EGINDA, BUELTATU MYRIOA OREKA PUNTURA, bestela rondaz pasatzean detektatuko dizu eskubian/ezkerrean zaudela eta eskatzen zaizuna kontrakoa bada, jokoa galduko duzu")
            print("\nKontuan izan nahiz eta erabaki ona hartu, ez zaizu norabide berria aterako ronda pasa arte, beraz itzuli ahalik eta azkarren hasierako posiziora")
            print("Rondaz pasatzerakoan, myrioa OREKAN egon behar du, eskialari bat zuzen joan behar duen modura")
            time.sleep(15)

        denb_max = hasierako_denb
        puntuak = 0

        try:
            while True:
                print("Zorte on!")
                norabidea = random.choice(["EZKERRERA", "ESKUBIRA"])
                print("\nnorabidea: " + norabidea)

                pasatako_denb = time.time()
                asmatu = False

            # ----------------------------------------------------
            # NAHIZ ETA ASMATU, RONDAKO DENBORA PASA ARTE, EZ DIZU NORABIDE BERRIA EMANGO ETA GEROZ ETA AZKARRAGO DOA
            # ----------------------------------------------------
                while True:

                    x, y, z = myrio1.read_analog_accelerometer()

                    # Inklinazio egokia detektatu: (ya ez badu asmatu)
                    if not asmatu:

                        # ACIERTO:
                        if norabidea == "EZKERRERA" and y > UMBRAL:
                            asmatu = True

                        elif norabidea == "ESKUBIRA" and y < -UMBRAL:
                            asmatu = True

                        # Konfunditzen bazara, jokoa amaitu da:
                        elif norabidea == "EZKERRERA" and y < -UMBRAL:
                            print("PLAS! Aldez konfunditu zara eta kriston zartakoa jo duzu!")
                            print("Amaierako puntuaketa: " + str(puntuak))
                            return puntuak

                        elif norabidea == "ESKUBIRA" and y > UMBRAL:
                            print("PLAS! Aldez konfunditu zara eta kriston zartakoa jo duzu!")
                            print("Amaierako puntuaketa: " + str(puntuak))
                            return puntuak

                    # Denbora amaitzerakoan ronda bukatu:
                    if time.time() - pasatako_denb >= denb_max:
                        break

                    time.sleep(0.05)

                # RONDA BUKATU DA: Puntuak kontatu
                if asmatu:
                    puntuak = puntuak + 1
                    print("Ondo! Puntuak: " + str(puntuak))

                    # Zailtasuna igo: denbora pixkat gutxiago dezu orain
                    denb_max = denb_max - NIBEL_denb
                    if denb_max < 1:
                        denb_max = 1

                    print("Denbora maximo berria: " + str(round(denb_max, 2)) + "s")

                else:
                    print("ZART! Ez zera garaiz mugitu eta zuhaitzaren aurka jo zara")
                    print("Amaierako puntuaketa: " + str(puntuak))
                    time.sleep(4)
                    return puntuak

        except KeyboardInterrupt:
            print("\nJokoa eskuz eten da")
            return puntuak


    # =============================================================================
    # BERRIRO JOLASTEKO BUKLEA (berriro instrukzio guztiak irakurri beharrik gabe)
    # =============================================================================

    while True:

        emaitza = jokatu(True)   # Lehenengo instrukzioekin

        print("\nJolasa amaitu da. Zure puntuazioa: " + str(emaitza))
        time.sleep(4)

        erantzuna = input("\nBerriro jolastu nahi? sakatu b (bai) edo e (ez):").strip().lower()

        if erantzuna != "b":
            print("Jolasetik irteten...")
            break

        print("\nBerriro hasiko da jokoa...")
        time.sleep(2)

        jokatu(False)  # Instrukzio gabe jokatu

# ------------------- MENU NAGUSIA -------------------  
def main_menu():  

    while True:
        print("\nOngi etorri MyRio kontsolara: 4 minijoko dituzu zure esku:")
        print("Jokatu, hobetu zure errekorra eta ondo pasa!")   
        print("\nAukeratu joko bat:")  
        print("1. Errefleju jokoa")  
        print("2. Argitasuna asmatzeko jokoa")  
        print("3. Tenperatura asmatzeko jokoa")  
        print("4. Eskialariaren jokoa")
        print("5. Atera")  

        choice = input("\nAukeratzeko idatzi zenbakia (1/2/3/4/5): ")  

        if choice == '1':  
            errefleju_jokoa()  

        elif choice == '2':  
            argitasun_jokoa()  

        elif choice == '3':  
            tenperatura_jokoa()
          
        elif choice == '4':  
            eskialariaren_jokoa(myrio1)

        elif choice == '5':  
            print("Programatik ateratzen")  

            break  

        else:  
            print("ERROR: Mesedez idatzi baliozko aukera bat: 1, 2, 3, 4 edo 5")  

 # KONTSOLA PIZTU: 
main_menu()  

 