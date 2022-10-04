import sys
import toml

with open("powers.toml", "r") as ifile:
    parsed = toml.loads(ifile.read())

# print(parsed)

standard_keys = ['general', 'name', 'fluff', 'requires', 'action', 'effect', 'sections']

for power in sorted(parsed["powers"], key=lambda x: x['name']):
    if 'general' not in power or power['general'] == False:
        continue

    sys.stdout.write(f"### {power['name']}\n\n")

    if "fluff" in power:
        sys.stdout.write(f"{power['fluff']}\n\n")

    if "requires" in power:
        sys.stdout.write(f"- **Requires:** {power['requires']}\n")
    if "action" in power:
        sys.stdout.write(f"- **Action:** {power['action']}\n")
    sys.stdout.write(f"- **Effect:** {power['effect']}\n")
    if 'sections' in power:
        for section in power['sections']:
            sys.stdout.write(f"- **{section['label']}:** {section['content']}\n")

    sys.stdout.write("\n")

    for key in power.keys():
        if key not in standard_keys:
            sys.stderr.write(f"Power {power['name']} contianed non-standard key {key}\n")

