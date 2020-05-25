import React from "react";
import { useStaticQuery, graphql } from "gatsby";

import { List, ListItem, TextField, InputAdornment, Hidden } from "@material-ui/core";
import { Search } from "@material-ui/icons";
import { TOCMenuItem, TOCTreeElem } from "./tocmenuitem";

//

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

    const nodeTrees = data.allMarkdownRemark.edges.map(({ node }) => TOCTreeElem.fromResultNode(node));

    return (
        <List>
            <Hidden smDown>
                <ListItem>
                    <TextField 
                        label="Search"
                        variant="outlined"
                        fullWidth
                        InputProps={{
                            startAdornment: (
                                <InputAdornment position="start">
                                    <Search />
                                </InputAdornment>
                            )
                        }}
                        />
                </ListItem>
            </Hidden>

            {
                nodeTrees.map(nodeTree => (
                    <TOCMenuItem tree={nodeTree} key={nodeTree.url} />
                ))
            }
        </List>
    );
};

