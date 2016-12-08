# py2dart
Since many programmers and web developers will find that it is easier to use the easy syntax features on python and the robustness of javascript and/or dart for web development, a suitable method would require a translator which converts python code written by the developer to Dart(https://www.dartlang.org/), which can be directly used in its varied options, or converted to Javascript using dart2js plugin.


#Implementation

My version of the python to dart translator is called Py2D.A.R.T, and here are the features included in it.

• It can convert individual commands and function definitions from python to DART.

• The list of commands which are applicable to be converted has been shown in the next section.

• The user can either specify a .py file which gets converted into a .dart file with the translated code in it, or additionally specify one by one the different commands which he/she wants to translate into an equivalent DART code.

• This model is still in β stage, and some features may also be added later on.


#Guidelines on Usage

1. Type the command on the shell after the >>> mark, and it is assumed that the syntax is proper.

2. If a command is of multiple lines, then keep typing the lines one by one and end it with a ”—” sign

Eg: The ""for"" loop in python.

a) Type ""- for i in range(5):""

 Now the translator will find out that this will span for multiple lines
\# and keep accepting the inputs each in a seperate line, until a new line
\# with only ’$’ sign is present.

3. It is better to avoid nesting of loops and conditional statements since this tool is still in the beta stage, even though the working of these is done, but a successful output is not guaranteed.

4. Only one command or one block is allowed at a time.

5. Type ’help’,’developer details’ or ’exit’ anytime the prompt arrives.

#Usage Constraints

There are some usage constraints also in this particular translator, whcih will removed as newer features get added as a part of the future work.

1. Only those types of for loops are allowed where it is of the form, for <variable> in range((min),(max)):
where (max) is necessary, while (min), which is optional, by default is 0. Other forms of for loops are not allowed.


2. The variables and function names are to be represented in regular form
or Hungarian notation,

In regular form without Hungarian notation , the type of the variable is assumed to be ’var’(generic) .

In hungarian notation,
–’n’ means int, –’c’ means char, –’d’ means double, –’s’ means string


3. ’If’ conditions are not designed to have an else, since it is in beta stage.


4. Only these commands are allowed,

• ’If’,

• ’while’,

• ’for’,

• ’def’,

• ’print’,’mathematical expressions’


5. Every variable gets declared automatically in the default type, based on the name of the variable


6. These are default types, and if the translator couldn’t learn and identify which type of the variable it is, it declares as ’var’ generic type

#Principle of Translation

The following steps take place in  Py2DART translator which converts a source code or a source command in python to an equivalent code in DART( listed in the file translation_principle.PNG)

Here are the steps involved in the processing of the python code, which gets converted into dart code. The steps involved in the form of a cycle are,


1. Tokenizing: This is the step where the tokens are being identified in the input sentence or the input code line.It also identifies if the whether based on a block or single line

• For block it uses recursion, or re-enterant code


2. Segmentation: This splits the tokenized command to segments, which individually get translated, and this can enable a form of parallel trans- lations and hence speedup the process of translation.


3. Segment translation: This step involves translation of individual segments from Python to Dart


4. Segment Reassembly: Gets code in DART by joining the segments translated and obtained above.


These steps happen repeatedly one after the other especially in the case of a file supplied via the input in the form of a python file in the extension ”.py”

This cycle keeps on repeating until the exit command has been encountered. 

Further, since the code in python is based on indentation, the end of the blocks has been identified by the $ symbol for every block.

However one problem may be thought of, that is the inconsistency in the types between the python and the DART code, and this can be resolved by the use of Hungarian notation, as specified in the sub section on the guidelines.

#Future-work

A prospective future work may involve improvisation of the Py2D.A.R.T implementation, primarily on increasing the range of keywords and functions accepted by the tool. 

Further, this tool can be made more machine learning and language technologies oriented so that it learns as we go, to convert programming languages to python. 

Additionally, this tool can also be made more extensive to make it accept more programming language codes like Java, HasKell, Ruby on Rails, C, C++, apart from python which it already is using.
