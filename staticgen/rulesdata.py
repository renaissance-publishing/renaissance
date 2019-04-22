from click import secho
from dataclasses import dataclass
from os.path import join
from typing import Iterator, List, Optional, Tuple
import yaml


@dataclass(order=True)
class Skill(object):
    name: str
    aptitude: str
    categories: List[str]
    description: str
    fields: Optional[str]
    specializations: Optional[str]


class RulesData(object):
    def __init__(self, walk_iter: Iterator[Tuple[str, List[str], List[str]]]):
        secho('Loading rules data:', fg='yellow')

        self.skills: List[Skill] = []

        for root, _, files in walk_iter:
            for fn in files:
                with open(join(root, fn)) as f:
                    try:
                        rule = yaml.load(f)
                    except yaml.YAMLError as e:
                        secho('Error: failed loading rules file {}'.format(fn), fg='red', bold=True)
                        raise e

                    try:
                        if rule['type'] == 'skill':
                            self.skills.append(Skill(
                                rule['name'], rule['aptitude'], rule['categories'], rule['description'],
                                rule.get('fields'), rule.get('specializations')
                            ))
                    except KeyError as e:
                        if e.args[0] != 'type':
                            secho(
                                'Error: {} file {} is missing required key "{}:"'.format(rule['type'], fn, e.args[0]),
                                fg='red', bold=True
                             )
                        else:
                            secho(
                                'Error: rules file {} is missing required key "type:".'.format(fn),
                                fg='red', bold=True
                            )
                    else:
                        secho('• Loaded {} file {}.'.format(rule['type'], fn), fg='green')
        
        self.skills.sort(key=lambda x: x.name)

    def __getitem__(self, item: str):
        if item not in ['skills']:
            raise KeyError(item)

        return sorted(getattr(self, item))
