const path = require(`path`);
const { createFilePath } = require(`gatsby-source-filesystem`);

exports.onCreateNode = ({ node, getNode, actions }) => {
  const { createNodeField } = actions;

  if (node.internal.type === `MarkdownRemark`) {
    const defaultSlug = createFilePath({ node, getNode, basePath: `chapters`, trailingSlash: false });
    const realSlug = defaultSlug.substring(defaultSlug.indexOf('-') + 1);
    const chapterNum = parseInt(defaultSlug.substring(1, defaultSlug.indexOf('-')), 10);

    createNodeField({
      node,
      name: `slug`,
      value: `/${realSlug}/`,
    });
    createNodeField({
      node,
      name: `chapter`,
      value: chapterNum,
    });
  }
}

exports.createPages = async ({ graphql, actions }) => {
  const { createPage } = actions;

  const result = await graphql(`
    query {
      allMarkdownRemark(filter: {fields: {chapter: {ne: 0}}}) {
        edges {
          node {
            fields {
              slug
            }
          }
        }
      }
    }
  `);

  result.data.allMarkdownRemark.edges.forEach( ({ node }) =>
    createPage({
      path: node.fields.slug,
      component: path.resolve(`./src/templates/chapter.tsx`),
      context: {
        slug: node.fields.slug
      }
    })
  );
}
