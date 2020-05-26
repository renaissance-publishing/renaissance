import React from "react";
import { graphql } from "gatsby";

import SEO from "../components/seo";
import Layout from "../components/layout";

export default function Chapter({ data }) {
    const chapter = data.markdownRemark;
    
    return (
        <Layout>
            <SEO title={ chapter.frontmatter.title } />

            <article>
                <h1>{ chapter.frontmatter.title }</h1>

                <div dangerouslySetInnerHTML={{ __html: chapter.html }} />
            </article>
        </Layout>
    );
}

export const query = graphql`
    query($slug: String!) {
        markdownRemark(fields: { slug: { eq: $slug } }) {
            html
            frontmatter {
                title
            }
        }
    }
`;
