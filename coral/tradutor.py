#!/usr/bin/env python
#-*- coding:utf-8 -*-

from  StringIO import StringIO
import tokenize
import yaml
from os import path, getcwd
import sys
from copy import deepcopy



class Tradutor(object):

    def __init__(self):
        self.dicionario = {'Falso': 'False',
 'Vazio': 'None',
 'Verdadeiro': 'True',
 'abrir': 'open',
 'ajuda': 'help',
 'algum': 'any',
 'anexar': 'append',
 'apague': 'del',
 'aplicar': 'apply',
 'arquivo': 'file',
 'arredondar': 'round',
 'atualizar': 'reload',
 'boliano': 'bool',
 'chamar': '__call__',
 'chamavel': 'callable',
 'chaves': 'keys',
 'classe': 'class',
 'com': 'with',
 'como': 'as',
 'como_chave': 'has_key',
 'conjunto': 'set',
 'contar': 'count',
 'de': 'from',
 'defina': 'def',
 'deletar': '__del__',
 'dicionario': 'dict',
 'e': 'and',
 'eh': 'is',
 'ehinstancia': 'isinstance',
 'ehsubclasse': 'issubclass',
 'elevar': 'pow',
 'em': 'in',
 'enquanto': 'while',
 'entrar': '__enter__',
 'enumerar': 'enumerate',
 'exceto': 'except',
 'exprecao': 'lambda',
 'extender': 'extend',
 'faixa': 'xrange',
 'fatiar': 'slice',
 'finalmente': 'finally',
 'formato': 'format',
 'funcao': 'def',
 'importe': 'import',
 'imprima': 'print',
 'imprimir': 'print',
 'indece': 'index',
 'iniciar': '__init__',
 'inserir': 'insert',
 'intervalo': 'xrange',
 'invertido': 'reversed',
 'itens': 'items',
 'iterar': 'iter',
 'iteritens': 'iteritems',
 'itervalores': 'itervalues',
 'l': 'lambda',
 'licensa': 'license',
 'lista': 'list',
 'methodoestatico': 'staticmethod',
 'metodo': 'def',
 'metodoDeClasse': 'classmethod',
 'na': 'in',
 'nao': 'not',
 'objeto': 'object',
 'ordenado': 'sorted',
 'ordenar': 'sort',
 'ou': 'or',
 'para': 'for',
 'passar': 'pass',
 'produza': 'yield',
 'propriedade': 'property',
 'provoque': 'raise',
 'proximo': 'next',
 'reduzir': 'reduce',
 'remover': 'remove',
 'retirar': 'pop',
 'retorne': 'return',
 'reverter': 'reverse',
 'romper': 'break',
 'sair': 'exit',
 'se': 'if',
 'senao': 'else',
 'senaose': 'elif',
 'somar': 'sum',
 'tamanho': 'len',
 'tente': 'try',
 'tipo': 'type',
 'todos': 'all',
 'tupla': 'tuple'}

        pastas = deepcopy(sys.path)
        pastas += [getcwd()]
        arquivos = [path.join(getcwd(), 'dicionario.yaml') for pasta in pastas]
        for arquivo in arquivos:
            if path.isfile(arquivo):
                with open(arquivo) as f:
                    self.dicionario.update(yaml.load(f.read()))

    def coralToPy(self, texto):
        codigo = StringIO(texto)
        return self.traduzir_linhas(codigo.readline)

    def traduzir_linhas(self, readline):
        result = []
        last_tokennum, last_tokenvalue = None, None

        for tokennum, value, _,_,_ in tokenize.generate_tokens(readline):
            if (tokennum == tokenize.NAME) and (value in self.dicionario.keys()):
                result.append((tokennum, self.dicionario.get(value)))
            elif tokenize.NAME == tokennum and last_tokenvalue == 'para' and value == 'cada':
                pass
            else:
                result.append([tokennum, value])
            last_tokennum, last_tokenvalue = tokennum, value
        return tokenize.untokenize(result)

    def pyToCoral(self, texto):
        self.dicionario = dict([ (v, k) for (k, v) in self.dicionario.items()])
        codigo = StringIO(texto)
        codigo_traduzido = self.traduzir_linhas(codigo.readline)
        self.dicionario = dict([ (v, k) for (k, v) in self.dicionario.items()])
        return codigo_traduzido





