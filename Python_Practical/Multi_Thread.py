import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from io import StringIO
from threading import Thread, Event
from queue import Queue
import tarfile
import os


class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = "http://1231s212e%s.sz"
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print("Download", self.sid)
        data = self.download(self.url)
        self.queue.put((self.sid, data))


class ConvertThread(Thread):
    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

    def csv_to_xml(scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = list(map(lambda h: h.replace(' ', ''), headers))
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
            et = ElementTree(root)
            et.write()

    def run(self):
        count = 0
        while True:
            sid, data = self.queue.get()
            print("Convert", sid)
            if sid == -1:
                self.cEvent.set()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csv_to_xml(data, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0


class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tar_Xml(self):
        self.count += 1
        tfname = "%d.tgz" % self.count
        tf = tarfile.open(tfname, "w:gz")
        for fname in os.listdir("."):
            if fname.endswith(".xml"):
                tf.add(fname)
                os.remove(fname)
        tf.close()
        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()
            self.tar_Xml()
            self.cEvent.clear()
            self.tEvent.set()


if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i, q) for i in range(1, 11)]
    cEvent = Event()
    tEvent = Event()
    cThread = ConvertThread(q, cEvent, tEvent)
    tThread = TarThread(cEvent, tEvent)
    tThread.star()

    for t in dThreads:
        t.start()
    cThread.start()

    q.put((-1, None))
