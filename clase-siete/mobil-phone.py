class MobilePhone:
    def __init__(self, manufacturer, screen_size, apps, num_cores, status = False ):
        self.manufacturer_mobilePhone = manufacturer
        self.screen_size_mobilePhone = screen_size
        self.num_cores_mobilePhone =  num_cores
        self.apps_mobilePhone = apps
        self.status = status
    
    def switch_on(self):
        print('Hello, Nihao, Hola, Hallo, Bonjour... Choose your language ')
        self.power_on = True

    def switch_off(self):
        print('Good bye')
        self.power_on = False

    def install_app(self, app):
        print('La app se ha instalado con éxito')
        self.install_app = app

    def uninstall_app(self, app):
        print('La app se ha desinstalado con éxito')
        self.uninstall_app = app


Iphone = MobilePhone('China', 6.06, 'Instagram', 6 )
print('\n--------------------------------\n',
      'Fabricado en: ', Iphone.manufacturer_mobilePhone,
      '\n--------------------------------\n',
      'Tamaño de la pantalla (inch):', Iphone.screen_size_mobilePhone,
      '\n--------------------------------\n',
      'Cantidad de núcleos: ', Iphone.num_cores_mobilePhone,
      '\n--------------------------------\n')

Iphone.switch_on()
print('Power on:', Iphone.power_on)
print('\n--------------------------------\n')
Iphone.install_app('Instagram')
print(Iphone.apps_mobilePhone)
print('\n--------------------------------\n')
Iphone.uninstall_app('Spotify')
print(Iphone.uninstall_app)
print('\n--------------------------------\n')
Iphone.switch_off()
print('Power on: ', Iphone.power_on)
print('\n--------------------------------\n')


