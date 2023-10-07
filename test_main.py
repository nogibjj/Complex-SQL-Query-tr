"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transfrom_load"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_general_query():
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            """
            SELECT a.country,
                SUM(a.beer_servings + a.spirit_servings + a.wine_servings) AS total_alcohol_consumption
            FROM default.alcoholDB AS a
            INNER JOIN default.toyDB AS t ON a.id = t.id
            GROUP BY a.country
            ORDER BY total_alcohol_consumption DESC
            LIMIT 10
            """,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    # print(result)
    assert result.returncode == 0


if __name__ == "__main__":
    # test_extract()
    # test_transform_load()

    # complex query
    test_general_query()