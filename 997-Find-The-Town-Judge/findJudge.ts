function findJudge(N: number, trust: number[][]): number {
  let scores: Array<number> = Array(N + 1).fill(0);
  
  for (let [truster, trustee] of trust) {
      scores[truster]--;
      scores[trustee]++;
  }
  
  for (let i: number = 1; i < N + 1; i++) {
      if (scores[i] === N - 1) return i;
  }
  
  return -1;
};