import json

class Node:
    """
        Node Commands
            knife node from file FILE (options)
            knife node show NODE (options)
            knife node create NODE (options)
            knife node run_list add [NODE] [ENTRY] (options)
            knife node bulk delete REGEX (options)
            knife node list (options)
            knife node edit NODE (options)
            knife node run_list remove [NODE] [ENTRY] (options)
            knife node delete NODE (options)
    """
    def __init__( self, knife ):
        self.knife = knife

    def fromFile( self ):
        raise NotImplementedError

    def parse_short_format( self, output ):
        """
            Parses the following into json format
                Node Name:   chef
                Environment: Production
                FQDN:        chef.cns.montana.edu
                IP:          153.90.178.154
                Run List:    role[rcg_server], role[nagios_client]
                Roles:       rcg_server, nagios_client
                Recipes      rcg, nagios::client
                Platform:    ubuntu 10.04
        """
        output = output.replace( ' ', '' ).splitlines( )
        temp = {}
        for kp in output:
            t = kp.split( ':', 1 )
            temp[t[0]] = t[1]

        json = {}
        for k,v in temp.items():
            if k[:7] == 'Recipes':
                temp = k[7:] + ':' + v
                json['Recipes'] = temp.split( ',' )
            elif ',' in v:
                json[k] = v.split( ',' )
            else:
                json[k] = v

        return json

    def show( self, node, what = 'short' ):
        """
            node                Name of the node to show
            what          Pick one of the following
                                  - attribute <name of attribute> => of attribute to display
                                  - long => all attributes
                                  - medium => normal attributes
                                  - short => default
                                  - runlist => only the run list
                                  - environment => only the environment
        """
        command = [ 'node', 'show', node ]
        if what == None:
            pass
        elif what[:3] == 'att':
            command.append( '-a' )
            command.append( what.split( ' ' )[1] )
        elif what == 'long':
            command.append( '-l' )
        elif what == 'medium':
            command.append( '-m' )
        elif what == 'runlist':
            command.append( '-r' )
        elif what == 'environment':
            command.append( '-E' )
        elif what == 'short':
            return self.parse_short_format( self.knife.command( command, 'summary' ) )
        else:
            raise BadNodeOptionxception( what )
            
        return json.loads( self.knife.command( command ) )
            

    def create( self ):
        raise NotImplementedError

    def run_listAdd( self ):
        """
            -a, --after ITEM                 Place the ENTRY in the run list after ITEM
        """
        raise NotImplementedError

    def bulkDelete( self, REGEX ):
        raise NotImplementedError

    def list( self ):
        command = ['node', 'list']
        return json.loads( self.knife.command( command ) )

    def edit( self, NODE ):
        raise NotImplementedError

    def run_listRemove( self, NODE, ENTRY ):
        raise NotImplementedError

    def delete( self, NODE ):
        raise NotImplementedError

class BadNodeOptionException( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( "%s is not a valid option" % self.value )

class NoNodeException( Exception ):
    def __init__( self, value ):
        self.value = value

    def __str__( self ):
        return repr( "%s is not a valid node" % self.value )
