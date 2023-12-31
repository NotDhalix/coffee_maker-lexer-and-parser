
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AT HIGH IN LOW MAKE_COFFEE MEDIUM NOW SEPARATOR SETUP SHOW START STOP TIME WARM_DEPOSIT\n    command : command SEPARATOR command\n            | routine\n            | empty\n    \n    routine : START instruction STOP\n            | START setuping STOP\n    \n    setuping : SETUP instruction\n             | SHOW SETUP\n    \n    instruction : MAKE_COFFEE time\n                | WARM_DEPOSIT temperature time\n    \n    time : NOW\n         | IN TIME\n         | AT TIME\n    \n    temperature : LOW\n                | MEDIUM\n                | HIGH\n    \n    empty : \n    '
    
_lr_action_items = {'START':([0,5,],[4,4,]),'SEPARATOR':([0,1,2,3,5,12,13,14,],[-16,5,-2,-3,-16,5,-4,-5,]),'$end':([0,1,2,3,5,12,13,14,],[-16,0,-2,-3,-16,-1,-4,-5,]),'MAKE_COFFEE':([4,10,],[8,8,]),'WARM_DEPOSIT':([4,10,],[9,9,]),'SETUP':([4,11,],[10,24,]),'SHOW':([4,],[11,]),'STOP':([6,7,15,16,23,24,25,26,27,],[13,14,-8,-10,-6,-7,-11,-12,-9,]),'NOW':([8,19,20,21,22,],[16,16,-13,-14,-15,]),'IN':([8,19,20,21,22,],[17,17,-13,-14,-15,]),'AT':([8,19,20,21,22,],[18,18,-13,-14,-15,]),'LOW':([9,],[20,]),'MEDIUM':([9,],[21,]),'HIGH':([9,],[22,]),'TIME':([17,18,],[25,26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'command':([0,5,],[1,12,]),'routine':([0,5,],[2,2,]),'empty':([0,5,],[3,3,]),'instruction':([4,10,],[6,23,]),'setuping':([4,],[7,]),'time':([8,19,],[15,27,]),'temperature':([9,],[19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> command","S'",1,None,None,None),
  ('command -> command SEPARATOR command','command',3,'p_command','coffee_maker.py',46),
  ('command -> routine','command',1,'p_command','coffee_maker.py',47),
  ('command -> empty','command',1,'p_command','coffee_maker.py',48),
  ('routine -> START instruction STOP','routine',3,'p_routine','coffee_maker.py',52),
  ('routine -> START setuping STOP','routine',3,'p_routine','coffee_maker.py',53),
  ('setuping -> SETUP instruction','setuping',2,'p_setuping','coffee_maker.py',58),
  ('setuping -> SHOW SETUP','setuping',2,'p_setuping','coffee_maker.py',59),
  ('instruction -> MAKE_COFFEE time','instruction',2,'p_instruction','coffee_maker.py',74),
  ('instruction -> WARM_DEPOSIT temperature time','instruction',3,'p_instruction','coffee_maker.py',75),
  ('time -> NOW','time',1,'p_time','coffee_maker.py',80),
  ('time -> IN TIME','time',2,'p_time','coffee_maker.py',81),
  ('time -> AT TIME','time',2,'p_time','coffee_maker.py',82),
  ('temperature -> LOW','temperature',1,'p_temperature','coffee_maker.py',99),
  ('temperature -> MEDIUM','temperature',1,'p_temperature','coffee_maker.py',100),
  ('temperature -> HIGH','temperature',1,'p_temperature','coffee_maker.py',101),
  ('empty -> <empty>','empty',0,'p_empty','coffee_maker.py',108),
]
