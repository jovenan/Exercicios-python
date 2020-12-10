def vogal(letra):
    vogais = "aeiou"
    if letra.lower() not in vogais: # verificar se a letra digitada minuscula nao existe na nossa variavel vogais
        return False
    return True