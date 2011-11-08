import unittest
from ..pyKnife import pyKnife, KnifeCommandError

class TestShow( unittest.TestCase ):
    def setUp( self ):
       self.knife = pyKnife()
       self.basic_keys = ['NodeName', 'Environment', 'FQDN', 'IP', 'RunList', 'Roles', 'Recipes', 'Platform']

    def test_no_node( self ):
        # Make sure correct return for no node found
        self.assertRaises( KnifeCommandError, self.knife.node.show, "NoNodeForThisName" )

    def test_found_node( self ):
        # Make sure basic node info is returned for node
        info = self.knife.node.show( "chef" )
        self.assertEqual( set( info.keys() ), set( self.basic_keys ) )

    def test_attribute( self ):
        # Make sure only the attribute requested is returned
        info = self.knife.node.show( "chef", what = "attribute uptime" )
        self.assertTrue( 'uptime' in info and len( info.keys() ) == 1 )

    def test_long_info( self ):
        # Make sure all attributes are returned
        info = self.knife.node.show( "chef", what = "long" )
        self.assertTrue( 'automatic' in info )

    def test_medium_info( self ):
        # Make sure normal attributes are returned
        info = self.knife.node.show( "chef", "medium" )
        self.assertTrue( 'normal' in info )

    def test_runlist( self ):
        # Make sure run list is returned
        info = self.knife.node.show( "chef", "runlist" )
        self.assertTrue( 'run_list' in info and len( info.keys() ) == 1 )

    def test_environment( self ):
        # Make sure environment is returned
        info = self.knife.node.show( "chef", "environment" )
        self.assertTrue( 'chef_environment' in info and len( info.keys() ) == 1 )

if __name__ == '__main__':
    unittest.main()
