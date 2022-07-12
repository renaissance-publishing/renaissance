import sys
import toml

with open("powers.toml", "r") as ifile:
    parsed = toml.loads(ifile.read())

# print(parsed)

standard_keys = ['General', 'Name', 'Fluff', 'Requires', 'Action', 'Effect', 'Sections']

for power in sorted(parsed["Powers"], key=lambda x: x['Name']):
    if 'General' not in power or power['General'] == False:
        continue

    sys.stdout.write(f"### {power['Name']}\n\n")

    if "Fluff" in power:
        sys.stdout.write(f"{power['Fluff']}\n\n")

    if "Requires" in power:
        sys.stdout.write(f"- **Requires**: {power['Requires']}\n")
    if "Action" in power:
        sys.stdout.write(f"- **Action**: {power['Action']}\n")
    sys.stdout.write(f"- **Effect**: {power['Effect']}\n")
    if 'Sections' in power:
        for section in power['Sections']:
            sys.stdout.write(f"- {section['Label']}: {section['Content']}\n")

    sys.stdout.write("\n")

    for key in power.keys():
        if key not in standard_keys:
            sys.stderr.write(f"Power {power['Name']} contianed non-standard key {key}\n")

