#Command Line Phonebook App

##Summary:
This project is a phonebook app used from the command line that allows a user to save, lookup, and delete phonebook entires.  The entries consist of a name key connected to

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


##Code Snippets (OOP version)

##Screenshots (identical for both versions)
