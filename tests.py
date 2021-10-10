import unittest
import importlib
key_value = importlib.import_module("key-value")



class KeyValueTests(unittest.TestCase):
    def test_put_value_returns_ok(self):
        assert key_value.put_value("my_name", "amber")== "ok"

    def test_put_value_adds_to_dict(self):
        key_value.put_value("my_name", "amber")
        assert key_value.stored_values["my_name"] == "amber"    

    def test_fetch_value_returns_value(self):
        key_value.put_value("my_name", "amber")
        assert key_value.fetch_value("my_name") == "amber"

    def test_fetch_value_returns_error_if_key_not_found(self):
        key_value.put_value("my_name", "amber")
        assert key_value.fetch_value("my_age") == "Value not found"

    def test_error_message_if_command_not_recognized(self):
        assert key_value.eval_array(["do", "something"]) == "Unknown command. Known commands are: put, fetch, exit"

    def test_eval_array_always_returns_string(self):
        assert isinstance(key_value.eval_array(["put", "my_name", "amber"]), str)
    

    


    
if __name__ == '__main__':
    unittest.main()