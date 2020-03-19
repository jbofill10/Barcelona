import Population as population
import AccidentPrediction as ap

import trends.AccidentTrends as at


def main():
    population.graph_population()

    at.trends()

    ap.make_prediction()


if __name__ == '__main__':
    main()
