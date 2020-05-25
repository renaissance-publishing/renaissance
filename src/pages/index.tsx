import { graphql } from "gatsby";

import Chapter from "../templates/chapter";

export default Chapter;

export const query = graphql`
    query {
        markdownRemark(fields: {chapter: {eq: 0}}) {
            html
            frontmatter {
                title
            }
        }
    }
`;
