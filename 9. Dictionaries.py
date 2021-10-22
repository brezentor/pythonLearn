lehadobryi = {'ebalo': 'veseloe', 'nastroyenie': 'ahuennoe', 'zhytki': 100}
lehazloy = dict (ebalo = 'zloe', nastroyenie = 'huevoe', zhytki = 70)

mashyna = input('Mashyna uebalas? Skazhy da ili net')

if (mashyna == 'net'):
    print('lehadobryi:', lehadobryi)
    print('Zaebis')
elif (mashyna == 'da'):
    print('lehazloy:', lehazloy)
    print('Vipit` vodki ili doebatsya do musorov\n================================')
    vopros = input('Cho delat nahuy? Vodka ili dat` pizdu?')
    butylka = 0
    udar = 0
    if (vopros == 'vodka'):
        for l in range(3):
            butylka += 1
            lehazloy['zhytki'] += 10
            if (lehazloy['zhytki'] < 90):
                lehazloy['nastroyenie'] = 'huevoe'
                lehazloy['ebalo'] = 'zloe'
            elif (lehazloy['zhytki'] > 90):
                lehazloy['nastroyenie'] = 'zaebis'
                lehazloy['ebalo'] = 'norm'
            print('vypil', butylka, 'butylochku')
            print(lehazloy)
    elif (vopros == 'dat` pizdu'):
        for d in range(2):
            udar += 1
            lehazloy['zhytki'] -= 20
            if (lehazloy['zhytki'] < 40):
                lehazloy['nastroyenie'] = 'nema'
                lehazloy['ebalo'] = 'nema'
            print('poluchil', udar, 'raz po ebalu')
            print(lehazloy)
    else:
        print('dinahuy')
else:
    print('ne ebi mozgi chort')

