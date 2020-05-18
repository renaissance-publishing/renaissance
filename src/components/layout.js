import React from "react"
import PropTypes from "prop-types"
import { useStaticQuery, graphql } from "gatsby"
import styled from "@emotion/styled"

import Header from "./header"
import "normalize.css"
import "./layout.css"

const Wrapper = styled("div")`
  min-height: 100%;
  display: grid;
  grid-template-rows: auto 1fr auto;
  grid-template-columns: 100vh;
`

const Layout = ({ children }) => {
  const data = useStaticQuery(graphql`
    query SiteTitleQuery {
      site {
        siteMetadata {
          title
        }
      }
    }
  `)

  return (
    <Wrapper>
      <Header siteTitle={data.site.siteMetadata.title} />
      <main>{children}</main>
      <footer>
        <p>
          Renaissance is © 2018–{new Date().getFullYear()} David Bolding and is available under the terms of the <a href="https://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)</a> license.
        </p>
        <p>
          <a href="https://github.com/typedrat/renaissance">The Renaissance website</a> is © 2018—{new Date().getFullYear()} Alexis Williams and David Bolding, and is available under the terms of the <a href="https://www.mozilla.org/en-US/MPL/2.0/">Mozilla Public License, version 2.0</a>.
        </p>
      </footer>
    </Wrapper>
  )
}

Layout.propTypes = {
  children: PropTypes.node.isRequired,
}

export default Layout
