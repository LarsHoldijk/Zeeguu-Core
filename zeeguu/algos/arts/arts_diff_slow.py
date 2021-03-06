import math


class ArtsDiffSlow:
    """
    ARTS algorithm with default values as described in:
    Adaptive response-time-based category sequencing in perceptual learning
    by Everett Mettler and Philip J. Kellman
    """

    """ Constant: maximal possible priority """
    MAX_PRIORITY = 1000

    """ Constant: enforced delay (trials) """
    D = 2

    """ Constant: general weight """
    a = 0.1

    """ Constant: weight for the response time """
    b = 1.1

    """ Constant: weight for the response time (inside log) """
    d = 1.7

    """ Constant: priority increment for an error 
    Higher values let incorrect items appear quicker again
    """
    w = 20

    """ Calculate the ARTS priority
    
    Parameters:
     N: number of trials since item was presented
     alpha: 0, if item was last answered correct; 1 otherwise
     RT: response time on most recent presentation
    """

    def calculate(self, N, alpha, sd):
        return self.a \
               * (N - self.D) \
               * (
                   (1 - alpha) * self.b / (math.e ** (self.d * sd))
                   + (alpha * self.w)
               )
