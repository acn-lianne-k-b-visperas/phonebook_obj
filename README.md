#Command Line Phonebook App

##Summary:
This project is a phonebook app used from the command line that allows a user to save, lookup, and delete phonebook entires.  The entries consist of a name key connected to 3 different phone numbers (work, home, and cell)

There are two files included in this project: phonebook_obj.py and phonebook.py.  This project was programmed twice, once using object classes for the phonebook and contacts and once without.  Both files run an app that functions in the same way.

This project was completed as part of the Python curriculum for Digital Crafts

##Github Link
[Phonebook Apps](https://github.com/jesslynlandgren/phonebook_obj)

##What was used:
* Python 2.7.12 (Including the following modules):
  - sys
  - pickle
  - os

##Requirements:
* Python 2 or Python 3

##Goals:
* User interacts with the phonebook by selecting an option from a list
* The following basic options should be supported:
  * Look up an entry
  * Set an entry
  * Delete an entry
  * List all entries
  * Save entries
  * Clear ALL entries
  * Exit the phonebook
* User receives feedback on the success or failure of their chosen option
* Three different phone numbers can be stored for each contact (home, work, cell), but not all 3 are required
* Entries must be unique
* App continues to function if the user selects operations in a non-typical order (e.g. tries to look up an entry from an empty phonebook, tries to delete an entry that doesn't exist)
* Support the saving of the phonebook entries so that the user can close or exit the script and the saved entries will be available the next time the program is run.

##Code Snippets (Non-OOP version)
The user input choice list and corresponding code is very similar for both versions.  The choice list is printed out, the user is prompted for their choice, and a function or method is called depending on the number entered.
```Python
#Prompts user with option list and calls function based on choice
def phonebook(dic):
    print '\nElectronic Phone Book'
    print '====================='
    print '1. Look up an entry'
    print '2. Set an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Save entries'
    print '6. Clear ALL entries'
    print '7. Quit'

    choice = choose()

    if choice == 1:
        lookUpEntry(dic)
    elif choice == 2:
        setEntry(dic)
    elif choice == 3:
        deleteEntry(dic)
    elif choice == 4:
        listEntries(dic)
    elif choice == 5:
        saveEntries(dic)
    elif choice == 6:
        clearEntries()
    else:
        return dic
        quitPhonebook()
    return dic
```
For the Non-OOP version, the phonebook entries are stored in a dictionary and requests for entries and entry actions are made using functions that take the dictionary as a parameter.
```Python
def setEntry(dic):
    name = raw_input('Name: ')
    print 'Enter phone numbers: '
    print '(if none, press enter)'
    work = raw_input('work: ')
    home = raw_input('home: ')
    cell = raw_input('cell: ')
    try:
        numDict = {'work': work, 'home': home, 'cell': cell}
        dic[name] = numDict
        print 'Entry stored for {0}: work: {1}  home: {2}  cell: {3}'.format(name, numDict['work'], numDict['home'], numDict['cell'])
        phonebook(dic)
    except:
        print 'Invalid entry! - try again'
        out = False
        while not out:
            out = goBack()
            if not out:
                setEntry(dic)
            else:
                break
        phonebook(dic)

def deleteEntry(dic):
    name = raw_input('Name: ')
    try:
        del dic[name]
        print 'Deleted entry for {0}\n'.format(name)
        phonebook(dic)
    except:
        print 'That person is not in the phonebook!'
        out = False
        while not out:
            out = goBack()
            if not out:
                lookUpEntry(dic)
            else:
                break
        phonebook(dic)
```
The entries persist from run to run of the app by using the pickle module for python and storing the current dictionary as a pickle file whenever the user selects "Save entries" or the program quits.  When the phonebook function is first run or when the phonebook object is first created, the code checks for an existing phonebook.pickle file to load entries from automatically.

```Python
def phoneApp():
    try:
        f = open('phonebook.pickle', 'r')
        dic = pickle.load(f)
        print 'Entries Loaded'
        phonebook(dic)
    except:
        print 'No entries to load!'
        dic = {}
        phonebook(dic)
```
```Python
def saveEntries(dic):
    f = open('phonebook.pickle', 'w')
    pickle.dump(dic, f)
    f.close
    print 'Entries Saved!'
    phonebook(dic)
```

##Code Snippets (OOP version)
In the object-oriented version of this app, each entry is an object of a custom class Contact, the code creates a single object of a custom class Phonebook, and the different menu choices all call a method of this Phonebook class.
```Python
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
```
```Python
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
```

##Screenshots (identical for both versions)
