#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
from pkg_resources import load_entry_point
from coral.tradutor import Tradutor
from IPython.iplib import InteractiveShell, ini_spaces_re
import __builtin__


def interact(self, banner=None):
    """Closely emulate the interactive Python console.

    The optional banner argument specify the banner to print
    before the first interaction; by default it prints a banner
    similar to the one printed by the real Python interpreter,
    followed by the current class name in parentheses (so as not
    to confuse this with the real interpreter -- since it's so
    close!).

    """
    
    if self.exit_now:
        # batch run -> do not interact
        return
    cprt = 'O Coral iterativo é baseado no IPython'

    self.write("Python %s no %s\n%s\n(%s)\n" %
                   (sys.version, sys.platform, cprt,
                    "icoral 1.0"))


    more = 0
    
    # Mark activity in the builtins
    __builtin__.__dict__['__IPYTHON__active'] += 1
    
    if self.has_readline:
        self.readline_startup_hook(self.pre_readline)
    # exit_now is set by a call to %Exit or %Quit, through the
    # ask_exit callback.
    
    while not self.exit_now:
        self.hooks.pre_prompt_hook()
        if more:
            try:
                prompt = self.hooks.generate_prompt(True)
            except:
                self.showtraceback()
            if self.autoindent:
                self.rl_do_indent = True
        else:
            try:
                prompt = self.hooks.generate_prompt(False)
            except:
                self.showtraceback()
        try:
            line = self.raw_input(prompt,more)
            if self.exit_now:
                # quick exit on sys.std[in|out] close
                break
            if self.autoindent:
                self.rl_do_indent = False
                
        except KeyboardInterrupt:
            #double-guard against keyboardinterrupts during kbdint handling
            try:
                self.write('\nKeyboardInterrupt\n')
                self.resetbuffer()
                # keep cache in sync with the prompt counter:
                self.outputcache.prompt_count -= 1

                if self.autoindent:
                    self.indent_current_nsp = 0
                more = 0
            except KeyboardInterrupt:
                pass
        except EOFError:
            if self.autoindent:
                self.rl_do_indent = False
                self.readline_startup_hook(None)
            self.write('\n')
            self.exit()
        except bdb.BdbQuit:
            warn('The Python debugger has exited with a BdbQuit exception.\n'
                 'Because of how pdb handles the stack, it is impossible\n'
                 'for IPython to properly format this particular exception.\n'
                 'IPython will resume normal operation.')
        except:
            # exceptions here are VERY RARE, but they can be triggered
            # asynchronously by signal handlers, for example.
            self.showtraceback()
        else:
            indent_match = ini_spaces_re.search(line)
            indent = indent_match.group() if indent_match else ''
            coral = Tradutor()
            more = self.push(indent+coral.coralToPy(line))
            if (self.SyntaxTB.last_syntax_error and
                self.rc.autoedit_syntax):
                self.edit_syntax_error()

setattr(InteractiveShell, 'interact', interact)


def icoral():
    sys.exit(
       load_entry_point('ipython', 'console_scripts', 'ipython')()
    )



