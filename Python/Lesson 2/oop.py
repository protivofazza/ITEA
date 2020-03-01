class Phone:

    mobile_type = 'Common Phone'

    def __init__(self, model, imei):
        self._model = model
        self._imei = imei

    def call(self, to):
        self._connect_to_another_device(to)
        print(f'Okay, I am calling {to} from {self._model}')

    def _connect_to_another_device(self, to):
        print("Some connection magic...")

    def get_model(self):
        return self._model

    def set_model(self, value):
        self._model = value

    def get_imei(self):
        return self._imei

    def set_imei(self, value):
        self._imei = value


class Application:

    def __init__(self, name, marketplace):
        self._name = name
        self._marketplace = marketplace
        self._downloaded = False

    def start(self):
        if self._downloaded:
            print(f"Starting the {self._name} application")

    def download(self):
        print(f"Downloading {self._name} from the {self._marketplace}")
        self._downloaded = True


class MobilePhone(Phone):

    def send_message(self, message_text, to):
        print(f'Sending message "{message_text}" to {to}...')


class SmartPhone(MobilePhone):

    def play_audio(self):
        print("Playing audio")

    def play_video(self):
        print("Playing video")

    # Aggregation
    # Waiting for object type Application
    def start_application(self, application_object):
        application_object.start()


class SmartPhoneComposition(MobilePhone):
    def play_audio(self):
        print("Playing audio")

    def play_video(self):
        print("Playing video")

    def download_application(self, app_name, marketplace):
        app = Application(app_name, marketplace)
        app.download()
        self._app = app

    # Composition
    # Starting an app object that is already created
    def start_application(self, application_object):
        self._app.start()


class SatelitePhone(Phone):

    def call(self, satelite_coordinates, to):
        print(f'Calling to {to} from {self.get_model()} by satelite {satelite_coordinates}')


mobile_phone = MobilePhone('model', 'QEOQEWQ')
mobile_phone.send_message("SDF", "+380951236123")
print(mobile_phone.get_model())

satelite_phone = SatelitePhone('satelite model', '3473234')
satelite_phone.call('45.3/12.5', '+380962514351')

smartphone = SmartPhone('Apple', '77777777')
application = Application("player", "PlayMarket")
application.download()
smartphone.start_application(application)


class Cat:

    def __init__(self, name, weight = 3):
        self._name = name
        self._weight = weight

    def __len__(self):
        return 1

    def __add__(self, other):
        return Cat(self._name + other._name, self._weight + other._weight)


cat1 = Cat("Kitty", 3)
cat2 = Cat("Cat", 5)
cat3 = Cat("KOT", 6)

cat4 = cat1 + cat2 + cat3
print(cat4._name)