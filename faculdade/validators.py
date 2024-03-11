def cpf_valido(cpf_num ):
    qnt_nums = len(cpf_num) == 11
    only_nums = cpf_num.isalpha()

    validacao = {
        "qnt_nums" : qnt_nums,
        "only_nums": only_nums
    }

    return validacao


def rg_valido(rg_num):
    return len(rg_num) == 9
