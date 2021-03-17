# stdlib
from typing import Union as TypeUnion
from typing import Any as TypeAny
import functools

# syft relative
from ..util import generic_update_ast
from ...ast import add_classes
from ...ast import add_methods
from ...ast import add_modules
from ...ast.globals import Globals


# The library name
LIB_NAME = "syfertext"

# Torch is a dependency for SyferText
PACKAGE_SUPPORT = {"lib": LIB_NAME, "torch": {"min_version": "1.4.0"}}

def create_ast(client: TypeAny = None) -> Globals:

    import syfertext
    from .tokenizers import spacy_tokenizer
    from .data.units import text_doc
    from .data.iterators import BPTTIterator
    from .data.metas import TextDatasetMeta
    
    ast = Globals(client = client)


    # Define which SyferText modules to add to the AST
    modules = ['syfertext',
               'syfertext.tokenizers',
               'syfertext.encoders',
               'syfertext.data',
               'syfertext.data.units',
               'syfertext.data.readers',
               'syfertext.data.iterators',
               'syfertext.data.metas',               
    ]

    # Define which SyferText classes to add to the AST    
    classes = [
        ('syfertext.tokenizers.SpacyTokenizer',
         'syfertext.tokenizers.SpacyTokenizer',
         syfertext.tokenizers.SpacyTokenizer
        ),
        ('syfertext.data.units.TextDoc',
         'syfertext.data.units.TextDoc',
         syfertext.data.units.TextDoc
        ),
        ('syfertext.data.units.TokenMeta',
         'syfertext.data.units.TokenMeta',
         syfertext.data.units.TokenMeta
        ),
        ('syfertext.data.iterators.BPTTIterator',
         'syfertext.data.iterators.BPTTIterator',
         syfertext.data.iterators.BPTTIterator
        ),
        ('syfertext.data.readers.TextReader',
         'syfertext.data.readers.TextReader',
         syfertext.data.readers.TextReader
        ),
        ('syfertext.encoders.SentenceEncoder',
         'syfertext.encoders.SentenceEncoder',
         syfertext.encoders.SentenceEncoder
        ),
        ('syfertext.data.metas.TextDatasetMeta',
         'syfertext.data.metas.TextDatasetMeta',
         syfertext.data.metas.TextDatasetMeta
        ),
        
    ]

    # Define which methods to add to the AST
    methods = [
        ('syfertext.tokenizers.SpacyTokenizer.__call__',
         'syfertext.data.units.TextDoc'
        ),
        ('syfertext.data.iterators.BPTTIterator.load',
         "syft.lib.python._SyNone"
        ),
        ('syfertext.data.iterators.BPTTIterator.__iter__',
         "syfertext.data.iterators.BPTTIterator"
        ),
        ('syfertext.data.iterators.BPTTIterator.__next__',
         "torch.Tensor"
        ),
        ('syfertext.data.iterators.BPTTIterator.yo',
         "torch.Tensor"
        ),
        
        
    ]


    add_modules(ast, modules)
    add_classes(ast, classes)
    add_methods(ast, methods)    
    
    
    for klass in ast.classes:
        
        klass.create_pointer_class()
        klass.create_send_method()
        klass.create_storable_object_attr_convenience_methods()
        
    return ast    


update_ast = functools.partial(generic_update_ast, LIB_NAME, create_ast)