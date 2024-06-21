"""BREAK statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The break statement, like in C, breaks out of the innermost enclosing "for" or "while" loop.
"""


def test_break_statement():
    """BREAK statement"""

    loop1_number = 3
    loop2_number = 50
    
    check1 = 0
    check2 = 0
    
    for i in range(10):
    
        for j in range(100):
    	    if j == loop2_number:
    	        check2 = j
    	        break
	
        assert check2 == loop2_number

        if i == loop1_number:
            check1 = i
            break
    		
    assert check1 == loop1_number
    assert check2 == loop2_number
