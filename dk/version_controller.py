class VersionController:
    versions = {}

    @classmethod
    def register(cls, version_name):
        def decorator(func):
            cls.versions[(cls, version_name)] = func
            return func
        return decorator

    @classmethod
    def get(cls, version_name):
        if (cls, version_name) not in cls.versions:
            raise ValueError(f'Version {version_name} not found')
        else:
            return cls.versions.get((cls, version_name), None)
    
    @classmethod
    def get_version_info(cls, version_name):
        return cls.versions.get((cls, version_name), None).__doc__
    
    @classmethod
    def get_all_version_info(cls,):
        for k, v in cls.versions.items():
            print(f'Version: {k[1]}')
            print(f'Doc: {v.__doc__}')
            print('-----------------------------------')


@VersionController.register('v1')
def version_1():
    """This is version 1"""
    print('This is version 1')

@VersionController.register('v2')
def version_2():
    """This is version 2"""
    print('This is version 2')


if __name__ == '__main__':
    VersionController.get('v1')()
    VersionController.get('v2')()