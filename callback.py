def callback(data):
    if(data.data == 'red_sign'):
        on_off = 1
        count = 0
    else :
        if(on_off == 1):
            if(count >= 5):
                on_off = Order[idx] # it must not be 1
                idx += 1
            else:
                count +=1
        else:
            pass