import myTesla

my_model_s = myTesla.connect('replaceme@gmail.com', 'mySupersecretPassword')
charge_state = my_model_s.charge_state()
door_lock = my_model_s.door_lock()

print(charge_state)
print(door_lock)