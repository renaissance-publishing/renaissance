import blessings
from click import echo
from dataclasses import dataclass
from os.path import join
from typing import Iterator, List, Optional, Tuple
import yaml

term = blessings.Terminal()


@dataclass
class Skill(object):
    name: str
    aptitude: str
    categories: List[str]
    description: str
    fields: Optional[str]
    specializations: Optional[str]


class RulesData(object):
    def __init__(self, walk_iter: Iterator[Tuple[str, List[str], List[str]]]):
        echo(term.green('Loading rules data:'))

        self.skills: List[Skill] = []

        for root, _, files in walk_iter:
            for fn in files:
                with open(join(root, fn)) as f:
                    try:
                        rule = yaml.load(f)
                    except yaml.YAMLError as e:
                        echo(term.bold_red('Error: failed loading rules file {}'.format(fn)))
                        raise e

                    try:
                        if rule['type'] == 'skill':
                            self.skills.append(Skill(
                                rule['name'], rule['aptitude'], rule['categories'], rule['description'],
                                rule.get('fields'), rule.get('specializations')
                            ))
                    except KeyError as e:
                        if e.args[0] != 'type':
                            echo(term.bold_red(
                                'Error: {} file {} is missing required key "{}:"'.format(rule['type'], fn, e.args[0])
                             ))
                        else:
                            echo(term.bold_red(
                                'Error: rules file {} is missing required key "type:".'.format(fn)
                            ))
                    else:
                        echo(term.green('• Loaded {} file {}.').format(rule['type'], fn))

    def __getitem__(self, item: str):
        if item not in ['skills']:
            raise KeyError(item)

        return getattr(self, item)
