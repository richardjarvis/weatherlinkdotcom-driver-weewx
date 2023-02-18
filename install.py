from setup import ExtensionInstaller


def loader():
    return WLDCDriverInstaller()


class WLDCDriverInstaller(ExtensionInstaller):
    def __init__(self):
        super(WLDCDriverInstaller, self).__init__(
            version='0.1',
            name='WLDCDriver',
            description='Request both archive and live data from Weatherlink.com',
            author="richardjarvis",
            config={
                'WLDCDriver': {
                    'driver': 'user.WLDCDriver',
                    'max_tries': 10,
                    'retry_wait': 5,
                    'poll_interval': 10,
                    'realtime_enable': 0,
                    'hostname': 'change_me',
                    'time_out': 10,
                    'device_id': 'iss:1',
                    'wl_archive_enable': 0,
                },
                'Accumulator': {
                    'rainRate': {
                        'extractor': 'max'
                    }
                },
            },

            files=[('bin/user', ['bin/user/WLDCDriver.py'])]

        )