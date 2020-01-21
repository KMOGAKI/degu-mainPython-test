import degu
import ujson
import time

if __name__ == '__main__':
    reported = {'state':{'reported':{}}}
    reported['state']['reported']['message'] = 'OK'

    while True:
        degu.update_shadow(ujson.dumps(reported))
        print("Hello! I'm Bob.")
        time.sleep(2)
