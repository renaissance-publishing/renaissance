import React from "react";
import PropTypes from "prop-types";

import Header from "./header";
import Footer from "./footer";
import TOCMenu from "./tocmenu";
import "./layout.css";
import { Container, Drawer, CssBaseline, createMuiTheme, ThemeProvider } from "@material-ui/core";
import { makeStyles } from '@material-ui/core/styles';

const theme = createMuiTheme({
    typography: {
        fontFamily: 'english, sans-serif',
        fontSize: 16
    }
});

const tocWidth = 320;

const useStyles = makeStyles({
    root: {
        display: 'flex'
    },
    tocDrawer: {
        width: tocWidth
    },
    tocDrawerPaper: {
        width: tocWidth
    }
})

const Layout = ({ children }) => {
    const classes = useStyles();

    return (
    <ThemeProvider theme={theme}>
        <CssBaseline />

        <div className={ classes.root }>
            <Drawer 
                variant="permanent"
                className={ classes.tocDrawer }
                classes={{
                    paper: classes.tocDrawerPaper
                }}
                >
                <TOCMenu />
            </Drawer>
            <Container maxWidth='md'>
                <Header />
                {children}
                <Footer />
            </Container>
        </div>
    </ThemeProvider>
    );
};


Layout.propTypes = {
    children: PropTypes.node.isRequired,
};

export default Layout;
