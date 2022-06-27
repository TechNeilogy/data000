class Config:

    '''
    Configuration is encapsulated to clean up the code a little.
    '''

    __config = {
        'root_path': 'data/output',
        'common_files': [
            {
                'filename': 'df_1.csv'
            },
            {
                'filename': 'df_2.csv'
            },
            {
                'filename': 'df_4.csv'
            },
            {
                'filename': 'df_8.csv'
            },
            {
                'filename': 'df_16.csv'
            }
        ],
        'servers': [
            {
                'name': 'Server A',
                'path': 'a',
                'files': None
            },
            {
                'name': 'Server B',
                'path': 'b',
                'files': None
            },
            {
                'name': 'Server C',
                'path': 'c',
                'files': None
            },
            {
                'name': 'Server D',
                'path': 'd',
                'files': None
            }
        ]
    }

    @staticmethod
    def __config_normalize(
        config
    ):
        for server in config['servers']:
            if server['files'] is None:
                server['files'] = config['common_files']

    @staticmethod
    def get_config():

        '''
        Get the current configuration.
        '''

        Config.__config_normalize(
            Config.__config
        )

        return Config.__config
