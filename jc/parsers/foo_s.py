"""jc - JSON CLI output utility `foo` command output streaming parser

Usage (cli):

    $ foo | jc --foo_s

Usage (module):

    import jc.parsers.foo_s
    result = jc.parsers.foo_s.parse(foo_command_output)    # result is an iterable object
    for item in result:
        # do something

Schema:

    {
      "foo":            string,
      "_meta":                       # This object only exists if using -q or quiet=True
        {
          "success":    booean,      # true if successfully parsed, false if error
          "error_msg":  string,      # exists if "success" is false
          "line":       string       # exists if "success" is false
        }
    }

Examples:

    $ foo | jc --foo-s
    {example output}
    ...

    $ foo | jc --foo-s -r
    {example output}
    ...
"""
import jc.utils


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.0'
    description = '`foo` command streaming parser'
    author = 'John Doe'
    author_email = 'johndoe@gmail.com'

    # compatible options: linux, darwin, cygwin, win32, aix, freebsd
    compatible = ['linux', 'darwin', 'cygwin', 'aix', 'freebsd']
    streaming = True


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (Dictionary) raw structured data to process

    Returns:

        Dictionary. Structured data to conform to the schema.
    """
    # process the data

    return proc_data


def parse(data, raw=False, quiet=False):
    """
    Main text parsing generator function. Produces an iterable object.

    Parameters:

        data:        (string)  line-based text data to parse
        raw:         (boolean) output preprocessed JSON if True
        quiet:       (boolean) suppress warning messages and ignore parsing errors if True

    Yields:

        Dictionary. Raw or processed structured data.
    """
    if not quiet:
        jc.utils.compatibility(__name__, info.compatible)

    for line in data:
        try:
            # parse the input here

            if quiet:
                output_line['_meta'] = {'success': True}
            
            if raw:
                yield output_line
            else:
                yield _process(output_line)
            
        except Exception as e:
            yield jc.utils.stream_error(e, quiet, line)
