#!/usr/bin/env python
#-*- coding:utf-8 -*-

from  StringIO import StringIO
import tokenize
import yaml
from os import path, getcwd
import sys
from copy import deepcopy
from ghelpers import folder


class Tradutor(object):

    def __init__(self):
        self.dicionario = {}
        pastas = deepcopy(sys.path)
        pastas += [folder(), getcwd()]
        arquivos = [path.join(pasta, 'dicionario.yaml') for pasta in pastas]
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





