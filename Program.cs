using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace ProgrammingLanguages
{
  class Program
  {
    static void Main()
    {
      List<Language> languages = File.ReadAllLines("./languages.tsv")
        .Skip(1)
        .Select(line => Language.FromTsv(line))
        .ToList();

      var query = from q in languages
        where (q.Year > 1995 && q.Year < 2005)
        select $"'{q.Name}' was invented in {q.Year} and is based on {q.Predecessors}";

      PrintAll(query);
    }

    public static void PrettyPrintAll(IEnumerable<Language> languages) {
      foreach (var lang in languages) {
        Console.WriteLine(lang.Prettify());
      }
    }

    public static void PrintAll(IEnumerable<Object> o) {
      foreach (var obj in o) {
        Console.WriteLine(obj);
      }
    }
  }
}
