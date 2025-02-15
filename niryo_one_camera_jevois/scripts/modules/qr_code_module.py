from modules.jevois_module import JevoisModule


class QRCodeModule(JevoisModule):

    def __init__(self, name):
        super(QRCodeModule, self).__init__(
            name=name, fps=30, should_start_guvcview=False)

    def get_params(self):
        return ['streamoff',
                'setpar serlog USB',
                'setmapping2 YUYV 320 240 30 Jevois DemoQRcode',
                'setpar serstyle Detail',
                'setpar serout USB',
                'streamon']
