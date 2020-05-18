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
    `gatsby-plugin-emotion`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `chapters`,
        path: `${__dirname}/content/chapters`,
      },
    },
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          {
            resolve: `gatsby-remark-custom-blocks`,
            options: {
              blocks: {
                example: {
                  classes: `example`
                },
                designnote: {
                  classes: `designnote`
                },
                gmguidance: {
                  classes: `gmguidance`
                },
                playerguidance: {
                  classes: `playerguidance`
                },
                clarification: {
                  classes: `clarification`
                }
              }
            }
          }
        ]
      }
    },
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `gatsby-starter-default`,
        short_name: `starter`,
        start_url: `/`,
        background_color: `#663399`,
        theme_color: `#663399`,
        display: `minimal-ui`,
        icon: `src/images/gatsby-icon.png`, // This path is relative to the root of the site.
      },
    },
    // this (optional) plugin enables Progressive Web App + Offline functionality
    // To learn more, visit: https://gatsby.dev/offline
    // `gatsby-plugin-offline`,
  ],
}