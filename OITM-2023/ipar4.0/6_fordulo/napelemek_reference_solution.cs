public static double Solve(int w, int h, int n, List<Tuple<Point, Point>> cuts)
{
    // annak tárolása, hogy az adott indexű sort/oszlopot hol kereszteznek vágások
    // a napelem szélei is vágásnak számítanak
    var verticalCut = Enumerable.Range(0, h).Select(_ => new List<int> { 0, w }).ToList();
    var horizontalCut = Enumerable.Range(0, w).Select(_ => new List<int> { 0, h }).ToList();
    foreach (var c in cuts)
    {
        if (c.Item1.X == c.Item2.X)
            Enumerable.Range(c.Item1.Y, c.Item2.Y - c.Item1.Y).ToList().ForEach(y => verticalCut[y].Add(c.Item1.X));
        else
            Enumerable.Range(c.Item1.X, c.Item2.X - c.Item1.X).ToList().ForEach(x => horizontalCut[x].Add(c.Item1.Y));
    }
    // rendezzük a vágásdarabokat, hogy egyszerű legyen a következőre ugrani
    verticalCut.ForEach(c => c.Sort());
    horizontalCut.ForEach(c => c.Sort());

    // az egész napelem cellái
    var cells = new bool[w, h];
    // a megtalált elemek területe
    var areas = new List<long>();
    // a feldolgozott cellák száma
    var totalCells = 0;

    // sorfolytonosan végigmegyünk a cellákon
    for (var row = 0; row < h; row++)
    {
        for (var col = 0; col < w; col++)
        {
            // ha már feldolgozott a cella, mehetünk a következőre
            if (cells[col, row])
                continue;

            // megkeressük azt az elemet, amelynek ez a cella a bal felső cellája
            FindTileForTopLeftCell(row, col, verticalCut, horizontalCut, cells, areas, ref totalCells);

            // ha már minden cellát feldolgoztunk, akkor visszaadjuk a szórást
            if (totalCells == w * h)
            {
                return GetVariance(areas.ToArray());
            }
        }
    }

    return 0;
}

private static void FindTileForTopLeftCell(int row, int col, 
    IReadOnlyList<List<int>> verticalCut, IReadOnlyList<List<int>> horizontalCut, 
    bool[,] cells, ICollection<long> areas, ref int totalCells)
{
    // az adott cella lesz a bal felső cella az elemben
    var topLeft = new Point(col, row);

    // megkeressük, hogy hol van az adott cellát balról érintő függőleges vágás
    // (biztos, hogy van ilyen, hiszen ha nem lenne, akkor már feldolgozott cella lenne)
    var left = verticalCut[row].IndexOf(col);
    // meghatározzuk, hogy hol lesz ebben a sorban a következő függőleges vágás -> itt lesz az elem jobb széle
    var right = verticalCut[row][left + 1];
    // megkeressük, hogy hol van a jobb szélső cellát felülről érintő vízszintes vágás
    // (biztos, hogy van ilyen, hiszen ha nem lenne, akkor már feldolgozott cella lenne)
    var top = horizontalCut[right - 1].IndexOf(row);
    // meghatározzuk, hogy hol van a jobb szélső oszlopban a következő víszintes vágás -> itt lesz az elem alsó széle
    var bottom = horizontalCut[right - 1][top + 1];

    // kiszámoljuk és eltároljuk a talált elem területét
    var area = (right - topLeft.X) * (long)(bottom - topLeft.Y);
    areas.Add(area);

    // feldolgozottnak állítjuk az elem celláit
    for (var c = topLeft.X; c < right; c++)
    {
        for (var r = topLeft.Y; r < bottom; r++)
        {
            cells[c, r] = true;
            totalCells++;
        }
    }
}

private static double GetVariance(long[] array)
{
    var mean = array.Average();
    return Math.Sqrt(array.Aggregate(0.0, (acc, x) => acc + Math.Pow(x - mean, 2)) / array.Length);
}
