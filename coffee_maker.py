import ply.lex as lex
import ply.yacc as yacc
import datetime as dt

tokens = [
    'START',
    'MAKE_COFFEE',
    'NOW',
    'STOP',
    'SETUP',
    'IN',
    'AT',
    'TIME',
    'SHOW',
    'SEPARATOR',
    'LOW',
    'MEDIUM',
    'HIGH',
    'WARM_DEPOSIT'
]

t_START = r'START'
t_MAKE_COFFEE = r'MAKE_COFFEE'
t_NOW = r'NOW'
t_STOP = r'STOP'
t_SETUP = r'SETUP'
t_IN = r'IN'
t_AT = r'AT'
t_LOW = r'LOW'
t_MEDIUM = r'MEDIUM'
t_HIGH = r'HIGH'
t_SHOW = r'SHOW'
t_WARM_DEPOSIT = r'WARM_DEPOSIT'
t_TIME = r'\d{2}:\d{2}'
t_SEPARATOR = r';'

t_ignore = ' '

mc_saved_time=[]
wd_saved_time=[]

def t_error(t):
    print("UNKNOW COMMAND:", t.value)
    t.lexer.skip(len(t.value))

lexer = lex.lex()

def p_command(p):
    '''
    command : command SEPARATOR command
            | routine
            | empty
    '''
def p_routine(p):
    '''
    routine : START instruction STOP
            | START setuping STOP
    '''

def p_setuping(p):
    '''
    setuping : SETUP instruction
             | SHOW SETUP
    '''
    global mc_saved_time
    global wd_saved_time
    if p[1] == 'SHOW':
        if mc_saved_time:
            print('MAKE COFFEE ROUTINE(S) SAVED:', )
            for i in mc_saved_time:
                print('\tMAKE COFFEE EVERYDAY AT', i)
            print('-'*50)
        else:
            print('NO MAKING COFFEE ROUTINES YET')
            print('-'*50)
        if wd_saved_time: 
            print('WARM DEPOSIT ROUTINE(S) SAVED:')   
            for j in wd_saved_time:
                print('\tWARM DEPOSIT EVERYDAY AT', j)
        else:
            print('NO WARMING DEPOSIT ROUTINES YET')


def p_instruction(p):
    '''
    instruction : MAKE_COFFEE time
                | WARM_DEPOSIT temperature time
    '''

def getCurrentTime():
    return dt.datetime.now().strftime('%H:%M')

def addHours(currentTime, hours, minutes):
    current_datetime = dt.datetime.strptime(currentTime, '%H:%M')
    new_datetime = current_datetime + dt.timedelta(hours=hours, minutes=minutes)
    return new_datetime.strftime('%H:%M')

def p_time(p):
    '''
    time : NOW
         | IN TIME
         | AT TIME
    '''
    global mc_saved_time 
    global wd_saved_time
    global temp
    if p[-1]=='MAKE_COFFEE':
        if p[-2]=='SETUP' and p[1]=='NOW':
            mc_saved_time.append(getCurrentTime())
            print('NEW ROUTINE ADDED: MAKING COFFEE AT', getCurrentTime())
        elif p[-2]=='SETUP' and p[1]=='IN':
            hours, minutes = map(int, p[2].split(':'))
            mc_saved_time.append(addHours(getCurrentTime(), hours, minutes))
            print('NEW ROUTINE ADDED: MAKING COFFEE AT', addHours(getCurrentTime(), hours, minutes))
        elif p[-2]=='SETUP' and p[1]!='NOW':
            mc_saved_time.append(p[2])
            print('NEW ROUTINE ADDED: MAKING COFFEE', p[1], p[2])
        elif p[1]=='NOW':
            print('MAKING COFFEE NOW')
        else:
            print('MAKING COFFEE', p[1], p[2])
            
    if p[-2]=='WARM_DEPOSIT':
        if p[-3]=='SETUP' and p[1]=='NOW':
            wd_saved_time.append(getCurrentTime() + ', TEMPERATURE: ' + temp)
            print('NEW ROUTINE ADDED: WARM DEPOSIT AT', getCurrentTime() + ', TEMPERATURE:', temp)
        elif p[-3]=='SETUP' and p[1]=='IN':
            hours, minutes = map(int, p[2].split(':'))
            wd_saved_time.append(addHours(getCurrentTime(), hours, minutes) + ', TEMPERATURE: ' + temp)
            print('NEW ROUTINE ADDED: WARM DEPOSIT AT', addHours(getCurrentTime(), hours, minutes) +  ', TEMPERATURE:', temp)
        elif p[-3]=='SETUP' and p[1]!='NOW':
            wd_saved_time.append(getCurrentTime() + ', TEMPERATURE: ' + temp)
            print('NEW ROUTINE ADDED: WARM DEPOSIT', p[1], p[2], 'AT', temp)
        elif p[1]=='NOW':
            print('WARMING DEPOSIT NOW AT', temp)
        else:
            print('WARMING DEPOSIT', p[1], p[2], 'AT', temp)

temp=''

def p_temperature(p):
    '''
    temperature : LOW
                | MEDIUM
                | HIGH
    '''
    global temp
    temp=p[1]

def p_error(p):
    if p:
        print(f'SYNTAX ERROR FOUND AT LINE {p.lineno}, POSITION {p.lexpos}: UNEXPECTED TOKEN {p.type}({p.value})')
    else:
        print('SYNTAX ERROR FOUND: INCOMPLETE COMMAND')

def p_empty(p):
    '''
    empty : 
    '''
    pass

parser = yacc.yacc()

print('TYPE "EXIT" TO EXIT THE PROGRAM.')
while True:
    try:
        s = (input('->')).upper()
        if s=='EXIT':
            break
    except EOFError:
        break
    parser.parse(s)

