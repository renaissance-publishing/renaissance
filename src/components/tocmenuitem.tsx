import React from "react";
import { AnchorLink } from "gatsby-plugin-anchor-links";
import { List, ListItem, ListItemText, ListItemSecondaryAction, IconButton, Collapse } from "@material-ui/core";
import { ExpandLess, ExpandMore } from "@material-ui/icons";


type Heading = {
    id: string,
    depth: number,
    value: string
}

type GraphQLQueryResultNode = {
    headings: Heading[],
    fields: {
        slug: string
    },
    frontmatter: {
        title: string
    }
}

export class TOCTreeElem {
    title: string;
    url: string;
    depth: number;
    children: TOCTreeElem[];

    constructor(title: string, url: string, depth: number) {
        this.title = title;
        this.url = url;
        this.depth = depth;
        this.children = [];
    }

    static fromResultNode(node: GraphQLQueryResultNode): TOCTreeElem {
        let parentNode = new TOCTreeElem(node.frontmatter.title, node.fields.slug, 1);

        function addNodeToTree(tree: TOCTreeElem, child: Heading) {
            if (tree.depth < child.depth - 1 && tree.children.length > 0) {
                addNodeToTree(tree.children[tree.children.length - 1], child);
                return;
            }

            tree.children.push(new TOCTreeElem(child.value, `${parentNode.url}#${child.id}`, child.depth));
        }

        for (const heading of node.headings) {
            addNodeToTree(parentNode, heading);
        }

        return parentNode;
    }
}

export class TOCMenuItem extends React.Component<{ tree: TOCTreeElem, key: string }, { isExpanded: boolean }> {
    title: string;
    url: string;
    children: TOCTreeElem[];
    constructor(props) {
        super(props);
        this.state = { isExpanded: false };
    }

    handleToggleExpand() {
        const { isExpanded } = this.state;
        this.setState({ isExpanded: !isExpanded });
    }

    render(): React.ReactNode {
        let expandableToggle: React.ReactNode = null;
        let expandableContent: React.ReactNode = null;

        if (this.props.tree.children.length > 0) {
            expandableToggle = (
                <ListItemSecondaryAction>
                    <IconButton edge="end" aria-label="toggle-expand" onClick={this.handleToggleExpand.bind(this)}>
                        { this.state.isExpanded ? <ExpandLess /> : <ExpandMore /> }
                    </IconButton>
                </ListItemSecondaryAction>
            );

            expandableContent = (
                <Collapse in={ this.state.isExpanded } style={{ paddingLeft: 20 }}>
                    <List component="ul" disablePadding>
                        {
                            this.props.tree.children.map( child => (
                                <TOCMenuItem tree={ child } key={ child.url } />
                            ))
                        }
                    </List>
                </Collapse>
            );
        }

        return (
            <>
                <ListItem button component={ AnchorLink } to={ this.props.tree.url }>
                    <ListItemText primary={ this.props.tree.title } />
                    { expandableToggle }
                </ListItem>
                { expandableContent }
            </>
        );
    }
}


