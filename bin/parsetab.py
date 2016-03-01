
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'CF9AAD546266EEE7D0B932B79D5944E3'
    
_lr_action_items = {'FUNCTION':([0,2,3,4,6,7,10,15,19,20,22,24,],[1,-6,1,-4,-7,-13,-5,1,1,1,-9,-8,]),'RPAREN':([11,13,14,21,],[12,16,-10,-11,]),'OPEN_BRACE':([12,16,],[15,20,]),'COMMA':([13,14,21,],[17,-10,-11,]),'LPAREN':([9,],[11,]),'CLOSE_BRACE':([2,4,6,7,10,18,19,22,23,24,],[-6,-4,-7,-13,-5,22,-12,-9,24,-8,]),'IDENTIFIER':([0,1,2,3,4,6,7,10,11,15,17,19,20,22,24,],[7,9,-6,7,-4,-7,-13,-5,14,7,21,7,7,-9,-8,]),'$end':([0,2,3,4,5,6,7,8,10,22,24,],[-1,-6,-2,-4,0,-7,-13,-3,-5,-9,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'functionBody':([15,20,],[18,23,]),'functionDeclaration':([0,3,15,19,20,],[2,2,2,2,2,]),'sourceElements':([0,15,20,],[3,19,19,]),'sourceElement':([0,3,15,19,20,],[4,10,4,10,4,]),'start':([0,],[5,]),'statement':([0,3,15,19,20,],[6,6,6,6,6,]),'formalParameterList':([11,],[13,]),'empty':([0,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',12),
  ('start -> sourceElements','start',1,'p_start','parser.py',16),
  ('start -> empty','start',1,'p_start','parser.py',17),
  ('sourceElements -> sourceElement','sourceElements',1,'p_sourceElements','parser.py',21),
  ('sourceElements -> sourceElements sourceElement','sourceElements',2,'p_sourceElements','parser.py',22),
  ('sourceElement -> functionDeclaration','sourceElement',1,'p_sourceElement','parser.py',26),
  ('sourceElement -> statement','sourceElement',1,'p_sourceElement','parser.py',27),
  ('functionDeclaration -> FUNCTION IDENTIFIER LPAREN formalParameterList RPAREN OPEN_BRACE functionBody CLOSE_BRACE','functionDeclaration',8,'p_functionDeclaration','parser.py',31),
  ('functionDeclaration -> FUNCTION IDENTIFIER LPAREN RPAREN OPEN_BRACE functionBody CLOSE_BRACE','functionDeclaration',7,'p_functionDeclaration','parser.py',32),
  ('formalParameterList -> IDENTIFIER','formalParameterList',1,'p_formalParameterList','parser.py',35),
  ('formalParameterList -> formalParameterList COMMA IDENTIFIER','formalParameterList',3,'p_formalParameterList','parser.py',36),
  ('functionBody -> sourceElements','functionBody',1,'p_functionBody','parser.py',39),
  ('statement -> IDENTIFIER','statement',1,'p_statement','parser.py',42),
]
