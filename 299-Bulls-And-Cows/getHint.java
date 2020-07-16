class Solution {
  public String getHint(String secret, String guess) {
      Map<Character, Integer> counts = new HashMap<>();
      int bulls = 0;
      int cows = 0;
      
      for (int i = 0; i < secret.length(); i++) {
          char s_char = secret.charAt(i);
          char g_char = guess.charAt(i);
          
          if (s_char == g_char) {
              bulls++;
          }
          else {
              counts.put(s_char, counts.getOrDefault(s_char, 0) + 1);
              counts.put(g_char, counts.getOrDefault(g_char, 0) - 1);
              
              if (counts.get(s_char) <= 0) {
                  cows++;
              }
              if (counts.get(g_char) >= 0) {
                  cows++;
              }
          }
      }
      return bulls + "A" + cows + "B";
  }
}