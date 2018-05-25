msg = 'Hi Milk'
print(msg.swapcase())
def is_stressful(subj):
    if subj.isupper() or subj.endswith('!!!'):

        print(True)
        return True
    else:
        print(False)
        return False

is_stressful(msg)