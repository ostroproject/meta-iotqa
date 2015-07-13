'''Verify sensor can't be connected twice'''
import os
import readConfigFile
from oeqa.oetest import oeRuntimeTest

class TestConnectSensorAlreadyConnected(oeRuntimeTest):
    '''Fail to connect sensor if it's already connected'''
    def test(self):
        '''push binary to target and run it with argument'''
        #Prepare test binaries to image        
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_connect_sensor_already_connected')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        #run test get sensor by id and show it's information
        client_cmd = "/opt/sensor-test/apps/test_connect_sensor_already_connected "\
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','valid-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)