import React from "react";
import { List, ListItem, ListItemText, styled, ListItemSecondaryAction, IconButton } from "@material-ui/core";
import { ExpandLess, ExpandMore } from "@material-ui/icons";
import { Link, useStaticQuery, graphql } from "gatsby";

type GraphQLQueryResultNode = {
    headings: {
        id: string,
        depth: number,
        value: string
    }[],
    fields: {
        slug: string
    },
    frontmatter: {
        title: string
    }
}

const TOCLink = styled(Link)({
    textDecoration: 'none'
});

function nodeToListItem({ fields: { slug }, frontmatter: { title }, headings }: GraphQLQueryResultNode): JSX.Element {
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

