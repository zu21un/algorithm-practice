class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citation_cnt = len(citations)
        sorted_citations = sorted(citations)

        for i in range(citation_cnt):
            paper = citation_cnt - i
            citation = sorted_citations[i]
            
            if paper <= citation:
                return paper

        return 0