from mistletoe import block_token, html_renderer
import re


toAnchorRegex = re.compile(r'[^\w\d]')


class RenaissanceHTMLRenderer(html_renderer.HTMLRenderer):
    @staticmethod
    def heading_to_anchor(heading: block_token.Heading) -> str:
        text: str = heading.children[0].content
        return toAnchorRegex.sub('', text)

    def render_heading(self, token):
        template = '<h{level} id="{anchor}"><a class="header-link" href="#{anchor}">{inner}</a></h{level}>'
        inner = self.render_inner(token)
        return template.format(level=token.level, anchor=self.heading_to_anchor(token), inner=inner)

    def render_block_code(self, token):
        if isinstance(token, block_token.CodeFence) and token.language in ['devnotes', 'aside']:
            template = '<aside class="{klass}">{inner}</aside>'
            inner = self.render_inner(token)
            return template.format(klass=token.language, inner=inner)
        else:
            super(RenaissanceHTMLRenderer, self).render_block_code(token)
