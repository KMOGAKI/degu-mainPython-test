import degu
import ujson
import time
import machine

if __name__ == '__main__':
    reported = {'state':{'reported':{}}}
    reported['state']['reported']['message'] = 'OK'

    while True:
        degu.update_shadow(ujson.dumps(reported))
        if (degu.check_update()):
            print("New script is comming! Restarting...")
            machine.reset();
        print("Hello! I'm Bob.")
        time.sleep(2)
