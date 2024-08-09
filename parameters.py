import csv
from utils import str2bool


def extract(uploaded_files, skip_params):
    unique_parameters = {}

    for f in uploaded_files:
        # Get the filename without the extension
        filename = f.name.replace(".csv","")

        reader = csv.DictReader(f.getvalue().decode("utf-8").splitlines())
        for row in reader:
            is_instance = str2bool(row['IsInstance'])
            appendix = " (default)" if is_instance else ""
            param_name = row['Name'] + appendix
            parameter_group = row['Group'].replace("PG_","")
            parameter_group = parameter_group.replace("GEOMETRY", "DIMENSIONS").replace("REBAR_SYSTEM_LAYERS", "LAYERS")

            param_tuple = (row['StorageType'], row['IsInstance'], row['BuiltIn'], parameter_group)
            
            if param_name not in unique_parameters:
                # If it's a new parameter, initialize its entry with the parameter details and filename
                unique_parameters[param_name] = {
                    'details': param_tuple,
                    'files': [filename]
                }
            else:
                # If the parameter already exists, append the filename to its list if it's not already there
                if filename not in unique_parameters[param_name]['files']:
                    unique_parameters[param_name]['files'].append(filename)

    output = []
    for param_name, data in sorted(unique_parameters.items(), key=lambda x: (x[1]['details'][3], x[0])):
        if data['details'][3] in skip_params:
            continue
        row = [param_name] + list(data['details']) + [", ".join(data['files'])]
        output.append(row)

    output_csv = "Name;StorageType;IsInstance;BuiltIn;Group;Families\n"
    for row in output:
        output_csv += ";".join(row) + "\n"

    return output_csv
        