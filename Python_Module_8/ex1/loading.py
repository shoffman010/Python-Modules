import importlib
import sys


DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies():
    """Import dependencies and display their installed versions."""
    loaded_modules = {}
    missing_modules = []

    print("Checking dependencies:")
    for module_name, description in DEPENDENCIES.items():
        try:
            module = importlib.import_module(module_name)
            version = getattr(module, "__version__", "unknown version")
            print(f"[OK] {module_name} ({version}) - {description}")
            loaded_modules[module_name] = module
        except ImportError:
            print(f"[MISSING] {module_name} - {description}")
            missing_modules.append(module_name)

    if missing_modules:
        print("\nMissing dependencies:", ", ".join(missing_modules))
        print("Install with pip:")
        print("python -m pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print("poetry install")
        return None

    return loaded_modules


def explain_package_management():
    """Explain the dependency files used by pip and Poetry."""
    print("\nDependency management:")
    print("pip reads package versions from requirements.txt.")
    print("Poetry reads them from pyproject.toml and creates poetry.lock.")


def analyze_matrix_data(modules):
    """Generate, analyze, and plot simulated Matrix data."""
    pandas = modules["pandas"]
    numpy = modules["numpy"]
    pyplot = importlib.import_module("matplotlib.pyplot")

    data_point_count = 1000
    generator = numpy.random.default_rng(42)
    matrix_data = pandas.DataFrame(
        {
            "signal": generator.normal(50, 12, data_point_count),
            "anomaly_score": generator.random(data_point_count),
        }
    )
    matrix_data["moving_average"] = (
        matrix_data["signal"].rolling(window=25, min_periods=1).mean()
    )

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(matrix_data)} data points...")
    print("Generating visualization...")

    figure, axis = pyplot.subplots(figsize=(10, 5))
    axis.plot(
        numpy.arange(data_point_count),
        matrix_data["signal"],
        color="green",
        alpha=0.35,
        label="Matrix signal",
    )
    axis.plot(
        numpy.arange(data_point_count),
        matrix_data["moving_average"],
        color="black",
        linewidth=2,
        label="Moving average",
    )
    axis.set_title("Matrix Signal Analysis")
    axis.set_xlabel("Data point")
    axis.set_ylabel("Signal strength")
    axis.legend()
    figure.tight_layout()
    figure.savefig("matrix_analysis.png")
    pyplot.close(figure)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...\n")
    modules = check_dependencies()
    explain_package_management()

    if modules is None:
        return 1

    analyze_matrix_data(modules)
    return 0


if __name__ == "__main__":
    sys.exit(main())
