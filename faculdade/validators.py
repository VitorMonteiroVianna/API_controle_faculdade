from validate_docbr import CPF



def cpf_valido(cpf_num ):
    cpf = CPF()
    return cpf.validate(cpf_num)


def rg_valido(rg_num):
    return len(rg_num) == 9
