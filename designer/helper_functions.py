def get_indent_str(indentation):
    i = 0
    s = ''
    while i < indentation:
        s += ' '
        i += 1
    
    return s

def get_line_end_pos(string, line):
    _line = 0
    _line_pos = -1
    _line_pos = string.find('\n', _line_pos + 1)
    while _line < line:
        _line_pos = string.find('\n', _line_pos + 1)
        _line += 1
    
    return _line_pos

def get_line_start_pos(string, line):
    _line = 0
    _line_pos = -1
    _line_pos = string.find('\n', _line_pos + 1)
    while _line < line - 1:
        _line_pos = string.find('\n', _line_pos + 1)
        _line += 1
    
    return _line_pos

def get_indent_level(string):
    lines = string.splitlines()
    lineno = 0
    line = lines[lineno]
    indent = 0
    total_lines = len(lines)
    while line < total_lines and indent == 0:
        indent = len(line)-len(line.lstrip())
        line = lines[lineno]
        line += 1
    
    return indent

def get_indentation(string):
    count = 0
    for s in string:
        if s == ' ':
            count+=1
        else:
            return count
    
    return count
    