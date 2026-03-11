from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    output_dir = project_root / "output"

    data_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    print("Tech Stock Dynamics project initialized successfully.")
    print(f"Project root: {project_root}")
    print(f"Data directory: {data_dir}")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()