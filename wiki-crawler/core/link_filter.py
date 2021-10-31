class CommonFilters:
    in_page_jump = (lambda x: not x.get('href', '').startswith('#'))


class LinkFilter:
    def __init__(self, filters=None):
        if filters is None:
            filters = [CommonFilters.in_page_jump]
        self.filters = filters

    def filter_link(self, link) -> bool:
        return all(f(link) for f in self.filters)

    def __call__(self, link_elements):
        for elem in link_elements:
            if self.filter_link(elem):
                yield elem
