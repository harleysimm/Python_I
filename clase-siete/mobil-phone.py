class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores =  num_cores
        self.apps = []
        self.status = False
    
    def switch_on(self):
        print('Hello, Nihao, Hola, Hallo, Bonjour... Choose your language ')
        self.status = True

    def switch_off(self):
        print('Good bye')
        self.status = False

    def install_app(self, app):
        print('La app se ha instalado con éxito')
        self.apps= app

    def uninstall_app(self, app):
        print('La app se ha desinstalado con éxito')
        self.apps = app


Iphone = MobilePhone('China', 6.06, 6 )
print('\n--------------------------------\n',
      'Fabricado en: ', Iphone.manufacturer,
      '\n--------------------------------\n',
      'Tamaño de la pantalla (inch):', Iphone.screen_size,
      '\n--------------------------------\n',
      'Cantidad de núcleos: ', Iphone.num_cores,
      '\n--------------------------------\n')

Iphone.switch_on()
print('Power on:', Iphone.status)
print('\n--------------------------------\n')
Iphone.install_app('Instagram')
print(Iphone.apps)
print('\n--------------------------------\n')
Iphone.uninstall_app('Spotify')
print(Iphone.apps)
print('\n--------------------------------\n')
Iphone.switch_off()
print('Power on: ', Iphone.status)
print('\n--------------------------------\n')


