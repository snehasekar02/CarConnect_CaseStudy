class SqlConnection:

    @staticmethod
    def get_property_string(property_file):
        try:
            with open(property_file, 'r') as file:
                properties = {}
                for line in file:
                    key, value = line.strip().split('=')
                    properties[key.strip()] = value.strip()
                return properties
        except FileNotFoundError:
            print(f"Error: Property file '{property_file}' not found.")
            return None
