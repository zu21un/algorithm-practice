class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citation_cnt = len(citations)
        sorted_citations = sorted(citations)
        max_value = 0

        for i in range(citation_cnt):
            paper = citation_cnt - i
            citation = sorted_citations[i]
            
            max_value = max(max_value, min(paper, citation))

        return max_value