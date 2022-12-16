https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
instruction_type = ['NULL','A_INSTRUCTION','C_INSTRUCTION','L_INSTRUCTION']

instruction_dest = ['NULL','M','D','MD','A','AM','AD','AMD']

instruction_jump = ['NULL','JGT','JEQ','JGE','JLT','JNE','JLE','JMP']

instruction_comp = ['NULL',
                    '0','1','-1',
                    'A','M','D',
                    '!A','!M','!D',
                    '-A','-M','-D',
                    'A+1','M+1','D+1',
                    'A-1','M-1','D-1',
                    'D+A','D+M',
                    'D-A','D-M','A-D','M-D',
                    'D&A','D&M',
                    'D|A','D|M']

class SymbolTable:

    def __init__(self):
        """
        Symbol table constructor
        """
        pass

    def addSymbol(self, symbol, value):
        """
        Adds a symbol to the symbol table

        @param symbol: The name of the symbol
        @param value: The address for the symbol
        """
        pass


    def getSymbol(self, symbol):
        """
        Gets a symbol from the symbol table
        
        @param symbol: The name of the symbol
        @return: The address for the symbol or -1 if the symbol isn't in the table
        """
        return -1


class Assembler:

    def doFirstPass(instructions, symbolTable):
        """
        Assembler first pass; populates symbol table with label locations.

        @param instructions: A list of the assembly language instructions.
        @param symbolTable: The symbol table to populate.
        """
        pass
    

    def generateMachineCode(instructions, symbolTable):
        """
        Translates a set of instructions to machine code.

        @param instructions: A list of the assembly language instructions to be converted to machine code.
        @param symbolTable: The symbol table to reference/update.
        @return: A String containing the generated machine code as strings of 16-bit binary instructions, 1-per-line.
        """
        return ""
       

    def parseInstructionType(instruction):
        """
        Parses the type of the provided instruction

        @param instruction: The assembly language representation of an instruction.
        @return: The type of the instruction (A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION, NULL)
        """
        return "NULL"
    

    def parseInstructionDest(instruction):
        """
        Parses the destination of the provided C-instruction

        @param instruction: The assembly language representation of a C-instruction.
        @return: The destination of the instruction (see instruction_dest) 
        """
        return "NULL"
    

    def parseInstructionJump(instruction):
        """
        Parses the jump condition of the provided C-instruction

        @param instruction: The assembly language representation of a C-instruction.
        @return: The jump condition for the instruction (see instruction_jump)
        """
        return "NULL"
    

    def parseInstructionComp(instruction):
        """
        Parses the computation/op-code of the provided C-instruction

        @param instruction: The assembly language representation of a C-instruction.
        @return: The computation/op-code of the instruction (see instruction_comp)
        """
        return "NULL"
    
    
    def parseSymbol(instruction):
        """
        Parses the symbol of the provided A/L-instruction

        @param instruction: The assembly language representation of a A/L-instruction.
        @return: A string containing either a label name (L-instruction), 
                a variable name (A-instruction), or a constant integer value (A-instruction)
        """
        return ""
    

    def translateDest(dest):
        """
        Generates the binary bits of the dest part of a C-instruction

        @param dest: The destination of the instruction
        @return: A String containing the 3 binary dest bits that correspond to the given dest value.
        """
        return "000"
    

    def translateJump(jump):
        """
        Generates the binary bits of the jump part of a C-instruction

        @param jump: The jump condition for the instruction
        @return: A String containing the 3 binary jump bits that correspond to the given jump value.
        """
        return "000"
    
    
    def translateComp(comp):
        """
        Generates the binary bits of the computation/op-code part of a C-instruction

        @param comp: The computation/op-code for the instruction
        @return: A String containing the 7 binary computation/op-code bits that correspond to the given comp value.
        """
        return "0000000"
    
    
    def translateSymbol(symbol, symbolTable):
        """
        Generates the binary bits for an A-instruction, parsing the value, or looking up the symbol name.

        @param symbol: A string containing either a label name, a variable name, or a constant integer value
        @param symbolTable: The symbol table for looking up label/variable names
        @return: A String containing the 15 binary bits that correspond to the given sybmol.
        """
        return "000000000000000"
    

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        instructions = []
        # Open file
        with open(sys.argv[1], "r") as a_file:
            # Read line-by-line, skip comments and empty line
            for line in a_file:
                if line[0] != '/' and line[0] != "\n":
                    instructions.append(line.strip())
        symbolTable = SymbolTable()
        # First pass
        Assembler.doFirstPass(instructions,symbolTable)
        # Second pass
        code = Assembler.generateMachineCode(instructions,symbolTable)
        # Print output
        print(code)
