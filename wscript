# -*- python -*-

# imports ---------------------------------------------------------------------
import os
import os.path as osp

import waflib.Logs as msg

# functions -------------------------------------------------------------------

def pkg_deps(ctx):
    return

def options(ctx):
    ctx.load('find_llvm')
    return

def configure(ctx):

    ctx.load('find_llvm')
    ctx.find_llvm()
    ctx.find_libclang()

    return

def build(ctx):
    ctx(
        features="cxx cxxprogram",
        name="clang-format",
        source=["ClangFormat.cpp",
                ],
        target="clang-format",
        #cxxflags = "-std=c++11",
        use="LLVM-static clang-static",
        )
    return

## EOF ##
    
