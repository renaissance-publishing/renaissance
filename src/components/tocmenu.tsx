import React from "react";
import { List } from "@material-ui/core";
import { useStaticQuery, graphql } from "gatsby";
import TOCMenuItem from "./tocmenuitem";

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

    return (
        <List>
            {
                data.allMarkdownRemark.edges.map(({ node }) => {
                    const nodeTree = TOCTreeElem.fromResultNode(node);
                    return (
                        <TOCMenuItem tree={nodeTree} key={nodeTree.url}></TOCMenuItem>
                    );
                })
            }
        </List>
    );
};

