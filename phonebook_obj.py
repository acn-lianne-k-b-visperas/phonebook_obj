from sys import exit
import pickle
import os

class Contact(object):
    def __init__(self,name, home, work, cell):
        self.name = name
        self.home = home
        self.work = work
        self.cell = cell

    def __str__(self):
        return '{0}: work: {1}  home: {2}   cell: {3}'.format(self.name,self.home,self.work,self.cell)

    def __hash__(self):
        return hash((self.name))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.name == other.name

class Phonebook(object):
    def __init__(self,entries):
        self.entries = entries
        self.pickfile = 'phonebook_obj.pickle'

    def choose(self):

        print '\nElectronic Phone Book'
        print '====================='
        print '1. Look up an entry'
        print '2. Set an entry'
        print '3. Delete an entry'
        print '4. List all entries'
        print '5. Save entries'
        print '6. Clear ALL entries'
        print '7. Quit'

        choice = int(raw_input('Please choose an option (1-8): \n'))
        if choice not in range(1,8):
            print "Only enter 1-8!"
            self.choose()
        else:
            return choice

    def newContact(self):
        name = raw_input('Name: ')
        print 'Enter phone numbers: '
        print '(if none, leave blank and press enter)'
        work = raw_input('work: ')
        home = raw_input('home: ')
        cell = raw_input('cell: ')
        c = Contact(name,work,home,cell)
        try:
            c = Contact(name,work,home,cell)
            return c
        except:
            self.newContact()

    def findContact(self):
        name = raw_input('Name: ')
        c = None
        for entry in self.entries:
            if entry.name == name:
                c = entry
        return c

    def lookUpEntry(self,contact):
        if contact in self.entries:
            print'\nFound entry for ' + str(contact)
        else:
            print 'That person is not in the phonebook!'

    def setEntry(self,contact):
        if contact not in self.entries:
            self.entries.add(contact)
            print 'Entry stored for ' + str(contact)
        else:
            print 'Invalid entry - try again'

    def deleteEntry(self,contact):
        try:
            self.entries.discard(contact)
            print 'Delted entry for ' + str(contact)
        except:
            print 'That person is not in the phonebook'

    def listEntries(self):
        if len(self.entries) == 0:
            print 'No entries yet!'
        else:
            for entry in self.entries:
                print 'Found entry for ' + str(entry)

    def saveEntries(self):
        f = open(self.pickfile, 'w')
        pickle.dump(self.entries, f)
        f.close
        print 'Entries Saved!'

    def clearEntries(self):
        os.remove(self.picklefile)

    def quitPhonebook(self):
        q = raw_input('Are you sure you want to quit? (y/n) ')
        if q == 'y' or q == 'n':
            f = open(self.pickfile, 'w')
            pickle.dump(self.entries, f)
            f.close
            print 'Entries Saved! - GOODBYE\n'
            exit(0)
        elif q =='n':
            self.choose()
        else:
            print "Only enter 'y' or 'n'!"
            self.quitPhonebook()

def openPhonebook():

    f = open('phonebook_obj.pickle', 'r')
    pb = pickle.load(f)
    p = Phonebook(pb)

    while True:
        choice = p.choose()
        if choice == 1:
            c = p.findContact()
            p.lookUpEntry(c)
        elif choice == 2:
            c = p.newContact()
            p.setEntry(c)
        elif choice == 3:
            c = p.findContact()
            p.deleteEntry(c)
        elif choice == 4:
            p.listEntries()
        elif choice == 5:
            p. saveEntries()
        elif choice == 6:
            p.clearEntries()
        else:
            p.quitPhonebook()

openPhonebook()
