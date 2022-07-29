import os.path

from PySide2 import QtWidgets
from mapclientplugins.saveargondocumentstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None
        self._workflow_location = None
        self._previousLocation = ''

        self.setWhatsThis("Please read documentation: \nhttps://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.saveargondocumentstep/docs/index.html")

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEditIdentifier.textChanged.connect(self.validate)
        self._ui.pushButtonDIrectoryChooser.clicked.connect(self._directoryChooserClicked)

    def setWorkflowLocation(self, location):
        self._workflow_location = location

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(
                self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEditIdentifier.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEditIdentifier.text())
        if valid:
            self._ui.lineEditIdentifier.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEditIdentifier.setStyleSheet(INVALID_STYLE_SHEET)

        output_directory = self._ui.lineEditOutputDirectory.text()
        directory_valid = os.path.isdir(os.path.join(self._workflow_location, output_directory))

        return valid and directory_valid

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEditIdentifier.text()
        config = {
            'identifier': self._ui.lineEditIdentifier.text(),
            'consolidate_resources': self._ui.checkBoxConsolidateResources.isChecked(),
            'output_directory': self._ui.lineEditOutputDirectory.text(),
            'previous_location': self._previousLocation
        }
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEditIdentifier.setText(config['identifier'])
        self._ui.checkBoxConsolidateResources.setChecked(config['consolidate_resources'])
        self._ui.lineEditOutputDirectory.setText(config['output_directory'])
        self._previousLocation = os.path.join(self._workflow_location, config['previous_location'])

    def _directoryChooserClicked(self):
        # Second parameter returned is the filter chosen
        location = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Destination for Argon document', self._previousLocation)

        if location:
            self._previousLocation = location
            self._ui.lineEditOutputDirectory.setText(os.path.relpath(location, self._workflow_location))
