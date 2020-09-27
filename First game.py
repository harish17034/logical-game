print('This is my first python game')
name=input('enter your name')
age=input('enter your age')
print('hello',name,'you are',age,'years old' )
health=10


if int(age) >= 18:
    print('you are old enough to play!')
    wants_to_play=input('do you want to play? ').lower()
    if wants_to_play=='yes':

        print('you are starting wth', health, 'health')
        print('lets play!')

        left_or_right=input('first choce ..left/right?')
        if left_or_right=='left':
            ans=input('nice..you follow the path and reach the lake..do you swim across or go around..swim/go around?' )
            if ans=='around':
                print('you went around and reach other side of the lake')
            elif ans=='across':
                print('you manages to get across ,but bit by a fish and lose 5 health')
                health-=5
            ans=input('you notice a house and a river.which will you chose ..river/house?  ')
            if ans =='house':
                print('you chose house and greeted by the owner..you lose 5 health ')
                health -=5
                if health<=0:
                    print('you have 0 health and lost the game ')
                else:
                     print('you survived and won')
            else:
                print('you fell in the river and lost')
        else:
            print('you fell and lost')


    else:
        print('cya..')
else:
    print('you are not old enough to play!')