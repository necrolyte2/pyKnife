import unittest
from ..pyKnife import pyKnife, BadKnifeCommandException

class TestCommand( unittest.TestCase ):
    def setUp( self ):
        self.knife = pyKnife()

    def test_command( self ):
        # Make sure a valid command will run and returns a tuple
        output = self.knife.command( [ 'node', 'list' ] )
        self.assertTrue( type( output ) == type( () ) )

    def test_bad_command( self ):
        # Make sure a bad command raises an exception
        self.assertRaises( BadKnifeCommandException, self.knife.command, ['bad_command'] )


if __name__ == '__main__':
    unittest.main()
