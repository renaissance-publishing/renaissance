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
        <Container maxWidth='md'>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <Header />
                <Drawer 
                    variant="permanent"
                    className={ classes.tocDrawer }
                    classes={{
                        paper: classes.tocDrawerPaper
                    }}
                    >
                    <TOCMenu />
                </Drawer>

                {children}
                <Footer />
            </ThemeProvider>
        </Container>
    );
};


Layout.propTypes = {
    children: PropTypes.node.isRequired,
};

export default Layout;
