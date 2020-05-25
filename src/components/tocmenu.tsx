import React from "react";
import { List, ListItem, ListItemText, styled, ListItemSecondaryAction, IconButton } from "@material-ui/core";
import { ExpandLess, ExpandMore } from "@material-ui/icons";
import { Link, useStaticQuery, graphql } from "gatsby";

//

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

class TOCTreeElem {
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

//

const TOCLink = styled(Link)({
    textDecoration: 'none'
});

function nodeToListItem(node: GraphQLQueryResultNode): JSX.Element {
    const { fields: { slug }, frontmatter: { title }, headings } = node;
    console.log(TOCTreeElem.fromResultNode(node));

    let expander: JSX.Element;

    if (headings.length > 0) {
        expander = (
            <ListItemSecondaryAction>
                <IconButton edge="end" aria-label="expand">
                    <ExpandMore />
                </IconButton>
            </ListItemSecondaryAction>
        );
    }
    else {
        expander = null;
    }

    return (
        <ListItem button component={TOCLink} to={slug}>
            <ListItemText primary={ title } />
            { expander }
        </ListItem>
    );
}

export default () => {
    const data = useStaticQuery(graphql`
        query {
            allMarkdownRemark(sort: {fields: fields___chapter}, filter: {fields: {chapter: {ne: 0}}}) {
                edges {
                    node {
                        headings {
                            id
                            depth
                            value
                        }
                        fields {
                            slug
                        }
                        frontmatter {
                            title
                        }
                    }
                }
            }
        }
    `);

    return (
        <List>
            {
                data.allMarkdownRemark.edges.map(({ node }) => nodeToListItem(node))
            }
        </List>
    );
};

