import openfst.python as fst


def example():
    input_sym = fst.SymbolTable()
    output_sym = fst.SymbolTable()

    input_sym.add_symbol('<eps>')

    input_sym.add_symbol('a' ) # i n p u t symb ol s
    input_sym.add_symbol('b' )

    output_sym.add_symbol('c' ) # Output symbols
    output_sym.add_symbol('d' )

    f = fst.Fst()
    f.set_input_symbols(input_sym)
    f.set_output_symbols(output_sym)

    s0 = f.add_state()
    s1 = f.add_state()
    s2 = f.add_state()
    s3 = f.add_state()




