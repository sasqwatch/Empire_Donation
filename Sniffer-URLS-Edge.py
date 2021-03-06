from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Sniffer-URLS-Edge.ps1',

            'Author': ['@matthomjxi0e'],

            'Description': ('Operation Sniffer URLS About Browser User in Microsoft Edge.'),

            'Background' : True,

            'OutputExtension' : None,

            'NeedsAdmin' : False,

            'OpsecSafe' : True,

            'Language' : 'powershell',

            'MinLanguageVersion' : '2',

            'Comments': [
                'https://twitter.com/matthomjxiex02x'
            ]
        }

         
        self.options = {
            
            
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

       
        self.mainMenu = mainMenu

        for param in params:
          
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value


    def generate(self):

        moduleName = self.info["Name"]

         
        moduleSource = self.mainMenu.installPath + "/data/module_source/collection/Sniffer-URLS-Edge.ps1"

        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode

        script += "\nwio.sh"

        for option,values in self.options.iteritems():
            if option.lower() != "agent":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])
	script += ' | Out-String | %{$_ + \"`n\"};"`n'+str(moduleName)+' completed!"'
   		    
        return script

