"""
MAP Client Plugin Step
"""
import json
import os.path

from shutil import copyfile
from PySide2 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.saveargondocumentstep.configuredialog import ConfigureDialog


class SaveArgonDocumentStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(SaveArgonDocumentStep, self).__init__('Save Argon Document', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Sink'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/saveargondocumentstep/images/data-sink.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'https://opencmiss.org/1.0/rdf-schema#ArgonDocument'))
        # Port data:
        self._document = None  # https://opencmiss.org/1.0/rdf-schema#ArgonDocument
        # Config:
        self._config = {
            'identifier': '',
            'consolidate_resources': True,
            'output_directory': '',
            'previous_location': ''
        }

    def _save(self):
        # make model sources relative to current location if possible
        # note that sources on different windows drives have absolute paths
        base_path = os.path.join(self._location, self._config['output_directory'])
        state = self._document.serialize(base_path)
        name = self._document.getName()
        with open(os.path.join(base_path, f'{name}.json'), 'w') as f:
            f.write(state)

    def _consolidate_regions_resources(self, region):
        base_path = os.path.join(self._location, self._config['output_directory'])
        model_sources = region.getModelSources()
        for model_source in model_sources:
            if model_source.getType() == "FILE":
                src_file_name = model_source.getFileName()
                if not is_subdirectory(src_file_name, base_path):
                    _, filename = os.path.split(src_file_name)
                    dst_file_name = os.path.join(base_path, filename)
                    copyfile(src_file_name, dst_file_name)
                    model_source.setFileName(dst_file_name)
        for index in range(region.getChildCount()):
            self._consolidate_regions_resources(region.getChild(index))

    def _consolidate_resources(self):
        root_region = self._document.getRootRegion()
        self._consolidate_regions_resources(root_region)

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        self._save()
        if self._config['consolidate_resources']:
            self._consolidate_resources()
            self._save()
        self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        self._document = dataIn  # https://opencmiss.org/1.0/rdf-schema#ArgonDocument

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.setWorkflowLocation(self._location)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.setWorkflowLocation(self._location)
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


def is_subdirectory(child_path, parent_path):
    parent_path = os.path.realpath(os.path.join(parent_path, ''))
    child_path = os.path.realpath(os.path.join(child_path, ''))

    return os.path.commonpath([parent_path]) == os.path.commonpath([parent_path, child_path])
