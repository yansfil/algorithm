"""
https://leetcode.com/problems/rank-scores/

기존의 RANK 함수를 사용하려 했으나, 계산이 복잡해질 것 같음(사실 Next Step 생각이 안남)
Distinct한 Score와 Join해서 Count하는 방식을 사용함 (JOIN할 때 꼭 equal만 사용할 필요는 없음)
"""

" Write your MySQL query statement below "

SELECT S.Score, count(D.Score) as `RANK`
FROM
SCORES as S
LEFT JOIN (
    SELECT DISTINCT SCORE
    FROM SCORES
) as D
ON S.Score <= D.Score
GROUP BY S.Id
ORDER BY 1 desc



