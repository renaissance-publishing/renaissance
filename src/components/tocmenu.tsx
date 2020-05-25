import React from "react";
import { List, ListItem } from "@material-ui/core";
import { Link, useStaticQuery, graphql } from "gatsby";


type GraphQLQueryResultNode = {
    headings: {
        depth: number,
        value: string
    },
    fields: {
        slug: string
    },
    frontmatter: {
        title: string
    }
}

function nodeToListItem({ fields: { slug }, frontmatter: { title } }: GraphQLQueryResultNode): JSX.Element {
    return (
        <ListItem>
            <Link to={ slug }>{ title }</Link>        
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

