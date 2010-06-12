#!/usr/bin/env python
#-*- coding:utf-8 -*-

from compiler.pycodegen import Module
from coral.tradutor import Tradutor
import os
import sys




class Comandos:
    """
    linha de comando para coral:
       * traduzir:
            - traduz aquivos de ingles par portugues e vice-versa de acordo com a extenção.
       * coral:
            - Compila para ".pyc" e executa aquivos ".coral"
    """

    coral = Tradutor()

    def __init__(self):

        self.nome_do_arquivo = sys.argv[1]
        self.local_de_execucao = os.getcwd()
        self.pasta_do_arquivo = os.path.join(self.local_de_execucao, os.path.dirname(self.nome_do_arquivo))
        sys.path = [self.pasta_do_arquivo, self.local_de_execucao] + sys.path
        self._iniciar_paths()

    def copilar(self):
        self._compilar()
        self._apagar_ou_sobescrever_arquivo_py()


    def executar(self):
        self.copilar()
        self._executar_pyc()

    def traduzir(self):
        if self._extencao() == '.coral':
            self._coral_para_py()
        if self._extencao() == '.py':
            self._py_para_coral()

    def _py_para_coral(self):
        codigo_coral = self.coral.pyToCoral(self._ler_arquivo())
        self._criar_arquivo(self.path_coral, codigo_coral)

    def _coral_para_py(self):
        codigo_py = self.coral.coralToPy(self._ler_arquivo())
        self._criar_arquivo(self.path_py, codigo_py)

    def _executar_pyc(self):
        os.system('python '+self.path_pyc)


    def _apagar_ou_sobescrever_arquivo_py(self):
        if os.path.isfile(self.path_py):
            if self._remover():#?
                os.remove(self.path_py)
            else:
                self._criar_arquivo(self.path_py, codigo_py)

    def _compilar(self):
        codigo_coral = self._ler_arquivo()
        codigo_py = self.coral.coralToPy(codigo_coral)
        codegen_modulo = Module(codigo_py, self.path)
        try:
            codegen_modulo.compile()
        except SyntaxError:
            raise
        else:
            with file(self.path_pyc, "wb") as f:
                codegen_modulo.dump(f)

    def _remover(self):#?
        return (raw_input("Existe um arquivo .py com o mesmo nome.\nDeseja apagalo?[s]    (Caso contrário, será sobrescrito)")
                in ["sim", "s", "y", "yes", "S", "","Y"])

    def _extencao(self):
        nome_do_arquivo , extencao = os.path.splitext(self.path)
        return extencao

    def _criar_arquivo(self, path, texto):
         with file(path, 'w') as f:
            f.write(texto)

    def _ler_arquivo(self, path=None):
        path = path or self.path
        f = open(path)
        texto = f.read()
        f.close()
        return texto

    def _iniciar_paths(self):
        self.path = path = os.path.join(self.local_de_execucao, self.nome_do_arquivo)
        self.path_py = path.replace('.coral','.py') if path.endswith('.coral') else path
        self.path_coral = path.replace('.py', '.coral') if path.endswith('.py') else path
        self.path_pyc = path.replace('.coral','.pyc') if path.endswith('.coral') else path + 'c'



comandos_coral = Comandos()
copilar = comandos_coral.copilar
executar = comandos_coral.executar
traduzir = comandos_coral.traduzir





