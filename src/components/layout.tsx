import React from "react";
import PropTypes from "prop-types";

import Header from "./header";
import Footer from "./footer";
import TOCMenu from "./tocmenu";
import "./layout.css";
import { Container, Drawer, CssBaseline, createMuiTheme, ThemeProvider, Hidden, AppBar, Toolbar } from "@material-ui/core";
import { Link } from "gatsby";
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
    mobileBranding: {
        margin: 0,
        fontFamily: 'voluta-script-pro, serif',
        fontSize: '48pt',
        fontWeight: 'normal',
        textAlign: 'center',
        lineHeight: 'normal',
        color: 'white'
    },
    mobileBrandingLink: {
        textDecoration: 'none'
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
        <Hidden mdUp>
            <AppBar position="sticky">
                <Toolbar>
                    <Link to="/" className={ classes.mobileBrandingLink }>
                        <h1 className={ classes.mobileBranding }>Renaissance Games</h1>
                    </Link>
                </Toolbar>
            </AppBar>
        </Hidden>
        <div className={ classes.root }>
            <Hidden smDown>
                <Drawer 
                        variant="permanent"
                        className={ classes.tocDrawer }
                        classes={{
                            paper: classes.tocDrawerPaper
                        }}
                        >
                            <TOCMenu />
                </Drawer>
            </Hidden>
            <Container maxWidth='md'>
                <Hidden smDown>
                    <Header />
                </Hidden>
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
