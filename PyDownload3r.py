# Requirements:
# Download a file from the url found in QLineEdit
# Display QProgressBar
# Allow the user to select the save location using a "File Save" dialog
# Display a message when the download is completed
# Handle errors(exceptions) by displaying an error message

# Work Flow:
# Basic UI: Set the label, line_edit, button
# Basic functionality
# Extended functionality
#

from PyQt4.QtCore import *    # Import python modules
from PyQt4.QtGui import *    # Import python modules
import sys    # Import modules
import urllib.request     # This is how we download the file and how we navigate to the url

class Downloader(QDialog):    # QDialog is a window this is where we override a constructor QDialog is a class so we
                              ## need to create a class.
    def __init__(self):
        QDialog.__init__(self)    # must call the parent with QDialog

        layout = QVBoxLayout()   # This says how it should be lade out V H or G for virtical, horizontal, and grid

        #label = QLabel("PyDownload")    # This creates a label adding self. makes this variable an instance variable so
                                         ## it can be used anywhere in the code
        self.url = QLineEdit()    # This creates a Line Edit to use everywhere in the code add self. to the variable see
        self.save_location = QLineEdit()    # This creates a Line Edit
        self.progress = QProgressBar()   # This creates a progress bar
        download = QPushButton("Download")    # This creates a push button when this button is clicked it sends an event
                                              ## so an event handler will be needed in the future.
        browse = QPushButton("Browse")    # create a push button for thr browse option
        self.url.setPlaceholderText("URL")    # This put a Place Holder in the line edit until it is clicked
        self.save_location.setPlaceholderText("File Save Location")    # This puts the text File Save Location in the line
                                                                  ## edit until it is clicked and text is entered

        self.progress.setValue(0)   # This sets the value to 0 and is displayed as a percentage in the window
        self.progress.setAlignment(Qt.AlignHCenter)    # this puts the set value in the center of the progress bar (aligns
                                                  ## horizantal and center this is why we imported QtCore

        layout.addWidget(self.url)     # Add qwidget to lay out. use layouts there your friend.
        layout.addWidget(self.save_location)    # Adds a line edit widget to window
        layout.addWidget(browse)    # this adds the browse button to the layout
        layout.addWidget(self.progress)     # Adds progress bar widget to window
        layout.addWidget(download)    # This adds a button widget

        self.setLayout(layout)    # instruct QDialog constructor method to use this lay out to display elements

        self.setWindowTitle("PyDownloader")    # This will set the title of the window
        self.setFocus()     # This removes focus from QLineEdit this means you have to click on the line edt box
        #button.clicked.connect(self.close)     # This is the event handler connect attaches the event to the handler
                                               ## self.close this self.close closes the window
        #line_edit.textChanged.connect(label.setText)    # This says when the text is changed in line_edit to set label
                                                        ## to that changed text

        download.clicked.connect(self.download)    # this is the event that happens when the download button is clicked

        browse.clicked.connect(self.browse_file)

    def browse_file(self):    # this crestea the function that lets user brows the files
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".",
                                                filter="All Files (*.*)")    #self is pairent caption is the title the
                                                                             ##directory is the starting dir the . cwd
        self.save_location.setText(QDir.toNativeSeparators(save_file))    # this updates the save location QDir to
                                                                          ## native separators sets the save path to
                                                                          ## the proper OS
    def download(self):
        #pass    # This is a filler for now
        url = self.url.text()    #ceat local variable, call the text method so that you can get the text user inputs
        save_location = self.save_location.text()    # creates a local variable set it to
        try:    # this is where we try to get url if there is a failure it will pass an error
            urllib.request.urlretrieve(url, save_location, self.report)     #this gets url from user and requests it if/when
                                                                        ## it is recived it says where to download

        except Exception:    # this is a brod exception claws in here we want to display a message box titled warning
                             ## and with the message download failed
            QMessageBox.warning(self, "Warning", "Download Failed")    #this creates the warning message box and adds info
            return
        QMessageBox.information(self, "Imformation", "The download is complete")    # Function to display infgo, self is
                                                                                    ##the pairent QWidget, the second
                                                                                    ##argument is the title the third
                                                                                    ## is the content of the message
        self.progress.setValue(0)    # this resets the value of the progress bar to 0
        self.url.setText("")    # this resets the line edit
        self.save_location.setText("")     # this resets the save location after this the window is reset
    def report(self, blocknum, blocksize, totalsize):   # this is a function that url.retrive will report to this takes
                                                        ## three arguments to determine the download percentage
        readsofar = blocknum *blocksize    # This determines how much has been read so far
        if totalsize > 0:    # This if statement is check that the server is sending the total size of the file
            percent = readsofar * 100 / totalsize    # this does the math to get the percent
            self.progress.setValue(int(percent))    # this resets the value of the progress bar


app = QApplication(sys.argv)    # This creates the Q application should only have one even if there are multiple windows
dl = Downloader()    # This is just to make it less typing and to call the class
dl.show()    # This Displays the appropriate code in the class Downloader this calls the QDialog
app.exec_()    # This is saying execute the application
#sys.exit(app.exec_())    # This is will get same results but with a exit code