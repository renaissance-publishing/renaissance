import React from "react";
import PropTypes from "prop-types";

import Container from '@material-ui/core/Container';
import Header from "./header";
import Footer from "./footer";
import TOCMenu from "./tocmenu";
import "./layout.css";
import { Drawer, CssBaseline, createMuiTheme, ThemeProvider } from "@material-ui/core";
import { makeStyles } from '@material-ui/core/styles';

const theme = createMuiTheme({
    typography: {
        fontFamily: 'de-walpergens-pica, sans-serif',
        fontSize: 16
    }
});

const tocWidth = 360;

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
