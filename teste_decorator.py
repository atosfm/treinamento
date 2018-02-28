param = {'nome': 'atos', 'email': 'atos@ciandt.com', 'idade': '99', 'celular': '99999-8888'}


def valida(**kwargs):
    if (kwargs.get('nome')):
        if (kwargs.get('email') and kwargs.get('email').find('@') != -1):
            if (kwargs.get('idade') and kwargs.get('idade').isdigit() and len(kwargs.get('idade')) <= 2):
                print kwargs.get('idade')
                if (kwargs.get('celular')):
                    celular = kwargs.get('celular').replace("-", "")
                    if (celular.isdigit() and len(celular) == 9):
                        print celular
                    else:
                        raise Exception('celular invalido')
                else:
                    raise Exception('celular invalido')

            else:
                raise Exception('idade invalida')
        else:
            raise Exception('email invalido')
    else:
        raise Exception('nome invalido')


def valida_form (func):
    def wrapper(*args,**kwargs):
        valida(**kwargs)
        return func(*args,**kwargs)
    return wrapper


@valida_form
def request(**kwargs):
    print(kwargs)


request(**param)
