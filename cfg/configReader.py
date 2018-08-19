import configparser
import copy

class DarkNetConfigReader:
    

    def __init__(self):
        self.layers = []
        self.net = []
        self.raw_config_list = None
    def parse_raw(self, cfg_file):
        with open(cfg_file) as f:
            contents = f.read().strip()
            # Not as bad as it seems.
            self.raw_config_list = list((map(lambda x: '[' + x,
                                             filter(lambda x: bool(x),
                                                    contents.split('[')))))

        self.to_dicts()
                    
    def to_dicts(self) -> None:
        assert (self.raw_config_list is not None)
        self.config_dict_list = []        
        for cfg_str in self.raw_config_list:
            config = configparser.ConfigParser()
            config.read_string(cfg_str)
            sections = config.sections()
            assert(len(sections) == 1), ("Len of %s is %d " % (sections, len(sections) ))
            name = sections[0]
            attributes = dict(config.items(name))
            temp = copy.deepcopy(attributes)
            temp.update({"name" : name})
            self.config_dict_list.append(temp)
                

    # ret_lists :: [Dict]
    def ret_lists(self) -> list:
        return self.config_dict_list

    
if __name__ == "__main__":
    
    cfg_file = "./yolov3.cfg"
    config = DarkNetConfigReader()
    config.parse_raw(cfg_file)
    config.to_dicts()
