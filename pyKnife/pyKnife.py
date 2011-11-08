from subprocess import Popen, PIPE
from pyKnifeCommands.node import Node

class pyKnife:
    def __init__( self ):
        self.environment = None
        self.execute = None
        self.help = None
        self.index = None
        self.node = Node( self )
        self.recipe = None
        self.role = None
        self.search = None
        self.ssh = None
        self.status = None
        self.environment = None

    def command( self, command, format = 'json' ):
        """
            Runs the knife command with a given format for output
            knife formats accepted:
                - json
                - summary
        """
        knife_command = ['/usr/bin/knife'] + command + ['-F', format]
        p = Popen( knife_command, stdout = PIPE, stderr = PIPE )
        output = p.communicate()
        if output[0].startswith( 'FATAL' ):
            raise BadKnifeCommandException( "Bad Knife command given: \n%s" % knife_command )
        elif output[0].startswith( 'ERROR' ):
            raise KnifeCommandError( command, output[0] )
        return output[0]

class BadKnifeCommandException( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( self.value )

class KnifeCommandError( Exception ):
    def __init__( self, command, error ):
        self.command = command
        self.error = error

    def __str__( self ):
        return repr( "There was an error running %s.\n%s" % (self.command,self.error) )
