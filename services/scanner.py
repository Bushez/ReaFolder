from pathlib import Path
class Scanner():
    @staticmethod
    def scan(path: Path) -> list[Path]:
        return list(path.rglob("*.rpp"))


if __name__ == "__main__":
    print(*Scanner.scan(Path("C:/Users/user/Documents")))