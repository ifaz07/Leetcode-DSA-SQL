class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7

        # [A=0,L=0], [A=0,L=1], [A=0,L=2],
        # [A=1,L=0], [A=1,L=1], [A=1,L=2]
        dp = [1, 0, 0, 0, 0, 0]

        for _ in range(n):
            a0 = (dp[0] + dp[1] + dp[2]) % MOD
            a1 = (dp[0] + dp[1] + dp[2]) % MOD

            a2 = (dp[0] + dp[1]) % MOD

            b0 = (dp[0] + dp[1] + dp[2] +
                  dp[3] + dp[4] + dp[5]) % MOD

            b1 = (dp[3] + dp[4]) % MOD
            b2 = dp[3]

            dp = [a0, dp[0], dp[1], b0, dp[3], dp[4]]

        return sum(dp) % MOD