import { Link } from "gatsby"
import PropTypes from "prop-types"
import React from "react"
import styled from "@emotion/styled"

const Branding = styled.h1`
  margin: 0;
  font-family: voluta-script-pro, serif;
  font-size: 72pt;
  font-weight: normal;
  text-align: center;
  line-height: normal;

  a {
    color: black;
    text-decoration: none;
  }
`

const Header = ({ siteTitle }) => (
  <header
    style={{
      height: `140px`
    }}
  >
    <Branding>
      <Link to="/">
        {siteTitle}
      </Link>
    </Branding>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header
