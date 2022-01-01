import time;
from threading import Timer;

def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'));

def run_once():
    display('Start: ');
    t = Timer(5, display, ['Finished:']);
    t.start();

run_once();
print('Waiting...');        

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs);
        print('Done!');

timer = RepeatTimer(1, display, ['Repeating: ']);
timer.start();
print('Threading Started...');
# time.sleep(10);
print('Threading Waiting...');

timer.cancel();            
