repeat = 'yes'

while(repeat =='yes'):
    shift_number = ''
    user_input = input('Type "encode" to encrypt, "decode" to decrypt: \n').lower()
    
    if((user_input != 'encode') and (user_input !='decode')):
         print('Invalid input')
         continue
    
    message = input('Type your message: \n').lower()
    while(shift_number.isnumeric() == False):
        shift_number = (input('Type the shift number: \n'))
        if(shift_number.isnumeric() == False):
            print('Invalid input. Please enter a number.')
    shift_number = int(shift_number)    
    
    while(shift_number > 26):
        shift_number = shift_number - 26
    
    if(user_input == 'encode'):
        caeser_cipher = [chr(ord(letter) + shift_number) if ((ord(letter) + shift_number) < 123) else (chr(ord(letter) + shift_number - 26)) for letter in message ]
        print('Here\'s the encoded result: ' + "".join(caeser_cipher))
    else:
        caeser_cipher = [chr(ord(letter) - shift_number) if ((ord(letter) - shift_number) > 96) else(chr(ord(letter) - shift_number + 26)) for letter in message]
        print('Here\'s the decoded result: '+ "".join(caeser_cipher))
    
    repeat = input('Type "yes" if you want to go again. Otherwise type "no"\n')
    
       

