import React from "react";
import { AnchorLink } from "gatsby-plugin-anchor-links";
import { List, ListItem, ListItemText, ListItemSecondaryAction, IconButton, Collapse } from "@material-ui/core";
import { ExpandLess, ExpandMore } from "@material-ui/icons";

import { TOCTreeElem } from "./tocmenu";


class TOCMenuItem extends React.Component<{ tree: TOCTreeElem, key: string }, { isExpanded: boolean }> {
    title: string;
    url: string;
    children: TOCTreeElem[];
    constructor(props) {
        super(props);
        this.title = props.tree.title;
        this.url = props.tree.url;
        this.children = props.tree.children;
        this.state = { isExpanded: false };
    }

    handleToggleExpand() {
        const { isExpanded } = this.state;
        this.setState({ isExpanded: !isExpanded });
    }

    render(): React.ReactNode {
        let expandableToggle: React.ReactNode = null;
        let expandableContent: React.ReactNode = null;

        if (this.children.length > 0) {
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
                            this.children.map( child => (
                                <TOCMenuItem tree={ child } key={ child.url } />
                            ))
                        }
                    </List>
                </Collapse>
            );
        }

        return (
            <>
                <ListItem button component={ AnchorLink } to={ this.url }>
                    <ListItemText primary={ this.title } />
                    { expandableToggle }
                </ListItem>
                { expandableContent }
            </>
        );
    }
}

export default TOCMenuItem;
