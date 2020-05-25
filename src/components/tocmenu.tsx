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

function nodeToListItem(node: GraphQLQueryResultNode): JSX.Element {
    console.log(node);

    return (
        <ListItem>
            
        </ListItem>
    );
}

export default () => {
    const data = useStaticQuery(graphql`
        query {
            allMarkdownRemark(sort: {fields: fields___chapter}) {
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
                data.allMarkdownRemark.edges.forEach(nodeToListItem)
            }
        </List>
    );
};

