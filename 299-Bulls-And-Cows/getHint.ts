function getHint(secret: string, guess: string): string {
  let counts: Record<string, number> = {};
  let bulls = 0;
  let cows = 0;
  
  for (let i = 0; i < secret.length; i++) {
      if (secret[i] === guess[i]) {
          bulls++;
      }
      else {
          counts[secret[i]] = (counts[secret[i]] || 0) + 1;
          counts[guess[i]] = (counts[guess[i]] || 0) - 1;
          
          if (counts[secret[i]] <= 0) cows++;
          if (counts[guess[i]] >= 0) cows++;
      }
  }
  
  return bulls + 'A' + cows + 'B';
};