import threading

class ThreadTime(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.etat = True

    def run(self):
        self._running()

    def _running(self):
        print("TODO: TRAITEMENT DES ON/OFF EVENTS")
        print("SHOULD NOT BE A WHILE!")
        while self.etat:
            None

    def stop(self):
        etat =  False
