module.exports = {
  siteMetadata: {
    title: `Renaissance Games`,
    description: `Renaissance is an open-source pen-and-paper RPG that aims to enable more diverse play-styles than traditional games.`,
    author: `Alexis Williams (@typedrat)`,
  },
  plugins: [
    `gatsby-plugin-react-helmet`,
    {
      resolve: 'gatsby-plugin-web-font-loader',
      options: {
        typekit: {
          id: `bqv1ebv`
        }
      }
    },
    `gatsby-plugin-material-ui`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `chapters`,
        path: `${__dirname}/content/chapters`,
      },
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/content/images`,
      },
    },
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          `gatsby-remark-relative-images`,
          {
            resolve: `gatsby-remark-images`,
            options: {
              maxWidth: 960,
            },
          },
          {
            resolve: `gatsby-remark-custom-blocks`,
            options: {
              blocks: {
                example: {
                  classes: `standout example`,
                  title: "optional",
                },
                designnote: {
                  classes: `standout designnote`,
                  title: "optional",
                },
                gmguidance: {
                  classes: `standout gmguidance`,
                  title: "optional",
                },
                playerguidance: {
                  classes: `standout playerguidance`,
                  title: "optional",
                },
                clarification: {
                  classes: `standout clarification`,
                  title: "optional",
                },
                fiction: {
                  classes: `standout fiction`,
                  title: "optional",
                },
                optionalrule: {
                  classes: `standout optional`,
                  title: "optional",
                },
                hook: {
                  classes: `standout hook`,
                  title: "optional",
                },
                abstract: {
                  classes: `standout floating short`,
                  title: "optional",
                },
              }
            }
          },
          {
            resolve: `gatsby-remark-autolink-headers`,
            options: {
              enableCustomId: true,
            },
          },
        ]
      }
    },
    `gatsby-plugin-anchor-links`,
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `Renaissance`,
        short_name: `Renaissance`,
        start_url: `/`,
        background_color: `#663399`,
        theme_color: `#663399`,
        display: `minimal-ui`,
      },
    },
    // this (optional) plugin enables Progressive Web App + Offline functionality
    // To learn more, visit: https://gatsby.dev/offline
    // `gatsby-plugin-offline`,
  ],
}
